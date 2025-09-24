import sqlite3
from Crypto.Cipher import AES
import keyring
import os
import datetime
import json
import base64

# source cook_env/bin/activate    

def convert_chrome_time(chrome_time):
    """Конвертирует Chrome FILETIME в Unix timestamp"""
    if chrome_time == 0:
        return 0  # Сессионная кука
    
    epoch_diff = 11644473600000000  # Разница между эпохами в микросекундах
    try:
        return (chrome_time - epoch_diff) // 1000000
    except:
        return 0

def get_chrome_cookies():
    cookie_path = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Cookies') # место где лежат куки
    keychain_path = os.path.expanduser('~/Library/Application Support/Google/Chrome/Local State')
    
    if not os.path.exists(cookie_path):
        print("Файл cookies не найден!")
        return []
    
    try:
        temp_cookie = '/tmp/chrome_cookies'
        os.system(f'cp "{cookie_path}" {temp_cookie}')
        
        conn = sqlite3.connect(temp_cookie)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT host_key, name, value, encrypted_value, path, 
                   expires_utc, is_secure, is_httponly 
            FROM cookies""")
        
        cookies = []
        for item in cursor.fetchall():
            expires_utc = convert_chrome_time(item[5])  # Конвертируем время
            
            cookies.append({
                'domain': item[0],
                'name': item[1],
                'value': item[2] if not item[3] else decrypt_chrome_cookie(item[3], keychain_path) or item[2],
                'path': item[4],
                'expires': expires_utc,
                'secure': bool(item[6]),
                'httponly': bool(item[7])
            })
        
        conn.close()
        os.remove(temp_cookie)
        return cookies
    
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        return []

def decrypt_chrome_cookie(encrypted_value, keychain_path):
    try:
        with open(keychain_path, 'r') as f:
            local_state = json.load(f)
        encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])[5:] #чистим лишнее
        key = keyring.get_password('Chrome Safe Storage', 'Chrome')   # Достаём пароль из связки ключей браузера
        if not key:
            return None
        cipher = AES.new(key, AES.MODE_GCM, nonce=encrypted_value[3:15])  # Создаём инструмент для расшифровки
        return cipher.decrypt(encrypted_value[15:])[:-16].decode() #расшифровываем
    except Exception:
        return None

if __name__ == '__main__':
    cookies = get_chrome_cookies()
    for cookie in cookies:
        expires = "Сессионная" if cookie['expires'] == 0 else datetime.datetime.fromtimestamp(cookie['expires']).strftime('%Y-%m-%d %H:%M:%S')
        print(f"""
        Сайт: {cookie['domain']}
        Имя: {cookie['name']}
        Значение: {cookie['value']}
        Действует до: {expires}
        Защищённая: {'Да' if cookie['secure'] else 'Нет'}
        """)