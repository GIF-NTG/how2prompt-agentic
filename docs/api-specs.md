# API Specifications — how2prompt

This document details the HTTP data contracts for the `how2prompt` backend services. All endpoints require strict JSON payloads. Core endpoints communicate state using JWT tokens in the `Authorization: Bearer <JWT>` header.

---

## 1. Gateway Backend Endpoints (Spring Boot)

These endpoints handle authentication, template persistence, user variables storage, and copy histories.

### JWT Authentication
- **Endpoint:** `POST /api/v1/auth/login`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "developer1",
    "password": "secure_password"
  }
  ```
- **Response Body (200 OK):**
  ```json
  {
    "token": "eyJhbGciOiJIUzI1NiIsIn..."
  }
  ```

### Templates Management
- **Endpoint:** `/api/v1/templates`
- **Methods:**
  - `GET`: Returns lists of system templates, user-created templates, and team-shared templates.
  - `POST`: Creates a new template.
- **Request Body (POST):**
  ```json
  {
    "name": "C# Code Review",
    "content": "Please review this C# code: {code_to_review}. Coding standards: {team_coding_standards}.",
    "tags": ["csharp", "code-review"],
    "team_shared": true
  }
  ```

### User Variables Configs
- **Endpoint:** `/api/v1/users/me/variables`
- **Methods:**
  - `GET`: Fetches user variables mapping.
  - `PUT`: Sets or updates user variables.
- **Request Body (PUT):**
  ```json
  {
    "team_coding_standards": "Prefer LINQ queries where readability improves, avoid nested loops.",
    "target_framework": ".NET 8"
  }
  ```

### Quick History Drawer
- **Endpoint:** `/api/v1/history`
- **Methods:**
  - `GET`: Returns the user's past copied snapshots (paginated, maximum default 20 records).
  - `POST`: Saves a new snapshot. Called silently in the background when `Ctrl+Enter` is clicked.
- **Request Body (POST):**
  ```json
  {
    "template_id": "8f244199-a9a7-40d6-848e-f14d9b012674",
    "variable_snapshot": {
      "code_to_review": "public void Run() { ... }",
      "team_coding_standards": "Prefer LINQ queries where readability improves, avoid nested loops.",
      "target_framework": ".NET 8"
    }
  }
  ```

---

## 2. Agentic Prompt Service Endpoint (`how2prompt-agentic`)

This endpoint is stateless and performs structural analyses/optimizations.

- **Endpoint:** `/api/v1/agent/optimize`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "prompt_idea": "write a python script to fetch web urls",
    "team_standards": "Always write docstrings and enforce type hints.",
    "variables": {
      "language": "python"
    }
  }
  ```
- **Response Body (200 OK):**
  ```json
  {
    "template": "Write a highly optimized {language} script to fetch a list of web URLs. Ensure you follow these coding rules: {team_standards}.",
    "detected_variables": ["language", "team_standards"],
    "explanation": "Structured the prompt, extracted active language and injected team guidelines as variable placeholders."
  }
  ```

---

## 3. RFC-7807 Error Responses

The agentic service and gateway return error payloads matching the **RFC-7807 (Problem Details for HTTP APIs)** standard.

### Example: Upstream LLM Failure (HTTP 502 Bad Gateway)
If the AI provider (e.g. Anthropic/OpenAI) is rate-limited or offline, the service intercepts the failure and returns a structured payload:

```json
{
  "type": "https://how2prompt.com/errors/llm-provider-error",
  "title": "Bad Gateway",
  "status": 502,
  "detail": "The agentic prompt service received an invalid response or timeout from the upstream LLM provider.",
  "instance": "/api/v1/agent/optimize",
  "error_code": "LLM_PROVIDER_ERROR"
}
```

### Example: Validation Schema Error (HTTP 422 Unprocessable Entity)
If request validation parameters fail validation schemas (e.g. missing required `prompt_idea` field):

```json
{
  "type": "https://how2prompt.com/errors/validation-error",
  "title": "Unprocessable Entity",
  "status": 422,
  "detail": "Field 'prompt_idea' is required but was missing in the request payload.",
  "instance": "/api/v1/agent/optimize",
  "error_code": "VALIDATION_ERROR"
}
```
