question = ()
answer  = ('no reply')
indice = 1
print('question')
for indice in range(1, 5):
    question = input('type quetion: ')
    if len(question) > 0:
        print(f'the aswer is :{answer}')
    else:
        print('error')
    answer = input('type aswer: ')

    indice = + 1

