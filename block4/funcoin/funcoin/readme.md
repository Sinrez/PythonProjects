# Простая модель блокчейна

Проект для изучения блокчейна: 
формирует цепочку блоков ввиде списка со связью через хэш каждого следующего блока с предыдущим

## Архитектура
<img src= "/block4/funcoin/funcoin/arch.png" width = "800" height = "300" > 

## Интерфейсы
Реализован простой REST API на FAST API
Метод GET http://127.0.0.1:8000/blockchain
Возвращает все цепочки блоков

## UI:
Простой UI для ввода текстовых данных в блок.
Реализован на easygui

Ввод данных:
<img src= "/block4/funcoin/funcoin/UI1.png" width = "600" height = "400" >

Отображение блоков:
<img src= "/block4/funcoin/funcoin/UI2.png" width = "600" height = "400" >

## Пример:
<img src= "/block4/funcoin/funcoin/block_diag.jpg" width = "600" height = "400" >

