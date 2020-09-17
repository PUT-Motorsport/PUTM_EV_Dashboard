fb0:
	sudo FRAMEBUFFER=/dev/fb0 xinit ./display-rework.py $* -- :1

fb1:
	sudo FRAMEBUFFER=/deb/fb1 xinit ./display-rework.py $* -- :1
