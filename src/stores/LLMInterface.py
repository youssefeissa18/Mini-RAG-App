from abc import ABC, abstractmethod
class LLMInterface(ABC):

    @abstractmethod
    def set_generation_model(self, Model_id : str):
        pass

    @abstractmethod
    def set_embedding_model(self, Model_id : str, embedding_size:int):
        pass

    @abstractmethod
    def generate_text(self, prompt : str,chat_history:list=[], max_output_tokens : int=None,     temperature : float = None):
        pass

    @abstractmethod
    def embed_text(self, text:str, doucment_type:str = None):
        pass

    @abstractmethod
    def construct_prompt(self, prompt : str, role:str):
        pass
    

