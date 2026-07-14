import os
import sys
import subprocess
import shutil
from pathlib import Path
from yt_dlp import YoutubeDL

class YouTubeDownloader:
    def __init__(self, output_path="./youtube_downloads"):
        self.output_path = output_path
        self._ensure_output_dir()
        self._check_ffmpeg()
    
    def _ensure_output_dir(self):
        """Tạo thư mục output"""
        Path(self.output_path).mkdir(parents=True, exist_ok=True)
    
    def _check_ffmpeg(self):
        """Kiểm tra FFmpeg đã cài chưa"""
        if shutil.which('ffmpeg') is None:
            print("⚠️  FFmpeg chưa được cài đặt!")
            print("📥 Vui lòng cài FFmpeg từ: https://www.gyan.dev/ffmpeg/builds/")
            print("Sau đó chạy lại chương trình")
            sys.exit(1)
        else:
            print("✅ FFmpeg đã sẵn sàng")
    
    def download_video_with_audio(self, url):
        """Tải video + âm thanh"""
        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': os.path.join(self.output_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'quiet': False,
            'progress_hooks': [self._progress_hook],
        }
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                print(f"\n📥 Đang tải: {url}")
                print("-" * 60)
                info = ydl.extract_info(url, download=True)
                print("-" * 60)
                print(f"✅ Tải thành công: {info['title']}")
                print(f"📂 Lưu tại: {os.path.abspath(self.output_path)}")
                return True
        except Exception as e:
            print(f"❌ Lỗi: {str(e)}")
            return False
    
    def download_playlist(self, url):
        """Tải playlist"""
        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': os.path.join(self.output_path, '%(playlist)s/%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'progress_hooks': [self._progress_hook],
        }
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                print(f"\n📥 Đang tải playlist: {url}")
                print("-" * 60)
                ydl.download([url])
                print("-" * 60)
                print(f"✅ Tải playlist thành công!")
                return True
        except Exception as e:
            print(f"❌ Lỗi: {str(e)}")
            return False
    
    @staticmethod
    def _progress_hook(d):
        """Hiển thị tiến trình tải"""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"   {percent} | Tốc độ: {speed} | ETA: {eta}", end='\r')
        elif d['status'] == 'finished':
            print("\n   ✓ Tải video xong, đang xử lý...")

def main():
    print("=" * 60)
    print("  🎬 YouTube Downloader (Video + Âm thanh)")
    print("=" * 60)
    
    downloader = YouTubeDownloader()
    
    while True:
        print("\n📋 Chọn chức năng:")
        print("1. Tải 1 video")
        print("2. Tải playlist")
        print("3. Thoát")
        
        choice = input("\nNhập lựa chọn (1-3): ").strip()
        
        if choice == "1":
            url = input("Nhập link video YouTube: ").strip()
            if url:
                downloader.download_video_with_audio(url)
        elif choice == "2":
            url = input("Nhập link playlist YouTube: ").strip()
            if url:
                downloader.download_playlist(url)
        elif choice == "3":
            print("Tạm biệt! 👋")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")
        
        input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main()
