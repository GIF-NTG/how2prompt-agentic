# SOFTWARE REQUIREMENT SPECIFICATION

# How2Prompt

*A prompt-skill enhancement platform for AI agents*

Version: 2.0

---

## 1. Introduction

### 1.1 Purpose of the Document

This SRS document defines the detailed requirements for the How2Prompt platform — a full-stack web application that helps users improve their prompt-writing skills for popular AI agents (ChatGPT, Claude, Gemini, Midjourney, DALL·E, etc.). The document serves as a shared reference for the entire development team (Frontend, Backend, DevOps, Product) throughout the product lifecycle, from MVP through enterprise-scale expansion.

### 1.2 Product Vision

How2Prompt is built with the vision of becoming the standard platform for how people communicate with AI. Instead of leaving users to struggle writing prompts on their own (which often produces poor results), the product provides:

- A library of high-quality prompt templates, curated by experts.
- Dynamic forms that let users fill in information based on a template and automatically generate a complete prompt.
- AI-powered prompt optimization, scoring, and live testing (Playground).
- A community for sharing templates, plus team workspaces for organizations.

### 1.3 System Scope

#### 1.3.1 In Scope

- Web application (desktop-first, then responsive for tablet/mobile in Phase 2).
- Multi-model AI support: OpenAI, Anthropic, Google, Midjourney, DALL·E, and extensible to more.
- A template library curated by admins initially, gradually opened up to user submissions and the community.
- Dynamic forms that generate prompts based on variables declared in the template.
- Multi-tenancy built in from the start (personal workspace → team/enterprise workspace).
- Multi-language support (Vietnamese & English) from the MVP onward.
- Template fork & customization mechanism (Phase 2).
- Playground for live prompt testing with an LLM (Phase 2).
- Community features: upvote, comment, follow, marketplace (Phase 3).
- Freemium subscription and team features (Phase 4).

#### 1.3.2 Out of Scope — Month 1 MVP

- Native mobile apps (iOS/Android) — planned from Phase 4 onward.
- Fine-tuning a proprietary AI model.
- Payment integration (available only in Phase 4).
- API for external developers (available only in Phase 4).

### 1.4 Target Users

The product serves four main user groups, prioritized in increasing order across phases:

| Group | Description | Main Need | Priority |
|---|---|---|---|
| General Users (A) | Individuals new to AI with no technical background. | Need easy-to-understand templates to quickly create quality prompts. | Phase 1 |
| Developers / Prompt Engineers (B) | Software engineers who work extensively with LLMs. | Need technical templates (code review, debugging, refactoring), deep customization, and model comparison. | Phase 1 |
| Content Creators / Marketers / Teachers (C) | Content creators, teachers, and marketers. | Need templates for copywriting, SEO, lesson plans, and content ideas. | Phase 1 |
| Enterprises / Teams (D) | Teams and organizations that want to standardize how they use AI. | Need a shared workspace, role-based permissions, internal template sharing, and quota control. | Phase 4 |

### 1.5 Glossary

| Term | Definition |
|---|---|
| Template | A pre-designed prompt template containing variables that the user fills in through a form. |
| Variable / Field | An information field in a template that the user fills in to personalize a prompt (e.g., tone, topic, audience). |
| Generated Prompt | The complete prompt produced after the user fills in the form and the system renders the template. |
| AI Model | The target AI model the prompt is intended for (GPT-4o, Claude, Gemini, Midjourney, etc.). |
| Template Variant | A specialized version of a template optimized for a specific AI model. |
| Template Version | A version of a template (v1, v2, ...). Each major edit creates a new version while preserving history. |
| Workspace | A working space that holds templates and data. There are two types: personal and team. |
| Fork | Creating a copy of a template to customize within a user's own workspace without affecting the original. |
| Playground | An environment for testing prompts live with an LLM directly inside the app to see the output. |
| AI Refine | A feature that uses an LLM to optimize and improve the quality of a prompt written by the user. |
| AI Score | A quality score for a prompt, evaluated by AI according to criteria (clarity, specificity, context, etc.). |
| i18n | Internationalization — support for multiple languages (Vietnamese, English). |

---

## 2. Overall Description

### 2.1 Overall Architecture

The system uses a layered client-server architecture, ready to scale horizontally as the number of users grows.

- **Frontend Layer:** React SPA (Single Page Application) with TypeScript, TailwindCSS, Zustand for state management, React Query for server state, and i18next for multi-language support.
- **Backend Layer:** Spring Boot REST API (Java 21), stateless, JWT + OAuth2, using the Adapter pattern to integrate multiple AI providers.
- **Data Layer:** PostgreSQL 15+ (with JSONB for dynamic data), Redis for cache/rate-limiting/session, and S3 or MinIO for media files.
- **AI Integration Layer:** A standardized adapter for calling OpenAI, Anthropic, Google Gemini, and Midjourney (via proxy), etc., easily extensible for new models.

### 2.2 Tech Stack

| Layer | Technology | Notes |
|---|---|---|
| Frontend | React 18+, TypeScript, TailwindCSS v4, Zustand, React Query, i18next, React Router, Framer Motion | Bulletproof React structure, feature-based folders. |
| Backend | Java 21, Spring Boot 3+, Spring Security, Spring Data JPA, Flyway | REST API + Swagger/OpenAPI docs. |
| Database | PostgreSQL 15+ | Uses JSONB for dynamic data, pg_trgm for fuzzy search, tsvector for full-text search. |
| Cache | Redis 7+ | Rate limiting, session, hot templates. |
| Storage | S3 or MinIO | Cover images, avatars, media. |
| AI Provider | OpenAI, Anthropic, Google Gemini, Midjourney API | Adapter pattern in the backend. |
| Infrastructure | Docker, Docker Compose, GitHub Actions | CI/CD, container deployment. |
| Monitoring (Phase 3+) | Prometheus + Grafana, Sentry | Logs, metrics, error tracking. |

### 2.3 Core User Workflows

#### Flow 1: Generate a prompt from an existing template (UJ1) — Core MVP

1. The user logs in (email/password or Google OAuth).
2. The user browses the template library, filters by category, tag, or target model, or searches using full-text search.
3. The user selects a template, views the description and example output, and selects the AI model to use.
4. The system renders a dynamic form based on the template's list of variables.
5. The user fills in the required and optional fields and sees a real-time preview of the generated prompt.
6. The user may enter additional free-form 'Additional Instructions' for light customization.
7. The user clicks 'Generate' → the system renders the final prompt, displays it, and allows copying to the clipboard.
8. The generated prompt is automatically saved to the user's history and can be favorited.

#### Flow 2: Optimize a prompt with AI (UJ2) — Phase 2

9. The user has a prompt (from a template or written themselves) and wants to improve its quality.
10. The user clicks 'Refine with AI' → the system calls an LLM to analyze and suggest a more optimized version.
11. The system displays a comparison view: the original prompt vs. the refined prompt, along with criteria scores.
12. The user accepts, manually edits, or rejects the suggestion.

#### Flow 3: Fork and customize a template (UJ3) — Phase 2

13. The user finds a good template but wants to add/remove fields to suit their own needs.
14. The user clicks 'Fork' → the system clones the template into their personal workspace.
15. The user opens the template editor, edits the prompt body, adds/edits/removes variables, and selects the target model.
16. The user saves the template as Private (for their own use only) or Publish (shared with the community).

#### Flow 4: Enterprise sharing of internal templates (UJ4) — Phase 4

17. A company admin creates a workspace of type 'team' and invites members with roles (owner/admin/editor/viewer).
18. The admin/editor creates internal (non-public) templates and assigns categories, tags, and models.
19. Team members use the shared templates, and all changes are recorded in an audit log.
20. The company purchases a subscription plan to raise quotas (AI refine, playground, number of seats).

### 2.4 Constraints and Assumptions

- Authentication via stateless JWT (access + refresh token). The frontend stores the refresh token in an httpOnly cookie.
- No AI API keys are stored on the client — all LLM calls go through the backend proxy.
- Multi-tenancy: all template/prompt data is tied to a workspace_id. Authorization is enforced at the service layer.
- Internationalization from the start: every translatable field uses a JSONB pattern such as `{"en": "...", "vi": "..."}`.
- Soft-delete: uses a deleted_at field; important data is never hard-deleted.
- Rate limiting via Redis to prevent abuse of the LLM API.

---

## 3. Detailed Functional Requirements

User stories are grouped by Epic. Each Epic is tied to a phase in the roadmap.

### Epic 1: User Identity & Access Management (Phase 1)

| ID | Feature Name | Summary | Actor |
|---|---|---|---|
| US-1.1 | Register / Log in with email | The user registers an account with email + password. Email verification is included. | User |
| US-1.2 | Log in with Google OAuth | Support fast login via Google (later extended to GitHub, Microsoft). | User |
| US-1.3 | Manage personal profile | The user edits full_name, avatar, bio, locale, and timezone. | User |
| US-1.4 | Change / reset password | A password-reset flow via email. | User |
| US-1.5 | Auto-create personal workspace | Upon registration, the system automatically creates a personal workspace for the user. | User |

*Acceptance criteria: Every API (except auth/register) requires a valid JWT. Tokens auto-refresh on expiry. OAuth callbacks are secured per the OIDC standard.*

### Epic 2: Template Discovery & Browsing (Phase 1)

| ID | Feature Name | Summary |
|---|---|---|
| US-2.1 | Browse templates by category | Display a list of categories (Writing, Coding, Marketing, etc.) with template counts. |
| US-2.2 | Filter by tag & AI model | Filter by tag and target model (GPT-4o, Claude, Midjourney, etc.). |
| US-2.3 | Full-text template search | Search templates by title and description (supports EN & VI). |
| US-2.4 | View template details | The detail page shows the description, guide, example output, per-model variants, and usage count. |
| US-2.5 | Featured & trending templates | The homepage shows featured templates (marked by admins via featured_at) and trending templates. |

*Acceptance criteria: Search latency < 200ms for 10K templates. Results are paginated and sortable (newest, most popular).*

### Epic 3: Prompt Generation Engine (Phase 1 — Core MVP)

| ID | Feature Name | Summary |
|---|---|---|
| US-3.1 | Render dynamic form | The frontend reads the list of template_variables and renders an appropriate form (text, textarea, select, multiselect, number, boolean, slider, etc.). |
| US-3.2 | Input validation per configuration | Apply the rules defined in the JSONB validation field (min, max, regex, required). |
| US-3.3 | Real-time preview | When the user changes a field, the prompt preview updates immediately via client-side rendering. |
| US-3.4 | Additional instructions field | A free-form field at the end of the form for the user to add custom instructions. |
| US-3.5 | Select target model | The user selects an AI model (GPT-4o, Claude, etc.). If the template has a variant for that model, the variant is used. |
| US-3.6 | Generate prompt (backend render) | The backend is the source of truth: it re-renders the final prompt to ensure consistency and enable auditing. |
| US-3.7 | Copy to clipboard | A copy button with a confirmation toast. |
| US-3.8 | Auto-save to history | After generation, the prompt is saved to generated_prompts along with its input_values. |

*Acceptance criteria: Prompts render correctly with every type of placeholder syntax. Backend rendering must match the frontend preview. History is saved asynchronously without blocking the UX.*

### Epic 4: Prompt History & Favorites (Phase 1)

| ID | Feature Name | Summary |
|---|---|---|
| US-4.1 | Personal prompt history | The History page shows generated prompts, filterable by template, model, and date. |
| US-4.2 | View and reload | Clicking a history item reopens the form with its previous input_values. |
| US-4.3 | Favorite templates | Users can mark templates as favorites and view the 'My Favorites' page. |
| US-4.4 | Delete / restore history | Soft-delete history, with an option for permanent deletion. |

### Epic 5: Admin & Content Management (Phase 1)

| ID | Feature Name | Summary |
|---|---|---|
| US-5.1 | Manage AI models | Admin CRUD for the list of models, default configuration, and capabilities. |
| US-5.2 | Manage categories & tags | Admin CRUD for taxonomy, supporting nested categories. |
| US-5.3 | Create & approve templates | Admins create official templates (is_official = true) and review user-submitted templates. |
| US-5.4 | Template editor | An editor for modifying the prompt body, variables, per-model variants, and publish/unpublish status. |
| US-5.5 | Analytics dashboard | Statistics on number of users, prompts generated, popular templates, and most-used models. |

### Epic 6: AI Enhancement (Phase 2)

| ID | Feature Name | Summary |
|---|---|---|
| US-6.1 | AI refine prompt | Calls an LLM to improve a user-written prompt and returns an optimized version. |
| US-6.2 | AI score prompt | Scores a prompt against criteria (clarity, specificity, context, format). |
| US-6.3 | Multi-model translation | Converts a prompt from one model's format to another's (e.g., from GPT to Claude). |
| US-6.4 | Playground | Live prompt testing: select a model, call the API, and display the response and metadata (tokens, latency). |
| US-6.5 | Share a prompt via public link | Generates a share_slug so a prompt can be shared externally and viewed without logging in. |

### Epic 7: Template Customization & Versioning (Phase 2)

| ID | Feature Name | Summary |
|---|---|---|
| US-7.1 | Fork template | Clones the original template into the user's personal workspace, keeping a reference to forked_from_template_id. |
| US-7.2 | Edit personal template | The user performs CRUD on variables, the prompt body, and the target model within the fork. |
| US-7.3 | Version control | Each save creates a new template_version, preserving history. Old history still uses the old version. |
| US-7.4 | Submit template to the community | The user publishes a template to a pending state → admin approves it. |

### Epic 8: Community & Social (Phase 3)

| ID | Feature Name | Summary |
|---|---|---|
| US-8.1 | Upvote / downvote template | Polymorphic voting (template / generated_prompt / comment). |
| US-8.2 | Threaded comments & replies | Hierarchical comments (parent_id) on templates and generated prompts. |
| US-8.3 | Follow author | Follow other users to be notified when they publish a new template. |
| US-8.4 | Trending / featured / newest | A community discovery page. |
| US-8.5 | Report abuse | Report a template/comment/user for violations — handled by admin moderation. |
| US-8.6 | Public user profile | A public page at /u/{username} showing the user's public templates and prompts. |
| US-8.7 | Notification system | In-app notifications for comments, follows, template approvals, etc. |

### Epic 9: Team Workspace & Billing (Phase 4)

| ID | Feature Name | Summary |
|---|---|---|
| US-9.1 | Create team workspace | A company creates a workspace of type 'team' and invites members via email. |
| US-9.2 | Role-based access control | Owner/Admin/Editor/Viewer with corresponding permissions. |
| US-9.3 | Shared template library | A team's internal templates, not shared publicly with the community. |
| US-9.4 | Team analytics | Statistics on most-used templates, active members, and quota usage. |
| US-9.5 | Freemium subscription | Free / Pro / Team Starter / Team Pro. Integrated with Stripe. |
| US-9.6 | Usage quota enforcement | Counts and limits AI Refine calls, Playground calls, and template creation per plan. |
| US-9.7 | Developer API access | Issues API keys, manages scopes, and logs call history. |
| US-9.8 | Audit log | Records all significant actions for enterprise compliance. |

---

## 4. Data & Interface Specifications

### 4.1 Database Design Principles

- PostgreSQL 15+ as the primary database. UUID as the primary key (gen_random_uuid) for safe exposure and easy merging.
- Multi-tenancy ready: every business table includes a workspace_id.
- Soft-delete using a deleted_at field plus a partial index for efficient querying.
- Standard audit fields: created_at, updated_at, created_by. A trigger auto-updates updated_at.
- JSONB for dynamic data (i18n, options, validation, capabilities) — with a GIN index where needed.
- Full-text search using tsvector with an auto-update trigger. Fuzzy search with pg_trgm.
- Polymorphic pattern (target_type + target_id) for votes, comments, and reports.
- Denormalized counters (usage_count, upvote_count) updated at the service layer for fast list queries.

### 4.2 Main Table Groups

| Group | Main Tables | Purpose |
|---|---|---|
| Identity & Tenancy | users, user_identities, workspaces, workspace_members | Authentication, authorization, multi-tenancy. |
| AI Catalog | ai_models | Catalog of supported AI models. |
| Taxonomy | categories, tags | Template classification. |
| Templates (core) | templates, template_versions, template_variables, template_variants, template_categories, template_tags, template_models | The heart of the system. |
| Generated Prompts | generated_prompts | History of prompts generated by users. |
| Community | favorites, votes, comments, follows, reports | Community interactions. |
| Billing | plans, subscriptions, usage_quotas | Freemium and enterprise billing. |
| System | audit_logs, notifications, api_keys, refresh_tokens | Operations and security. |

Full details of all tables, columns, indexes, and constraints are specified in the accompanying schema SQL file (schema.sql / how2prompt.dbml).

### 4.3 API Format (REST)

- Base URL: `/api/v1`
- Auth header: `Authorization: Bearer <access_token>` for every endpoint except `/auth/*`.
- Standard error format: `{ "error": { "code": "STRING_CODE", "message": "Human readable", "details": {} } }`
- Pagination: cursor-based for long lists (`?cursor=...&limit=20`).
- Payload format: JSON, all fields use snake_case.

#### Main Endpoints (MVP)

| Endpoint | Method | Description |
|---|---|---|
| /auth/register | POST | Register a new user and auto-create a personal workspace. |
| /auth/login | POST | Log in with email/password, returns access + refresh tokens. |
| /auth/oauth/google | GET/POST | Log in via Google OIDC. |
| /auth/refresh | POST | Refresh the access token using the refresh token. |
| /users/me | GET / PATCH | View / update the personal profile. |
| /workspaces | GET / POST | List a user's workspaces; create a new workspace (Phase 4). |
| /ai-models | GET | List active AI models. |
| /categories | GET | List categories (including nested). |
| /tags | GET | List popular tags. |
| /templates | GET | List templates with filters (category, tag, model, search). |
| /templates/{id} | GET | Template details with current version, variables, and variants. |
| /templates/{id}/favorite | POST / DELETE | Toggle favorite. |
| /templates/{id}/generate | POST | Render prompt (backend is the source of truth). |
| /generated-prompts | GET | Personal prompt history, paginated. |
| /generated-prompts/{id} | GET / DELETE | View details / delete. |
| /admin/templates | POST / PATCH | Admin CRUD for templates (requires is_admin). |
| /admin/ai-models | POST / PATCH | Admin CRUD for models. |

#### Phase 2+ Endpoints (Extension)

- `POST /generated-prompts/{id}/refine` — AI Refine.
- `POST /generated-prompts/{id}/score` — AI Score.
- `POST /playground/run` — Run a prompt in the playground.
- `POST /templates/{id}/fork` — Fork a template into the personal workspace.
- `POST /templates/{id}/comments` — Post a comment (Phase 3).
- `POST /subscriptions` — Subscribe to a plan (Phase 4).
- `POST /api-keys` — Create an API key (Phase 4).

### 4.4 Third-Party Integrations

| Integration | Phase | Notes |
|---|---|---|
| Google OAuth (OIDC) | Phase 1 | Fast login. |
| OpenAI API | Phase 2 | AI Refine, Score, Playground. |
| Anthropic API | Phase 2 | AI Refine, Score, Playground. |
| Google Gemini API | Phase 2 | Playground. |
| Midjourney (proxy) | Phase 2 | Prompts for the image model. |
| Stripe | Phase 4 | Subscription billing. |
| SendGrid / Resend | Phase 1 | Sends verification emails, password resets, and notifications. |
| Sentry | Phase 2 | Error tracking. |

---

## 5. Non-Functional Requirements

### 5.1 Performance

- First Contentful Paint (FCP) < 1.5s on a 4G network.
- Time to Interactive (TTI) < 3s.
- API response time p95 < 300ms for read endpoints, < 500ms for write endpoints.
- Full-text template search p95 < 200ms with 10K templates.
- Frontend prompt preview render < 50ms.

### 5.2 Security

- Password hashing with BCrypt / Argon2, cost >= 12.
- JWT signed with RS256 (asymmetric). 15-minute access tokens, 30-day refresh tokens stored in an httpOnly cookie.
- HTTPS mandatory in production, with HSTS and a strict Content-Security-Policy.
- Rate limiting: 60 requests/minute for regular users, 600/minute for Pro users; API keys are locked on anomalies.
- No AI API keys stored on the client. All LLM calls go through the backend.
- Input sanitization to prevent prompt injection and XSS (especially in template bodies).
- Compliant with the OWASP Top 10. CSRF tokens for form-based flows.
- Data isolation: every query must filter by workspace_id/user_id. The frontend is never trusted.
- Audit log for sensitive actions (admin login, template deletion, plan changes).

### 5.3 Scalability

- Stateless backend, deployed as multiple pods behind a load balancer.
- Redis used for sessions, rate limiting, and caching hot templates — enabling horizontal scaling.
- DB read replicas for heavy queries starting in Phase 3+.
- CDN for static assets and cover images.
- Job queue (RabbitMQ or Redis Streams) for heavy tasks (AI refine, playground calls) in Phase 2.

### 5.4 Reliability

- Uptime target of 99.5% for the MVP, 99.9% for Phase 4 (enterprise).
- Daily database backups with 30-day retention. Point-in-time recovery from Phase 3.
- Circuit breaker for LLM calls (Resilience4j). Clear fallback behavior when a provider is down.
- Health check endpoint `/actuator/health` for Kubernetes.

### 5.5 Internationalization

- Languages supported at MVP: Vietnamese (vi), English (en).
- Frontend: i18next with JSON resource files, automatically detecting locale from user.locale.
- Database: JSONB for translatable fields (title, description, label, options).
- Fallback: if the current language is missing, the English version is shown.

### 5.6 Accessibility

- Meets WCAG 2.1 level AA on the main screens.
- Full keyboard navigation with clear focus indicators.
- Contrast ratio >= 4.5:1 for normal text.
- Screen reader support (complete ARIA labels).

### 5.7 Maintainability

- Codebase follows SOLID and DRY principles. Frontend follows Bulletproof React; backend follows Clean Architecture (Domain/Application/Infrastructure).
- Unit test coverage >= 70% for the backend, >= 60% for the frontend.
- Integration tests for critical flows (auth, prompt generation, billing).
- API docs auto-generated with Swagger/OpenAPI, always kept up to date.
- CI/CD with GitHub Actions: lint → test → build → deploy staging → deploy production (with approval).

---

## 6. Development Roadmap

### Phase 1 — MVP (Month 1)

Goal: launch a usable MVP version, focused on the core flow.

- Auth (email + Google OAuth), auto-created personal workspace.
- Browse templates, categories, tags, and search.
- Generate prompts from existing templates (core MVP), copy to clipboard.
- Additional Instructions field.
- Prompt history, favorites.
- Admin panel: CRUD for templates, categories, tags, and models.
- i18n EN/VI.
- Seed 30-50 high-quality templates curated by admins.
- Production deployment on Docker + VPS/Railway.

### Phase 2 — AI Enhancement (Months 2-3)

- AI Refine, AI Score.
- Multi-model variants & translation.
- Playground for live prompt testing.
- Share prompts via public link.
- Fork templates and customize fields.
- Template versioning.
- User template submission (moderation queue).

### Phase 3 — Community (Months 4-6)

- Upvote/downvote, threaded comments, follow author.
- Trending / featured / newest.
- Report abuse, moderation dashboard.
- Public user profile.
- Notification system.

### Phase 4 — Enterprise & Monetization (Month 6+)

- Team workspace, role-based access.
- Internal shared template library.
- Freemium subscription (Stripe), usage quota enforcement.
- Team analytics dashboard.
- Developer API access + API key management.
- Full audit log for compliance.
- Mobile app (React Native).

---

## 7. Risks and Assumptions

| Risk / Assumption | Level | Mitigation |
|---|---|---|
| LLM API costs rise quickly as users grow | High | Apply rate limiting, cache aggressively, open AI Refine only to verified users, enforce Freemium quotas. |
| Initial template quality determines retention | High | Admins curate 30-50 quality templates with clear example outputs. |
| Slow launch due to over-engineering | Medium | Limit MVP scope to Phase 1, keep the schema extensible. |
| Users don't understand how to use templates | Medium | Inline guides in templates, example outputs, tooltips for each field. |
| UGC spam in Phase 3 | Medium | Moderation queue, report abuse, rate-limit template creation. |
| Vendor lock-in with a single LLM provider | Low | Adapter pattern from the start, easy to swap providers. |
| Data compliance (GDPR, Vietnam's Decree 13) | Medium | From Phase 4: audit log, data deletion rights, personal data export. |

---

## 8. Appendix

- **schema.sql** — Full PostgreSQL migration for all tables and indexes.
- **how2prompt.dbml** — ERD diagram in DBML format, directly importable into dbdiagram.io.
- **OpenAPI spec (next up in Phase 1)** — Auto-generated from Spring Boot Swagger, hosted at `/swagger-ui`.
