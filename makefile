run: main.py
	python3 main.py
	@echo img.png

clean:
	# rm *.pyc
	rm *.ppm
	rm *img.png
	# rm *~
