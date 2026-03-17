from .BaseController import BaseController
from fastapi import UploadFile, File
from models import ResponseSignal
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