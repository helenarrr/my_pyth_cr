from itertools import zip_longest


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]



gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(next(gen))
print(next(gen))


gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor is not None)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))













