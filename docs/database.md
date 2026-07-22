# Database Schema & Variable Strategy — how2prompt

The database schema of how2prompt is built in PostgreSQL (v15+) to manage users, teams, templates, variables, and request logs. 

## Table Schema Definitions

```text
+-------------------+
|       teams       |
|-------------------|
| id          (PK)  |
| name              |
| created_at        |
+---------+---------+
          | 1
          |
          | N
+---------+---------+        +-------------------+
|       users       | 1    1 |   user_variables  |
|-------------------|--------|-------------------|
| id          (PK)  |        | user_id (PK, FK)  |
| username          |        | variables (JSONB) |
| password_hash     |        | updated_at        |
| team_id     (FK)  |        +-------------------+
| created_at        |
+----+----+---------+
     |    | 1
     |    |
     |    | N
     |  +-+------------------+
     |  |       history      |
     |  |--------------------|
     |  | id            (PK) |
     |  | user_id       (FK) |
     |  | template_id   (FK) |
     |  | variable_snap(JSONB|
     |  | created_at         |
     |  +--------------------+
     | 1
     |
     | N
+----+----+---------+
|     templates     |
|-------------------|
| id          (PK)  |
| name              |
| content           |
| tags              |
| team_id     (FK)  |
| created_by  (FK)  |
| created_at        |
+-------------------+
```

### 1. `teams`
Represents developer teams inside an organization. Enables sharing of templates and global coding guidelines.
- `id` (UUID, Primary Key)
- `name` (VARCHAR)
- `created_at` (TIMESTAMP)

### 2. `users`
Represents individual developers.
- `id` (UUID, Primary Key)
- `username` (VARCHAR, Unique)
- `password_hash` (VARCHAR)
- `team_id` (UUID, Foreign Key referencing `teams.id`, Nullable)
- `created_at` (TIMESTAMP)

### 3. `user_variables`
Holds user-defined default values for template variables (e.g. `{language} = "C#"`).
- `user_id` (UUID, Primary Key, Foreign Key referencing `users.id`)
- `variables` (JSONB) — Key-value collection mapping variable names to their configurations.
- `updated_at` (TIMESTAMP)

### 4. `templates`
Holds standard prompt templates created by users or shared across teams.
- `id` (UUID, Primary Key)
- `name` (VARCHAR)
- `content` (TEXT) — The prompt template body containing placeholders (e.g., `"Review this {language} code: {code}"`).
- `tags` (TEXT[]) — Array of tags for categorization and search index.
- `team_id` (UUID, Foreign Key referencing `teams.id`, Nullable) — If non-null, indicates the template is shared with this team.
- `created_by` (UUID, Foreign Key referencing `users.id`)
- `created_at` (TIMESTAMP)

### 5. `history`
Represents snapshot records of copied prompts. Used to power the Quick-History Drawer (showing up to 20 past logs).
- `id` (UUID, Primary Key)
- `user_id` (UUID, Foreign Key referencing `users.id`)
- `template_id` (UUID, Foreign Key referencing `templates.id`, Nullable) — Identifies the base template used. Null if it was a custom ad-hoc prompt optimization.
- `variable_snapshot` (JSONB) — Snapshot of all active variables and values used during that copy action.
- `created_at` (TIMESTAMP)

---

## JSONB for Variable Storage: Rationale

The platform stores active variables (within `user_variables` and `history`) inside PostgreSQL `JSONB` columns. 

### Why JSONB instead of Entity-Attribute-Value (EAV)?
An Entity-Attribute-Value schema (e.g., `user_variable_values` table with `user_id`, `variable_key`, `variable_value` columns) is the traditional approach to storing dynamic, open-ended key-value pairs. However, it introduces significant downsides:
1. **Query Overhead:** Loading 15 active variables for a user requires performing joins or scanning multiple rows. With JSONB, all variables for a user are read in a single, index-backed row fetch.
2. **Simplified Writes:** Updating variables requires multiple SQL inserts/updates in EAV. JSONB allows overwriting or patching the entire dictionary in a single query.
3. **Snapshot Integrity:** For prompt execution logs (`history`), the database must store an immutable snapshot of all variable states used *at the moment of copying*. A JSONB column makes it trivial to save a static dictionary without needing foreign keys that could break if users delete variables in the future.
