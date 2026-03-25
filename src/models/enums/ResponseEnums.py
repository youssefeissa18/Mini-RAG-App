from enum import Enum

class ResponseSignal(str, Enum):
    INVALID_FILE_TYPE = "Invalid file type. Allowed types are: "
    FILE_TOO_LARGE = "File size exceeds the maximum limit of "
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
    FILE_VALIDATE_SUCCESS = "File is valid"
    FILE_VALIDATE_FAILED = "File is invalid"
    PROCESSING_SUCCESS = "File processed successfully"
    PROCESSING_FAILED = "Processing failed"
    NO_FILES_ERROR = "Not found any files to process"
    FILE_ID_ERROR = "File ID is required for processing"
