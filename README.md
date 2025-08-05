

instructions = """
How to Run the YouTube Video Downloader Flask App
==================================================

📁 Prerequisites:
-----------------
- Python installed (version 3.6 or above)
- pip (Python package manager)
- Git (optional, for cloning)

🧱 Step-by-Step Setup:
-----------------------

1. Open your terminal or command prompt.

2. (Optional but recommended) Create a virtual environment:
   For Windows:
       python -m venv venv
       venv\\Scripts\\activate
   For macOS/Linux:
       python3 -m venv venv
       source venv/bin/activate

3. Install the required packages:
       pip install flask yt-dlp

4. Ensure the project folder has the following structure:
       - app.py
       - templates/
           - index.html  <-- You need to create this with a basic HTML form
       - downloads/ (will be auto-created)

5. Run the application:
       python app.py

6. Open your browser and go to:
       http://127.0.0.1:5000/

7. Enter a YouTube URL and click "Download" to get the video.

🛑 Notes:
---------
- If `index.html` is missing, the home page will not render. Make sure to include it in a `templates` folder.
- Downloaded videos are saved temporarily in the `downloads` directory.
- Ensure a stable internet connection during download.
"""

# Save to a text file
file_path = "/mnt/data/How_to_Run.txt"
with open(file_path, "w") as f:
    f.write(instructions)

file_path
