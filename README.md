# LLMS.txt Generator Web App

This web application allows users to generate a single text file (`LLMS.txt`) by extracting content from:
1.  A website URL.
2.  An uploaded single text file.
3.  All text files within an uploaded folder.

The generated text can be viewed in the app and then downloaded.

## Features

*   **URL Processing:** Fetches HTML from a URL, attempts to extract main textual content.
*   **File Upload:** Reads content from a single uploaded text-based file (e.g., .txt, .md, .py).
*   **Folder Upload:** Reads and concatenates content from all text-based files within a selected folder and its subfolders.
*   **Content Preview:** Displays the extracted text.
*   **Download:** Allows saving the combined text as `LLMS.txt`.

## Technology Stack

*   **Frontend:** React (created with `create-react-app`)
*   **Backend:** Python, Flask (for URL processing)
*   **HTML Parsing (URL):** BeautifulSoup4
*   **HTTP Requests (URL):** requests library

## Setup and Installation

### Prerequisites

*   Node.js and npm (or yarn) for the frontend.
*   Python 3.x and pip for the backend.

### Backend Setup

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Create a Python virtual environment (recommended):
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    *   Windows: `venv\Scripts\activate`
    *   macOS/Linux: `source venv/bin/activate`
4.  Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Frontend Setup

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
    (If you are in `backend/`, use `cd ../frontend`)
2.  Install Node.js dependencies:
    ```bash
    npm install
    ```
    (or `yarn install` if you prefer yarn)

## Running the Application

You need to run both the backend and frontend servers simultaneously.

1.  **Run the Backend (Flask server):**
    *   Open a terminal, navigate to the `backend` directory.
    *   Ensure your virtual environment is activated.
    *   Start the Flask development server:
        ```bash
        python app.py
        ```
    *   The backend will typically run on `http://localhost:5000`.

2.  **Run the Frontend (React dev server):**
    *   Open another terminal, navigate to the `frontend` directory.
    *   Start the React development server:
        ```bash
        npm start
        ```
        (or `yarn start`)
    *   The frontend will typically open automatically in your browser at `http://localhost:3000`.

Now you can access the web app at `http://localhost:3000`.

## How to Use

1.  Select the input type: "From URL", "From File", or "From Folder".
2.  **URL:** Enter the full URL (e.g., `https://example.com`) and click "Generate from URL".
3.  **File:** Click the "Choose File" button, select a single text-based file. Processing starts automatically.
4.  **Folder:** Click the "Choose Files" (or similar, browser-dependent) button and select a folder. All text-based files within will be processed.
5.  The extracted text will appear in the textarea below.
6.  Click "Save LLMS.txt" to download the file.

## Limitations

*   **URL Text Extraction:** The current HTML parsing is basic and might not always perfectly isolate main content.
*   **File Types:** Client-side file/folder processing primarily supports plain text files (.txt, .md, .py, .js, .html, .css etc.). Binary files like PDFs or DOCX are not processed for text content in this version.
*   **Large Folders:** Processing very large folders with many files client-side might be slow or consume significant browser resources.