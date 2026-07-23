# User Story 2.1: Member Account Registration & Login

## Overview
- **Epic**: Epic 2: Authentication & Context Configurations
- **Priority**: P2
- **User Persona**: Guest (Unauthenticated)

## Story Description
- **As a** Guest,
- **I want to** register an account and log in securely,
- **So that** I can unlock personalized context retention and history logging.

## Acceptance Criteria (BDD Format)
- **Given** a guest is on the Registration page.
- **When** they submit their email, username, and password.
- **Then** the backend Gateway verifies the email is unique, hashes the password using BCrypt, saves the user to PostgreSQL, and redirects to the Login page.
- **Given** the user is on the Login page.
- **When** they submit valid credentials.
- **Then** the Spring Boot Gateway generates a secure, stateless JWT token (valid for 7 days) and returns it.
- **When** they submit invalid credentials.
- **Then** the Gateway responds with an `HTTP 401 Unauthorized` status wrapped in a standard RFC-7807 error detail envelope.

## Technical Implementation Details
- **Frontend Layer**:
  - Registration Form Component (validates inputs: valid email format, secure password strength, username present).
  - Login Form Component (captures email/username and password).
  - Handle redirection paths: registration success redirects to `/login`; login success redirects to the dashboard.
- **Backend API Layer**:
  - REST endpoints under `/api/v1/auth/` namespace:
    - `POST /api/v1/auth/register` - Creates user record.
    - `POST /api/v1/auth/login` - Performs validation, issues stateless JWT token.
  - Password hashing utilizing Spring Security's `BCryptPasswordEncoder` (BCrypt hashing).
  - Token generation: Secure HMAC-SHA256 signature, payload containing user identity/claims, with validity expiration set to 7 days.
- **Database Layer**:
  - `users` table:
    - `id` (UUID, Primary Key)
    - `email` (VARCHAR, Unique Constraint)
    - `username` (VARCHAR)
    - `password_hash` (VARCHAR)
    - `created_at` (TIMESTAMP)
- **Exception & Error Handling**:
  - Invalid credentials or registration validation errors must return standard RFC-7807 error envelopes (e.g. `HTTP 401 Unauthorized` with `UNAUTHORIZED_ACCESS` code) as specified in [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md).

## Verification & Testing
- Attempt registration with a duplicate email and confirm validation fails.
- Complete registration with a new email and verify password is encrypted (stored as hash, not plaintext) in the database.
- Attempt login with invalid password, verify receipt of `401 Unauthorized` standard RFC-7807 error payload.
- Log in with valid credentials, verify response returns status code `200 OK` and a JWT token.
- Refer to [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md), [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md), and [how2prompt-agentic/docs/epics.md](how2prompt-agentic/docs/epics.md) for full system specifications.
