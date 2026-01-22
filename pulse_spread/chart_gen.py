# chart_gen.py
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, date, timedelta
import numpy as np
import os

def create_comparison_chart(data: list, output_path: str = "comparison_chart.png") -> str:
    """Создает компактный график для телеграма с данными ОТ 01.01.2026"""
    if not data:
        print("❌ Нет данных для графика")
        return None
    
    print(f"Получено {len(data)} записей")
    
    # Подготовка данных
    dates = []
    spreads = []
    
    # Определяем начальную дату - 01.01.2026
    start_date = date(2026, 1, 1)
    print(f"📅 Фильтруем данные с {start_date.strftime('%d.%m.%Y')}")
    
    for row in data:
        date_val = row[3]
        current_date = None
        
        # Преобразуем дату в datetime объект
        if isinstance(date_val, str):
            try:
                current_date = datetime.strptime(date_val, '%Y-%m-%d').date()
            except:
                try:
                    current_date = datetime.strptime(date_val, '%Y-%m-%d %H:%M:%S').date()
                except:
                    continue
        elif isinstance(date_val, date):
            current_date = date_val
        elif isinstance(date_val, datetime):
            current_date = date_val.date()
        else:
            try:
                date_str = str(date_val)
                current_date = datetime.strptime(date_str.split()[0], '%Y-%m-%d').date()
            except:
                continue
        
        # Фильтруем: берем только данные С 01.01.2026
        if current_date and current_date >= start_date:
            dates.append(datetime.combine(current_date, datetime.min.time()))
            spreads.append(float(row[2]))
            print(f"  ✓ {current_date.strftime('%d.%m.%Y')}: спред {row[2]:.2f} руб")
    
    if not dates:
        print("❌ Нет данных с 01.01.2026")
        return None
    
    print(f"✅ Обработано {len(dates)} записей с 01.01.2026")
    
    # Сортируем по дате
    sorted_data = sorted(zip(dates, spreads))
    dates = [d for d, _ in sorted_data]
    spreads = [s for _, s in sorted_data]
    
    # Определяем диапазон для оси X - ОБЯЗАТЕЛЬНО С 01.01.2026
    x_min = datetime(2026, 1, 1)  # НАЧАЛО ОСИ X - 01.01.2026
    # x_max = dates[-1] if dates else datetime(2026, 12, 31)
    x_max = datetime(2026, 12, 31)
    # Если у нас мало дат, добавляем фиктивные даты для оси X
    if len(dates) == 1:
        # Если только одна дата, показываем неделю вперед
        x_max = dates[0] + timedelta(days=200)
    
    print(f"📊 Ось X: от {x_min.strftime('%d.%m.%Y')} до {x_max.strftime('%d.%m.%Y')}")
    
    # Если данных больше 30, берем последние 30 точек
    if len(dates) > 30:
        print(f"📉 Берем последние 30 точек из {len(dates)}")
        dates = dates[-30:]
        spreads = spreads[-30:]
    
    print(f"📊 Для графика: {len(dates)} точек")
    
    # Создаем график
    plt.figure(figsize=(14, 8))
    
    # График спреда с улучшенным стилем
    plt.plot(dates, spreads, 'b-', linewidth=3, marker='o', 
             markersize=8, markerfacecolor='white', markeredgewidth=2,
             markeredgecolor='blue', label='Спред (руб)')
    
    # НАСТРОЙКА ОСИ X - НАЧИНАЕМ С 01.01.2026
    ax = plt.gca()
    
    # Устанавливаем пределы оси X
    ax.set_xlim([x_min, x_max])
    
    # Настройки графика
    plt.title(f'Динамика спреда USD/RUB ({x_min.strftime("%d.%m.%Y")} - {x_max.strftime("%d.%m.%Y")})', 
              fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Дата', fontsize=14)
    plt.ylabel('Спред (руб)', fontsize=14)
    
    # Ось Y от 0 до 20 (или максимум + 20%)
    max_spread = max(spreads) if spreads else 0
    y_max = max(5, max_spread * 1.2)  # Минимум 5, максимум +20% от макс.спреда
    y_max = min(y_max, 20)  # Но не более 20
    plt.ylim(0, y_max)
    
    # Добавляем горизонтальную линию среднего значения
    if spreads:
        avg_spread = np.mean(spreads)
        plt.axhline(y=avg_spread, color='red', linestyle='--', linewidth=2, 
                    alpha=0.7, label=f'Средний: {avg_spread:.2f} руб')
    
    # ФОРМАТИРОВАНИЕ ДАТ на оси X - ПОЛНЫЙ ФОРМАТ
    date_format = mdates.DateFormatter('%d.%m.%Y')  # ПОЛНЫЙ ФОРМАТ ДД.ММ.ГГГГ
    ax.xaxis.set_major_formatter(date_format)
    
    # Настраиваем расположение меток дат
    # Рассчитываем разницу в днях
    days_diff = (x_max - x_min).days
    
    # Автоматический расчет интервала для меток
    if days_diff <= 7:  # Неделя
        interval = 1  # Каждый день
        locator = mdates.DayLocator(interval=interval)
    elif days_diff <= 30:  # Месяц
        interval = max(2, days_diff // 10)
        locator = mdates.DayLocator(interval=interval)
    elif days_diff <= 90:  # Квартал
        interval = max(5, days_diff // 10)
        locator = mdates.WeekdayLocator(interval=1)
    else:  # Более 3 месяцев
        interval = max(7, days_diff // 15)
        locator = mdates.WeekdayLocator(interval=2)
    
    ax.xaxis.set_major_locator(locator)
    
    plt.xticks(rotation=45, ha='right', fontsize=11)
    plt.yticks(fontsize=11)
    
    # Добавляем подписи к точкам
    for i, (d, s) in enumerate(zip(dates, spreads)):
        plt.annotate(f'{s:.2f}', 
                     xy=(d, s),
                     xytext=(0, 10), textcoords='offset points',
                     fontsize=9, ha='center', alpha=0.7)
    
    # Сетка
    plt.grid(True, alpha=0.3, linestyle='--', which='both')
    
    # Легенда
    plt.legend(loc='upper left', fontsize=12, framealpha=0.9)
    
    # Добавляем статистику в правый верхний угол
    if spreads:
        stats_text = (f"Мин: {min(spreads):.2f} руб\n"
                     f"Макс: {max(spreads):.2f} руб\n"
                     f"Средн: {avg_spread:.2f} руб")
        
        plt.text(0.98, 0.98, stats_text, transform=ax.transAxes,
                 fontsize=11, verticalalignment='top', horizontalalignment='right',
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # Добавляем текущее значение сбоку
    if spreads:
        last_value = spreads[-1]
        last_date = dates[-1]
        plt.annotate(f'Текущий: {last_value:.2f} руб', 
                     xy=(last_date, last_value),
                     xytext=(15, 0), textcoords='offset points',
                     fontsize=11, fontweight='bold',
                     bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
                     arrowprops=dict(arrowstyle='->', color='blue', alpha=0.7))
    
    # Улучшаем отступы
    plt.tight_layout()
    
    # Сохраняем график с высоким качеством
    plt.savefig(output_path, dpi=120, bbox_inches='tight')
    plt.close()
    
    print(f"✅ График сохранен: {output_path}")
    print(f"📈 Ось X начинается с: {x_min.strftime('%d.%m.%Y')}")
    print(f"📈 Ось X заканчивается: {x_max.strftime('%d.%m.%Y')}")
    
    return output_path

