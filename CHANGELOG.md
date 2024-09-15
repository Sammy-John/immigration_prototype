# **Changelog**

All notable changes to this project will be documented in this file.

## [Unreleased]

### Planned Features
- Set up Django project with core structure.
- Develop `auth_app` for managing authentication and authorization.
- Create `crm` app for client relationship management.
- Implement `payment` app to simulate payment processing.
- Build `email_service` app for managing email communication.
- Add `cloud_storage` app for secure file storage and management.
- Create `document_management` app for word processing and document handling.
- Develop `communication` app for live chat, notifications, and messaging.
- Implement `analytics` app for generating reports and data visualization.
- Add `ticketing` app for managing client inquiries and support requests.
- Develop `feedback` app for collecting and analyzing client feedback.
- Create `lms` app for training modules and educational content.
- Add `chatbot` app to automate responses to common client queries.
- Develop `appointment` app for scheduling client appointments and meetings.
- Build `workflow_automation` app for automating repetitive tasks.
- Add `marketing` app for managing marketing campaigns and newsletters.
- Create `client_portal` app for providing a secure client interface.
- Develop `hr_management` app for managing internal HR functions.
- Build `internal_communication` app for internal communication and collaboration.
- Create `website` app to simulate user interaction with the system.

### Future Enhancements for `auth_app`
- Implement password reset and change features.
- Integrate email verification and notifications.
- Enable user profile management.
- Enhance security with two-factor authentication (2FA) and additional password policies.
- Develop an admin dashboard for user management and audit log viewing.
- Expand audit logging to cover additional user actions.
- Improve the UI/UX of authentication and authorization pages.

### Future Enhancements for `crm` App
- Add functionality for listing leads with notes and mailing list fields.
- Implement role-based access control specific to CRM operations.
- Ensure all CRUD operations are fully tested and validated.
- Sync users between `auth_app` and `crm` to maintain cross-database consistency.

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
