# User Story 6.4: Run a Prompt in the Playground (UC-06.03)

## Overview
- **Epic**: Epic 6: AI Enhancement
- **Priority**: High
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User,
- **I want to** test my prompt live against a real AI model,
- **So that** I can see the actual response before using the prompt elsewhere.

## Acceptance Criteria (BDD Format)
- **Given** I am logged in and have Playground quota remaining
- **When** I open `/playground` (or click `[Try in Playground]`), select a model, adjust temperature/max_tokens within my plan's limits, and click `[Run]`
- **Then** the backend calls the corresponding LLM Adapter, measuring latency and token usage
- **And** the response streams back in real time if the model supports streaming
- **And** the response plus metadata (`tokens_used`, `latency_ms`, `model_version`) is saved to `generated_prompts.playground_response`.

## Exception Scenarios
- The provider returns a rate limit → the circuit breaker opens and a fallback message is shown.
- The response exceeds `max_tokens` → truncated, with a warning shown to the user.

## Technical Implementation Details
- **Frontend Layer**:
  - `/playground` page: model selector, temperature/max_tokens controls (bounded by plan), Run button, streaming response panel.
  - Displays latency and token usage after the run completes.
- **Backend Layer**:
  - `POST /api/v1/playground/run` — resolves the target LLM Adapter, applies plan-based limits, invokes the provider, streams the response if supported.
  - Wraps every provider call in a circuit breaker (Resilience4j, per SRS §5.4) with a defined fallback.
- **Database Layer**:
  - Persist `playground_response`, `tokens_used`, `latency_ms`, `model_version` on `generated_prompts`.

## Business Rules
- Free: 10 runs/day, capped at 500 output tokens.
- Pro: 200 runs/day, capped at 4000 output tokens.
- Team: unlimited per seat (Phase 4).

## Verification & Testing
- Run a prompt against a streaming-capable model → verify tokens appear incrementally in the UI.
- Run against a non-streaming model → verify the full response renders on completion.
- Exceed daily quota (Free plan) → verify the Run action is blocked with an upgrade prompt.
- Simulate a provider rate-limit error → verify the circuit breaker opens and the fallback message is shown instead of a raw error.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
