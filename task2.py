# задание 2
time = int(input('Напишите количество секунд: '))
hours = time//3600
minuts = time%3600//60
seconds = time%60
if hours <10:
    hours = '0'+str(hours)
if minuts <10:
    minuts = '0'+str(minuts)
if seconds <10:
    seconds ='0'+str(seconds)
print(f'{hours}:{minuts}:{seconds}')
