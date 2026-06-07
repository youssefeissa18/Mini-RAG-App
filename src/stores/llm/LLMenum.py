from enum import Enum
class LLMEnum(Enum):
    OPENAI = "OPENAI"
    COHERE = "COHERE"

class OpenAienum(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class CohereEnum(Enum):
    SYSTEM = "SYSTEM"
    USER = "USER"
    ASSISTANT = "CHATBOT"
    DOUCMENT = "search_doucment"
    QUERY = "search_query"

class DoucmentTypeEnum(Enum):
    DOUCMENT = "doucment"
    QUERY = "query"