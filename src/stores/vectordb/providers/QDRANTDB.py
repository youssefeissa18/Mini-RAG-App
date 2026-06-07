from qdrant_client import QdrantClient, models
from ..VectorDBInterface import VectorDBInterface
from .VectorDBEnum import VectorDBType, DistanceMethodEnums
import logging
from typing import List
class QDRANTDB(VectorDBInterface):
    def __init__(self, db_path: str, distance_method:DistanceMethodEnums):
        self.db_path = db_path
        self.distance_method = None
        self.client = None
        if distance_method == DistanceMethodEnums.COSINE:
            self.distance_method = models.Distance.COSINE
        elif distance_method == DistanceMethodEnums.DOT:
            self.distance_method = models.Distance.DOT
        else:
            logging.warning(f"Unsupported distance method: {distance_method}, default to COSINE")
            self.distance_method = models.Distance.COSINE
    
    def connect(self):
        self.client = QdrantClient(path=self.db_path)
    def disconnect(self):
        self.client = None

    def is_connection_existed(self, collection_name:str) -> bool:
        return self.client.collection_exists(collection_name=collection_name)
    
    def list_all_collections(self) -> List:
        return self.client.get_collections().collections
    
    def get_collection_info(self, collection_name:str) -> dict:
        return self.client.get_collection(collection_name=collection_name)
    
    def delete_collection(self, collection_name:str) -> bool:
        if self.is_connection_existed(collection_name=collection_name):
            self.client.delete_collection(collection_name=collection_name)
            return True
        return False
    
    def create_collection(self, collection_name:str, embedding_size:int, do_reset:bool = False):
        if do_reset:
            _ = self.delete_collection(collection_name=collection_name)
        if not self.is_connection_existed(collection_name=collection_name):
            _ = self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(size=embedding_size, distance=self.distance_method)
            )

            return True
        return False
    
    def insert_one(self, collection_name:str,
                    text:str, vector:List, 
                    metadata:dict=None,
                    record_id:str=None):
        if not self.is_connection_existed(collection_name=collection_name):
            self.logger.error(f"Collection {collection_name} does not exist, failed to insert record")
            return False
        try:
            _ = self.client.upload_records(
                collection_name=collection_name,
                records=[
                    models.Record(
                        id = [record_id],
                        vector=vector,
                        payload={
                            "text": text,
                            "metadata": metadata
                        }
                    )
                ]
            )
        except Exception as e:            
            self.logger.error(f"Error occurred while uploading record to collection {collection_name}: {e}")

        return True
    
    def insert_many(self, collection_name:str,
                    texts:List, vectors:List, 
                    metadatas:List = None,
                    record_ids:List = None, batch_size:int = 50):
        if metadatas is None:
            metadatas = [None] * len(texts)
        if record_ids is None:
            record_ids = list(range(0,len(texts)))
            
        for i in range(0, len(texts), batch_size):
            batch_end = i + batch_size
            batch_texts = texts[i:batch_end]
            batch_vectors = vectors[i:batch_end]
            batch_metadatas = metadatas[i:batch_end]
            batch_record_id = record_ids[i:batch_end]
            batch_records = [
                models.Record(
                    id = batch_record_id,
                    vector=batch_vectors[x],
                    payload={
                        "text": batch_texts[x],
                        "metadata": batch_metadatas[x]
                    }
                )
                for x in range(len(batch_texts))
            ]
            try:
                _ = self.client.upload_records(
                collection_name=collection_name,
                records=batch_records
                )
            except Exception as e:
                self.logger.error(f"Error occurred while uploading records to collection {collection_name}: {e}")
                return False
        return True 
    
    def search_by_vector(self, collection_name:str, vector:List, limit:int = 5):
        return self.client.search(
            collection_name=collection_name,
            query_vector=vector,
            limit=limit
        )