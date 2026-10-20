# Stem Splitter

A simple desktop application for separating music tracks using [Demucs](https://github.com/facebookresearch/demucs) and Python.

## About the Project

Stem Splitter was created to solve a practical, everyday problem: creating backing tracks from existing songs.

The idea was to build a simple application that allows users to select an audio file and separate it into individual stems, making it easier to prepare backing tracks for practice.

This project is also part of my learning journey with Python. While developing it, I had the opportunity to explore mainly GUI development with Tkinter and handle audio files.

The main goal was not to create a fully featured audio production tool, but to build something useful while learning through practice.

## Features

- **Audio file selection:** choose a music file through a graphical file dialog.
- **Stem separation:** use Demucs to separate a song into individual audio stems.
- **Progress indicator:** display an animated progress bar while the separation process is running. (Doesn't represent the actual percentage of completion, is only a animation)
- **Status updates:** inform the user when processing starts, finishes, or encounters an error.
- **Simple graphical interface:** interact with the application without manually running Demucs commands.

## How It Works

1. Launch the application.
2. Select an audio file.
3. Click **Split tracks**.
4. Wait while Demucs processes the song.
5. Find the resulting stems in the output directory.

By default, Demucs saves the separated tracks inside a `separated` directory, organized by model and song name.

The standard `htdemucs` model separates audio into **4 stems**:

- Vocals
- Drums
- Bass
- Other

## Requirements

- Python 3.11
- Demucs and its required dependencies
- An audio file supported by Demucs

```bash
python -m pip install --upgrade pip
python -m pip install demucs
```

## Usage

Run the application from the project directory:

```bash
python main.py
```