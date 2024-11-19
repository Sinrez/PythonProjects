import cv2
# source open_env/bin/activate

# Шаг 1: Загрузка изображения
def load_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Ошибка: Не удалось загрузить изображение по пути {image_path}")
        return None
    return img

# Шаг 2: Использование предварительно обученного классификатора
def load_classifier(classifier_type):
    if classifier_type == "face":
        # Загрузим каскад для обнаружения лиц
        cascade_src = "cascades/haarcascade_frontalface_alt.xml"
        classifier = cv2.CascadeClassifier(cascade_src)
    elif classifier_type == "eye":
        # Загрузим каскад для обнаружения глаз
        cascade_src = "cascades/haarcascade_eye.xml"
        classifier = cv2.CascadeClassifier(cascade_src)
    elif classifier_type == "car":
        # Загрузим каскад для обнаружения автомобилей
        cascade_src = "cascades/cars.xml"      
        classifier = cv2.CascadeClassifier(cascade_src)
    else:
        print("Ошибка: Неизвестный классификатор.")
        return None
    if classifier.empty():
        print("Ошибка: Не удалось загрузить классификатор.")
        return None
    return classifier

# Шаг 3: Обнаружение лиц
def detect_faces(img, classifier):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
    return faces

# Шаг 4: Обнаружение глаз
def detect_eyes(img, classifier):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))
    return eyes

# Шаг 5: Обнаружение автомобилей
def detect_cars(img, classifier):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(40, 40))
    return cars

# Шаг 6: Отображение результата
def show_result(img, objects, object_type):
    for (x, y, w, h) in objects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow(f"Обнаруженные {object_type}", img)
    
    # Ожидаем нажатие клавиши для закрытия окна
    cv2.waitKey(0)
    # Закрываем все окна после нажатия клавиши
    cv2.destroyAllWindows()


def menu():
    while True:
        print("\nМеню:")
        print("1. Обнаружение лиц")
        print("2. Обнаружение глаз")
        print("3. Обнаружение автомобилей")
        print("4. Выход")
        
        choice = input("Выберите действие (1/2/3/4): ")

        if choice == '1':
            classifier = load_classifier("face")
            image_path = input("Введите путь к изображению: ")
            img = load_image(image_path)
            if img is not None:
                faces = detect_faces(img, classifier)
                show_result(img, faces, "лиц")
        elif choice == '2':
            classifier = load_classifier("eye")
            image_path = input("Введите путь к изображению: ")
            img = load_image(image_path)
            if img is not None:
                eyes = detect_eyes(img, classifier)
                show_result(img, eyes, "глаз")
        elif choice == '3':
            classifier = load_classifier("car")
            image_path = input("Введите путь к изображению: ")
            img = load_image(image_path)
            if img is not None:
                cars = detect_cars(img, classifier)
                show_result(img, cars, "автомобилей")
        elif choice == '4':
            print("Завершаем программу.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()