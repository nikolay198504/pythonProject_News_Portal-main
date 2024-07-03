# from django import template
#
# register = template.Library()
#
# # Пример списка нежелательных слов
# forbidden_words = ['Авиация', 'Пирамиды', 'Страница']
#
# @register.filter
# def hide_forbidden(value):
#     words = value.split()
#     result = []
#     for word in words:
#         if word in forbidden_words:
#             if len(word) > 2:
#                 result.append(word[0] + "*"*(len(word)-2) + word[-1])
#             else:
#                 result.append(word)  # Для слов длиной 2 или меньше ничего не меняем
#         else:
#             result.append(word)
#     return " ".join(result)
