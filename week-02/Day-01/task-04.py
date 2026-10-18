def word_frequency_analyser(sentence: list):
    if sentence:
        new_string = sentence.split()
        new_dict = dict()
        for _ in new_string:
            new_dict[_] = 0
        for _ in new_string:
            new_dict[_] += 1
        most_occurence = 0
        word = ' '
        for item in new_dict:
            if new_dict[item] > most_occurence:
                word = item
                most_occurence = new_dict[item]
    print(word)

word = "python is fun and python is useful"
word_frequency_analyser(word)
