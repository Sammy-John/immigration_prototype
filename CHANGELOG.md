# **Changelog**

All notable changes to this project will be documented in this file.

## [Unreleased]

## [Initial Setup] - 2024-09-13
- Repository created: `immigration_prototype`.
- Initial project planning and scope defined.
- Outline planned core features and functionality.

## [Completed] - 2024-09-14
### `auth_app` Development
- Implemented user authentication (login/logout).
- Added user authorization with role-based access control (RBAC).
- Created user creation view for Managers and Super Admins.
- Implemented meaningful audit logging for user management actions.
- Error handling and messaging for authentication and authorization.
- Set up the admin interface for user and group management.
- Fixed bugs related to logging and user permissions.

## [In Progress] - 2024-09-15
### `crm` App Development
- Implemented user creation and update logic.
- Developed functionality for creating, updating, and listing leads.
- Synced users from `auth_app` to `crm` for cross-database consistency.
- Enhanced error handling for lead creation and updates.
- Added initial validation for duplicate leads.
- Fixed issues related to foreign key constraints between `auth_app` and `crm`.

---

**Note:** This changelog is a living document and will be updated regularly to reflect the project's progress and new changes.
