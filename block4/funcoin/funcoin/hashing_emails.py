from hashlib import sha256

secret_phrase = "bolognese"
def get_hash_with_secret_phrase(input_data, secret_phrase):
    combined = input_data + secret_phrase
    return sha256(combined.encode()).hexdigest ()
email_body = "Эй, Боб, я думаю, тебе стоит узнать о блокчейнах! Я инвестировала в Биткойн, и в настоящее время на моем счете ровно 12,03 BTC. "

print(get_hash_with_secret_phrase(email_body, secret_phrase))