import whisper
import os
from tqdm import tqdm
import subprocess
from pathlib import Path

def transcribe_local_video(video_path, model_size="base", language="ru"):
    """
    Транскрибация локального видеофайла
    
    Args:
        video_path (str): путь к видеофайлу
        model_size (str): размер модели whisper ("tiny", "base", "small", "medium", "large")
        language (str): язык транскрибации (ru, en, ...)
    
    Returns:
        str: распознанный текст
    """
    
    print("🎵 Транскрибация локального видео")
    print("=" * 50)
    
    # Проверяем существование файла
    if not os.path.exists(video_path):
        print(f"❌ Файл не найден: {video_path}")
        return None
    
    # Получаем информацию о файле
    file_size = os.path.getsize(video_path) / (1024 * 1024)  # в МБ
    print(f"📁 Файл: {os.path.basename(video_path)}")
    print(f"📏 Размер: {file_size:.2f} MB")
    
    # Загружаем модель
    print(f"🔄 Загружаем модель '{model_size}'...")
    model = whisper.load_model(model_size, device="cpu")
    print("✅ Модель загружена")
    
    # Извлекаем аудио из видео (если нужно)
    audio_path = extract_audio_from_video(video_path)
    
    if not audio_path:
        print("❌ Не удалось извлечь аудио из видео")
        return None
    
    # Транскрибируем
    print("🎤 Транскрибируем аудио...")
    try:
        with tqdm(total=100, desc="Обработка") as pbar:
            result = model.transcribe(audio_path, language=language, verbose=False)
            pbar.update(100)
        
        # Удаляем временный аудиофайл
        if audio_path != video_path:
            os.remove(audio_path)
            print("🗑️ Временный аудиофайл удален")
        
        return result['text']
        
    except Exception as e:
        print(f"❌ Ошибка транскрибации: {e}")
        if audio_path != video_path and os.path.exists(audio_path):
            os.remove(audio_path)
        return None


def extract_audio_from_video(video_path):
    """
    Извлекает аудио из видеофайла с помощью ffmpeg
    
    Args:
        video_path (str): путь к видеофайлу
    
    Returns:
        str: путь к аудиофайлу (mp3)
    """
    
    print("🔊 Извлекаем аудио из видео...")
    
    # Путь для сохранения аудио
    audio_path = os.path.splitext(video_path)[0] + "_audio.mp3"
    
    # Проверяем, не является ли файл уже аудио
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv', '.wmv', '.m4v']
    file_ext = os.path.splitext(video_path)[1].lower()
    
    if file_ext not in video_extensions:
        # Если это уже аудиофайл, используем его напрямую
        print("✅ Файл уже является аудио, пропускаем извлечение")
        return video_path
    
    # Извлекаем аудио с помощью ffmpeg
    try:
        # Проверяем наличие ffmpeg
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ ffmpeg не установлен. Установите ffmpeg:")
            print("   macOS: brew install ffmpeg")
            print("   Ubuntu: sudo apt install ffmpeg")
            print("   Windows: скачайте с ffmpeg.org")
            return None
        
        # Команда для извлечения аудио
        cmd = [
            'ffmpeg', '-i', video_path,
            '-vn',  # без видео
            '-acodec', 'libmp3lame',  # кодек mp3
            '-ab', '192k',  # битрейт
            '-ar', '44100',  # частота дискретизации
            '-y',  # перезаписывать существующий файл
            audio_path
        ]
        
        # Выполняем с подавлением вывода
        subprocess.run(cmd, capture_output=True, text=True)
        
        if os.path.exists(audio_path) and os.path.getsize(audio_path) > 0:
            print(f"✅ Аудио извлечено: {audio_path}")
            return audio_path
        else:
            print("❌ Не удалось создать аудиофайл")
            return None
            
    except Exception as e:
        print(f"❌ Ошибка при извлечении аудио: {e}")
        return None


def transcribe_local_video_simple(video_path, model_size="base", language="ru"):
    """
    Упрощенная версия - без извлечения аудио (whisper сам умеет работать с видео)
    Требуется ffmpeg в системе
    """
    
    print("🎵 Транскрибация локального видео (упрощенная)")
    print("=" * 50)
    
    if not os.path.exists(video_path):
        print(f"❌ Файл не найден: {video_path}")
        return None
    
    print(f"📁 Файл: {os.path.basename(video_path)}")
    
    # Загружаем модель
    print(f"🔄 Загружаем модель '{model_size}'...")
    model = whisper.load_model(model_size, device="cpu")
    print("✅ Модель загружена")
    
    # Транскрибируем напрямую (whisper сам извлечет аудио через ffmpeg)
    print("🎤 Транскрибируем видео...")
    try:
        with tqdm(total=100, desc="Обработка") as pbar:
            result = model.transcribe(video_path, language=language, verbose=False)
            pbar.update(100)
        
        return result['text']
        
    except Exception as e:
        print(f"❌ Ошибка транскрибации: {e}")
        print("💡 Убедитесь, что ffmpeg установлен в системе")
        return None


def batch_transcribe(folder_path, model_size="base", language="ru"):
    """
    Транскрибация всех видео в папке
    
    Args:
        folder_path (str): путь к папке с видео
        model_size (str): размер модели
        language (str): язык
    
    Returns:
        dict: словарь {имя_файла: текст}
    """
    
    print(f"📁 Обработка папки: {folder_path}")
    print("=" * 50)
    
    # Поддерживаемые форматы
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv', '.wmv', '.m4v', '.mp3', '.wav', '.m4a'}
    
    # Находим все видео/аудио файлы
    video_files = []
    for ext in video_extensions:
        video_files.extend(Path(folder_path).glob(f"*{ext}"))
        video_files.extend(Path(folder_path).glob(f"*{ext.upper()}"))
    
    if not video_files:
        print("❌ Видео/аудио файлы не найдены")
        return {}
    
    print(f"🎬 Найдено файлов: {len(video_files)}")
    
    results = {}
    
    for i, video_file in enumerate(video_files, 1):
        print(f"\n[{i}/{len(video_files)}] Обработка: {video_file.name}")
        
        text = transcribe_local_video(str(video_file), model_size, language)
        
        if text:
            results[video_file.stem] = text
            
            # Сохраняем каждый результат отдельно
            output_file = video_file.stem + "_transcript.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"💾 Сохранено в: {output_file}")
    
    return results


# ============================================
# Примеры использования
# ============================================

if __name__ == "__main__":
    
    # ===== Пример 1: Один файл (с извлечением аудио) =====
    video_path = "/Volumes/D/архивы из загрузки/YTDown.com_YouTube_Media_bPZVItwmZR4_002_720p.mp4"  # Укажите путь к вашему видео
    
    # Если у вас есть реальный файл, раскомментируйте:
    # text = transcribe_local_video(video_path, model_size="base", language="ru")
    
    # ===== Пример 2: Упрощенная версия =====
    # text = transcribe_local_video_simple(video_path, model_size="tiny", language="ru")
    
    # ===== Пример 3: Обработка всей папки =====
    # results = batch_transcribe("/path/to/folder/with/videos", model_size="base", language="ru")
    
    # ===== Пример 4: Использование разных моделей =====
    """
    # tiny - самая быстрая, но менее точная
    text_tiny = transcribe_local_video("video.mp4", model_size="tiny", language="ru")
    
    # base - баланс скорости и качества
    text_base = transcribe_local_video("video.mp4", model_size="base", language="ru")
    
    # large - самая точная, но медленная
    text_large = transcribe_local_video("video.mp4", model_size="large", language="ru")
    """
    
    # ===== Демонстрация работы (если файл существует) =====
    if os.path.exists(video_path):
        text = transcribe_local_video(video_path)
        
        if text:
            print("\n✅ Транскрибация завершена!")
            print(f"📝 Получено символов: {len(text)}")
            
            # Сохраняем результат
            output_file = "transcription_result.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"💾 Текст сохранен в '{output_file}'")
            
            # Показываем превью
            print("\n📄 Превью текста:")
            print("=" * 50)
            print(text[:500] + "..." if len(text) > 500 else text)
    else:
        print("⚠️ Укажите путь к видеофайлу в переменной video_path")
        print("\nПример использования:")
        print('  video_path = "my_video.mp4"')
        print('  text = transcribe_local_video(video_path)')