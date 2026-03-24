from .Base_data_model import BaseDataModel
from .enums.DataBaseEnums import DataBaseEnum
from .db_schemes.asset import Asset
from bson import ObjectId
class AssetsModel(BaseDataModel):
    def __init__(self, db_client : object):
        super().__init__(db_client=db_client)
        self.collection_name = self.db_client[DataBaseEnum.COLLECTION_ASSETS_NAME.value]

    @classmethod
    async def create_instance(cls, db_client : object):
        instance = cls(db_client)
        await instance.init_collection()
        return instance
    
    async def init_collection(self):
        all_collections = await self.db_client.list_collection_names()
        if DataBaseEnum.COLLECTIONS_ASSETS_NAME.value not in all_collections:
            self.collection = self.db_client[DataBaseEnum.COLLECTIONS_ASSETS_NAME.value]
            indexes = Asset.get_indexs()
            for index in indexes:
                await self.collection.create_index(index["keys"], name=index["name"], unique=index["unique"])
    
    async def create_asset(self, asset: Asset):
        result = await self.collection.insert_one(asset.dict(by_alias=True, exclude_unset=True))
        asset.id = result.inserted_id
        return asset
    
    async def get_all_projects_assets(self, asset_project_id : str):
        return await self.collection.find({
            "asset_project_id": ObjectId(asset_project_id) if isinstance(asset_project_id, str) else asset_project_id}).to_list(length=None)
    