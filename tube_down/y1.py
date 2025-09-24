# source tube_env/bin/activate

import yt_dlp
import os
import ssl
import certifi
from fake_useragent import UserAgent
UserAgent().chrome

# ФИКСИМ SSL ПРОБЛЕМУ НА MACOS
ssl._create_default_https_context = ssl._create_unverified_context
os.environ['SSL_CERT_FILE'] = certifi.where()

def download_youtube_video(url, output_path="/Volumes/D/архивы из загрузки"):
    """
    Скачивает видео с YouTube по ссылке с помощью yt-dlp.
    """
    try:
        # Проверяем и создаем папку для загрузок
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"Создана папка: {output_path}")
        
        fake_ua = {'User-Agent': UserAgent().chrome, 'Referer': 'https://www.ya.ru/'} #выдаем себя за браузер

        # Настройки для обхода проблем с SSL сертами: fuck off google
        ydl_opts = {
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'verbose': False,
            'noplaylist': True,
            'quiet': False,
            'no_warnings': True,  # Игнорируем предупреждения
            'no_check_certificate': True,  # ОБХОДИМ ПРОВЕРКУ СЕРТИФИКАТОВ
            # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'user-agent': fake_ua,
            'extractor_args': {
                'youtube': {
                    'skip': ['dash', 'hls'],
                }
            }
        }

        print("🔄 Подключаемся к YouTube...")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            #  инфо о видео
            info = ydl.extract_info(url, download=False)
            
            print(f"🎬 Название: {info['title']}")
            print(f"👤 Автор: {info['uploader']}")
            print(f"⏱️ Длительность: {info['duration']} сек.")
            print("-" * 50)

            print("⏬ Начинаем загрузку...")
            ydl.download([url])
            
        print(f"✅ Видео успешно скачано!")

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

if __name__ == "__main__":
    video_url = input("Введите ссылку на YouTube видео: ").strip()
    download_youtube_video(video_url)