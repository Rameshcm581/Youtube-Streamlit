import yt_dlp
import streamlit as st
import os

def get_youtube_video(youtube_url, download_path):
    # Streamlit progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()

    def progress_hook(d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded_bytes = d.get('downloaded_bytes', 0)
            if total_bytes:
                progress = int(downloaded_bytes / total_bytes * 100)
                progress_bar.progress(progress)
                status_text.text(f"Download progress: {progress}%")
            else:
                progress_bar.progress(0)
                status_text.text("Starting download...")

    try:
        # Create an instance of yt-dlp with the necessary options
        ydl_opts = {
            'allow_unplayable_formats': True,
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Save video to specified directory
            'progress_hooks': [progress_hook],  # Hook for progress updates
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get the video info
            info_dict = ydl.extract_info(youtube_url, download=False)
            formats = info_dict.get('formats', [])
            
            # Display available qualities
            st.write("\n### Available video qualities:")
            format_list = []
            for i, f in enumerate(formats):
                if f['vcodec'] != 'none' and f['acodec'] != 'none':  # Show only video+audio formats
                    format_list.append(f"{i+1}: {f['format_id']} - {f['format_note']} - {f['ext']}")
            
            # Let the user select a quality
            choice = st.selectbox("Select the video quality", format_list)
            selected_format_index = int(choice.split(':')[0]) - 1
            selected_format = formats[selected_format_index]['format_id']
            
            # Update ydl_opts for downloading the selected format
            ydl_opts['format'] = selected_format
            
            # Download the video
            st.write(f"\nDownloading '{info_dict['title']}' in selected format...")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_url])
            st.success(f"Download completed! Video saved to {download_path}")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        progress_bar.progress(0)
        status_text.text("")

# Streamlit app
def main():
    st.title("YouTube Video Downloader")
    
    # Get the YouTube link from the user
    youtube_url = st.text_input("Enter the YouTube video URL:")
    
    # Specify or get download directory
    default_path = os.path.join(os.getcwd(), 'downloads')
    download_path = st.text_input("Enter the directory where you want to save the video:", value=default_path)
    
    # Create the directory if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    if youtube_url:
        get_youtube_video(youtube_url, download_path)

if __name__ == "__main__":
    main()
