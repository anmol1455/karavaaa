# karavaaa

# Chat API

## Purpose

The Chat API chatting functionality, and accessing chat history. It allows users to log in, send messages, and retrieve chat history.

## Setup

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:

    - **For Windows**:

        ```bash
        env\Scripts\activate
        ```

    - **For Unix/macOS**:

        ```bash
        source env/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Starting the Server

To start the server, run the following command:

```bash
python start_Server.py
```

This will start the server locally, and it will be accessible at http://localhost:8000.

Running Tests
To run the test cases, use pytest:

```bash
pytest test.py
```

1. **/chat/login** - POST

    - **Purpose:** Allows users to log in and obtain a session ID.
    - **Authentication:** Basic HTTP authentication with username and password.
    - **Response:** Returns a JSON object containing a session ID upon successful login.

2. **/chat/logout** - POST

    - **Purpose:** Logs out the user and deletes the session ID.
    - **Parameters:** 
        - `session_id` (string) - The session ID of the user.
    - **Response:** Returns a JSON object confirming successful logout.

3. **/chat/** - GET

    - **Purpose:** Allows authenticated users to send messages.
    - **Parameters:** 
        - `user_input` (string) - The message to send.
        - `session_id` (string) - The session ID of the user.
    - **Response:** Returns a JSON object containing the response from the chatbot.

4. **/chat/history** - GET

    - **Purpose:** Retrieves the chat history for the authenticated user.
    - **Parameters:** 
        - `session_id` (string) - The session ID of the user.
    - **Response:** Returns a JSON object containing the chat history.

To access the Swagger UI for the API documentation, go to:

```bash
http://localhost:8000/docs
```

To access the user interface (UI) for the chat application, go to:

```bash
http://localhost:8000/chat/signin
```