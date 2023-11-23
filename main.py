def print_greetings():
    greetings = {
        'English': 'Hello!',
        'Spanish': '¡Hola!',
        'French': 'Bonjour!',
        'German': 'Hallo!',
        'Italian': 'Ciao!',
        'Russian': 'Привет!',
        'Chinese': '你好!',
        'Japanese': 'こんにちは!',
        'Korean': '안녕하세요!',
        'Arabic': 'مرحبا!'
    }

    print("Greetings in 10 Languages:")
    for language, greeting in greetings.items():
        print(f"{language}: {greeting}")

if __name__ == "__main__":
    print_greetings()
