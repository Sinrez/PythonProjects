import matplotlib.pyplot as plt
import numpy as np

def plot_graph1() -> None:
    x = np.linspace(-10, 10, 1000)

    # Функция 1: y(x) = x^2 + 2x + 1
    plt.plot(x, x**2 + 2*x + 1, color='green', alpha=0.45, label='y(x) = x^2 + 2x + 1')
    #белый не видно

    # Функция 2: y(x) = -x^2 - 0.5x
    plt.plot(x, -x**2 - 0.5*x, color=(0.5, 0.5, 0.5), alpha=0.7, label='y(x) = -x^2 - 0.5x')

    # Функция 3: y(x) = e^x + 2x
    plt.plot(x, np.exp(x) + 2*x, color='#FF5933', alpha=0.95, label='y(x) = e^x + 2x')

    plt.scatter(0, 1, color='black', marker='o')  # Пересечение координат

    plt.xlim(-10, 10)
    plt.ylim(-10, 50)

    plt.legend()
    plt.grid()
    plt.savefig('functions_plot.png')
    plt.show()


def linear_eq(x):
    return [x**2 + 2*x + 1,      # Функция 1
            -x**2 - 0.5*x]        # Функция 2

def exponential_eq(x):
    return [np.exp(x) + 2*x,     # Функция 3
            np.exp(-2*x)]         # Функция 4

def trigonometric_eq(x):
    return [np.sin(x),            # Функция 5
            np.cos(3*x)]           # Функция 6

def logarithmic_eq(x):
    return [np.log2(x),           # Функция 7
            np.log(np.pi*x)]      # Функция 8


def plot_graph2() -> None:
    # Значения x для построения графиков
    x_values = np.linspace(0.1, 10, 400)
    
    # Создание графика
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    # Вывод всех функций на одном графике
    axs[0, 0].set_title('All Functions')
    for func in [linear_eq, exponential_eq, trigonometric_eq, logarithmic_eq]:
        for y in func(x_values):
            axs[0, 0].plot(x_values, y)

    # Линейные уравнения
    axs[0, 1].set_title('Linear Equations')
    for y in linear_eq(x_values):
        axs[0, 1].plot(x_values, y)

    # Экспоненциальные уравнения
    axs[0, 2].set_title('Exponential Equations')
    for y in exponential_eq(x_values):
        axs[0, 2].plot(x_values, y)

    # Тригонометрические уравнения
    axs[1, 0].set_title('Trigonometric Equations')
    for y in trigonometric_eq(x_values):
        axs[1, 0].plot(x_values, y)
    
    # Логарифмические уравнения
    axs[1, 1].set_title('Logarithmic Equations')
    for y in logarithmic_eq(x_values):
        axs[1, 1].plot(x_values, y)

    # Пустой график, чтобы сделать место для пятого графика
    axs[1, 2].axis('off')

    plt.tight_layout()
    plt.show()

def plot_word_lengths(sentence):
    # Разделение предложения на слова
    words = sentence.strip('.,"-:;?!').split()

    # Извлечение длин слов
    word_lengths = [len(word.strip('.,"-:;?!')) for word in words]

    # Создание графика
    plt.bar(range(len(words)), word_lengths, align='center')
    plt.xticks(range(len(words)), words, rotation=45, ha='right')
    plt.xlabel('Слова')
    plt.ylabel('Длина слова')
    plt.show()

def plot_sentence_lengths(sentences):
    # Создаем список для хранения длин слов в предложениях
    word_lengths = []
    # Создаем списки для самых длинных и самых коротких слов с их принадлежностью к предложению
    longest_words = []
    shortest_words = []

    # Проходимся по каждому предложению
    for i, sentence in enumerate(sentences):
        # Разбиваем предложение на слова
        words = sentence.strip('.,"-:;?!').split()
        # Добавляем длины слов в список
        word_lengths.extend([len(word) for word in words])
        # Находим самые длинные и самые короткие слова в предложении
        longest_word = max(words, key=len)
        shortest_word = min(words, key=len)
        # Добавляем их в соответствующие списки с указанием номера предложения
        longest_words.append((longest_word, i+1))
        shortest_words.append((shortest_word, i+1))

    # Строим график длин слов
    plt.figure(figsize=(10, 5))
    plt.hist(word_lengths, bins=range(1, max(word_lengths) + 2), alpha=0.7)
    plt.title('Распределение длин слов в предложениях')
    plt.xlabel('Длина слова')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()

    # Выводим самые длинные слова с указанием номера предложения
    print("Самые длинные слова в предложениях:")
    for word, sentence_num in longest_words:
        print(f"Предложение {sentence_num}: {word}")

    # Выводим самые короткие слова с указанием номера предложения
    print("\nСамые короткие слова в предложениях:")
    for word, sentence_num in shortest_words:
        print(f"Предложение {sentence_num}: {word}")

if __name__ == '__main__':
    #Для наглядности часть вызовов функций закомментирована
    # plot_graph1()
    #plot_graph2()
    sentence = "Пример предложения с разной длиной слов, для построения графика!"
    # plot_word_lengths(sentence) 
    sentences = [
    "Это предложение содержит несколько слов.",
    "Это другое предложение.",
    "И это еще одно.",
    "И, наконец, последнее предложение."]

    plot_sentence_lengths(sentences)
