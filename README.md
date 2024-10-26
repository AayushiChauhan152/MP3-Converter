# StreamToMP3 - YouTube to MP3 Converter

## Overview
StreamToMP3 is a simple web application that allows users to convert their favorite YouTube videos into MP3 (audio) or MP4 (video) files and download them for free. The application is built using Django and leverages the **yt-dlp** library for downloading and converting videos.

## Features
- Convert YouTube videos to MP3 or MP4 format.
- Easy-to-use interface with a simple form for inputting video URLs.
- Downloadable audio files with a maximum length of 90 minutes.
- No installation required—works directly from the web.

## Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS (Tailwind CSS)
- **Video Downloading**: yt-dlp
- **Audio Conversion**: FFmpeg

## Installation

### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Clone the Repository
git clone https://github.com/YourUsername/MP3-Converter.git

### Install the required packages:
pip install -r requirements.txt

### Run the Django development server:
python manage.py runserver
