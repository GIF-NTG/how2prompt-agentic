# User Story 2.2: Context Retention & Decoupled JWT Sessions

## Overview
- **Epic**: Epic 2: Authentication & Context Configurations
- **Priority**: P2
- **User Persona**: Member (Authenticated)

## Story Description
- **As a** Member,
- **I want to** my authentication session to persist across visits and let me logout,
- **So that** I remain signed in securely without constant credential entries.

## Acceptance Criteria (BDD Format)
- **Given** a Member has successfully logged in and received a JWT token.
- **When** the login completes.
- **Then** the React SPA stores the token in `localStorage` and updates the React `AuthContext` to display user indicators.
- **When** the React application makes API requests.
- **Then** an Axios request interceptor attaches the JWT token to the `Authorization: Bearer <token>` header.
- **When** the page is reloaded (F5) or closed and reopened.
- **Then** the application checks `localStorage` for the token, updates context if valid, and redirects to Login if the token has expired or is invalid.
- **When** the user clicks "Đăng xuất" (Logout).
- **Then** the system purges the JWT token from `localStorage`, resets `AuthContext` to null, and redirects to the homepage.

## Technical Implementation Details
- **Frontend Layer**:
  - React `AuthContext` and custom `useAuth` hook to hold and manage authentication state (user info, token).
  - Session Persistence: On login, store the JWT in `localStorage` (`localStorage.setItem('jwt_token', token)`). On bootstrap, check if token exists, parse its expiration claim locally (or perform a lightweight token validation query), and set active context.
  - **Axios Interceptors configuration**:
    - Request interceptor: Centrally injects `Authorization: Bearer <token>` header to all outgoing requests if token is available in local storage as specified in [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md).
    - Response interceptor: Intercepts `401 Unauthorized` responses and automatically deletes the invalid/expired token, purges context, and forwards the browser routing context to `/login`.
  - Logout functionality: Clear `localStorage` and update react context to `null`, redirecting the user back to the homepage workspace.

## Verification & Testing
- Log in and verify that the JWT token is present in the browser `Application` storage (`localStorage`).
- Perform requests to private routes (e.g. History list) and check HTTP headers in Network tab to confirm `Authorization` header injection.
- Trigger a hard page refresh (F5) and ensure user remains logged in (does not redirect to login page).
- Click "Đăng xuất" (Logout), verify `localStorage` is cleared, state resets, and UI routes back to home.
- Refer to [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md), [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md), and [how2prompt-agentic/docs/epics.md](how2prompt-agentic/docs/epics.md) for full system specifications.
