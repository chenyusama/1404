text = input("Text: ").split(" ")

word_to_count = {}
for i in range(len(text)):
    if text[i] in word_to_count:
        word_to_count[text[i]] += 1
    else:
        word_to_count.update({text[i]: 1})

sorted_words = sorted(word_to_count.items())

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))

for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
