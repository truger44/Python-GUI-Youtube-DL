
import customtkinter as ctk
import json
import os
from yt_dlp import YoutubeDL
from threading import Thread

class YouTubeDownloader:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("YouTube Video Downloader")
        self.window.geometry("600x400")
        
        # Load settings
        self.settings_file = "settings.json"
        self.download_path = self.load_settings().get("download_path", os.path.expanduser("~/Downloads"))
        
        self.setup_gui()
    
    def setup_gui(self):
        # URL input
        url_frame = ctk.CTkFrame(self.window)
        url_frame.pack(pady=20, padx=20, fill="x")
        
        url_label = ctk.CTkLabel(url_frame, text="Video URL:")
        url_label.pack(side="left", padx=5)
        
        self.url_entry = ctk.CTkEntry(url_frame, width=400)
        self.url_entry.pack(side="left", padx=5, fill="x", expand=True)
        
        paste_btn = ctk.CTkButton(
            url_frame,
            text="📋",
            width=30,
            command=lambda: self.url_entry.insert(0, self.window.clipboard_get())
        )
        paste_btn.pack(side="left", padx=5)
        
        # Download button
        # MP3 Checkbox
        self.mp3_var = ctk.BooleanVar(value=False)
        mp3_checkbox = ctk.CTkCheckBox(
            self.window,
            text="Convert to MP3",
            variable=self.mp3_var
        )
        mp3_checkbox.pack(pady=5)

        button_frame = ctk.CTkFrame(self.window)
        button_frame.pack(pady=10)
        
        self.download_btn = ctk.CTkButton(
            button_frame,
            text="Download",
            command=self.start_download
        )
        self.download_btn.pack(side="left", padx=5)
        
        open_folder_btn = ctk.CTkButton(
            button_frame,
            text="📂 Open Folder",
            command=lambda: os.startfile(self.download_path) if os.name == 'nt' else os.system(f'xdg-open "{self.download_path}"')
        )
        open_folder_btn.pack(side="left", padx=5)
        
        # Status label
        self.status_label = ctk.CTkLabel(self.window, text="Ready")
        self.status_label.pack(pady=10)
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.window, width=400)
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)
        
        # Settings button
        settings_btn = ctk.CTkButton(
            self.window,
            text="Settings",
            command=self.show_settings
        )
        settings_btn.pack(pady=10)
        
        # Current path label
        self.path_label = ctk.CTkLabel(
            self.window,
            text=f"Download path: {self.download_path}"
        )
        self.path_label.pack(pady=10)

    def load_settings(self):
        try:
            with open(self.settings_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_settings(self):
        with open(self.settings_file, 'w') as f:
            json.dump({"download_path": self.download_path}, f)

    def show_settings(self):
        settings_window = ctk.CTkToplevel(self.window)
        settings_window.title("Settings")
        settings_window.geometry("500x200")
        
        # Path entry
        path_entry = ctk.CTkEntry(settings_window, width=300)
        path_entry.insert(0, self.download_path)
        path_entry.pack(pady=20, padx=20)

        # Credits
        credits_text = "This program utilizes:\nFFmpeg: https://github.com/FFmpeg/FFmpeg\nyoutube-DL: https://github.com/ytdl-org/youtube-dl"
        credits_label = ctk.CTkLabel(settings_window, text=credits_text, justify="left")
        credits_label.pack(pady=10)
        
        def save():
            self.download_path = path_entry.get()
            self.save_settings()
            self.path_label.configure(text=f"Download path: {self.download_path}")
            settings_window.destroy()
        
        save_btn = ctk.CTkButton(settings_window, text="Save", command=save)
        save_btn.pack(pady=10)

    def download_progress(self, d):
        if d['status'] == 'downloading':
            try:
                progress = float(d['_percent_str'].strip('%')) / 100
                self.progress_bar.set(progress)
                self.status_label.configure(text=f"Downloading: {d['_percent_str']}")
            except:
                pass
        elif d['status'] == 'finished':
            self.status_label.configure(text="Download completed!")
            self.progress_bar.set(1)
            self.download_btn.configure(state="normal")

    def start_download(self):
        url = self.url_entry.get().strip()
        if not url:
            self.status_label.configure(text="Please enter a valid URL")
            return
        
        self.download_btn.configure(state="disabled")
        self.progress_bar.set(0)
        
        def download():
            try:
                ydl_opts = {
                    'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                    'progress_hooks': [self.download_progress],
                    'keepvideo': True,
                    'keep_fragments': True
                }
                
                if self.mp3_var.get():
                    ydl_opts.update({
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    })
                
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
            except Exception as e:
                self.status_label.configure(text=f"Error: {str(e)}")
                self.download_btn.configure(state="normal")
        
        Thread(target=download, daemon=True).start()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.run()
