# User Story 3.1: Resilient Upstream Prompt Optimization

## Overview
- **Epic**: Epic 3: Stateless Optimization & History Management
- **Priority**: P2
- **User Persona**: Member (Authenticated)

## Story Description
- **As a** Member,
- **I want to** prompt optimization requests to be resilient and fail gracefully,
- **So that** transient network glitches do not disrupt my workflow.

## Acceptance Criteria (BDD Format)
- **Given** a Member requests a prompt optimization.
- **When** the Spring Boot Gateway routes the request to the Python FastAPI Prompt Service `/api/v1/agent/optimize`.
- **And** the FastAPI service interacts with LiteLLM and encounters transient exceptions (rate limits, network timeouts).
- **Then** the service triggers exponential backoff retries using Tenacity (maximum of 3 attempts).
- **When** the upstream connection fails terminally.
- **Then** the system returns an RFC-7807 Bad Gateway error payload (`HTTP 502`, `LLM_PROVIDER_ERROR`) detailing the provider failure.

## Technical Implementation Details
- **Frontend Layer**:
  - React Variable Canvas UI elements to trigger "Optimize Prompt" action.
  - Handle loading state and display spinner.
  - Clean error visualization if the optimization request fails, parsing the RFC-7807 details.
- **Backend API Gateway Layer (Spring Boot)**:
  - Gateway endpoint: `POST /api/v1/agent/optimize` (verifies user JWT session).
  - Routes request payload to Python FastAPI service.
  - Maps any FastAPI exceptions or gateway errors to uniform RFC-7807 Bad Gateway details (`HTTP 502`, error code `LLM_PROVIDER_ERROR`) as specified in [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md).
- **Python FastAPI Prompt Service**:
  - Stateless architecture: No databases, local caches, or disk state as dictated by [how2prompt-agentic/CLAUDE.md](how2prompt-agentic/CLAUDE.md).
  - Data Contracts: Rigid Pydantic model definitions for incoming request bodies and outgoing responses. No dynamic dictionary parsing on primary routes.
  - LLM integration: Interacts with LiteLLM using Pydantic. No usage of LangChain or LangGraph.
  - Resiliency: Outgoing LiteLLM requests are wrapped with `tenacity` retry logic:
    - Retries only transient errors (rate limit 429, timeouts, 5xx server issues).
    - Maximum of 3 attempts.
    - Exponential backoff algorithm.
- **Exception handling**:
  - Terminal exceptions are captured in a custom error handler and mapped to a standard RFC-7807 error format.

## Verification & Testing
- Trigger prompt optimization and verify successful response is parsed and displayed in under a reasonable network latency threshold.
- Simulate upstream transient exceptions (e.g. mock a 429 response on initial call) and verify that Tenacity retries the request.
- Simulate terminal upstream failure (e.g. shut down upstream mock or return 500 error after 3 attempts) and confirm Gateway responds with `HTTP 502 Bad Gateway` and `LLM_PROVIDER_ERROR` JSON payload.
- Refer to [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md), [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md), and [how2prompt-agentic/docs/epics.md](how2prompt-agentic/docs/epics.md) for full system specifications.
