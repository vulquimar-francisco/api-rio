from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from app.core.auth import get_current_user
import os
import mimetypes
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

MEDIA_DIRECTORY = os.getenv("MEDIA_DIRECTORY")

media_directory = MEDIA_DIRECTORY

def is_media_file(file_path: str) -> bool:
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and (mime_type.startswith('image') or mime_type.startswith('video'))

def get_media_files():
    media_files = []
    if os.path.exists(media_directory):
        for root, _, files in os.walk(media_directory):
            for file in files:
                file_path = os.path.join(root, file)
                if is_media_file(file_path):
                    media_files.append(file_path)
    return media_files

@router.get("/media", response_model=list)
async def list_media_files(current_user: str = Depends(get_current_user)):
    media_files = get_media_files()
    media_urls = [f"/api/v1/media/{os.path.basename(file)}" for file in media_files]
    return media_urls

@router.get("/media/{filename}")
async def get_media_file(filename: str, current_user: str = Depends(get_current_user)):
    file_path = os.path.join(media_directory, filename)
    if os.path.exists(file_path) and is_media_file(file_path):
        return FileResponse(file_path)
    return {"error": "File not found or not a media file"}
