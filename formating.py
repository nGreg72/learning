
primes = {1: 2, 2: 3, 4: 7, 7: 17}
# print(primes[primes[4]])
# print(primes[4])


a = input('Имя:')
b = input('Фамилия:')
c = input('Скока ? :')
d = input('В чём ? :')
# age = input('Возраст:')

"""Обычное форматирование текста"""
# template = 'Поехали {0} {1} с Петькой в командировку за границу. \n' \
#            'Разошлись в разные стороны. Встречаются через {2} месяца. \n' \
#            'Василий Иванович голодный, ободранный, а Петька весь в {3}. \n' \
#            'ВИ-Где взял. П - Захожу в клуб, а там в карты в очко играют. \n' \
#            'Вначале то карта не шла. А потом один говорит "У меня очко", \n' \
#            'а я ему ну-ка покажи, а он "Джентельменам верят на слово" \n' \
#            'И тут у меня карта как поперла.... '.format(a, b, c, d)


"""f-string notation"""
template = f'Поехали {a} {b} с Петькой в командировку за границу. \n' \
            f'Разошлись в разные стороны. Встречаются через {c} месяца. \n' \
            f'Василий Иванович голодный, ободранный, а Петька весь в {d}. \n' \
            'ВИ-Где взял. П - Захожу в клуб, а там в карты в очко играют. \n' \
            'Вначале то карта не шла. А потом один говорит "У меня очко", \n' \
            'а я ему ну-ка покажи, а он "Джентельменам верят на слово" \n' \
            'И тут у меня карта как поперла.... '


print(template)


# print('{0:*^12}'.format(first_name))


