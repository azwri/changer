from allnumbers import Numbers as __num__


languages = ['english', 'arabic', 'hindi', 'persian', 'bengali',
             'chinese_simple', 'chinese_complex', 'malayalam', 'thai', 'urdu']

for language_1 in languages:
    for language_2 in languages:
        if language_1 != language_2:
            locals()['{}_to_{}'.format(language_1, language_2)] = eval(
                '__num__().{}_to_{}'.format(language_1, language_2))
