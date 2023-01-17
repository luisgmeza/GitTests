from PIL import Image
import numpy as np

def mandelbrot(x, y):
	escapeVal = 0
	z = complex(0, 0)
	while abs(z) <= MAX_MAG:
		if escapeVal <= MAX_ITER:
			z = z * z + complex(x, y)
			escapeVal += 1
		else: break
	return escapeVal / MAX_ITER
	
def grayscale(x, y):
	return 255 * mandelbrot(x, y) 
	
def hsvpalette(x, y):
	h = int(255 * np.log2(1 + mandelbrot(x, y)))
	s = 255
	v = 255 - h
	return h, s, v
	
if __name__ == "__main__":

    LENGTH = 800
    WIDTH = 800
    MIN_X = -1.5
    MAX_X = 0.5
    MIN_Y = -1
    MAX_Y = 1
    MAX_ITER = 80
    MAX_MAG = 2
    
	fractal = Image.new('HSV', size = (WIDTH, LENGTH), color = (0, 0, 0))

    for x in range(WIDTH):
        for y in range(LENGTH):
            pixel = hsvpalette((MAX_X - MIN_X)/WIDTH * x + MIN_X, (MAX_Y - MIN_Y)/LENGTH * y + MIN_Y)
            fractal.putpixel(xy = (x, y), value = pixel)
            
    fractal.convert('RGB').show()