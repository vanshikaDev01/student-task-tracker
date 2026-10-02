# Student Task Tracker

## 📌 About the Project

Student Task Tracker is a simple web application where a user can enter a task and send it to a Python backend.

This project is made to understand how a **frontend and backend communicate with each other**.

## 🛠️ Technologies Used

* HTML — webpage structure
* CSS — webpage design
* JavaScript — sends the task to the backend
* Python — backend logic
* Flask — Python web framework

## 📁 Project Structure

```text
student-task-tracker/
│
├── frontend/
│   ├── index.html
│   └── style.css
│
├── backend/
│   └── app.py
│
└── README.md
```

## ⚙️ How It Works

1. The user enters a task in the frontend.
2. JavaScript sends the task to the Python backend.
3. Flask receives the task.
4. Python processes the task.
5. The backend sends a response back to the frontend.
6. The frontend displays the response.

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install Flask

Open the terminal and run:

```bash
pip install flask flask-cors
```

### 3. Start the Backend

Go to the backend folder:

```bash
cd backend
```

Then run:

```bash
python app.py
```

The backend will run at:

```text
http://127.0.0.1:5000
```

### 4. Open the Frontend

Open:

```text
frontend/index.html
```

in your browser.

Enter a task and click **Add Task**.

## 👥 Team Members

* Name — USN
* Name — USN
* Name — USN
* Name — USN

## 🚧 Current Status

The basic frontend-backend connection is working.

The project currently does not have a database or permanent task storage.
