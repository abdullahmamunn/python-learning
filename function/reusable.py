def emoji_converter(message):
    words = message.split()
    emojis = {
        ":)": "😃",
        "<3": "❤",
        ":(": "😒"
    }
    output = ""
    for word in words:
        output = output + emojis.get(word, word) + " "
    print(output)


message = input("> ")
emoji_converter(message)
