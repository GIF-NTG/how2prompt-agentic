import json
import logging
from app.clients.llm import LLMClient
from app.core.schemas import OptimizeResponse

logger = logging.getLogger(__name__)

class PromptOptimizerService:
    def __init__(self) -> None:
        self.llm_client = LLMClient()

    async def optimize(
        self, prompt_idea: str, team_standards: str, variables: dict[str, str]
    ) -> OptimizeResponse:
        """
        Takes raw prompt ideas and team standards, constructs the system and user instructions,
        queries the LLM, and formats the output into OptimizeResponse schema.
        """
        logger.info(f"Optimizing prompt idea: '{prompt_idea[:30]}...'")

        # Define system instructions for the LLM
        system_instruction = (
            "You are a master prompt architect. Your task is to optimize the given prompt idea "
            "into a reusable template containing variable placeholders enclosed in curly brackets (e.g. {language}). "
            "You must also extract the list of detected variable names and write a brief explanation "
            "summarizing your optimizations."
        )

        user_content = (
            f"Prompt Idea: {prompt_idea}\n"
            f"Team Guidelines to Enforce: {team_standards}\n"
            f"Current active variables context: {json.dumps(variables)}\n"
        )

        messages = [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_content}
        ]

        # Define schema output format (using LiteLLM JSON mode or structured outputs if supported)
        json_schema = {
            "type": "object",
            "properties": {
                "template": {
                    "type": "string",
                    "description": "The optimized prompt template with curly braces variable placeholders."
                },
                "detected_variables": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of placeholder names extracted from the template."
                },
                "explanation": {
                    "type": "string",
                    "description": "Short explanation of the optimizations."
                }
            },
            "required": ["template", "detected_variables", "explanation"]
        }

        # Query LLM
        response = await self.llm_client.completion(
            messages=messages,
            response_format={"type": "json_object", "schema": json_schema}
        )

        # Parse JSON content from the response
        try:
            content_str = response["choices"][0]["message"]["content"]
            content = json.loads(content_str)
            return OptimizeResponse(
                template=content["template"],
                detected_variables=content["detected_variables"],
                explanation=content["explanation"]
            )
        except (KeyError, IndexError, json.JSONDecodeError, ValueError) as e:
            logger.error(f"Failed to parse LLM response into schema: {str(e)}")
            raise ValueError("Upstream LLM output does not match expected JSON schema contract.")
