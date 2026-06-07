from .providers import QDRANTDB
from .VectorDBEnum import VectorDBType, DistanceMethodEnums
from controllers import BaseController

class VectorDBProviderFactory:
    def __init__(self, config: dict):
        self.config = config
        self.base_controller = BaseController()

    def create(self, provider:str):

        if provider == VectorDBType.QDRANT.value:
            db_path = self.base_controller.get_database_path(db_name=self.config.QDRANT_DB_PATH)

            return QDRANTDB(
                db_path = db_path,
                distance_method = self.config.QDRANT_DISTANCE_METHOD
            )
        return None