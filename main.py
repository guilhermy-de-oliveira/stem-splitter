# DEPENDÊNCIES
#
# Python 3.11, Demucs, Numpy, tkinter, pathlib, subprocess, threading, sys

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import threading
import sys
from pathlib import Path

# WINDOW
window = tk.Tk()

window.title("Stem Splitter")
window.geometry("480x360")

# ARCHIVE
selected_archive = None

def choose_archive():
    global selected_archive

    path = filedialog.askopenfilename(
        title="Insert a music",
        filetypes=[
            ("Audio archives", "*.mp3 *.wav *.flac *.ogg"),
            ("All archives", "*.*")
        ]
    )

    if path:
        selected_archive = Path(path)
        archive_name.config(
            text=selected_archive.name
        )

# SPLITTING
def finish_splitting(sucess, message):
    progress.stop()
    split_button.config(state="normal")

    if sucess:
        status.config(text="Splitting finished!")
        messagebox.showinfo(
            "Finished!",
            "The tracks were separated successfully!"
        )
    else:
        status.config(text="Error!")
        messagebox.showerror(
            "Error in splitting",
            message[-1800:] or "Doesn't possible execute the Demucs."
        )

def execute_demucs():
    try:
        result = subprocess.run(
            [
                sys.executable,
                "-m", "demucs",
                str(selected_archive)
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            window.after(
                0, finish_splitting, True, ""
            )
        else:
            error = result.stderr or result.stdout
            window.after(
                0, finish_splitting, False, error
            )

    except Exception as error:
        window.after(
            0, finish_splitting, False, str(error)
        )

def split():
    if not selected_archive:
        messagebox.showwarning(
            "Warning",
            "Insert a music first."
        )
        return

    split_button.config(state="disabled")
    status.config(text="Splitting...")
    progress.start(10)

    thread = threading.Thread(
        target=execute_demucs,
        daemon=True
    )
    thread.start()

# TEXTS
title = ttk.Label(
    window,
    text="Stem Splitter",
    font=("Segoe UI", 20, "bold")
)
title.pack(pady=20)

archive_name = ttk.Label(
    window,
    text="None archive selected"
)
archive_name.pack(pady=15)

status = ttk.Label(window, text="Ready")
status.pack(pady=8)

# BUTTON
archive_button = ttk.Button(
    window,
    text="Choose a archive",
    command=choose_archive
)
archive_button.pack()

split_button = ttk.Button(
    window,
    text="Split tracks",
    command=split
)
split_button.pack(pady=5)

# PROGRESS BAR
progress = ttk.Progressbar(
    window,
    mode="indeterminate",
    length=300
)
progress.pack(pady=10)

# EXECUTION
window.mainloop()