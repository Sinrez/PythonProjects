import os
import json
from datetime import datetime

def save_note(model, note):
    """Сохранение заметки в файл"""
    with open('notes.txt', 'a') as f:
        note_data = {
            'model': model,
            'note': note,

            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        f.write(json.dumps(note_data) + '\n')

def load_notes():
    """Загрузка ранее сохраненных заметок из файла"""
    if os.path.exists('notes.txt'):
        notes = []
        with open('notes.txt', 'r') as f:
            for line in f:
                try:
                    note = json.loads(line.strip())
                    notes.append(note)
                except json.JSONDecodeError:
                    print(f"Ошибка декодирования JSON для строки: {line.strip()}")
        return notes
    return []

def display_notes(notes):
    """Отображение всех заметок"""
    if notes:
        print("nРанее сохраненные заметки:")
        for idx, note in enumerate(notes, start=1):
            print(f"{idx}.Модель БПЛА: {note['model']} Описание: {note['note']} (создано: {note['timestamp']})")
    else:
        print("Нет сохраненных заметок.")

def main():
    print('Программа заметок о БПЛА')
    while True:
        print("\nМеню:")
        print("1. Ввести новую заметку о БПЛА")
        print("2. Просмотреть ранее сохраненные заметки")
        print("3. Выход")

        choice = input("Выберите опцию (1-3): ")

        if choice == '1':
            model = input("Введите модель БПЛА: ").strip()
            note = input("Введите описание БПЛА: ").strip()

            save_note(model, note)
            print("Заметка сохранена.")
        
        elif choice == '2':
            notes = load_notes()
            display_notes(notes)
        
        elif choice == '3':
            print("Рвбота завершена. Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()