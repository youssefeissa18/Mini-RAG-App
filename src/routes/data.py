from fastapi import FastAPI, APIRouter, Depends, File, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers.DataController import DataController, ProjectController
import aiofiles
from models.enums.ResponseEnums import ResponseSignal
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"],
)
@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, apps_settings: Settings = Depends(get_settings)):
    isvalid, result_signal = DataController().validate_uploaded_file(file)
    if not isvalid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": result_signal})
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = os.path.join(project_dir_path, file.filename)

    async with aiofiles.open(file_path, 'wb') as f:
        while chunks := await file.read(apps_settings.FILE_DEFAULT_CHUNK_SIZE):  # Read in chunks
            await f.write(chunks)    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": ResponseSignal.FILE_UPLOAD_SUCCESS.value, "file_path": file_path})
