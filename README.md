# Tutorial Setup Guide

## Setting Up the Environment

### Create a Python Virtual Environment (venv)
1. Navigate to your project directory.
2. Run the following command to create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

## Uploading a Video File
1. Place your video file in the appropriate directory.
2. Ensure that the file name is properly passed through in `main.py`.

## Running the Project
1. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```sh
   python main.py
   ```

## Additional Notes
- Ensure that all necessary dependencies are listed in `requirements.txt`.
- Check `main.py` for any additional configurations or parameters needed for video processing.


