import uvicorn
from src.config.config import Config
from src.interfaces.http_routers import DocuQ

# from src.repository.suggester_engine.anthropic import AnthropicSuggester


def launch(cfg: Config):
    docu_q_service = DocuQ().app
    uvicorn.run(docu_q_service, host="0.0.0.0", port=3000)
