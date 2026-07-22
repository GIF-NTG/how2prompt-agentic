from pydantic import BaseModel, Field

class OptimizeRequest(BaseModel):
    prompt_idea: str = Field(..., description="The user input or template raw content")
    team_standards: str = Field("", description="Team global standards to inject into optimization")
    variables: dict[str, str] = Field(default_factory=dict, description="Variables list and current values")

class OptimizeResponse(BaseModel):
    template: str = Field(..., description="Optimized template containing variable placeholders")
    detected_variables: list[str] = Field(..., description="List of variables found in the prompt")
    explanation: str = Field(..., description="Details and explanation of the optimization process")
