# GitOps

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd gitpractice

2.  **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```
3. **Activate the virtual environment:**

    On Windows:
    ```sh
    venv\Scripts\activate
    ```

    On macOS/Linux:
    ```sh
    source venv/bin/activate
    ```

4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```
