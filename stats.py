def total_words(text):
    word_count = text.split()
    return len(word_count)

def num_appears(text):
    char_bank_count = {}
    for i in text:
        i = i.lower()
        if i in char_bank_count:
            char_bank_count[i] += 1
        else:
            char_bank_count[i] = 1
    return char_bank_count

def sort_on(nums):
    return nums["num"]

def sort_text_chars(char_nums):
    converted_list = []
    for i in char_nums.items():
        dict_charandnum = {
            "char": i[0],
            "num": i[1]
        }
        converted_list.append(dict_charandnum)
    converted_list.sort(reverse=True, key=sort_on)
    return converted_list