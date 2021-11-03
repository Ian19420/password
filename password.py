password = 'a12345'
ans = input('請輸入密碼:')
i = 1
t = 2
while i < 3:
	if ans != 'a12345':
		ans = input(f'請再試一次,你還剩{t}次機會:')
		t -= 1
		i += 1
		continue
	else:
		print('登入成功!')
print('你沒機會了')
