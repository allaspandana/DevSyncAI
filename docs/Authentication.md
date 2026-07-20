# Authentication

## Purpose

This module manages user authentication and authorization.

## User Fields

- Username
- Email
- Phone Number
- Profile Picture
- Role
- Created At

## Roles

- Admin
- Team Leader
- Developer
- Tester

## Authentication Flow

User logs in → Django authenticates → Role determines permissions.

## Database Table

CustomUser