from typing import List, Tuple, Union, Any, Dict

from anthropic import Client, HUMAN_PROMPT, AI_PROMPT
from jinja2 import Template

from src.entity.models import History
from src.config.config import Config
from src.usecases.suggester import Suggester


class AnthropicSuggester(Suggester):
    def __init__(
        self,
        cfg: Config,
    ):
        super().__init__()
        self.cfg = cfg
        self.client = Client(api_key=cfg.ANTHROPIC_API_KEY)  # type: ignore

    def invoke(
        self,
        documents: List[str],
        page_content: str,
        history: History,
        query: str,
    ) -> str:

        if history:
            prompt = self.prepare_messages_api_prompt(
                documents, page_content, history, query
            )
        else:
            prompt = self.prepare_text_api_prompt(documents, page_content, query)

        result = self.client.messages.create(
            model="claude-3-haiku-20240307",  # TODO: Use config for model
            max_tokens=4000,
            temperature=0.1,
            messages=prompt,  # type: ignore
        )

        if result.content:
            res = str(result.content[0].text)  # type: ignore
        else:
            res = ""
        return res

    def prepare_messages_api_prompt(
        self,
        documents: List[str],
        page_content: str,
        history: History,
        query: str,
    ) -> List[Dict[str, Any]]:

        res = []
        for h in history:
            user_pair = {
                "role": "user",
                "content": [{"type": "text", "text": h.query}],  # type: ignore
            }
            res.append(user_pair)
            assistant_pair = {
                "role": "assistant",
                "content": [{"type": "text", "text": h.response}],  # type: ignore
            }
            res.append(assistant_pair)

        return res

    def prepare_text_api_prompt(
        self, documents: List[str], page_content: str, query: str
    ) -> List[Dict[str, Any]]:

        prompt_template = """
                {{HUMAN_PROMPT}} You are a expert of this documentation.
                Here's some documentation:\n\n{{page_content}}\n\n
                Using the documentation, give answer on the query: {{query}}.
                Give answer only related to the documentation.
                Write answer in markdown format.
                Code blocks should be in ```language code block ``` format.\n\n{{AI_PROMPT}}
        """

        template = Template(prompt_template)

        text_prompt = template.render(
            HUMAN_PROMPT=HUMAN_PROMPT,
            page_content=page_content,
            query=query,
            AI_PROMPT=AI_PROMPT,
        )

        res = []
        pair = {
            "role": "user",
            "content": [{"type": "text", "text": text_prompt}],
        }

        res.append(pair)

        return res
