import os
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

def download_video(url, save_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s')
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        save_path.set(folder_selected)

def start_download():
    url = url_entry.get()
    save_dir = save_path.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return
    if not save_dir:
        messagebox.showwarning("Input Error", "Please choose a save directory.")
        return
    download_video(url, save_dir)

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")

# Create and place the URL entry
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the save path entry
tk.Label(root, text="Save to:").grid(row=1, column=0, padx=10, pady=10)
save_path = tk.StringVar()
save_entry = tk.Entry(root, width=50, textvariable=save_path)
save_entry.grid(row=1, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse...", command=browse_folder)
browse_button.grid(row=1, column=2, padx=10, pady=10)

# Create and place the download button
download_button = tk.Button(root, text="Download", command=start_download)
download_button.grid(row=2, column=1, pady=20)

# Run the application
root.mainloop()
