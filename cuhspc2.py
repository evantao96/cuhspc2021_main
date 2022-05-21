time = input()
time = int(time)

if time == 0: 
	print('NOW')
elif time < 60:
	s = time
	print (s, "seconds")
elif time < 3600:
	m = int(time / 60)
	s = time % 60
	print (m, "minutes", s, "seconds")
elif time < 86400: 
	h = int(time / 3600)
	m = int((time % 3600) / 60)
	s = time % 60
	print (h, "hours", m, "minutes", s, "seconds")
else:
	d = int(time / 86400)
	h = int((time % 86400) / 3600)
	m = int((time % 3600) / 60)
	s = time % 60
	print (d, "days", h, "hours", m, "minutes", s, "seconds")
