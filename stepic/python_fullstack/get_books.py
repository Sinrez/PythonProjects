import requests as re
for i in range(1, 3):
    img_data = re.get(f'https://www.litres.ru/pages/get_pdf_page/?file=98856895&page={i}&rt=w1900&ft=gif').content
    with open(f'page{i}.gif', 'wb') as handler:
        handler.write(img_data)