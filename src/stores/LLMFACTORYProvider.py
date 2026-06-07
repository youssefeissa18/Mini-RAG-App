from .LLMenum import LLMEnum
from .providers import OpenAiProvider, COHEREProvider

class LLMFACTORYProvider:
    def __init__(self, config: dict):
        self.config = config

    def create(self, provider:str):
        if provider == LLMEnum.OPENAI.value:
            return OpenAiProvider(
                api_key = self.config.OPENAI_API_KEY,
                api_url = self.config.OPENAI_API_URL,
                INPUT_DEFAULT_MAX_CHARACTERS = self.config.INPUT_DEFAULT_MAX_CHARACTERS,
                GENERATION_DEFAULT_MAX_TOKENS = self.config.GENERATION_DEFAULT_MAX_TOKENS,
                GENERATION_DEFAULT_TEMPRETURE = self.config.GENERATION_DEFAULT_TEMPRETURE
            )
        if provider == LLMEnum.COHERE.value:
            return COHEREProvider(
                api_key = self.config.COHERE_API_KEY,
                INPUT_DEFAULT_MAX_CHARACTERS = self.config.INPUT_DEFAULT_MAX_CHARACTERS,
                GENERATION_DEFAULT_MAX_TOKENS = self.config.GENERATION_DEFAULT_MAX_TOKENS,
                GENERATION_DEFAULT_TEMPRETURE = self.config.GENERATION_DEFAULT_TEMPRETURE
            )
        return None
    
    

