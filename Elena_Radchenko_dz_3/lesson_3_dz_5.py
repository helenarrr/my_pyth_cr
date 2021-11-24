import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "красный", "утопичный", "мягкий"]


def get_jokes(num):
    joke_lst = []
    for i in range(num):
        ran_noun = random.choice(nouns)
        ran_adv = random.choice(adverbs)
        ran_adj = random.choice(adjectives)
        joke_lst.append(f"{ran_noun} {ran_adv} {ran_adj}")
    return joke_lst


print(get_jokes(2))


def get_jokes_adv(num, repeats=True):
    joke_lst = []
    if not repeats:
        if num > min(len(nouns), len(adverbs), len(adjectives)):
            return "Without variants"
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(num):
                joke_lst.append(f"{nouns[i]} {adverbs[i]} {adjectives[i]}")
    else:
        for i in range(num):
            ran_noun = random.choice(nouns)
            ran_adv = random.choice(adverbs)
            ran_adj = random.choice(adjectives)
            joke_lst.append(f"{ran_noun} {ran_adv} {ran_adj}")
    return joke_lst


print(get_jokes_adv(4, False))


