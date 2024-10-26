from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pydub import AudioSegment
import yt_dlp
import os

def index(request):
    return render(request, 'index.html')

def download_audio(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        if url:
            try:
                # Configure yt-dlp to get audio only
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(title)s.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'nocheckcertificate': True,
                    'quiet': False,  
                    'headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                    },
                }

                # Use a context manager to handle yt-dlp
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(url, download=True)
                    video_title = info_dict.get('title', None)
                    mp3_filename = f"{video_title}.mp3"

                # Serve the MP3 file for download
                mp3_path = os.path.join(settings.BASE_DIR, mp3_filename)
                with open(mp3_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='audio/mpeg')
                    response['Content-Disposition'] = f'attachment; filename="{mp3_filename}"'
                    return response

            except Exception as e:
                print(f"Error: {e}")
                return HttpResponse(f"An error occurred during processing: {e}", status=500)

        return HttpResponse("No URL provided.", status=400)

    return HttpResponse('Invalid request.', status=400)
