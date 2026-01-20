from __future__ import annotations

from fastapi import APIRouter, Request, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.services.storage import ensure_dirs
from backend.services.pipeline import run_full_pipeline
from backend.services.video_ingest import save_upload_to_disk, resolve_url_offline, IngestError
from backend.services.url_downloader import download_video_from_url

router = APIRouter()
templates = Jinja2Templates(directory="frontend/templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    ensure_dirs()
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/run", response_class=HTMLResponse)
async def run_from_web(
    request: Request,
    video_file: UploadFile | None = None,
    video_url: str | None = Form(default=None),
    text_hint: str | None = Form(default=None),
):
    """
    Input options:
      1) Upload a video file
      2) Provide a video URL
         - Strict offline mode: resolve from local URL cache only
         - Optional dev mode: if ALLOW_NET_DOWNLOAD=1, download with yt-dlp
    """
    ensure_dirs()

    video_path = None

    try:
        # -------- Option 1: File upload --------
        if video_file and video_file.filename:
            data = await video_file.read()
            video_path = save_upload_to_disk(video_file.filename, data)

        # -------- Option 2: Video URL --------
        elif video_url and video_url.strip():
            url = video_url.strip()

            # Try strict offline cache first
            try:
                video_path = resolve_url_offline(url)
            except IngestError:
                # If cache miss, optionally download (only if enabled)
                video_path = download_video_from_url(url)

        # -------- No input --------
        else:
            return templates.TemplateResponse(
                "result.html",
                {
                    "request": request,
                    "error": "Please upload a video file OR provide a video URL.",
                },
            )

        # Run the full pipeline (Phase-1 + Phase-2)
        result = run_full_pipeline(video_path=video_path, text_hint=text_hint)

        return templates.TemplateResponse(
            "result.html",
            {"request": request, "result": result, "error": None},
        )

    except Exception as e:
        # Never crash with 500 for user inputs; show a clean error instead
        return templates.TemplateResponse(
            "result.html",
            {"request": request, "error": str(e)},
        )
