# m1_optimizer.py - Дополнительные оптимизации для MacBook Air M1

import os
import psutil
import time
from tqdm import tqdm

def monitor_temperature():
    """Мониторинг температуры (упрощенный)"""
    try:
        # Для macOS можно использовать iStats или аналоги
        temp = os.popen('pmset -g thermal | grep "CPU_Speed_Limit"').read()
        if "100" not in temp:
            print("🌡️  Внимание: MacBook перегревается, снижаем производительность")
            return True
    except:
        pass
    return False

def reduce_cpu_load():
    """Снижение нагрузки на CPU"""
    print("🔽 Снижаем нагрузку на процессор...")
    
    # Ограничиваем фоновые процессы
    os.system('sudo powermetrics --samplers cpu_power -n 1 -i 1000 > /dev/null 2>&1 &')
    
    # Принудительное охлаждение
    os.system('sudo killall -STOP cfprefsd > /dev/null 2>&1')
    os.system('sudo killall -STOP sharingd > /dev/null 2>&1')

def restore_cpu_load():
    """Восстанавливаем нормальную работу"""
    print("🔼 Восстанавливаем нормальную нагрузку...")
    os.system('sudo killall -CONT cfprefsd > /dev/null 2>&1')
    os.system('sudo killall -CONT sharingd > /dev/null 2>&1')

def smart_throttle(duration):
    """Умное регулирование скорости"""
    chunk_size = 10  # секунд обработки
    pause_duration = 2  # секунд паузы
    
    for i in tqdm(range(0, int(duration), chunk_size), desc="Обработка с паузами"):
        # Обрабатываем chunk
        time.sleep(chunk_size)
        
        # Пауза для охлаждения
        if monitor_temperature():
            print("❄️  Пауза для охлаждения...")
            time.sleep(pause_duration * 2)  # Удлиненная пауза при перегреве
        else:
            time.sleep(pause_duration)