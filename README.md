# Task-Tracker-Practice-
Prroject URL- https://roadmap.sh/projects/task-tracker
# 🚀 Task Tracker CLI & Web Dashboard

**Project URL:** https://roadmap.sh/projects/task-tracker

A complete task management application built for the [roadmap.sh Task Tracker Project](https://roadmap.sh/projects/task-tracker). This repository includes both a **pure Python CLI tool** with zero external dependencies and local JSON persistence, as well as an extended **FastAPI REST API with an interactive HTML/JS web dashboard**.

---

## ✨ Features

- **Native CLI Interface (`task_cli.py`):** Runs purely on Python standard libraries (`sys`, `json`, `os`, `datetime`) without third-party dependencies.
- **Local File Persistence:** Stores tasks securely in `tasks.json` in the project directory.
- **FastAPI REST Engine (`main.py`):** Full CRUD endpoints (`POST`, `GET`, `PUT`, `DELETE`) with type safety via Pydantic and Enums.
- **Interactive Web Dashboard (`frontend.html`):** Native JavaScript fetch-based UI featuring real-time grid updates and pre-filled edit forms.
- **Timestamps & Schemas:** Auto-generates and tracks `createdAt` and `updatedAt` in UTC format across all tasks.

---

## 💻 CLI Usage (roadmap.sh Specification)

The CLI tool requires no external installation. Execute commands directly using Python:

### 1. Add a New Task
```bash
python task_cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
