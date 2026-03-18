import os

from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile, File
from models import ResponseSignal
import re
class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.sizescaele = 1048576  # Convert MB to Bytes
    def validate_uploaded_file(self, file: UploadFile):
        # Implement file validation logic here
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.INVALID_FILE_TYPE.value
        if file.spool_max_size > self.settings.FILE_MAX_SIZE_MB * self.sizescaele:
            return False, ResponseSignal.FILE_TOO_LARGE.value
        return True, ResponseSignal.FILE_VALIDATE_SUCCESS.value
    
    def generate_unique_filename(self, original_filename: str, project_id: str) -> str:
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id = project_id)

        clean_file_name = self.get_clean_file_name(original_filename = original_filename)
        
        new_file_path = os.path.join(project_path, random_key + '_' + clean_file_name)

        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(project_path,
                                        random_key + '_' + 
                                        clean_file_name
                                        )
        return new_file_path

    def get_clean_file_name(self, original_filename: str):
        # Remove special characters expect underscores and .
        clean_File_name = re.sub(r'[^a-zA-Z0-9_.]', '_', original_filename)

        # Replace spaces with underscores
        clean_File_name = clean_File_name.replace(' ', '_')
        return clean_File_name
