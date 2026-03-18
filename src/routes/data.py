from fastapi import FastAPI, APIRouter, Depends, File, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers.DataController import DataController
from controllers.ProjectController import ProjectController
import aiofiles
from models.enums.ResponseEnums import ResponseSignal
import logging

logger = logging.getLogger("uvicorn.error")
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"],
)
@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, apps_settings: Settings = Depends(get_settings)):
    
    # Validate the uploaded file
    data_controller = DataController()
    isvalid, result_signal = data_controller.validate_uploaded_file(file)
    if not isvalid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": result_signal})
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = data_controller.generate_unique_filename(original_filename=file.filename, project_id=project_id)

    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunks := await file.read(apps_settings.FILE_DEFAULT_CHUNK_SIZE):  # Read in chunks
                await f.write(chunks)
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": ResponseSignal.FILE_UPLOAD_FAILED.value, "error": str(e)})
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": ResponseSignal.FILE_UPLOAD_SUCCESS.value, "file_path": file_path})
