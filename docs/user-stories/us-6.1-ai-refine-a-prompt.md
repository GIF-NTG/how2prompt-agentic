# User Story 6.1: AI Refine a Prompt (UC-06.01)

## Overview
- **Epic**: Epic 6: AI Enhancement
- **Priority**: High
- **User Persona**: Logged-in, Verified User

## Story Description
- **As a** logged-in and verified User,
- **I want to** ask AI to refine a prompt I've generated,
- **So that** I get a clearer, more effective version without manually rewriting it.

## Acceptance Criteria (BDD Format)
- **Given** I have generated a prompt (US-3.5) and still have AI Refine quota remaining
- **When** I click `[Refine with AI]`
- **Then** the frontend calls `POST /api/v1/generated-prompts/{id}/refine`
- **And** the backend sends the prompt to the LLM Adapter (default GPT-4o) with an optimization meta-prompt
- **And** the LLM returns a refined version plus an explanation of the changes
- **And** the frontend shows a diff view: original on the left, refined on the right, with bullet-point explanations.
- **Given** I am viewing the refined result
- **When** I click `[Accept]`
- **Then** `generated_prompts.final_prompt` is replaced with the refined version.
- **Given** I am viewing the refined result
- **When** I click `[Edit manually]` or `[Reject]`
- **Then** I can either hand-edit the refined text before accepting, or discard it and keep the original.

## Exception Scenarios
- Quota exhausted → `402 Payment Required`, invites the user to upgrade to Pro.
- LLM timeout > 30s → `504 Gateway Timeout`, allows retry.
- LLM returns policy-violating content → filtered, returns a soft-refuse error instead of the raw output.

## Technical Implementation Details
- **Frontend Layer**:
  - `[Refine with AI]` button on the generated-prompt result view.
  - Diff view component (original vs. refined) with Accept / Edit manually / Reject actions.
- **Backend Layer**:
  - `POST /api/v1/generated-prompts/{id}/refine` — checks `usage_quotas`, increments `used_count`, calls the LLM Adapter, persists the result.
  - LLM Adapter pattern (per SRS §3.1) abstracts the provider (OpenAI/Anthropic/Gemini); the refine model is admin-configurable.
- **Database Layer**:
  - Persist the refined text to `generated_prompts.ai_refined`.
  - On Accept, overwrite `generated_prompts.final_prompt` with `ai_refined`.

## Business Rules
- Free plan: 5 refines/day. Pro: 100 refines/day.
- The LLM model used for refining is configurable globally by an admin.
- Unverified users cannot use AI Refine (per US-1.1 business rules).

## Verification & Testing
- Generate a prompt, click Refine → verify diff view renders with explanations.
- Click Accept → verify `final_prompt` is updated to the refined text.
- Click Reject → verify `final_prompt` is unchanged.
- Exhaust daily quota → verify `402` response and upgrade prompt.
- Simulate LLM timeout → verify `504` and retry option.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
