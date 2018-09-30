import random
star = input('請決定最小值: ')
end = input('請決定最大值: ')
star = int(star)
end = int(end)
r = random.randint(star,end)
count = 0
while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜答對!!')
		print('你用了', count, '次猜對')
		break
	elif num < r:
		print('比', num,'大')
	elif num > r:
		print('比', num,'小')
	print('這是你猜的第', count, '次')
		
	