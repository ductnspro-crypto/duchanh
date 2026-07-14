# 🎬 YouTube Downloader

Công cụ tải video + âm thanh từ YouTube về máy tính một cách dễ dàng.

## ✨ Tính năng

- ✅ Tải video với chất lượng tốt nhất
- ✅ Bao gồm âm thanh gốc
- ✅ Tải riêng lẻ hoặc toàn bộ playlist
- ✅ Giao diện dòng lệnh thân thiện
- ✅ Hiển thị tiến trình tải

## 📋 Yêu cầu

### Cách 1: Dùng file .exe (Đơn giản nhất - Windows)
- Chỉ cần download file `.exe` từ Releases
- Double-click để chạy
- Không cần cài gì thêm

### Cách 2: Chạy từ source code (Windows/Mac/Linux)

**Yêu cầu:**
- Python 3.7+
- FFmpeg

**Cài đặt Python:**
- Tải từ https://www.python.org/downloads/
- Chọn "Add Python to PATH" khi cài

**Cài đặt FFmpeg:**

**Windows:**
```bash
choco install ffmpeg
```
Hoặc tải từ: https://www.gyan.dev/ffmpeg/builds/

**Mac:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

**Cài đặt thư viện Python:**
```bash
pip install -r requirements.txt
```

## 🚀 Sử dụng

### Cách 1: File .exe
```bash
youtube_downloader.exe
```

### Cách 2: Python
```bash
python youtube_downloader.py
```

### Hướng dẫn:
1. Chọn chức năng (1 = tải video, 2 = tải playlist)
2. Dán link YouTube
3. Chờ tải xong

**Video sẽ được lưu vào thư mục: `youtube_downloads/`**

## 📝 Ví dụ

```
🎬 YouTube Downloader (Video + Âm thanh)

📋 Chọn chức năng:
1. Tải 1 video
2. Tải playlist
3. Thoát

Nhập lựa chọn (1-3): 1
Nhập link video YouTube: https://www.youtube.com/watch?v=...

📥 Đang tải: ...
60% | Tốc độ: 5.5MB/s | ETA: 00:30
✅ Tải thành công: Video Title
📂 Lưu tại: C:\path\youtube_downloads
```

## ⚙️ Build .exe từ source

Nếu bạn muốn build file `.exe` riêng:

```bash
pip install pyinstaller
pyinstaller --onefile --console youtube_downloader.py
```

File `.exe` sẽ nằm ở thư mục `dist/`

## 🐛 Khắc phục sự cố

**Lỗi: FFmpeg not found**
- Cài đặt FFmpeg theo hướng dẫn ở trên
- Khởi động lại Command Prompt/Terminal

**Lỗi: Video không tải được**
- Cập nhật yt-dlp: `pip install --upgrade yt-dlp`
- Kiểm tra link YouTube có hợp lệ không
- Một số video có thể bị chặn bằng địa phương

**Lỗi: Module not found**
- Cài đặt lại: `pip install -r requirements.txt`

## 📄 Giấy phép

MIT License - Tự do sử dụng, sửa đổi và phân phối

## 💡 Lưu ý

- Video được lưu dưới định dạng MP4
- Chất lượng tùy thuộc vào video source
- Một số video có thể không cho phép tải
- Tuân thủ điều khoản dịch vụ của YouTube

## 🤝 Đóng góp

Nếu bạn có ý kiến hoặc tìm thấy bug, vui lòng tạo issue hoặc pull request!

---

**Made with ❤️ by ductnspro-crypto**
