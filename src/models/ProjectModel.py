from .Base_data_model import BaseDataModel
from .db_schemes import Project
from .enums.DataBaseEnums import DataBaseEnum

class ProjectModel(BaseDataModel):
    def __init__(self, db_client : object):
        super().__init__(db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTIONS_PROJECTS_NAME.value]
        
    async def create_project(self, project: Project):
        result = await self.collection.insert_one(project.dict())
        project._id = result.inserted_id
        return project

    async def get_project_or_create_one(self, project_id : str):
        record = await self.collection.find_one(
            "project_id", project_id
        )
        if record is None:
            # Create a new project
            project = Project(project_id=project_id)
            project = await self.create_project(project)
            
            return project
        return Project(**record)

    async def get_all_project(self, page : int = 1, page_size : int = 10):
        # Count total number of documnets
        total_documnets = await self.collection.count_documnets({})

        # Calculate total number of pages
        total_pages = total_documnets // page_size
        if total_documnets % page_size > 0:
            total_pages += 1
        
        cursor = self.collection.find({}).skip((page - 1) * page_size).limit(page_size)
        projects = []
        for document in cursor:
            projects.append(
                Project(**document)
            )
        return projects, total_pages


