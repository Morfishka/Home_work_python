# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = input("текст: ")

def compressed(text):

    count = 1
    compressed_text = ''
    marker = text[0]

    for i in range(1, len(text)):
        if text[i] == marker:
            count +=1
        else:
            compressed_text += marker + str(count)
            count = 1
            marker = text[i+1]
    compressed_text += marker + str(count)
    return compressed_text

print(compressed(text))

cod ='q4w3e5r2'

def recovery(text):
    count = ''
    restored_text = ''
    for j in text:
        if j.isdigit():
            count += j
        else:
            restored_text += j * int(count)
            count = ''
    return restored_text

print(recovery(cod))
