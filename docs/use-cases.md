# USE CASE SPECIFICATION

# How2Prompt

*A prompt-skill enhancement platform for AI agents*

Version: 2.0

---

## 1. Introduction

### 1.1 Purpose of the Document

This document specifies all use cases for the How2Prompt platform — a system that provides a library of prompt templates, dynamic forms for generating prompts, and AI-powered enhancement features across multiple AI models. It covers all 4 phases of the roadmap: MVP → AI Enhancement → Community → Enterprise.

### 1.2 List of Actors

| Actor | Type | Description |
|---|---|---|
| Guest | Not logged in | Can view public templates, public prompts via share link, and register an account. |
| User (Registered) | Registered user | Includes 3 groups: general users, developers, content creators. Can use templates, create prompts, save history, fork templates. |
| Author | A user who has published a template | Can manage templates they created, and receives comments/votes/follows from the community. |
| Workspace Owner | Owner of a team workspace | Manages the workspace, invites/removes members, handles subscription billing (Phase 4). |
| Workspace Admin/Editor/Viewer | Team member | Has permissions corresponding to their role within the team workspace (Phase 4). |
| Admin (System) | Platform administrator | Manages AI models, categories, tags; approves user-submitted templates; moderation. |
| System (Automated) | System actor | Runs background jobs: rate limiting, sending emails, updating counters, syncing quotas, calling the LLM API. |
| External LLM Provider | Third party | OpenAI, Anthropic, Google Gemini, Midjourney, etc., called by the backend via an adapter. |
| Stripe (Billing) | Third party | Handles subscription payments (Phase 4). |

### 1.3 Document Structure

- **Section 2:** A consolidated catalog of all use cases grouped by functional area and phase.
- **Sections 3-9:** Detailed specification of each use case (including main flow, alternative flows, exceptions).
- **Section 10:** Traceability matrix: use case → user story (SRS) → API endpoint.
- **Section 11:** Overview of the use case diagram (described in structural form).

### 1.4 Use Case ID Convention

- **Format:** UC-XX.YY — where XX is the functional group number and YY is the sequence number within the group.
- **Example:** UC-03.02 = Group 3 (Prompt Generation), use case #2.
- **Phase:** P1 (MVP) / P2 (AI Enhancement) / P3 (Community) / P4 (Enterprise).
- **Priority:** High / Medium / Low.

---

## 2. Consolidated Use Case Catalog

The table below lists all 40 use cases across 9 functional groups, with clear phase and priority.

| Code | Use Case Name | Primary Actor | Phase | Priority |
|---|---|---|---|---|
| UC-01.01 | Register a new account | Guest | P1 | High |
| UC-01.02 | Log in with email + password | Guest | P1 | High |
| UC-01.03 | Log in with Google OAuth | Guest | P1 | High |
| UC-01.04 | Log out | User | P1 | High |
| UC-01.05 | Forgot & reset password | Guest | P1 | High |
| UC-01.06 | Verify email | User | P1 | High |
| UC-01.07 | Manage personal profile | User | P1 | Medium |
| UC-02.01 | Browse the template library | User/Guest | P1 | High |
| UC-02.02 | Filter by Category / Tag / AI Model | User/Guest | P1 | High |
| UC-02.03 | Full-text search templates | User/Guest | P1 | High |
| UC-02.04 | View template details | User/Guest | P1 | High |
| UC-02.05 | View Featured / Trending templates | User/Guest | P1 | Medium |
| UC-03.01 | Select the target AI Model for a prompt | User | P1 | High |
| UC-03.02 | Fill in the dynamic form per template | User | P1 | High |
| UC-03.03 | View real-time prompt preview | User | P1 | High |
| UC-03.04 | Add optional 'Additional Instructions' | User | P1 | Medium |
| UC-03.05 | Generate & copy the complete prompt | User | P1 | High |
| UC-03.06 | Backend renders the prompt (source of truth) | System | P1 | High |
| UC-04.01 | Automatically save prompt history | System | P1 | High |
| UC-04.02 | View personal prompt history | User | P1 | High |
| UC-04.03 | Reload a prompt from history | User | P1 | Medium |
| UC-04.04 | Favorite / unfavorite a template | User | P1 | Medium |
| UC-04.05 | Delete prompt history | User | P1 | Medium |
| UC-05.01 | Manage AI Models | Admin | P1 | High |
| UC-05.02 | Manage Categories & Tags | Admin | P1 | High |
| UC-05.03 | Create & publish official templates | Admin | P1 | High |
| UC-05.04 | Review user-submitted templates | Admin | P2 | High |
| UC-05.05 | View the analytics dashboard | Admin | P1 | Medium |
| UC-06.01 | Refine a prompt with AI | User | P2 | High |
| UC-06.02 | Score a prompt with AI | User | P2 | Medium |
| UC-06.03 | Run a prompt in the Playground | User | P2 | High |
| UC-06.04 | Translate a prompt between models | User | P2 | Medium |
| UC-06.05 | Share a prompt via public link | User | P2 | Medium |
| UC-07.01 | Fork a template into a Personal Workspace | User | P2 | High |
| UC-07.02 | Edit a personal template (CRUD fields) | User | P2 | High |
| UC-07.03 | Create a new template from scratch | User | P2 | Medium |
| UC-07.04 | Manage template versions | Author | P2 | Medium |
| UC-07.05 | Submit a template for community review | Author | P2 | Medium |
| UC-08.01 | Upvote / downvote a template | User | P3 | Medium |
| UC-08.02 | Comment & reply on a template | User | P3 | Medium |
| UC-08.03 | Follow an author | User | P3 | Medium |
| UC-08.04 | View a user's public profile page | User/Guest | P3 | Medium |
| UC-08.05 | Report abuse | User | P3 | Medium |
| UC-08.06 | Receive & view notifications | User | P3 | Medium |
| UC-09.01 | Create a Team Workspace | User (Owner) | P4 | High |
| UC-09.02 | Invite members to a Team Workspace | Workspace Owner/Admin | P4 | High |
| UC-09.03 | Assign permissions by role | Workspace Owner/Admin | P4 | High |
| UC-09.04 | Manage the internal template library | Workspace Editor+ | P4 | High |
| UC-09.05 | Subscribe & pay for a subscription | Workspace Owner | P4 | High |
| UC-09.06 | Enforce usage quota | System | P4 | High |
| UC-09.07 | Create & manage a developer API Key | User (Pro+) | P4 | Medium |
| UC-09.08 | View the team analytics dashboard | Workspace Admin+ | P4 | Medium |

---

## 3. Group 1 — Authentication & Account Management

### UC-01.01: Register a new account

| Primary Actor | Phase | Priority |
|---|---|---|
| Guest | P1 | High |

**Preconditions:** The user does not yet have an account on the system.

**Postconditions:** The account is created, a Personal Workspace is automatically initialized, and a verification email has been sent.

**Main Flow:**

1. The guest visits the Register page and enters an email, password, display name, and selects a locale (vi/en).
2. The frontend validates the email format and password strength (>= 8 characters, containing letters and numbers).
3. The guest clicks 'Register'; the system calls `POST /api/v1/auth/register`.
4. The backend checks the email doesn't already exist and hashes the password with BCrypt (cost >= 12).
5. The backend creates a record in `users`, automatically creates a Personal Workspace (type='personal'), and appoints the user as owner.
6. The backend sends a verification email containing a token valid for 24 hours.
7. The backend returns `201 Created` with an `access_token` + `refresh_token`.
8. The frontend stores the tokens and redirects to the home page with a banner prompting email verification.

**Alternative Flow:**

- The guest can choose 'Sign up with Google' → switches to the UC-01.03 flow.

**Exception Flow:**

- Email already exists → returns `409 Conflict`, displays 'Email is already in use'.
- Password not strong enough → returns `422 Unprocessable Entity` with a detailed message.
- Rate limit exceeded (10 requests/minute/IP) → returns `429 Too Many Requests`.

**Business Rules:**

- Each user has exactly one Personal Workspace, which cannot be deleted.
- A user who hasn't verified their email can still use the app but is limited (cannot create public templates, cannot use AI Refine in Phase 2).

### UC-01.02: Log in with email + password

| Primary Actor | Phase | Priority |
|---|---|---|
| Guest | P1 | High |

**Preconditions:** The user has a registered account.

**Postconditions:** An access token + refresh token are issued, and the user is redirected to the dashboard.

**Main Flow:**

1. The guest enters their email and password on the Login page.
2. The frontend calls `POST /api/v1/auth/login`.
3. The backend authenticates the credentials, matching `password_hash` with BCrypt.
4. The backend updates `users.last_login_at` and creates a `refresh_tokens` record (30 days).
5. The backend returns `{ access_token, refresh_token, user_profile }`.
6. The frontend stores `access_token` in memory, `refresh_token` in an httpOnly cookie, and redirects to the dashboard.

**Exception Flow:**

- Wrong email or password → returns `401 Unauthorized`, without revealing which field is wrong.
- Account suspended → returns `403 Forbidden`.
- 5 failed login attempts within 15 minutes → temporarily locked, requiring CAPTCHA.

**Business Rules:**

- Access tokens are valid for 15 minutes and auto-refresh on expiry if the refresh token is valid.
- Refresh tokens rotate on each use to increase security.

### UC-01.03: Log in with Google OAuth

| Primary Actor | Phase | Priority |
|---|---|---|
| Guest | P1 | High |

**Preconditions:** The guest has a Google account.

**Postconditions:** The user is logged in; if they don't already have an account, one is automatically created.

**Main Flow:**

1. The guest clicks 'Sign in with Google' on the Login/Register page.
2. The frontend redirects to the Google OAuth Authorization endpoint with the `openid email profile` scope.
3. The guest approves on Google's consent page.
4. Google calls back to `/api/v1/auth/oauth/google/callback` with an authorization code.
5. The backend exchanges the code for an ID token and profile, verifying the ID token's signature.
6. The backend checks `user_identities` for (provider='google', provider_uid). If not found, it creates a new user + Personal Workspace + user_identity.
7. The backend returns an access_token + refresh_token as in UC-01.02.

**Exception Flow:**

- The guest declines consent → redirected back to the login page with an error message.
- The email from Google matches an account already registered with email/password → merges identities, requiring confirmation.
- Google returns an error/timeout → returns `502 Bad Gateway`, displaying a fallback 'Please try again'.

*Note: In Phase 4, GitHub and Microsoft OAuth may be added using a similar flow.*

### UC-01.04: Log out

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | High |

**Preconditions:** The user is logged in.

**Postconditions:** The refresh token is revoked and the client session is cleared.

**Main Flow:**

1. The user clicks 'Log out' in the profile menu.
2. The frontend calls `POST /api/v1/auth/logout`.
3. The backend marks `revoked_at` on the current `refresh_tokens` record.
4. The backend clears the httpOnly cookie containing the refresh token.
5. The frontend clears the access token from memory and redirects to the public home page.

### UC-01.05: Forgot & reset password

| Primary Actor | Phase | Priority |
|---|---|---|
| Guest | P1 | High |

**Preconditions:** The user has an account with a registered email.

**Postconditions:** The new password is saved, and all old refresh tokens are revoked.

**Main Flow:**

1. The guest clicks 'Forgot password' and enters their registered email.
2. The backend calls `POST /api/v1/auth/forgot-password`, generates a reset token (valid 1h), and sends an email.
3. The user opens the email and clicks the link containing the reset token → the `/reset-password` page.
4. The user enters the new password twice.
5. The frontend calls `POST /api/v1/auth/reset-password` with the token + new password.
6. The backend verifies the token, updates `password_hash`, revokes all old refresh tokens, and sends a confirmation email.
7. The user is redirected to the Login page.

**Exception Flow:**

- Email doesn't exist → still returns `200 OK` (doesn't reveal this, to prevent enumeration).
- Reset token expired or already used → returns `410 Gone`, requiring a new request.

### UC-01.06: Verify email

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | High |

**Preconditions:** The user has just registered and hasn't verified their email.

**Postconditions:** `email_verified_at` is updated, and the verification reminder banner disappears.

**Main Flow:**

1. The user opens the verification email and clicks the link containing the verify token.
2. The frontend calls `GET /api/v1/auth/verify-email?token=...`.
3. The backend verifies the token and updates `users.email_verified_at = NOW()`.
4. The user is redirected to the home page with a 'Verification successful' message.

**Alternative Flow:**

- The user can request the email be resent from the banner (rate limited to once per 5 minutes).

### UC-01.07: Manage personal profile

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | Medium |

**Preconditions:** The user is logged in.

**Postconditions:** The profile is updated, which may affect the UI (locale) or the public profile (username).

**Main Flow:**

1. The user goes to `/settings/profile`.
2. The frontend calls `GET /api/v1/users/me` to display current data.
3. The user edits `full_name`, avatar (image upload), bio, username, locale, timezone.
4. The frontend calls `PATCH /api/v1/users/me` with the changed payload.
5. The backend validates (unique username, image <= 2MB, png/jpg format) and updates `users`.
6. The frontend refreshes state and shows a success toast.

**Exception Flow:**

- Username already exists → `409 Conflict`, suggests another username.
- Image exceeds size limit → `413 Payload Too Large`.

**Business Rules:**

- Changing the locale applies immediately in the UI and is used as the default when rendering i18n titles/descriptions.

---

## 4. Group 2 — Template Discovery & Search

### UC-02.01: Browse the template library

| Primary Actor | Phase | Priority |
|---|---|---|
| User / Guest | P1 | High |

**Preconditions:** None (guests can still view public templates).

**Postconditions:** The list of templates is displayed, paginated.

**Main Flow:**

1. The user visits `/explore` or `/templates`.
2. The frontend calls `GET /api/v1/templates?sort=popular&limit=20`.
3. The backend queries templates where `status='published' AND is_public=true` (if a guest), also including the user's workspace if logged in.
4. The backend returns a list with metadata: title, cover, category, `upvote_count`, `usage_count`, author.
5. The frontend renders a grid of cards, supporting infinite scroll or load-more.

**Business Rules:**

- Templates with `is_official=true` are prioritized at the top under the 'default' sort.
- Templates with `deleted_at` set are not shown.

### UC-02.02: Filter by Category / Tag / AI Model

| Primary Actor | Phase | Priority |
|---|---|---|
| User / Guest | P1 | High |

**Preconditions:** The template list is being displayed.

**Postconditions:** The list is narrowed by the filters, and the URL query string is updated (deep-linkable).

**Main Flow:**

1. The user selects one or more categories from the sidebar (e.g., Writing + Marketing).
2. The user selects a target AI Model (e.g., Claude Opus 4).
3. The user selects tags (multi-select).
4. The frontend calls `GET /api/v1/templates?category=writing,marketing&model=claude-opus-4&tags=email,formal`.
5. The backend applies filters via the N:M tables (`template_categories`, `template_tags`, `template_models`).
6. Returns results with a total count for a badge display.

**Alternative Flow:**

- The user clicks 'Clear filters' to reset to the original list.

### UC-02.03: Full-text search templates

| Primary Actor | Phase | Priority |
|---|---|---|
| User / Guest | P1 | High |

**Preconditions:** None.

**Postconditions:** Search results are ranked by relevance.

**Main Flow:**

1. The user types a keyword into the search box (e.g., 'email marketing').
2. The frontend debounces for 300ms, then calls `GET /api/v1/templates?q=email+marketing`.
3. The backend queries using the `search_vector` column (tsvector) with `to_tsquery`, with a pg_trgm fallback for fuzzy matching.
4. Results are sorted by `ts_rank + usage_count`.
5. The frontend displays results with keyword highlighting.

**Business Rules:**

- Search supports both English and Vietnamese (using the 'simple' dictionary since there's no standard Vietnamese stemmer).
- Search latency must be p95 < 200ms with 10,000 templates.

### UC-02.04: View template details

| Primary Actor | Phase | Priority |
|---|---|---|
| User / Guest | P1 | High |

**Preconditions:** The template is public or belongs to the user's workspace.

**Postconditions:** The detail page displays full metadata, and `view_count` is incremented.

**Main Flow:**

1. The user clicks on a template card.
2. The frontend calls `GET /api/v1/templates/{id}` to retrieve: template info, `current_version` (`prompt_body`, guide), variables, variants by model, author info, usage count, favorite status.
3. The backend increments `view_count` (asynchronously, non-blocking).
4. The frontend displays: description, example output, usage guide, list of variables (form not yet rendered), list of supported models, and `[Use template]`, `[Favorite]`, `[Fork]` (Phase 2) buttons.

**Exception Flow:**

- Template doesn't exist or has been deleted → returns `404`.
- Template is private to another workspace → returns `403`.

### UC-02.05: View Featured / Trending templates

| Primary Actor | Phase | Priority |
|---|---|---|
| User / Guest | P1 | Medium |

**Preconditions:** None.

**Postconditions:** The homepage shows two separate sections: Featured (marked by admins) and Trending (calculated by `usage_count` over the last 7 days).

**Main Flow:**

1. The user visits the homepage.
2. The frontend calls `GET /api/v1/templates/featured` and `GET /api/v1/templates/trending?window=7d`.
3. The backend caches the results in Redis for 10 minutes to reduce load.
4. The frontend renders two separate carousels.

---

## 5. Group 3 — Prompt Generation (Core MVP)

### UC-03.01: Select the target AI Model for a prompt

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | High |

**Preconditions:** On the template detail page.

**Postconditions:** The model is selected, and the system uses the corresponding variant if available.

**Main Flow:**

1. The user clicks `[Use template]` on the detail page.
2. The frontend displays a dropdown listing the `ai_models` supported by the template (via the `template_models` table).
3. The user selects a model (default = the model marked `is_primary`).
4. The frontend loads the corresponding variant: if `template_variants` exist (`template_version_id`, `ai_model_id`), it uses `prompt_body_override`; otherwise, it uses the original `prompt_body`.

**Alternative Flow:**

- If the template supports only one model, the dropdown is hidden and auto-selected.

**Business Rules:**

- The selected model affects the `system_prompt`, `model_config`, and how rendering happens (e.g., an image model has a different syntax).

### UC-03.02: Fill in the dynamic form per template

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | High |

**Preconditions:** The template and model have been selected.

**Postconditions:** All required fields are validly filled in.

**Main Flow:**

1. The frontend reads the list of `template_variables` (`input_type`, `is_required`, `options`, `validation`).
2. The frontend renders a dynamic form: text/textarea/select/multiselect/number/boolean/slider, etc., accordingly.
3. Labels, placeholders, and help text are pulled based on the current locale from the JSONB i18n data.
4. The user fills in each field one by one; client-side validation runs per the configuration (min, max, regex, minLength).
5. If required fields aren't filled in, the Generate button is disabled.

**Exception Flow:**

- File upload exceeds size limit → inline error message.
- Regex doesn't match → displays the message from `validation.message_i18n`.

### UC-03.03: View real-time prompt preview

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | High |

**Preconditions:** On the Generate screen, filling in the dynamic form.

**Postconditions:** The prompt preview updates immediately as the user types.

**Main Flow:**

1. On every field `onChange`, the frontend runs the Template Renderer (client-side): replacing `{{placeholder}}` with the current value (or an empty placeholder if not yet entered).
2. The preview is displayed in monospace with syntax highlighting for unfilled placeholders.
3. It also shows a character count and token estimate (using the `tiktoken` library or a heuristic).

**Business Rules:**

- The client-side preview is for UX only; the final value is always re-rendered by the backend (see UC-03.06).
- For image models (Midjourney/DALL·E), the preview adds suffix parameters (`--ar`, `--v`).

### UC-03.04: Add optional 'Additional Instructions'

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | Medium |

**Preconditions:** On the Generate form.

**Postconditions:** The extra string is appended to the end of the prompt.

**Main Flow:**

1. At the end of the form there's always a textarea 'Additional instructions (optional)'.
2. The user types additional instructions.
3. The renderer appends this string to the end of `prompt_body` (after a newline), or inserts it at a special location if the template declares a `{{__extra__}}` placeholder.

**Business Rules:**

- This field is unstructured — it's only meant to let the user 'escape' the template when they need light customization without forking.
- Content is escaped to guard against basic prompt injection.

### UC-03.05: Generate & copy the complete prompt

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | High |

**Preconditions:** The form is valid, and a model has been selected.

**Postconditions:** The final prompt is displayed, ready to copy or use in the Playground (Phase 2).

**Main Flow:**

1. The user clicks `[Generate]`.
2. The frontend calls `POST /api/v1/templates/{id}/generate` with the payload `{ template_version_id, ai_model_id, input_values, extra_instructions }`.
3. The backend renders the final prompt (UC-03.06), saves a record to `generated_prompts`, and increments `templates.usage_count`.
4. The backend returns `{ generated_prompt_id, final_prompt, tokens_estimate }`.
5. The frontend displays the prompt in a results panel with `[Copy]`, `[Save as favorite]`, `[Share link]` (Phase 2), `[Try in Playground]` (Phase 2) buttons.
6. The user clicks `[Copy]` → the prompt is written to the clipboard, showing a 'Copied' toast.

**Exception Flow:**

- Quota exceeded (Phase 4) → returns `402 Payment Required`.
- Backend rendering error (invalid placeholder) → returns `500` with detailed logs, displaying a fallback 'An error occurred, please try again'.

### UC-03.06: Backend renders the prompt (source of truth)

| Primary Actor | Phase | Priority |
|---|---|---|
| System | P1 | High |

**Preconditions:** Called by UC-03.05 or other endpoints.

**Postconditions:** The final prompt is a complete text string, saved to the database.

**Main Flow:**

1. Receives the payload `{ template_version_id, ai_model_id, input_values, extra_instructions }`.
2. Loads the corresponding `template_versions` and `template_variants`.
3. Selects the `prompt_body`: if `variant.prompt_body_override` exists → uses the variant; otherwise → uses `version.prompt_body`.
4. Runs the render engine (Mustache/Handlebars-style): `{{var_key}}` → `input_values[var_key]`.
5. Handles `default_value`: if the input is empty and there's a default → uses the default; if optional and empty → removes the placeholder + trims extra whitespace.
6. Appends `extra_instructions` at the end per the rule in UC-03.04.
7. Sanitizes (removes unusual control characters).
8. Saves `generated_prompts` with `final_prompt`, `input_values` (JSONB), `workspace_id`, `ai_model_id`, `template_version_id`.
9. Returns the result to the client.

**Business Rules:**

- The renderer is a separate service with >= 90% unit test coverage.
- The frontend is never trusted: all important validation (required, regex) is re-run on the backend.

---

## 6. Group 4 — History & Favorites

### UC-04.01: Automatically save prompt history

| Primary Actor | Phase | Priority |
|---|---|---|
| System | P1 | High |

**Preconditions:** UC-03.05 (Generate) has been triggered successfully.

**Postconditions:** A record is saved in `generated_prompts`.

**Main Flow:**

1. After UC-03.06 finishes rendering, the system creates a `generated_prompts` record with: `user_id`, `workspace_id`, `template_id`, `template_version_id`, `ai_model_id`, `input_values`, `extra_instructions`, `final_prompt`.
2. The system doesn't block the response of UC-03.05: the save runs within the same transaction to ensure consistency.

**Business Rules:**

- The record is soft-deleted (`deleted_at`), not hard-deleted, to preserve the audit trail.
- Free plan: keeps the 100 most recent history items per user. Pro: unlimited (Phase 4).

### UC-04.02: View personal prompt history

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | High |

**Preconditions:** The user is logged in.

**Postconditions:** The history list is displayed, paginated.

**Main Flow:**

1. The user goes to `/history`.
2. The frontend calls `GET /api/v1/generated-prompts?limit=20&cursor=...`.
3. The backend queries `generated_prompts` for the `user_id`, sorted by `created_at DESC`, with filters by `template_id`, `ai_model_id`, and date range.
4. Returns the list along with a snippet of `final_prompt` and the template thumbnail.
5. The user can click an item to view details or reload it (UC-04.03).

### UC-04.03: Reload a prompt from history

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | Medium |

**Preconditions:** Viewing history, and the original template still exists.

**Postconditions:** The Generate form is pre-filled with the old `input_values`, ready for editing and regenerating.

**Main Flow:**

1. The user clicks 'Re-run' on a history item.
2. The frontend navigates to the Generate page with the original `template_id` + `template_version_id`, and the model that was used.
3. The frontend calls `GET /api/v1/generated-prompts/{id}` to retrieve `input_values` and re-populate the form.
4. The user can edit fields and then click Generate → creates a new record (does not overwrite the old one).

**Exception Flow:**

- The original template has been deleted → displays a warning, only allows copying the old `final_prompt`, doesn't reload the form.
- The template has a newer version → displays a badge 'This used v1, v2 is now available' and asks if the user wants to use v2 instead.

### UC-04.04: Favorite / unfavorite a template

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | Medium |

**Preconditions:** The template is public or belongs to the user's workspace.

**Postconditions:** A record in `favorites` is created/deleted, and `favorite_count` is updated.

**Main Flow:**

1. The user clicks the heart icon on a template.
2. The frontend calls `POST /api/v1/templates/{id}/favorite` (or `DELETE` to unfavorite).
3. The backend inserts/deletes `favorites` and increments/decrements `templates.favorite_count`.
4. The frontend toggles the icon and shows a toast.

**Alternative Flow:**

- The user visits `/favorites` to view all favorited templates.

### UC-04.05: Delete prompt history

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P1 | Medium |

**Preconditions:** The user owns the history record.

**Postconditions:** The record is soft-deleted and no longer displayed.

**Main Flow:**

1. The user clicks the delete button on a history item.
2. A confirmation dialog appears.
3. The frontend calls `DELETE /api/v1/generated-prompts/{id}`.
4. The backend sets `deleted_at = NOW()`.
5. The frontend removes the item from the list.

**Alternative Flow:**

- The user can select multiple items and bulk-delete.
- The user can restore items within 30 days from Trash (Phase 2).

---

## 7. Group 5 — System Administration

### UC-05.01: Manage AI Models

| Primary Actor | Phase | Priority |
|---|---|---|
| Admin | P1 | High |

**Preconditions:** The admin is logged in with `is_admin = true`.

**Postconditions:** The model catalog is updated, affecting model-selection dropdowns across the whole system.

**Main Flow:**

1. The admin goes to `/admin/ai-models`.
2. The frontend calls `GET /api/v1/admin/ai-models` to list all models.
3. The admin performs CRUD on models: `code`, `name`, `provider`, `model_type`, `capabilities` (JSONB), `default_config`, `icon`, `is_active`, `sort_order`.
4. Clicking Save → `POST/PATCH /api/v1/admin/ai-models`.

**Business Rules:**

- A model cannot be deleted if templates are attached to it — it must be deactivated instead (`is_active=false`).
- Changing `default_config` doesn't affect already-saved `generated_prompts`.

### UC-05.02: Manage Categories & Tags

| Primary Actor | Phase | Priority |
|---|---|---|
| Admin | P1 | High |

**Preconditions:** The admin is logged in.

**Postconditions:** The taxonomy tree is updated.

**Main Flow:**

1. The admin goes to `/admin/taxonomy`.
2. Performs CRUD on categories (supporting nesting via `parent_id`), CRUD on tags.
3. The admin can merge duplicate tags (e.g., 'email' + 'emails' → merged into one).
4. The backend updates the tag's `usage_count` after merging.

### UC-05.03: Create & publish official templates

| Primary Actor | Phase | Priority |
|---|---|---|
| Admin | P1 | High |

**Preconditions:** The admin is logged in.

**Postconditions:** A template is created with `is_official=true`, `is_public=true`, `status=published`, available to all users.

**Main Flow:**

1. The admin goes to `/admin/templates` → `[+ New Template]`.
2. The admin enters the title, description (i18n EN + VI), cover image, and selects categories, tags, and supported models.
3. The admin writes the `prompt_body` using `{{placeholder}}` syntax.
4. The admin declares `template_variables`: `var_key`, `label`, `input_type`, `options`, `validation`, `sort_order`.
5. The admin optionally creates `template_variants` for specific models (e.g., a custom prompt for Midjourney).
6. The admin adds example output and a usage guide.
7. Clicks `[Save Draft]` or `[Publish]`.
8. If Publish: the system sets `status='published'`, `published_at=NOW()`, `is_official=true`.

**Business Rules:**

- Before publishing, the backend runs validation: every `{{placeholder}}` in `prompt_body` must have a corresponding variable.
- A template can be edited after publishing → creates a new version (does not overwrite).

### UC-05.04: Review user-submitted templates

| Primary Actor | Phase | Priority |
|---|---|---|
| Admin | P2 | High |

**Preconditions:** There's a template with `status='pending'` (submitted by a user via UC-07.05).

**Postconditions:** The template is approved (moved to published, `is_public=true`) or rejected.

**Main Flow:**

1. The admin goes to `/admin/moderation` → the 'Pending Templates' tab.
2. The frontend lists templates awaiting review with author information.
3. The admin views details and test-renders the prompt with sample input.
4. The admin clicks Approve → the template moves to published, `is_public=true`, and the author is notified.
5. Or the admin clicks Reject with a `rejection_reason` → the author receives a notification.

**Business Rules:**

- Review SLA of 48 hours.
- The admin can request changes: the status reverts to 'draft' with a comment.

### UC-05.05: View the analytics dashboard

| Primary Actor | Phase | Priority |
|---|---|---|
| Admin | P1 | Medium |

**Preconditions:** The admin is logged in.

**Postconditions:** Aggregated metrics are displayed.

**Main Flow:**

1. The admin goes to `/admin/dashboard`.
2. The backend returns metrics: DAU/WAU/MAU, prompts generated per day, most popular templates, most-used models, and the signup → first-generate funnel.
3. The frontend renders charts and tables.

**Business Rules:**

- Metrics are cached for 5 minutes to reduce database load.
- There's a filter for a custom date range.

---

## 8. Group 6 — AI Enhancement (Phase 2)

### UC-06.01: Refine a prompt with AI

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P2 | High |

**Preconditions:** The user is logged in, has verified their email, and still has AI Refine quota remaining.

**Postconditions:** The prompt is improved, with a side-by-side comparison displayed.

**Main Flow:**

1. After generating a prompt (UC-03.05), the user clicks `[Refine with AI]`.
2. The frontend calls `POST /api/v1/generated-prompts/{id}/refine`.
3. The backend checks `usage_quotas` (Phase 4) and increments `used_count`.
4. The backend sends a request to the LLM Adapter (default GPT-4o) with a meta-prompt requesting optimization.
5. The LLM returns a refined version + an explanation of the changes.
6. The backend saves it to `generated_prompts.ai_refined` and returns it to the client.
7. The frontend displays a diff view: the original prompt on the left, the refined prompt on the right, with bullet-point explanations.
8. The user can `[Accept]` (replaces `final_prompt`), `[Edit manually]`, or `[Reject]`.

**Exception Flow:**

- Quota exhausted → returns `402`, inviting the user to upgrade to Pro.
- LLM timeout > 30s → returns `504`, allows the user to retry.
- LLM returns policy-violating content → filtered and returns a soft-refuse error.

**Business Rules:**

- Free plan: 5 times/day. Pro: 100 times/day.
- The model used for refining can be configured globally by an admin.

### UC-06.02: Score a prompt with AI

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P2 | Medium |

**Preconditions:** A prompt has already been generated.

**Postconditions:** Scores for each criterion are saved and displayed.

**Main Flow:**

1. The user clicks `[Score this prompt]`.
2. The backend calls the LLM with a meta-prompt requesting a score across 4 criteria: clarity, specificity, context, format (scale 0-10).
3. The LLM returns JSON `{ clarity: 8, specificity: 7, context: 9, format: 8, overall: 8.0, suggestions: [...] }`.
4. The backend saves it to `generated_prompts.ai_score`.
5. The frontend renders a radar chart and list of suggestions.

**Business Rules:**

- Results may be inaccurate → a disclaimer 'AI assessment for reference only' is displayed.

### UC-06.03: Run a prompt in the Playground

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P2 | High |

**Preconditions:** The user is logged in and has Playground quota.

**Postconditions:** The LLM's response is displayed and saved to `generated_prompts.playground_response`.

**Main Flow:**

1. The user clicks `[Try in Playground]` or visits `/playground`.
2. Selects a model, adjusts temperature/max_tokens (limited by plan).
3. Clicks `[Run]`.
4. The backend calls the corresponding LLM Adapter for the model, measuring latency and tokens.
5. Returns the response to the client, displayed in real time if the model supports streaming.
6. The backend saves the response + metadata (`tokens_used`, `latency_ms`, `model_version`) to `generated_prompts`.

**Exception Flow:**

- The provider returns a rate limit → the circuit breaker opens, showing a fallback message.
- The response exceeds `max_tokens` → truncated with a warning.

**Business Rules:**

- Free: 10 times/day, limited to 500 output tokens.
- Pro: 200 times/day, 4000 output tokens.
- Team: unlimited per seat.

### UC-06.04: Translate a prompt between models

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P2 | Medium |

**Preconditions:** There's a prompt optimized for one model, and the user wants to use it on another.

**Postconditions:** The prompt is rewritten to fit the target model's syntax.

**Main Flow:**

1. The user clicks `[Translate to another model]` and selects the target model.
2. The backend calls the LLM with a meta-prompt: 'Convert the following prompt from ChatGPT to a style suited for Claude, preserving the original intent.'
3. Returns the new prompt, saved to history as a separate record.

**Business Rules:**

- Especially useful when converting from a text prompt to an image prompt (Midjourney/DALL·E) — requires a significant structural change.

### UC-06.05: Share a prompt via public link

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P2 | Medium |

**Preconditions:** The user owns the `generated_prompt`.

**Postconditions:** A public link is generated, viewable by anyone.

**Main Flow:**

1. The user clicks `[Share]` on a prompt.
2. The backend generates a `share_slug` (nanoid, 10 characters), sets `is_public=true`.
3. The frontend displays a URL in the form `https://how2prompt.app/p/{share_slug}`.
4. The user copies the link to share it.
5. Anyone visiting that URL will see the prompt (no login required).

**Alternative Flow:**

- The user can revoke sharing (sets `is_public=false`, `share_slug=NULL`).

**Business Rules:**

- The public page only shows the `final_prompt`, the original template, and the model used. Detailed `input_values` are not shown if the user chose 'hide inputs'.

---

## 9. Group 7 — Template Customization (Phase 2)

### UC-07.01: Fork a template into a Personal Workspace

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P2 | High |

**Preconditions:** The template is public or official.

**Postconditions:** A copy of the template is created in the user's Personal Workspace.

**Main Flow:**

1. The user clicks `[Fork]` on the detail page.
2. The frontend calls `POST /api/v1/templates/{id}/fork`.
3. The backend clones: `templates` + current `template_versions` + `template_variables` + `template_variants`.
4. Sets: `workspace_id` = the user's personal workspace, `author_id` = user, `author_type` = 'forked', `is_official=false`, `is_public=false`, `status='draft'`, `forked_from_template_id`, `forked_from_version_id`.
5. Increments `templates.fork_count` on the original.
6. Redirects the user to the template editor with the fork.

**Business Rules:**

- The fork does not automatically receive updates when the original template gets a new version.
- A user can fork the same template multiple times (each is an independent copy).

### UC-07.02: Edit a personal template (CRUD fields)

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P2 | High |

**Preconditions:** The user owns the template (a fork or one they created).

**Postconditions:** The template is updated, automatically creating a new version if needed.

**Main Flow:**

1. The user goes to the template editor.
2. Edits the title, description, `prompt_body`.
3. Performs CRUD on `template_variables`: adds a new field (choosing `input_type`, configuring options/validation), removes unneeded fields, reorders them.
4. Edits `template_variants` for other models.
5. Clicks `[Save]`.
6. The backend creates a new `template_versions` record if `prompt_body`/variables changed (preserving old history pointing to the old version).

**Exception Flow:**

- Deleting a variable still used in `prompt_body` → warning, requiring the placeholder to be removed first.

**Business Rules:**

- Maximum 30 fields per template (free), 100 fields (Pro).
- `var_key` must be unique within a `template_version`, in snake_case, with no diacritics.

### UC-07.03: Create a new template from scratch

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P2 | Medium |

**Preconditions:** The user is logged in and still has `template_create` quota.

**Postconditions:** A new template exists in draft status in the Personal Workspace.

**Main Flow:**

1. The user clicks `[+ New Template]` from `/my-templates`.
2. The frontend opens an empty editor.
3. The user fills in the title, description, selects categories, tags, models, and writes the `prompt_body` and variables.
4. Clicks `[Save Draft]` or `[Publish (submit for review)]`.

**Business Rules:**

- Free plan: limited to 10 templates per user. Pro: unlimited.

### UC-07.04: Manage template versions

| Primary Actor | Phase | Priority |
|---|---|---|
| Author | P2 | Medium |

**Preconditions:** The author owns a template that has multiple versions.

**Postconditions:** The author can view, compare, and switch which version is current.

**Main Flow:**

1. The author goes to the 'Versions' tab in the editor.
2. Views the list of `template_versions` with `version_number`, changelog, `created_by`, `created_at`.
3. Can compare a diff between two versions.
4. Can set one version as `is_current` (any new user using the template will use this version).

**Business Rules:**

- Old versions cannot be deleted since `generated_prompts` may still reference them (integrity).
- Old versions can be archived (not selectable when generating new prompts).

### UC-07.05: Submit a template for community review

| Primary Actor | Phase | Priority |
|---|---|---|
| Author | P2 | Medium |

**Preconditions:** The template is in draft status with sufficient valid variables and `prompt_body`.

**Postconditions:** The template moves to `status='pending'` and enters the review queue.

**Main Flow:**

1. The author clicks `[Submit for review]`.
2. The frontend displays a checklist: cover image, i18n description, example output, guide, at least 1 category.
3. If conditions are met, calls `POST /api/v1/templates/{id}/submit`.
4. The backend sets `status='pending'` and sends a notification to the admin queue.
5. The author receives a confirmation email.

**Exception Flow:**

- Content violation (keyword spam) → auto-rejected with a message.

---

## 10. Group 8 — Community (Phase 3)

### UC-08.01: Upvote / downvote a template

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P3 | Medium |

**Preconditions:** The template is public, and the user is logged in.

**Postconditions:** The vote is recorded, and the counter is updated.

**Main Flow:**

1. The user clicks ▲ or ▼ on a template or public `generated_prompt`.
2. The frontend calls `POST /api/v1/votes` with `{ target_type, target_id, value: 1 | -1 }`.
3. The backend upserts into `votes` (unique per `user_id` + target).
4. The backend updates the denormalized counter (`upvote_count`/`downvote_count`).
5. The frontend updates the UI immediately (optimistic).

**Alternative Flow:**

- The user clicks the same direction again → removes the vote (deletes the row).
- The user clicks the opposite direction → changes the value.

### UC-08.02: Comment & reply on a template

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P3 | Medium |

**Preconditions:** The template is public.

**Postconditions:** The comment is saved and displayed in threaded form.

**Main Flow:**

1. The user types a comment into the comment box below the detail page.
2. The frontend calls `POST /api/v1/comments` with `{ target_type, target_id, content, parent_id (optional) }`.
3. The backend saves it to `comments` and sends a notification to the author and everyone who has commented in the thread.
4. The frontend renders the new comment in the tree, supporting nested replies up to 3 levels.

**Exception Flow:**

- Content is filtered (spam, profanity) → auto-hidden pending moderation.

**Business Rules:**

- Rate limit: 20 comments/hour/user.
- Editable within 15 minutes after posting, then locked (edit history is kept).

### UC-08.03: Follow an author

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P3 | Medium |

**Preconditions:** Viewing another user's profile.

**Postconditions:** A follow relationship is created; the follower receives a notification when the followee publishes a new template.

**Main Flow:**

1. The user clicks `[Follow]` on the profile.
2. The backend inserts into `follows(follower_id, followee_id)`.
3. The frontend updates the UI to `[Following]`.

**Business Rules:**

- Following is public (anyone can see follower counts).
- The user can hide their following list in privacy settings (Phase 4).

### UC-08.04: View a user's public profile page

| Primary Actor | Phase | Priority |
|---|---|---|
| User / Guest | P3 | Medium |

**Preconditions:** That user has a public username.

**Postconditions:** The profile page displays: avatar, bio, public templates, follower count, shared public prompts.

**Main Flow:**

1. Visit the URL `/u/{username}`.
2. The frontend calls `GET /api/v1/users/by-username/{username}`.
3. The backend returns public info + a list of public templates + public generated prompts.
4. The frontend renders the profile page.

### UC-08.05: Report abuse

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P3 | Medium |

**Preconditions:** Content that can be reported (template, comment, user, generated prompt).

**Postconditions:** A record is created in `reports`, and the admin receives a notification.

**Main Flow:**

1. The user clicks the `[⋯]` menu → `[Report]`.
2. Selects a reason (spam / abuse / copyright / other) and enters details.
3. The frontend calls `POST /api/v1/reports`.
4. The backend saves it with `status='open'` and sends a notification to the admin.

**Business Rules:**

- One user cannot report the same target more than 3 times.
- Content reported multiple times within 1 hour → auto-hidden pending admin review.

### UC-08.06: Receive & view notifications

| Primary Actor | Phase | Priority |
|---|---|---|
| User | P3 | Medium |

**Preconditions:** The user is logged in.

**Postconditions:** The notification is marked as read.

**Main Flow:**

1. The system generates a notification when an event occurs (new comment, template approved, new follower, someone forked one of your templates, etc.).
2. The frontend displays a badge with the unread notification count.
3. The user clicks the bell icon → `GET /api/v1/notifications`.
4. The user clicks an item → marks `read_at`, navigates to the related page.

**Business Rules:**

- Notifications older than 30 days are automatically deleted.
- The user can turn off specific notification types in settings.

---

## 11. Group 9 — Enterprise & Billing (Phase 4)

### UC-09.01: Create a Team Workspace

| Primary Actor | Phase | Priority |
|---|---|---|
| User (about to become Owner) | P4 | High |

**Preconditions:** The user is logged in, has a Pro plan or wants to subscribe to Team.

**Postconditions:** A workspace with `type='team'` is created, with the user as owner.

**Main Flow:**

1. The user goes to `/workspaces` → `[+ New Team Workspace]`.
2. Enters a name, slug, and selects a plan.
3. If not yet subscribed to a Team plan → switches to UC-09.05.
4. After successful payment, the backend creates a `workspaces` record with `type='team'` and creates a `workspace_members` record with `role='owner'`.
5. The user is redirected to the new workspace.

**Business Rules:**

- A user can be the owner of multiple team workspaces.
- The workspace slug must be unique system-wide.

### UC-09.02: Invite members to a Team Workspace

| Primary Actor | Phase | Priority |
|---|---|---|
| Workspace Owner / Admin | P4 | High |

**Preconditions:** There are still available seats under the plan.

**Postconditions:** The member is added to `workspace_members`.

**Main Flow:**

1. The owner goes to `/workspaces/{slug}/members` → `[Invite]`.
2. Enters an email and selects a role (admin/editor/viewer).
3. The backend sends an invitation email containing a 7-day token.
4. The recipient clicks the link → if they don't have an account, they quickly register; then accept the invite.
5. The backend inserts into `workspace_members`.

**Exception Flow:**

- Seat limit exceeded → requires a plan upgrade.
- Email is already a member → `409 Conflict`.

### UC-09.03: Assign permissions by role

| Primary Actor | Phase | Priority |
|---|---|---|
| Workspace Owner / Admin | P4 | High |

**Preconditions:** There are at least 2 members in the workspace.

**Postconditions:** The role is updated.

**Main Flow:**

1. The owner goes to `/workspaces/{slug}/members`.
2. Selects a user → changes their role.
3. The backend updates `workspace_members.role`.

**Business Rules:**

- Owner: full permissions, including deleting the workspace and billing.
- Admin: invite/remove members, manage team templates, no billing access.
- Editor: CRUD team templates, no member management.
- Viewer: can only view/use team templates.
- Cannot self-downgrade the owner role if there is only 1 owner. Must transfer ownership first.

### UC-09.04: Manage the internal template library

| Primary Actor | Phase | Priority |
|---|---|---|
| Workspace Editor / Admin / Owner | P4 | High |

**Preconditions:** The user has Editor+ role in the workspace.

**Postconditions:** The template is created/edited within the team's `workspace_id`.

**Main Flow:**

1. Goes to `/workspaces/{slug}/templates`.
2. Performs CRUD on templates similar to UC-07.02/07.03 but with `workspace_id` = team.
3. Can set `is_public=false` (internal use only), without needing system admin approval.
4. Can fork a public template into the team's workspace.

**Business Rules:**

- Internal templates are not shown on `/explore`.
- Viewer can only view, not edit.
- A team template can be published to the community (moved to public status, requiring approval).

### UC-09.05: Subscribe & pay for a subscription

| Primary Actor | Phase | Priority |
|---|---|---|
| Workspace Owner | P4 | High |

**Preconditions:** The user has a valid Stripe account.

**Postconditions:** The subscription is active, and the workspace is upgraded to the new plan.

**Main Flow:**

1. The owner goes to `/workspaces/{slug}/billing` → selects a plan.
2. The backend calls Stripe to create a checkout session.
3. The user is redirected to Stripe Checkout and completes payment.
4. The Stripe webhook calls `POST /api/v1/webhooks/stripe`.
5. The backend upserts `subscriptions` with `status='active'`, `current_period_start/end`.
6. Updates `workspaces.plan`.
7. The owner receives a confirmation email.

**Alternative Flow:**

- The owner can cancel: subscription `status='canceled'`, still usable until the end of the period.

**Exception Flow:**

- Payment fails → subscription `status='past_due'`, the workspace temporarily retains Pro features for 7 days before downgrading.

### UC-09.06: Enforce usage quota

| Primary Actor | Phase | Priority |
|---|---|---|
| System | P4 | High |

**Preconditions:** The user performs a quota-consuming action (AI Refine, Playground call, template creation).

**Postconditions:** The quota is counted accurately, blocking when exceeded.

**Main Flow:**

1. Each time the user calls a quota-consuming feature, the backend queries `usage_quotas` by (`workspace_id`, `feature`, `period_start=today`).
2. If no row exists → inserts one with `limit_count` from `plans.features`.
3. Compares `used_count` vs `limit_count`. If there's room → increments `used_count` and allows the action.
4. If exceeded → returns `402 Payment Required` with a clear message.

**Business Rules:**

- Quota resets daily (`period_start=DATE_TRUNC('day')`).
- For Team plans, quota is counted per workspace (not per user).
- `limit_count = -1` means unlimited.

### UC-09.07: Create & manage a developer API Key

| Primary Actor | Phase | Priority |
|---|---|---|
| User (Pro plan and above) | P4 | Medium |

**Preconditions:** The workspace has a Pro/Team plan.

**Postconditions:** An API key is created, its hash saved in the database, with the plaintext shown only once.

**Main Flow:**

1. The user goes to `/workspaces/{slug}/api-keys` → `[+ Create key]`.
2. Enters a name, selects scopes, and an optional `expires_at`.
3. The backend generates a key `h2p_live_xxxxxxxxxxxx`, stores `key_hash`, and displays the `key_prefix` + plaintext once.
4. The user copies the key and stores it somewhere safe.
5. Afterward, only the `key_prefix` is shown for identification.

**Alternative Flow:**

- Revoking a key: sets `revoked_at`; any request using that key is subsequently rejected.

**Business Rules:**

- Every request using an API key is recorded in `audit_logs`.
- Rate limiting applies according to the key's scope.

### UC-09.08: View the team analytics dashboard

| Primary Actor | Phase | Priority |
|---|---|---|
| Workspace Admin / Owner | P4 | Medium |

**Preconditions:** The workspace has a Team plan.

**Postconditions:** Metrics are displayed.

**Main Flow:**

1. The admin goes to `/workspaces/{slug}/analytics`.
2. The backend queries aggregates: most-used templates in the team, most active members, remaining quota, AI costs.
3. The frontend renders charts and tables.

---

## 12. Traceability Matrix

The matrix below helps quickly trace between a Use Case, its Epic in the SRS, the main API endpoint, and the related database tables.

| Use Case | SRS Epic | Main API Endpoint | Main DB Tables |
|---|---|---|---|
| UC-01.01 | Epic 1 | POST /auth/register | users, workspaces |
| UC-01.02 | Epic 1 | POST /auth/login | users, refresh_tokens |
| UC-01.03 | Epic 1 | POST /auth/oauth/google | users, user_identities |
| UC-01.07 | Epic 1 | GET/PATCH /users/me | users |
| UC-02.01-04 | Epic 2 | GET /templates, GET /templates/{id} | templates, categories, tags |
| UC-03.01-06 | Epic 3 | POST /templates/{id}/generate | generated_prompts, template_variables, template_variants |
| UC-04.01-03 | Epic 4 | GET /generated-prompts | generated_prompts |
| UC-04.04 | Epic 4 | POST /templates/{id}/favorite | favorites |
| UC-05.01-03 | Epic 5 | POST /admin/ai-models, /admin/templates | ai_models, templates |
| UC-06.01 | Epic 6 | POST /generated-prompts/{id}/refine | generated_prompts (ai_refined) |
| UC-06.03 | Epic 6 | POST /playground/run | generated_prompts (playground_response) |
| UC-07.01 | Epic 7 | POST /templates/{id}/fork | templates (forked_from_*) |
| UC-07.02 | Epic 7 | PATCH /templates/{id} | templates, template_versions, template_variables |
| UC-08.01 | Epic 8 | POST /votes | votes |
| UC-08.02 | Epic 8 | POST /comments | comments |
| UC-09.01-04 | Epic 9 | POST /workspaces, /workspace-members | workspaces, workspace_members |
| UC-09.05 | Epic 9 | POST /subscriptions, /webhooks/stripe | subscriptions, plans |
| UC-09.06 | Epic 9 | (internal check) | usage_quotas |
| UC-09.07 | Epic 9 | POST /api-keys | api_keys |

---

## 13. Overview Use Case Diagram

Due to the limitations of a text document, the use case diagram below is described in structural form. You can convert it to PlantUML/draw.io when a visual diagram is needed.

### 13.1 Actor ↔ Use Case Group Distribution

| Actor | Can Execute These Groups |
|---|---|
| Guest | Group 2 (Discovery — public templates only), part of Group 1 (register, log in) |
| User (Registered) | Groups 1, 2, 3, 4, 6, 7, 8 |
| Author | Inherits User + Group 7 (manages their own templates), receives events from Group 8 |
| Workspace Owner | Inherits User + all of Group 9 |
| Workspace Admin/Editor/Viewer | Group 9 (according to role permissions) |
| Admin (System) | Group 5 (fully), moderation in Group 8 |
| System (Automated) | UC-03.06, UC-04.01, UC-09.06, and background jobs |
| External LLM Provider | Triggered via UC-06.01, UC-06.02, UC-06.03, UC-06.04 |
| Stripe | Triggered via UC-09.05 (webhook) |

### 13.2 `<<include>>` and `<<extend>>` Relationships

- **UC-03.05 (Generate & Copy)** `<<include>>` UC-03.06 (Backend render) and UC-04.01 (Auto-archive history).
- **UC-01.01 (Register)** `<<include>>` automatically creates a Personal Workspace.
- **UC-06.01 (AI Refine)** `<<extend>>` UC-03.05 (only when the user actively clicks it).
- **UC-06.03 (Playground)** `<<extend>>` UC-03.05.
- **UC-07.01 (Fork)** `<<extend>>` UC-02.04 (View template detail).
- **Every quota-consuming use case** `<<include>>` UC-09.06 (Quota enforcement) once the system is in Phase 4.

### 13.3 Generalization

- Workspace Owner, Admin, Editor, and Viewer all generalize from User.
- Author is a specialization of User once they have published a template.
- Guest and User share some read-only use cases (UC-02.01, UC-02.04) — using common includes.
