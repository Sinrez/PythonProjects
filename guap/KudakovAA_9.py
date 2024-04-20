import matplotlib.pyplot as plt

# Население пяти самых населенных стран на каждом континенте
population_data = {
    'Европа': {'Россия': 146745098, 'Германия': 83783942, 'Франция': 65273511, 'Великобритания': 67886011, 'Италия': 60461826},
    'Азия': {'Китай': 1439323776, 'Индия': 1380004385, 'Индонезия': 276361783, 'Пакистан': 225199937, 'Бангладеш': 164689383},
    'Африка': {'Нигерия': 206139587, 'Эфиопия': 114963588, 'Египет': 102334404, 'ДР Конго': 89561403, 'Танзания': 59734218},
    'Северная Америка': {'США': 331002651, 'Мексика': 128932753, 'Канада': 37742154, 'Гаити': 11402528, 'Гондурас': 9904607},
    'Южная Америка': {'Бразилия': 212559417, 'Колумбия': 50882891, 'Аргентина': 45195774, 'Венесуэла': 28435940, 'Перу': 32971854},
    'Австралия и Океания': {'Австралия': 25499884, 'Папуа-Новая Гвинея': 8947024, 'Новая Зеландия': 4822233, 'Фиджи': 896445, 'Тонга': 105695}
}

def plot_continent(continent, countries):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Данные для столбчатой диаграммы
    population_values = [population_data[continent][country] for country in countries]
    countries_colors = ['#FF0000', '#0000FF', '#00FF00', '#FFFF00', '#FF00FF']  # Пример цветов флагов
    axs[0].barh(countries, population_values, color=countries_colors)
    axs[0].set_xlabel('Население')
    axs[0].set_ylabel('Страны')
    axs[0].set_title('Столбчатая диаграмма для ' + continent)

    # Данные для круговой диаграммы
    axs[1].pie(population_values, labels=countries, autopct='%1.1f%%', colors=countries_colors)
    axs[1].set_title('Круговая диаграмма для ' + continent)

    plt.show()

# Задание №1
for continent, countries in population_data.items():
    plot_continent(continent, list(countries.keys()))

# Задание №2
top_countries = {'Европа': 'Россия', 'Азия': 'Китай', 'Африка': 'Нигерия', 'Северная Америка': 'США', 'Южная Америка': 'Бразилия', 'Австралия и Океания': 'Австралия'}
for continent, top_country in top_countries.items():
    plot_continent(continent, [top_country])
