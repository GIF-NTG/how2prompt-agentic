# Business Analysis Specification Document (BA) — How2Prompt Web App

This document serves as the Business Analyst (BA) specification for **How2Prompt**, detailing the functional requirements, prioritized user stories, BDD acceptance criteria, data definitions, and edge cases mapped from the Software Requirements Specification ([srs.md](../docs/srs.md)) and [use-cases.md](../docs/use-cases.md).

---

## 1. Project Vision & User Persona Mapping

### 1.1 Product Vision

**How2Prompt** is a full-stack web application that helps users improve their prompt-writing skills for popular AI agents (ChatGPT, Claude, Gemini, Midjourney, DALL·E, etc.). The platform provides:

- A library of high-quality prompt templates, curated by experts.
- Dynamic forms that let users fill in information based on a template and automatically generate a complete prompt.
- AI-powered prompt optimization, scoring, and live testing (Playground) in Phase 2.
- A community for sharing templates, plus team workspaces for organizations in later phases.

### 1.2 Persona & Access Matrix

| Feature / Action | Guest (Unauthenticated) | User (Registered) | Admin (System Administrator) |
| :--- | :---: | :---: | :---: |
| Browse Template Library & Search | Yes | Yes | Yes |
| View Template Details | Yes | Yes | Yes |
| Register / Login | Yes | — | — |
| Select AI Model & Fill Dynamic Form | No | Yes | Yes |
| Generate & Copy Prompt | No | Yes | Yes |
| View Real-Time Prompt Preview | No | Yes | Yes |
| View Prompt History | No | Yes | Yes |
| Reload Prompt from History | No | Yes | Yes |
| Favorite / Unfavorite Templates | No | Yes | Yes |
| Delete Prompt History | No | Yes | Yes |
| Manage AI Models (CRUD) | No | No | Yes |
| Manage Categories & Tags | No | No | Yes |
| Create & Publish Official Templates | No | No | Yes |
| View Analytics Dashboard | No | No | Yes |

*Note: Additional personas (Author, Workspace Owner/Admin/Editor/Viewer) are introduced in Phase 2-4. See [srs.md §1.4](../docs/srs.md) and [use-cases.md §1.2](../docs/use-cases.md) for the full actor list.*

---

## 2. Epic & User Story Specifications (BDD Format)

### Epic 1: User Identity & Access Management (Phase 1)

#### US-1.1: Register a New Account (UC-01.01) — Priority: P1

As a Guest,
I want to register a new account using my email,
So that I can use the platform and have my own personal workspace.

* **Acceptance Criteria:**
  * **Given** I am on the Register page.
  * **When** I submit a valid email, password, display name, and locale (vi/en).
  * **Then** the system creates my account and my personal workspace (type='personal').
  * **And** the system sends a verification email with a token valid for 24 hours.
  * **And** I receive access and refresh tokens and am redirected to the home page with a verification banner.

* **Exception Scenarios:**
  * Email already exists → `409 Conflict`, displays "Email is already in use".
  * Password not strong enough (< 8 chars, missing letters/numbers) → `422 Unprocessable Entity`.
  * Rate limit exceeded (10 req/min/IP) → `429 Too Many Requests`.

* **Business Rules:**
  * Each user has exactly one Personal Workspace, which cannot be deleted.
  * Unverified users can still use the app but are limited (cannot create public templates, cannot use AI Refine in Phase 2).

#### US-1.2: Log In with Email + Password (UC-01.02) — Priority: P1

As a Registered User,
I want to log in with my email and password,
So that I can access my workspace and saved prompts.

* **Acceptance Criteria:**
  * **Given** I have a registered account.
  * **When** I submit the correct email and password on the Login page.
  * **Then** I am authenticated and redirected to the dashboard.
  * **And** the system issues an access token (stored in memory) and a refresh token (stored in httpOnly cookie).
  * **And** `users.last_login_at` is updated.

* **Exception Scenarios:**
  * Wrong email or password → `401 Unauthorized` (does not reveal which field is wrong).
  * Account suspended → `403 Forbidden`.
  * 5 failed login attempts within 15 minutes → temporarily locked, requiring CAPTCHA.

* **Business Rules:**
  * Access tokens are valid for 15 minutes, signed with RS256 (asymmetric).
  * Refresh tokens are valid for 30 days and rotate on each use.

#### US-1.3: Log In with Google OAuth (UC-01.03) — Priority: P1

As a Guest,
I want to log in using my Google account,
So that I can access the platform quickly without creating a new password.

* **Acceptance Criteria:**
  * **Given** I click "Sign in with Google" on the Login/Register page.
  * **When** I approve the consent on Google's authorization page.
  * **Then** the system logs me in.
  * **And** if I don't have an account, the system automatically creates one along with a personal workspace.

* **Exception Scenarios:**
  * Guest declines consent → redirected back to login with an error message.
  * Email from Google matches an existing email/password account → merges identities, requiring confirmation.
  * Google returns an error/timeout → `502 Bad Gateway`, displays "Please try again".

#### US-1.4: Log Out (UC-01.04) — Priority: P1

As a Logged-in User,
I want to log out of my account,
So that my session is securely terminated on this device.

* **Acceptance Criteria:**
  * **Given** I am logged in.
  * **When** I click "Log out" from the profile menu.
  * **Then** my refresh token is revoked (`revoked_at` set) and the httpOnly cookie is cleared.
  * **And** the access token is cleared from memory.
  * **And** I am redirected to the public home page.

#### US-1.5: Forgot & Reset Password (UC-01.05) — Priority: P1

As a Guest,
I want to reset my password via email,
So that I can recover access to my account if I forget my password.

* **Acceptance Criteria:**
  * **Given** I submit my registered email in the "Forgot password" form.
  * **When** I click the reset link in the email and enter a new password.
  * **Then** my password is updated (BCrypt hashed, cost >= 12) and all old refresh tokens are revoked.
  * **And** I am redirected to the Login page.

* **Exception Scenarios:**
  * Email doesn't exist → still returns `200 OK` (prevents enumeration).
  * Reset token expired or already used → `410 Gone`, requiring a new request.

#### US-1.6: Verify Email (UC-01.06) — Priority: P1

As a Newly Registered User,
I want to verify my email address,
So that my account is fully activated.

* **Acceptance Criteria:**
  * **Given** I have received a verification email.
  * **When** I click the verification link.
  * **Then** my `email_verified_at` is updated.
  * **And** the verification reminder banner disappears.

* **Alternative Flow:**
  * User can request the email to be resent from the banner (rate limited to once per 5 minutes).

#### US-1.7: Manage Personal Profile (UC-01.07) — Priority: P2

As a Logged-in User,
I want to update my profile information,
So that my personal details and locale preferences are accurate.

* **Acceptance Criteria:**
  * **Given** I am on the Profile Settings page (`/settings/profile`).
  * **When** I update my full name, avatar, bio, username, locale, or timezone.
  * **Then** the system validates and saves the changes.
  * **And** the UI immediately reflects my locale preference (i18n).

* **Exception Scenarios:**
  * Username already exists → `409 Conflict`, suggests another username.
  * Image exceeds 2MB → `413 Payload Too Large`.

---

### Epic 2: Template Discovery & Browsing (Phase 1)

#### US-2.1: Browse the Template Library (UC-02.01) — Priority: P1

As a User or Guest,
I want to browse the template library,
So that I can discover available templates.

* **Acceptance Criteria:**
  * **Given** I navigate to the `/explore` page.
  * **When** the page loads.
  * **Then** I see a paginated grid of public templates sorted by popularity.
  * **And** templates with `is_official=true` are prioritized at the top.
  * **And** templates with `deleted_at` set are not shown.

#### US-2.2: Filter by Category / Tag / AI Model (UC-02.02) — Priority: P1

As a User or Guest,
I want to filter templates by category, tag, and AI model,
So that I can find the most relevant templates for my needs.

* **Acceptance Criteria:**
  * **Given** the template list is being displayed.
  * **When** I select categories, tags, and/or an AI model from the filter controls.
  * **Then** the list is narrowed by the filters and the URL query string is updated (deep-linkable).
  * **And** a total count badge reflects the filtered results.

#### US-2.3: Full-Text Search Templates (UC-02.03) — Priority: P1

As a User or Guest,
I want to search templates by keyword,
So that I can quickly find a template by name or description.

* **Acceptance Criteria:**
  * **Given** I type a keyword into the search box (e.g., "email marketing").
  * **When** the frontend debounces for 300ms and sends the search request.
  * **Then** the results are ranked by relevance (`ts_rank + usage_count`).
  * **And** search latency is p95 < 200ms with 10,000 templates.

* **Business Rules:**
  * Search uses `tsvector` with `to_tsquery`, with a `pg_trgm` fallback for fuzzy matching.
  * Supports both English and Vietnamese.

#### US-2.4: View Template Details (UC-02.04) — Priority: P1

As a User or Guest,
I want to view the details of a template,
So that I can understand what it does before using it.

* **Acceptance Criteria:**
  * **Given** I click on a template card.
  * **When** the detail page loads.
  * **Then** I see the description, example output, usage guide, list of variables, list of supported models, and buttons: `[Use template]`, `[Favorite]`.
  * **And** `view_count` is incremented asynchronously.

* **Exception Scenarios:**
  * Template doesn't exist or has been deleted → `404`.
  * Template is private to another workspace → `403`.

#### US-2.5: View Featured / Trending Templates (UC-02.05) — Priority: P2

As a User or Guest,
I want to see featured and trending templates on the homepage,
So that I can discover popular and recommended templates.

* **Acceptance Criteria:**
  * **Given** I visit the homepage.
  * **When** the page loads.
  * **Then** I see two separate sections: Featured (marked by admins via `featured_at`) and Trending (calculated by `usage_count` over the last 7 days).
  * **And** results are cached in Redis for 10 minutes.

---

### Epic 3: Prompt Generation Engine (Phase 1 — Core MVP)

#### US-3.1: Select the Target AI Model for a Prompt (UC-03.01) — Priority: P1

As a User,
I want to select a target AI model for my template,
So that the generated prompt uses the optimal format for that specific AI.

* **Acceptance Criteria:**
  * **Given** I am on the template usage page and click `[Use template]`.
  * **When** I select an AI model from the supported models dropdown.
  * **Then** the system loads the corresponding variant if `template_variants` exists; otherwise, it uses the original `prompt_body`.

* **Alternative Flow:**
  * If the template supports only one model, the dropdown is hidden and auto-selected.

#### US-3.2: Fill In the Dynamic Form per Template (UC-03.02) — Priority: P1

As a User,
I want to fill in a dynamic form tailored to the template I chose,
So that I can provide the specific inputs needed to generate my prompt.

* **Acceptance Criteria:**
  * **Given** a template and model have been selected.
  * **When** the form renders.
  * **Then** the frontend reads `template_variables` and renders appropriate field types (text, textarea, select, multiselect, number, boolean, slider, etc.).
  * **And** labels, placeholders, and help text are displayed in the current locale (from JSONB i18n data).
  * **And** client-side validation runs per the configuration (min, max, regex, minLength).
  * **And** if required fields aren't filled, the Generate button is disabled.

#### US-3.3: View Real-Time Prompt Preview (UC-03.03) — Priority: P1

As a User,
I want to see a real-time preview of my prompt as I fill in the form,
So that I can immediately see how my inputs affect the final prompt.

* **Acceptance Criteria:**
  * **Given** I am filling in the dynamic form.
  * **When** I change any field value.
  * **Then** the frontend runs the Template Renderer (client-side): replacing `{{placeholder}}` with the current value.
  * **And** the preview displays in monospace with syntax highlighting for unfilled placeholders.
  * **And** it shows a character count and token estimate.

* **Business Rules:**
  * The client-side preview is for UX only; the final value is always re-rendered by the backend (US-3.6).

#### US-3.4: Add Optional Additional Instructions (UC-03.04) — Priority: P2

As a User,
I want to add free-form additional instructions to my prompt,
So that I can customize the template without needing to fork it.

* **Acceptance Criteria:**
  * **Given** I am on the Generate form.
  * **When** I type in the "Additional instructions (optional)" textarea.
  * **Then** the renderer appends this string to the end of `prompt_body`, or inserts it at the `{{__extra__}}` placeholder location if declared.
  * **And** the content is escaped to guard against prompt injection.

#### US-3.5: Generate & Copy the Complete Prompt (UC-03.05) — Priority: P1

As a User,
I want to generate and copy the final prompt,
So that I can paste it into my AI tool of choice.

* **Acceptance Criteria:**
  * **Given** I have filled in all required fields.
  * **When** I click "Generate".
  * **Then** the frontend calls `POST /api/v1/templates/{id}/generate` with the payload `{ template_version_id, ai_model_id, input_values, extra_instructions }`.
  * **And** the backend renders the final prompt, saves it to `generated_prompts`, and increments `templates.usage_count`.
  * **And** I can click "Copy" to save the prompt to my clipboard with a confirmation toast.

* **Exception Scenarios:**
  * Backend rendering error (invalid placeholder) → `500` with detailed logs; frontend shows "An error occurred, please try again".

#### US-3.6: Backend Renders the Prompt — Source of Truth (UC-03.06) — Priority: P1

As the System,
I want to render the final prompt on the backend,
So that prompt integrity, consistency, and auditing are ensured.

* **Acceptance Criteria:**
  * **Given** the system receives a generate request.
  * **When** the render engine processes the payload.
  * **Then** it loads `template_versions` and `template_variants`, selects the appropriate `prompt_body`, resolves `{{var_key}}` → `input_values[var_key]`, handles defaults, removes empty optional placeholders, appends `extra_instructions`, and sanitizes the output.
  * **And** saves the result to `generated_prompts` with `final_prompt`, `input_values` (JSONB), `workspace_id`, `ai_model_id`, `template_version_id`.

* **Business Rules:**
  * The renderer is a separate service with >= 90% unit test coverage.
  * All important validation (required, regex) is re-run on the backend — the frontend is never trusted.

---

### Epic 4: Prompt History & Favorites (Phase 1)

#### US-4.1: Automatically Save Prompt History (UC-04.01) — Priority: P1

As the System,
I want to automatically save generated prompts,
So that users don't lose their work.

* **Acceptance Criteria:**
  * **Given** a prompt is successfully generated via the backend (US-3.6).
  * **When** the generation transaction completes.
  * **Then** a `generated_prompts` record is saved with: `user_id`, `workspace_id`, `template_id`, `template_version_id`, `ai_model_id`, `input_values`, `extra_instructions`, `final_prompt`.

* **Business Rules:**
  * Records are soft-deleted (`deleted_at`), not hard-deleted.
  * Free plan: keeps the 100 most recent history items per user. Pro: unlimited (Phase 4).

#### US-4.2: View Personal Prompt History (UC-04.02) — Priority: P1

As a Logged-in User,
I want to view my prompt history,
So that I can find and reuse previous prompts.

* **Acceptance Criteria:**
  * **Given** I navigate to `/history`.
  * **When** the page loads.
  * **Then** I see my generated prompts sorted by `created_at DESC`, paginated with cursor-based pagination.
  * **And** I can filter by `template_id`, `ai_model_id`, and date range.

#### US-4.3: Reload a Prompt from History (UC-04.03) — Priority: P2

As a Logged-in User,
I want to reload a previous prompt's inputs onto the form,
So that I can edit and regenerate without starting from scratch.

* **Acceptance Criteria:**
  * **Given** I am viewing my history.
  * **When** I click "Re-run" on a history item.
  * **Then** the Generate form is pre-filled with the old `input_values` and model selection, ready for editing.
  * **And** clicking Generate creates a new record (does not overwrite the old one).

* **Exception Scenarios:**
  * Original template deleted → warning displayed, only allows copying old `final_prompt`.
  * Template has a newer version → badge "This used v1, v2 is now available" with option to switch.

#### US-4.4: Favorite or Unfavorite a Template (UC-04.04) — Priority: P2

As a Logged-in User,
I want to favorite and unfavorite templates,
So that I can easily access templates I use frequently.

* **Acceptance Criteria:**
  * **Given** I click the heart icon on a template.
  * **When** the request completes.
  * **Then** the template is added to or removed from my `favorites` table.
  * **And** `templates.favorite_count` is incremented/decremented.
  * **And** the UI toggles the icon and shows a toast.

#### US-4.5: Delete Prompt History (UC-04.05) — Priority: P2

As a Logged-in User,
I want to delete specific prompts from my history,
So that I can keep my history clean.

* **Acceptance Criteria:**
  * **Given** I am viewing my history.
  * **When** I click the delete button on a history item and confirm.
  * **Then** the system sets `deleted_at = NOW()` (soft-delete) and removes the item from the list.

* **Alternative Flow:**
  * User can select multiple items and bulk-delete.
  * User can restore items within 30 days from Trash (Phase 2).

---

### Epic 5: Admin & Content Management (Phase 1)

#### US-5.1: Manage AI Models (UC-05.01) — Priority: P1

As an Admin,
I want to manage the catalog of supported AI models,
So that the system stays up to date with the latest AI capabilities.

* **Acceptance Criteria:**
  * **Given** I am on the `/admin/ai-models` page.
  * **When** I create or edit a model (`code`, `name`, `provider`, `model_type`, `capabilities`, `default_config`, `icon`, `is_active`, `sort_order`).
  * **Then** the changes are saved and reflected in the model selection dropdowns across the system.

* **Business Rules:**
  * A model cannot be deleted if templates are attached to it — it must be deactivated instead (`is_active=false`).

#### US-5.2: Manage Categories & Tags (UC-05.02) — Priority: P1

As an Admin,
I want to manage categories and tags,
So that templates are well-organized and easy to find.

* **Acceptance Criteria:**
  * **Given** I am on the `/admin/taxonomy` page.
  * **When** I perform CRUD on categories (supporting nesting via `parent_id`) or tags.
  * **Then** the taxonomy tree is updated.
  * **And** duplicate tags can be merged (e.g., "email" + "emails" → one tag), updating `usage_count`.

#### US-5.3: Create & Publish Official Templates (UC-05.03) — Priority: P1

As an Admin,
I want to create and publish official templates,
So that users have high-quality, verified templates available at launch.

* **Acceptance Criteria:**
  * **Given** I am on the `/admin/templates` page.
  * **When** I define a template (title, description i18n, cover image, categories, tags, models, `prompt_body`, `template_variables`, optional `template_variants`, example output, usage guide) and click Publish.
  * **Then** it is marked as `is_official=true`, `status='published'`, `published_at=NOW()`, and visible to all users.

* **Business Rules:**
  * Before publishing, the backend validates: every `{{placeholder}}` in `prompt_body` must have a corresponding variable.
  * Editing after publishing creates a new version (does not overwrite).

#### US-5.4: View the Analytics Dashboard (UC-05.05) — Priority: P2

As an Admin,
I want to view system analytics,
So that I can monitor active users, generated prompts, and popular templates.

* **Acceptance Criteria:**
  * **Given** I navigate to `/admin/dashboard`.
  * **When** the dashboard loads.
  * **Then** I see aggregated metrics: DAU/WAU/MAU, prompts generated per day, most popular templates, most-used models, signup → first-generate funnel.
  * **And** metrics are cached for 5 minutes.
  * **And** I can filter by custom date range.

#### US-5.5: Review User-Submitted Templates (UC-05.04) — Priority: P2

As an Admin,
I want to review templates submitted by users for community publication,
So that only quality, policy-compliant templates become publicly visible.

* **Acceptance Criteria:**
  * **Given** a template has `status='pending'` (submitted via US-7.5).
  * **When** I open `/admin/moderation` and approve, reject (with `rejection_reason`), or request changes on it.
  * **Then** it moves to `published`/`is_public=true`, `rejected`, or back to `draft` with my comment, respectively, and the author is notified.

* **Business Rules:**
  * Review SLA of 48 hours.
  * Content that trips automated spam/keyword filters is auto-rejected before reaching the admin queue.

---

### Epic 6: AI Enhancement (Phase 2)

#### US-6.1: AI Refine a Prompt (UC-06.01) — Priority: P1 (High)

As a logged-in, verified User,
I want to ask AI to refine a prompt I've generated,
So that I get a clearer, more effective version without manually rewriting it.

* **Acceptance Criteria:**
  * **Given** I have generated a prompt and still have AI Refine quota.
  * **When** I click `[Refine with AI]`.
  * **Then** the backend calls the LLM Adapter (default GPT-4o) with an optimization meta-prompt and returns a refined version plus an explanation.
  * **And** I see a diff view (original vs. refined) and can `[Accept]` (replaces `final_prompt`), `[Edit manually]`, or `[Reject]`.

* **Exception Scenarios:**
  * Quota exhausted → `402 Payment Required`, invites upgrade to Pro.
  * LLM timeout > 30s → `504 Gateway Timeout`, allows retry.
  * LLM returns policy-violating content → filtered, soft-refuse error.

* **Business Rules:**
  * Free plan: 5 refines/day. Pro: 100 refines/day.
  * The refine model is admin-configurable.

#### US-6.2: AI Score a Prompt (UC-06.02) — Priority: P2 (Medium)

As a logged-in User,
I want to have AI score my generated prompt against quality criteria,
So that I understand its strengths and weaknesses before using it.

* **Acceptance Criteria:**
  * **Given** I have already generated a prompt.
  * **When** I click `[Score this prompt]`.
  * **Then** the LLM returns scores (0-10) for clarity, specificity, context, format, plus an overall score and suggestions, saved to `generated_prompts.ai_score`.
  * **And** the frontend renders a radar chart with the suggestions list.

* **Business Rules:**
  * A disclaimer 'AI assessment for reference only' is always displayed alongside the score.

#### US-6.3: Multi-Model Translation (UC-06.04) — Priority: P2 (Medium)

As a logged-in User,
I want to convert a prompt written for one AI model into the equivalent for another model,
So that I can reuse my prompt on a different tool without rewriting it by hand.

* **Acceptance Criteria:**
  * **Given** I have a generated prompt optimized for one model.
  * **When** I click `[Translate to another model]` and select the target model.
  * **Then** the LLM converts the prompt's syntax/style to the target model while preserving intent, saved as a new, separate history record.

* **Business Rules:**
  * Especially relevant for text-to-image-model conversions (e.g., Midjourney/DALL·E), which require a significant structural rewrite.

#### US-6.4: Playground (UC-06.03) — Priority: P1 (High)

As a logged-in User,
I want to test my prompt live against a real AI model,
So that I can see the actual response before using the prompt elsewhere.

* **Acceptance Criteria:**
  * **Given** I have Playground quota remaining.
  * **When** I select a model, adjust temperature/max_tokens (within plan limits), and click `[Run]`.
  * **Then** the backend calls the LLM Adapter, streams the response if supported, and saves the response plus `tokens_used`, `latency_ms`, `model_version`.

* **Exception Scenarios:**
  * Provider rate limit → circuit breaker opens, fallback message shown.
  * Response exceeds `max_tokens` → truncated with a warning.

* **Business Rules:**
  * Free: 10 runs/day, 500 output tokens. Pro: 200 runs/day, 4000 output tokens. Team: unlimited per seat (Phase 4).

#### US-6.5: Share a Prompt via Public Link (UC-06.05) — Priority: P2 (Medium)

As a logged-in User who owns a generated prompt,
I want to share it via a public link,
So that others can view it without needing an account.

* **Acceptance Criteria:**
  * **Given** I own a `generated_prompt`.
  * **When** I click `[Share]`.
  * **Then** the backend generates a `share_slug` (nanoid, 10 chars), sets `is_public=true`, and I get a `/p/{share_slug}` URL viewable without login.
  * **And** I can revoke sharing (`is_public=false`, `share_slug=NULL`).

* **Business Rules:**
  * The public page only shows `final_prompt`, the original template, and the model used; `input_values` are hidden if the owner selected 'hide inputs'.

---

### Epic 7: Template Customization & Versioning (Phase 2)

#### US-7.1: Fork a Template into a Personal Workspace (UC-07.01) — Priority: P1 (High)

As a logged-in User,
I want to fork a public or official template into my personal workspace,
So that I can customize it without affecting the original.

* **Acceptance Criteria:**
  * **Given** a template is public or official.
  * **When** I click `[Fork]`.
  * **Then** the backend clones the template, its current version, variables, and variants into my personal workspace with `is_official=false`, `is_public=false`, `status='draft'`, and `forked_from_template_id`/`forked_from_version_id` set.
  * **And** the source template's `fork_count` is incremented.

* **Business Rules:**
  * A fork does not automatically receive updates when the original gets a new version.
  * A user can fork the same template multiple times, each an independent copy.

#### US-7.2: Edit a Personal Template (UC-07.02) — Priority: P1 (High)

As a User who owns a template (a fork or one I created),
I want to edit its title, description, prompt body, and variables,
So that I can tailor it to my exact needs.

* **Acceptance Criteria:**
  * **Given** I am in the editor for a template I own.
  * **When** I edit the content and CRUD `template_variables`/`template_variants`, then click `[Save]`.
  * **Then** a new `template_versions` record is created if `prompt_body`/variables changed, preserving old history against the old version.

* **Exception Scenarios:**
  * Deleting a variable still referenced in `prompt_body` → warning, requires removing the placeholder first.

* **Business Rules:**
  * Maximum 30 fields per template (Free), 100 (Pro).
  * `var_key` must be unique per `template_version`, snake_case, no diacritics.

#### US-7.3: Create a New Template from Scratch (UC-07.03) — Priority: P2 (Medium)

As a logged-in User with remaining template-creation quota,
I want to create a brand-new template from an empty editor,
So that I can build a prompt template for a use case not already covered by the library.

* **Acceptance Criteria:**
  * **Given** I click `[+ New Template]` from `/my-templates`.
  * **When** I fill in title, description, taxonomy, models, `prompt_body`, and variables.
  * **Then** I can `[Save Draft]` or `[Publish (submit for review)]`.

* **Business Rules:**
  * Free plan: limited to 10 templates per user. Pro: unlimited.

#### US-7.4: Manage Template Versions (UC-07.04) — Priority: P2 (Medium)

As an Author who owns a template with multiple versions,
I want to view, compare, and switch which version is current,
So that I can control which version new users receive while preserving history for old ones.

* **Acceptance Criteria:**
  * **Given** my template has multiple `template_versions`.
  * **When** I open the 'Versions' tab.
  * **Then** I see version metadata, can diff two versions, and can mark one as `is_current`.

* **Business Rules:**
  * Old versions cannot be deleted (existing `generated_prompts` may reference them); they can be archived instead.

#### US-7.5: Submit a Template for Community Review (UC-07.05) — Priority: P2 (Medium)

As an Author with a draft template that has valid variables and a `prompt_body`,
I want to submit it for community review,
So that it can become a publicly available template after admin approval.

* **Acceptance Criteria:**
  * **Given** my template is in draft status with sufficient content.
  * **When** I click `[Submit for review]` and pass the pre-flight checklist (cover image, i18n description, example output, guide, at least 1 category).
  * **Then** `status='pending'`, the admin queue is notified, and I receive a confirmation email.

* **Exception Scenarios:**
  * Content violation (keyword spam) → auto-rejected with a message, never enters the admin queue.

---

## 3. System Integration & Data Schemas

### 3.1 Technology Stack Summary

| Layer | Technology |
| :--- | :--- |
| Frontend | React 18+, TypeScript, TailwindCSS v4, Zustand, React Query, i18next, React Router, Framer Motion |
| Backend | Java 21, Spring Boot 3+, Spring Security, Spring Data JPA, Flyway |
| Database | PostgreSQL 15+ (JSONB, tsvector, pg_trgm) |
| Cache | Redis 7+ (rate limiting, session, hot templates) |
| Storage | S3 / MinIO (cover images, avatars) |
| AI Provider | OpenAI, Anthropic, Google Gemini, Midjourney API (Adapter pattern) |

### 3.2 Authentication Architecture

| Aspect | Specification |
| :--- | :--- |
| Access Token | JWT signed with RS256 (asymmetric), 15-minute validity, stored in memory |
| Refresh Token | 30-day validity, stored in httpOnly cookie, rotates on each use |
| Password Hashing | BCrypt, cost >= 12 |
| OAuth | Google OIDC (Phase 1); GitHub, Microsoft planned for Phase 4 |
| State Management | Zustand (frontend) — replaces React AuthContext |

### 3.3 Core Database Tables (Phase 1)

| Group | Tables | Purpose |
| :--- | :--- | :--- |
| Identity & Tenancy | `users`, `user_identities`, `workspaces`, `workspace_members`, `refresh_tokens` | Authentication, authorization, multi-tenancy |
| AI Catalog | `ai_models` | Catalog of supported AI models |
| Taxonomy | `categories`, `tags` | Template classification |
| Templates (core) | `templates`, `template_versions`, `template_variables`, `template_variants`, `template_categories`, `template_tags`, `template_models` | The heart of the system |
| Generated Prompts | `generated_prompts` | History of prompts generated by users |
| Community | `favorites` | User favorite templates |

### 3.4 JSONB Column Formats

#### `template_variables` — Variable Definition
```json
{
  "var_key": "audience",
  "label": { "en": "Target Audience", "vi": "Đối tượng mục tiêu" },
  "input_type": "select",
  "is_required": true,
  "options": [
    { "value": "developers", "label": { "en": "Developers", "vi": "Lập trình viên" } },
    { "value": "marketers", "label": { "en": "Marketers", "vi": "Nhà tiếp thị" } }
  ],
  "validation": { "min": 1, "message_i18n": { "en": "Please select an audience", "vi": "Vui lòng chọn đối tượng" } },
  "default_value": "developers",
  "sort_order": 1
}
```

#### `generated_prompts.input_values` — Snapshot at Generation Time
```json
{
  "audience": "developers",
  "tone": "professional",
  "topic": "microservices architecture",
  "extra_instructions": "Include code examples in Java"
}
```

### 3.5 API Format (REST)

- **Base URL:** `/api/v1`
- **Auth header:** `Authorization: Bearer <access_token>` for every endpoint except `/auth/*`.
- **Error format:**
  ```json
  {
    "error": {
      "code": "STRING_CODE",
      "message": "Human readable message",
      "details": {}
    }
  }
  ```
- **Pagination:** Cursor-based (`?cursor=...&limit=20`).
- **Payload format:** JSON, all fields use `snake_case`.

### 3.6 Key API Endpoints (Phase 1 MVP)

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/auth/register` | POST | Register a new user + auto-create personal workspace |
| `/auth/login` | POST | Log in with email/password → access + refresh tokens |
| `/auth/oauth/google` | GET/POST | Log in via Google OIDC |
| `/auth/logout` | POST | Revoke refresh token, clear cookie |
| `/auth/refresh` | POST | Refresh the access token |
| `/auth/forgot-password` | POST | Send password reset email |
| `/auth/reset-password` | POST | Reset password with token |
| `/auth/verify-email` | GET | Verify email with token |
| `/users/me` | GET / PATCH | View / update personal profile |
| `/ai-models` | GET | List active AI models |
| `/categories` | GET | List categories (including nested) |
| `/tags` | GET | List popular tags |
| `/templates` | GET | List templates with filters (category, tag, model, search) |
| `/templates/featured` | GET | Get featured templates |
| `/templates/trending` | GET | Get trending templates |
| `/templates/{id}` | GET | Template details with current version, variables, variants |
| `/templates/{id}/favorite` | POST / DELETE | Toggle favorite |
| `/templates/{id}/generate` | POST | Render prompt (backend source of truth) |
| `/generated-prompts` | GET | Personal prompt history, paginated |
| `/generated-prompts/{id}` | GET / DELETE | View details / soft-delete |
| `/admin/ai-models` | POST / PATCH | Admin CRUD for models |
| `/admin/taxonomy` | POST / PATCH / DELETE | Admin CRUD for categories & tags |
| `/admin/templates` | POST / PATCH | Admin CRUD for templates |

---

## 4. Edge Cases, Exception Scenarios & Error Mapping

### 4.1 Authentication Edge Cases

| Scenario | Response | Behavior |
| :--- | :--- | :--- |
| Email already registered | `409 Conflict` | "Email is already in use" |
| Weak password | `422 Unprocessable Entity` | Detailed validation message |
| Wrong credentials | `401 Unauthorized` | Does not reveal which field is wrong |
| Account suspended | `403 Forbidden` | "Account has been suspended" |
| 5 failed logins in 15 min | `429 Too Many Requests` | Requires CAPTCHA to continue |
| Reset token expired | `410 Gone` | "Token has expired, please request a new one" |
| Email not found (forgot pw) | `200 OK` | Silent — prevents enumeration |

### 4.2 Template & Generation Edge Cases

| Scenario | Response | Behavior |
| :--- | :--- | :--- |
| Template not found or deleted | `404 Not Found` | — |
| Template private to another workspace | `403 Forbidden` | — |
| Required field empty at generation | Button disabled | Frontend prevents submission; backend re-validates |
| Invalid placeholder in prompt body | `500 Internal Server Error` | Detailed log; user sees fallback error |
| Original template deleted (history reload) | Warning + copy only | Does not reload the form |
| Template has newer version (history) | Info badge | "This used v1, v2 is now available" |

### 4.3 Standard Error Envelope

All REST APIs serialize errors in the following format:

```json
{
  "error": {
    "code": "UNAUTHORIZED_ACCESS",
    "message": "Access token is expired or invalid.",
    "details": {
      "endpoint": "/api/v1/generated-prompts"
    }
  }
}
```

### 4.4 Performance Constraints

| Metric | Target |
| :--- | :--- |
| First Contentful Paint (FCP) | < 1.5s on 4G |
| Time to Interactive (TTI) | < 3s |
| API p95 read endpoints | < 300ms |
| API p95 write endpoints | < 500ms |
| Full-text search p95 (10K templates) | < 200ms |
| Frontend prompt preview render | < 50ms |

---

## 5. Traceability Matrix

| BA Story | Use Case | SRS Section | User Story File |
| :--- | :--- | :--- | :--- |
| US-1.1 | UC-01.01 | Epic 1, US-1.1 | `us-1.1-register-a-new-account.md` |
| US-1.2 | UC-01.02 | Epic 1, US-1.2 | `us-1.2-log-in-with-email-plus-password.md` |
| US-1.3 | UC-01.03 | Epic 1, US-1.2 (OAuth) | `us-1.3-log-in-with-google-oauth.md` |
| US-1.4 | UC-01.04 | Epic 1 | `us-1.4-log-out.md` |
| US-1.5 | UC-01.05 | Epic 1, US-1.4 | `us-1.5-forgot-and-reset-password.md` |
| US-1.6 | UC-01.06 | Epic 1, US-1.1 | `us-1.6-verify-email.md` |
| US-1.7 | UC-01.07 | Epic 1, US-1.3 | `us-1.7-manage-personal-profile.md` |
| US-2.1 | UC-02.01 | Epic 2, US-2.1 | `us-2.1-browse-the-template-library.md` |
| US-2.2 | UC-02.02 | Epic 2, US-2.2 | `us-2.2-filter-by-category--tag--ai-model.md` |
| US-2.3 | UC-02.03 | Epic 2, US-2.3 | `us-2.3-full-text-search-templates.md` |
| US-2.4 | UC-02.04 | Epic 2, US-2.4 | `us-2.4-view-template-details.md` |
| US-2.5 | UC-02.05 | Epic 2, US-2.5 | `us-2.5-view-featured--trending-templates.md` |
| US-3.1 | UC-03.01 | Epic 3, US-3.5 | `us-3.1-select-the-target-ai-model-for-a-prompt.md` |
| US-3.2 | UC-03.02 | Epic 3, US-3.1 | `us-3.2-fill-in-the-dynamic-form-per-template.md` |
| US-3.3 | UC-03.03 | Epic 3, US-3.3 | `us-3.3-view-real-time-prompt-preview.md` |
| US-3.4 | UC-03.04 | Epic 3, US-3.4 | `us-3.4-add-optional-additional-instructions.md` |
| US-3.5 | UC-03.05 | Epic 3, US-3.7 | `us-3.5-generate-and-copy-the-complete-prompt.md` |
| US-3.6 | UC-03.06 | Epic 3, US-3.6 | `us-3.6-backend-renders-the-prompt.md` |
| US-4.1 | UC-04.01 | Epic 3, US-3.8 | `us-4.1-automatically-save-prompt-history.md` |
| US-4.2 | UC-04.02 | Epic 4, US-4.1 | `us-4.2-view-personal-prompt-history.md` |
| US-4.3 | UC-04.03 | Epic 4, US-4.2 | `us-4.3-reload-a-prompt-from-history.md` |
| US-4.4 | UC-04.04 | Epic 4, US-4.3 | `us-4.4-favorite-or-unfavorite-a-template.md` |
| US-4.5 | UC-04.05 | Epic 4, US-4.4 | `us-4.5-delete-prompt-history.md` |
| US-5.1 | UC-05.01 | Epic 5, US-5.1 | `us-5.1-manage-ai-models.md` |
| US-5.2 | UC-05.02 | Epic 5, US-5.2 | `us-5.2-manage-categories-and-tags.md` |
| US-5.3 | UC-05.03 | Epic 5, US-5.3 | `us-5.3-create-and-publish-official-templates.md` |
| US-5.4 | UC-05.05 | Epic 5, US-5.5 | `us-5.4-view-the-analytics-dashboard.md` |
| US-5.5 | UC-05.04 | Epic 5 (Phase 2) | `us-5.5-review-user-submitted-templates.md` |
| US-5.6 | UC-05.06 | — (supplementary, not in base catalog) | `us-5.6-admin-mark-template-as-featured.md` |
| US-6.1 | UC-06.01 | Epic 6, US-6.1 (Phase 2) | `us-6.1-ai-refine-a-prompt.md` |
| US-6.2 | UC-06.02 | Epic 6, US-6.2 (Phase 2) | `us-6.2-ai-score-a-prompt.md` |
| US-6.3 | UC-06.04 | Epic 6, US-6.3 (Phase 2) | `us-6.3-translate-a-prompt-between-models.md` |
| US-6.4 | UC-06.03 | Epic 6, US-6.4 (Phase 2) | `us-6.4-run-a-prompt-in-the-playground.md` |
| US-6.5 | UC-06.05 | Epic 6, US-6.5 (Phase 2) | `us-6.5-share-a-prompt-via-public-link.md` |
| US-7.1 | UC-07.01 | Epic 7, US-7.1 (Phase 2) | `us-7.1-fork-a-template.md` |
| US-7.2 | UC-07.02 | Epic 7, US-7.2 (Phase 2) | `us-7.2-edit-a-personal-template.md` |
| US-7.3 | UC-07.03 | Epic 7 (Phase 2, not itemized in SRS §3 table) | `us-7.3-create-a-new-template-from-scratch.md` |
| US-7.4 | UC-07.04 | Epic 7, US-7.3 (Phase 2) | `us-7.4-manage-template-versions.md` |
| US-7.5 | UC-07.05 | Epic 7, US-7.4 (Phase 2) | `us-7.5-submit-a-template-for-community-review.md` |
