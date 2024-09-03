
# YouTube Video Downloader with Streamlit

This is a simple YouTube video downloader application built using Streamlit and `yt-dlp`. The application allows users to input a YouTube video URL, select a video quality, and download the video to a specified directory. The download progress is displayed in real-time.

## Features

- **Input YouTube URL**: Enter the URL of the YouTube video you want to download.
- **Select Video Quality**: Choose from available video qualities and formats.
- **Download Progress**: Real-time progress bar and status updates during the download.
- **Custom Download Directory**: Specify the directory where the video will be saved.

## Requirements

- Python 3.7 or later
- `yt-dlp` for downloading videos
- `streamlit` for creating the web interface

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Rameshcm581/Youtube-Streamlit.git
   cd Youtube-Streamlit
   ```

2. **Create a Virtual Environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

## Usage

1. **Open the App**

   After running the Streamlit app, a web browser will open displaying the app interface.

2. **Enter YouTube URL**

   Input the URL of the YouTube video you want to download.

3. **Select Quality**

   From the dropdown menu, select the desired video quality.

4. **Specify Download Directory**

   Enter the path to the directory where you want to save the downloaded video. If the directory does not exist, it will be created.

5. **Download Video**

   Click the download button to start the download. The progress bar will update as the video is being downloaded.

## Example Screenshot

![Screenshot](screenshot.png)

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).

```

### Notes:

1. **Replace Placeholders:**
   - `[https://github.com/Rameshcm581/Youtube-Streamlit.git](https://github.com/Rameshcm581/Youtube-Streamlit.git)` with your repository's URL.
   - `app.py` with the name of your Streamlit script.
   - `screenshot.png` with an actual screenshot of your application, if available.
   - `rameshc182003@gmail.com` with your contact email.

2. **Install `requirements.txt`:**
   
   **
   pip install requirements.txt
**


This `README.md` provides clear instructions for users to understand, install, and use your YouTube video downloader application.
