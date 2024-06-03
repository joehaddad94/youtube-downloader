from pytube import YouTube
from pydub import AudioSegment
import concurrent.futures
import os

def download_youtube_video_as_mp3(youtube_url, output_path):
    try:
        
        yt = YouTube(youtube_url)
        video_stream = yt.streams.filter(only_audio=True).first()
        downloaded_file = video_stream.download(output_path=output_path)

        base, ext = os.path.splitext(downloaded_file)
        mp3_file = base + '.mp3'
        AudioSegment.from_file(downloaded_file).export(mp3_file, format="mp3")

        os.remove(downloaded_file)

        print(f"Downloaded and converted: {mp3_file}")
        return mp3_file
    except Exception as e:
        print(f"Error downloading {youtube_url}: {e}")
        return None

def download_multiple_videos(youtube_urls, output_path):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_youtube_video_as_mp3, url, output_path) for url in youtube_urls]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return results

youtube_urls = [
    'https://www.youtube.com/watch?v=0OHc-zIp0ek',
    'https://www.youtube.com/watch?v=xzs7sJrBpOE',
    'https://www.youtube.com/watch?v=7hzTBNa6QeU',
    'https://www.youtube.com/watch?v=h_ZNVcgE0UQ',
    'https://www.youtube.com/watch?v=8LgWv5dVOxA',
    'https://www.youtube.com/watch?v=11JNLwQTLnc',
    'https://www.youtube.com/watch?v=c8uqLdZTBn0',
    'https://www.youtube.com/watch?v=wAF0eyjuQiw',
    'https://www.youtube.com/watch?v=pdyEFlcnPQA',
    'https://www.youtube.com/watch?v=QWP1jSsxzQE',
    'https://www.youtube.com/watch?v=VN8g8q3awtA'
]

output_path = r'C:\Users\Joe\Desktop\youtube downloader'
downloaded_files = download_multiple_videos(youtube_urls, output_path)
print("Downloaded files:", downloaded_files)