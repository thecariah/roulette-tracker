# Roulette Tracker - Backend

## Description

This backend service is built with FastAPI to track roulette game statistics. It is implemented in Python and uses Uvicorn as the ASGI server.

## Technologies Used

- **Python**: Programming language used for the backend logic.
- **FastAPI**: Web framework for building APIs with Python.
- **Uvicorn**: ASGI server for serving the FastAPI application.

## Setup Instructions

1. **Clone the repository** (if not already cloned):
    ```sh
    git clone https://github.com/thecariah/roulette-tracker.git
    cd roulette-tracker/backend
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the application**:
    ```sh
    uvicorn roulette-tracker.main:app --reload
    ```

This will start the FastAPI application and you can access it at `http://127.0.0.1:8000`.
