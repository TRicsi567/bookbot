def get_num_words(content):
    return len(content.split())

def get_char_counts(content):
    result = {}
    words = content.split()

    for word in words:
        for letter in word:
            lower_letter = letter.lower()
            if lower_letter in result:
                result[lower_letter] += 1
            else:
                result[lower_letter] = 1
    return result


def sort_char_counts(counts):
    result = []
    for k, v in counts.items():
        result.append({"char": k, "num": v })
    result.sort(key = lambda x: x["num"], reverse = True)
    return result





