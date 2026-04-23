# Task Manager API

## Run the application:
```bash
uvicorn app.main:app --reload
```

## Visit:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Features:
- Create Task
- Get All Tasks
- Get Task by ID
- Update Task
- Delete Task

## Database Testing
The main database `tasks.db` is ignored by Git to prevent data leaks or conflicts. 

### To use the reference database:
**MacOS / Linux / PowerShell:**
```bash
cp tasks.db.reference tasks.db
```
**Windows (Command Prompt):**
```cmd
copy tasks.db.reference tasks.db
```

### To reset the database:
**MacOS / Linux / PowerShell:**
```bash
rm tasks.db
```
**Windows (Command Prompt):**
```cmd
del tasks.db
```
