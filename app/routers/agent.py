from fastapi import APIRouter, Depends, HTTPException
from app.core.schemas import OptimizeRequest, OptimizeResponse
from app.services.optimizer import PromptOptimizerService

router = APIRouter(prefix="/agent", tags=["agent"])

@router.post("/optimize", response_model=OptimizeResponse)
async def optimize_prompt(
    payload: OptimizeRequest,
    optimizer: PromptOptimizerService = Depends()
) -> OptimizeResponse:
    """
    Endpoint to receive raw prompt concept, team guidelines, and parameters,
    and returns optimized templates containing placeholder variables.
    """
    try:
        result = await optimizer.optimize(
            prompt_idea=payload.prompt_idea,
            team_standards=payload.team_standards,
            variables=payload.variables
        )
        return result
    except ValueError as e:
        # Invalid LLM structure
        raise HTTPException(status_code=502, detail=str(e))
    except Exception as e:
        # Bubble up to be caught by global handlers
        raise e
