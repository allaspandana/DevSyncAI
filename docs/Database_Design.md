# Database Design

## 1. Users

| Column | Description |
|---------|-------------|
| id | Primary Key |
| username | Username |
| first_name | User's first name |
| last_name | User's last name |
| email | Email address |
| password | Password (hashed) |
| role | Admin, Team Leader, Developer, Tester |
| phone | Phone number |
| profile_image | Profile picture |
| created_at | Account creation date |

---

## 2. Teams

| Column | Description |
|---------|-------------|
| id | Primary Key |
| team_name | Team name |
| description | Team description |
| team_leader | Team leader (User) |
| created_at | Creation date |

---

## 3. TeamMembers

| Column | Description |
|---------|-------------|
| id | Primary Key |
| team | Team |
| user | User |
| joined_at | Date joined |

---

## 4. Projects

| Column | Description |
|---------|-------------|
| id | Primary Key |
| project_name | Project name |
| description | Project description |
| start_date | Start date |
| end_date | End date |
| status | Planned, Active, Completed |
| priority | Low, Medium, High |
| team | Assigned team |
| created_at | Creation date |

---

## 5. Sprints

| Column | Description |
|---------|-------------|
| id | Primary Key |
| project | Related project |
| sprint_name | Sprint name |
| goal | Sprint goal |
| start_date | Start date |
| end_date | End date |
| status | Planned, Active, Completed |

---

## 6. Tasks

| Column | Description |
|---------|-------------|
| id | Primary Key |
| sprint | Related sprint |
| title | Task title |
| description | Task description |
| assigned_to | Developer |
| status | Pending, In Progress, Completed |
| priority | Low, Medium, High |
| deadline | Due date |
| estimated_hours | Estimated work time |
| actual_hours | Actual work time |
| created_at | Creation date |

---

## 7. TaskComments

| Column | Description |
|---------|-------------|
| id | Primary Key |
| task | Related task |
| user | Comment author |
| comment | Comment text |
| created_at | Comment date |

---

## 8. Bugs

| Column | Description |
|---------|-------------|
| id | Primary Key |
| task | Related task |
| reported_by | Tester |
| assigned_to | Developer |
| title | Bug title |
| description | Bug description |
| priority | Low, Medium, High, Critical |
| status | Open, In Progress, Resolved, Closed |
| created_at | Report date |

---

## 9. Notifications

| Column | Description |
|---------|-------------|
| id | Primary Key |
| user | Notification receiver |
| message | Notification message |
| is_read | Yes/No |
| created_at | Notification date |

---

## 10. Files

| Column | Description |
|---------|-------------|
| id | Primary Key |
| task | Related task |
| uploaded_by | User |
| file_name | File name |
| file_path | File location |
| uploaded_at | Upload date |