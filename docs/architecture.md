# System Architecture & Integrations — how2prompt

The how2prompt platform is designed to allow developers to create, edit, copy, and optimize prompt templates in under 3 seconds using a keyboard-first web workspace.

## Component Overview

The platform uses a layered multi-tier architecture to decouple state storage, REST endpoints, UI interactions, and LLM processing:

```text
+-----------------------------------------------------------+
|                        Frontend                           |
|                       React SPA                           |
|      (Context API State, Tailwind CSS, Keyboard-First)    |
+-----------------------------+-----------------------------+
                              |
                     REST (JWT Auth Header)
                              v
+-----------------------------------------------------------+
|                    Core Backend Gateway                   |
|                     Java Spring Boot                      |
|       (Relational Logic, JWT Auth, History Tracking)      |
+-------------+-------------------------------+-------------+
              |                               |
          SQL queries                     REST POST
              v                               v
+-------------+-------------+    +-------------+-------------+
|          Database         |    |        Agentic Backend    |
|         PostgreSQL        |    |         FastAPI Service   |
|   (JSONB for variables)   |    |    (LiteLLM LLM Wrapper)  |
+---------------------------+    +--------------+------------+
                                                |
                                            LLM API
                                                v
                                 +--------------+------------+
                                 |         LLM Providers     |
                                 |     (Anthropic / OpenAI)  |
                                 +---------------------------+
```

### 1. Frontend (React SPA)
- **Tech Stack:** React 18+, Tailwind CSS 3+, Context API.
- **Role:** Renders the keyboard-driven variable canvas. Allows users to insert variables (Variable Pills) inline like `{role}` or `{language}` and type values by tabbing through pills. Pressing `Ctrl+Enter` copies the compiled text to the clipboard and triggers history recording.

### 2. Core Backend (Java Spring Boot)
- **Tech Stack:** Java 17+, Spring Boot 3+, Spring Security.
- **Role:** Handles identity management, JWT verification, saving and retrieving templates, user variables configurations, and request history. It acts as the gateway controller orchestrating requests to the Postgres database and the Python prompt optimizing agent.

### 3. Database (PostgreSQL)
- **Tech Stack:** PostgreSQL 15+.
- **Role:** Persists relational data (users, teams, templates, copy history logs) and implements JSONB fields to dynamically save variable mapping configurations without introducing complex schemas.

### 4. Agentic Backend (how2prompt-agentic)
- **Tech Stack:** Python 3.11+, Poetry 1.8+, FastAPI 0.110+, LiteLLM 1.30+, Pydantic 2.6+.
- **Role:** A completely stateless, high-performance web service built with FastAPI. It handles optimization requests by querying LLM providers (Anthropic, OpenAI, etc.) using LiteLLM. It parses input prompt ideas and outputs clean templates with detected variables using Pydantic structured output models.

---

## Service Integration Workflow

Below is the step-by-step lifecycle of a prompt optimization request:

1. **User Action:** The user inputs a prompt concept (e.g. `"Review this C# code checking security and performance"`) and clicks "Optimize" or uses the keyboard shortcut.
2. **Client Request:** The React client initiates a `POST` request to the Spring Boot endpoint `/api/v1/templates/optimize` carrying the JWT payload.
3. **Session Verification & Context Gathering:**
   - Spring Boot validates the JWT signature and extracts the user session.
   - Spring Boot queries PostgreSQL for the user's active variables (e.g., active language, target environment) and team-wide standards.
   - Spring Boot constructs a payload containing the prompt idea, active variables, and team coding guidelines.
4. **Agent Delegation:** Spring Boot sends a `POST` request containing this payload to the Python agentic service at `/api/v1/agent/optimize`.
5. **LLM Optimizations:**
   - The Python service receives the request, validates the input using Pydantic models, and formats instructions for the LLM.
   - The LLM client calls the LLM provider (like Anthropic Claude 3.5 Sonnet) via LiteLLM.
   - The LLM client extracts a structured response containing:
     - `template`: A prompt containing variable placeholders like `{variable_pills}` (e.g. `"Please review this code for security vulnerabilities. Standards to apply: {team_coding_standards}."`).
     - `detected_variables`: A list of the parsed placeholder names.
     - `explanation`: A summary of changes.
6. **Persistence and Response:**
   - Spring Boot receives the JSON response from the Python service.
   - Spring Boot writes a snapshot record containing the template id and the variable configurations into the PostgreSQL `history` table.
   - The Spring Boot backend maps the response to the client format and sends it back to the React UI.
   - The React UI displays the variables as editable inline Pills on the canvas workspace.
