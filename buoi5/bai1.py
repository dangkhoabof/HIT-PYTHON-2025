


def remove_punctuation(s):
    result = ""
    for char in s:
        if char.isalpha() or char.isspace():
            result += char
    return " ".join(result.split())


def to_lower(s: str) -> str:
    return s.lower()


def remove_stopwords(s: str, stopwords: list[str]) -> str:
    words = s.split()
    filter = [word for word in words if word not in stopwords]
    return ' '.join(filter)


def count_words(s: str) -> dict[str, int]:

    words = s.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count


def pipeline(text, functions):
    result = text
    for func in functions:
        result = func(result)
    return result

stopwords = ["is", "a", "this"]
text = "Chào bạn, hôm nay là một ngày rất đẹp!!! Bạn!!!"
steps = [
    remove_punctuation,
    to_lower,
    lambda x: remove_stopwords(x, stopwords)

]
clean_text = pipeline(text, steps)
print("Văn bản sau khi xử lý: \n", clean_text)

print(count_words(clean_text))