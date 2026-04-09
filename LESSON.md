# Spreadsheet-to-Database Lab ☕

Welcome to your mission as a **Junior Data Engineer**! Before we dive into complex systems like SQL, we're going to explore a simple truth: **a database is just a place to store and organize data.**

You will learn how to:
1.  **Launch** a containerized web application using Docker.
2.  **Explore** a live menu being powered by a simple spreadsheet.
3.  **Investigate** the "under-the-hood" CSV data that bridges the gap between spreadsheets and databases.
4.  **Create** your own version of the database by cloning a template.

---

## 🚀 Quick Start

### 0. Open Debian, Download the code. 
You need to get the code onto your computer, and yourself in the right place to start this work. 
```bash
# download the code from github
git clone https://github.com/RiceC-at-MasonHS/spreadsheet_example_db.git

# move into the repo you just downloaded
cd spreadsheet_example_db

# look around at the files you just downloaded:
ls -lAh
```

### 1. Launch the Lab
Everything is pre-configured with **Docker**. Just run:

```bash
# [!NOTE] You may need to start 'Docker Desktop' for this to work
# It is probably good to look around at the files you just downloaded...
# start the docker container from the files in the folder
docker compose up -d
```

This starts the **Vibe Coffee GUI (Flask)** service, which you can view at: [`http://localhost:5000`](http://localhost:5000)

### 2. View the Live Data
Open your browser and navigate to the link above. You should see the **Vibe Coffee Co.** menu.

**Wait... where is this data coming from?** There is no `menu.json` or `data.db` file in this folder! And you can go look at [the webpage's code](/templates/index.html) to see the data about these drinks are not hardcoded onto the webpage. 

---

## 🗺️ Your Learning Path

### Mission 0: The Secret Sauce (Spreadsheet)
The data you see on the website is actually living in a **Google Sheet**. 

1.  Open the [Source Google Sheet](https://docs.google.com/spreadsheets/d/1TdeCvbScLdZcFnfoobxCAtdztljMh2ssm2IRvq1xnHU/edit#gid=1999930924). This will open a view-only version of the Spreadsheet. There are two tabs: the 'secret' `data` tab that is not downloaded, and the `public` tab that is downloaded by the webapp. 
2.  On the `public` tab, look at the columns: `id`, `coffee`, `price`, `order_count`.
3.  Now look at the website again. Notice how each item in the spreadsheet corresponds to a "menu item" on the site?

**Think about:** If you were to add a new row to this spreadsheet, what would happen to the website? (In this demo, the sheet is "Published to Web" as a CSV, which the app fetches every time you refresh).

### Mission 1: Under the Hood (CSV)
Databases often export data in **CSV** (Comma-Separated Values) format. It's the "universal language" of data.

1.  Click the link at the bottom of the Vibe Coffee website: `>> download the raw CSV for yourself <<`. This should download a CSV file.
2.  Open the downloaded file in a text editor (like Notepad or VS Code).
3.  Compare the text format to the spreadsheet layout.

This is exactly what the Python code sees! It "parses" these lines of text and turns them into the beautiful menu you see in your browser.

Generally, this is how databases of all types do their thing. It's not a bad analogy to think of databases as 'headless' spreadsheets.

---

## 🏗️ Building Your Own

### Step 1: Clone the Spreadsheet
To see this in action for yourself, you need your own "database":
1.  Open this link: [**[CLICK HERE TO COPY THE TEMPLATE]**](https://docs.google.com/spreadsheets/d/1TdeCvbScLdZcFnfoobxCAtdztljMh2ssm2IRvq1xnHU/copy)
2.  Add your name to the menu as a "Special Drink"!
```
id,    coffee,         price,      order_count
21,    <your-name>,    1000000,    1
```
3.  In Google Sheets, go to: **File > Share > Publish to Web**.
4.  Select `public` (or your active sheet) and change the format to `Comma-separated values (.csv)`.
5.  Click **Publish** and copy the long URL.

> [!DANGER]
> This will *really* be a public spreadsheet with your name. 
> So pull it back down after you finish the assignment. 

### Step 2: Update the App
Now, tell the app to use *your* database instead of the default one:
1.  Open `app.py`.
2.  Find the `CSV_URL` variable on line 9.
3.  Replace the existing URL with your new published CSV URL.
4.  Save the file and refresh your browser! (You may need to stop and rebuild the docker containers for this to work.)

```shell
# stop the current Docker containers
docker compose down

# rebuild + restart the containers
docker compose up --build -d
```
5. Navigate back to the **Vibe Coffee GUI (Flask)** webpage, which you can view at: [`http://localhost:5000`](http://localhost:5000)

### Step 3: 📸 Take a Screenshot
You should collect a screenshot to submit for this assignment. The screenshot should be fullscreen, show your name on the website 'Vibe Coffee Co.' website, and show your copy of the spreadsheet. Ideally, your name or Google user-icon would also be clearly visible. 

Submit this screenshot to the assignment in Schoology. 

---

## 🧪 Test Your Knowledge

1.  **What is a CSV file?** How does it differ from a regular spreadsheet?
2.  **Why use a database instead of a spreadsheet?** (Think about what happens if 1,000 people try to edit the same row at the same time!)
3.  **Data Integrity:** What happens if you change a "Price" in the spreadsheet to a word (like "FREE")? Does the app break?

---

## 🏗️ Architecture Reminder

-   **Cloud Database**: Google Sheets (Source of Truth)
-   **Bridge**: CSV Export (The data format)
-   **Engine**: Python & Flask (The translator)
-   **Package**: Docker (The container)

## 📜 License
GPL-3
