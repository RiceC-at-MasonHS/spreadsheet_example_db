# Spreadsheet-to-Database Lab (Coffee Co. Example) ☕

A teaching tool designed to demonstrate that databases aren't magic—they're just structured data, much like the spreadsheets students already know and love. This project uses a live Google Sheet as a "database" to power a Flask web interface.

> [!IMPORTANT]
> **Students & Learners:** For the guided lab instructions and missions, please see [**LESSON.md**](./LESSON.md).
> ------------------------ This is your "onramp" to learning more complex database systems!

---

## 🛠️ Project Overview

This lab demonstrates how an application can interact with external data sources:
- **Cloud Source (Google Sheets)**: How a simple spreadsheet can act as a real-time data provider.
- **CSV Data (Requests)**: How Python can fetch and parse comma-separated data from the web.
- **Web UI (Flask)**: How data is dynamically rendered into a modern browser interface.
- **Containerization (Docker)**: How to package a web application so it runs the same way for everyone.

---

## 🏗️ Technical Architecture

- **Data Source**: [Google Sheets](https://docs.google.com/spreadsheets/) (Published as CSV)
- **Backend**: Python 3.9 with [Flask](https://flask.palletsprojects.com/) and [Requests](https://requests.readthedocs.io/)
- **Web Interface**: HTML5 + CSS3 (Modern "Vibe Coffee" aesthetic)
- **Containerization**: [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

---

## 🚀 Getting Started

### 1. Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or Docker Engine installed.
- [Git](https://git-scm.com/) installed.

### 2. Setup
Clone the repository and launch the environment:

```bash
git clone https://github.com/RiceC-at-MasonHS/spreadsheet_example_db.git
cd spreadsheet_example_db
docker compose up -d
```

This starts the following service:
- **Vibe Coffee GUI**: [http://localhost:5000](http://localhost:5000)

### 3. Live Updates
Because this app is connected directly to a Google Sheet, any changes made to the source spreadsheet (once published) will appear in the app after a simple page refresh!

---

## 🧪 Development & Exploration

To see the raw data being used by the app:
```bash
# You can view the CSV export URL directly in your browser:
# https://docs.google.com/spreadsheets/d/e/2PACX-1vTOJSjMWjpTEpNjEcTGwpo_t6gREpp_6tXQhsif1LXgR8tNWVfll7sUYQPS4tNowJLLMhSUzkF093LG/pub?gid=1999930924&single=true&output=csv
```

For more details on the "Spreadsheet vs. Database" mission, refer to the [**LESSON.md**](./LESSON.md) file.

---

## 📜 License
GPL-3