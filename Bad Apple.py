import cv2 as cv
import numpy as np
import time

def Bad_Apple():

	video_directory = "C:/Users/adity/Desktop/Bad Apple/"
	file_name = "Bad Apple.mp4"
	show_output = 1
	print_the_things = 1
	video_ratio = "4:3"
	final_height = 50
	framerate = 10
	outputratio = 0.6

	currentframerate = 0
	illumination_string = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"] 
	#backest to whitest in a console
	prev = -1
	cap = cv.VideoCapture(video_directory + file_name)
	ratio = int(video_ratio.split(":")[0])/int(video_ratio.split(":")[1])
	final_width = int(final_height*(109/50)*ratio)
	#block grid of 145x50 produces 4:3. 109x50 produces 1:1

	while(cap.isOpened()):
		currentframerate = 1/(time.time() - prev)
		if (currentframerate <= framerate):
			prev = time.time()

			ret, frame = cap.read()
			imageobject = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

			height , width = imageobject.shape[:2]
			
			#interpolation: cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming.
			resizedimageobject = cv.resize(imageobject, None, fx=final_width/width, fy=final_height/height, interpolation = cv.INTER_AREA)

			if print_the_things:
				string = ""
				for y in range(final_height):
					for x in range(final_width):
						string += illumination_string[int(9*(resizedimageobject[y][x])/255)]
					string += "\n"
				print(string + "\n"*(50-final_height), end="")

			if show_output:
				cv.imshow("Bad Apple", cv.resize(imageobject, None, fx=outputratio, fy=outputratio, interpolation = cv.INTER_AREA))
				if cv.waitKey(1) & 0xFF == ord('q'):
					break

	cap.release()
	cv.destroyAllWindows()

if __name__ == '__main__':
	Bad_Apple()
