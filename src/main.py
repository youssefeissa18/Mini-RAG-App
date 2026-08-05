from fastapi import FastAPI, File, UploadFile
from routes import base, data, nlp
from helpers.config import get_settings
from stores.llm.LLMFACTORYProvider import LLMFactoryProvider
from stores.vectordb.VectorDBFactoryProvider import VectorDBFactoryProvider
from stores.llm.templates.template_parser import TemplateParser
from sqlalalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalalchemy.orm import sessionmaker


app = FastAPI()

async def startup_span():
    settings = get_settings()
    postgres_con = f"postgresql+asyncpg://{settings.POSTGRESQL_USER}:{settings.POSTGRESQL_PASSWORD}@{settings.POSTGRESQL_HOST}:{settings.POSTGRESQL_PORT}/{settings.POSTGRESQL_MAIN_DATABASE}"
    app.db_engine = create_async_engine(postgres_con)

    app.db_client = sessionmaker(app.db_engine, class_=AsyncSession, expire_on_commit=False)

    llm_provider_factory = LLMFactoryProvider(settings)
    vectordb_provider_factory = VectorDBFactoryProvider(settings)

    # generation client
    app.generation_client = llm_provider_factory.create(provider = settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id = settings.GENERATION_MODEL_ID)

    # embedding client
    app.embedding_client = llm_provider_factory.create(provider = settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id = settings.EMBEDDING_MODEL_ID, embedding_size = settings.EMBEDDING_MODEL_SIZE)

    # vectordb client
    app.vectordb_client = vectordb_provider_factory.create(provider = settings.VECTOR_DB_TYPE)

    app.vectordb_client.connect()

    app.template_parser = TemplateParser(
        language=settings.PRIMARY_LANG,
        default_language=settings.DEFAULT_LANG,
    )
    
async def shutdown_span():
    app.db_engine.dispose()
    app.vectordb_client.disconnect()


app.on_event("startup")(startup_span)
app.on_event("shutdown")(shutdown_span)

app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router) 