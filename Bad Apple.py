import cv2 as cv
import numpy as np
import time

def Bad_Apple():

	video_directory = "/path/to/file/"
	file_name = "name.mp4"
	show_output = 1 #will show the mini screen if set to True.
	print_the_things = 1 #will print the ASCII text in console.
	video_ratio = "4:3" #you can adjust the code yourself so it defines video_ratio on its own. It's just needed to show a proportional console output.
	final_height = 50 #total height of your console in letter blocks.
	framerate = 10 #framerate at which you wanna play the video at.
	outputratio = 0.6 #size of the mini player w.r.t. initial dimensions. 

	currentframerate = 0
	illumination_string = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"] 
	#backest to whitest in a console
	prev = -1
	cap = cv.VideoCapture(video_directory + file_name)
	ratio = int(video_ratio.split(":")[0])/int(video_ratio.split(":")[1])
	final_width = int(final_height*(109/50)*ratio) ##automatically adjusting final width to have an undistorted output in console.
	#by default in Windows machines, block grid of 145x50 produces 4:3. 109x50 produces 1:1. Still check these values in your console and adjust the formula appropriately.

	while(cap.isOpened()):
		currentframerate = 1/(time.time() - prev)
		if (currentframerate <= framerate):
			prev = time.time()

			ret, frame = cap.read()
			imageobject = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

			height , width = imageobject.shape[:2]
			
			#interpolation: cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming.
			resizedimageobject = cv.resize(imageobject, None, fx=final_width/width, fy=final_height/height, interpolation = cv.INTER_AREA)

			if print_the_things: #we defined this variable earlier.
				string = ""
				for y in range(final_height):
					for x in range(final_width):
						string += illumination_string[int(9*(resizedimageobject[y][x])/255)]
					string += "\n"
				print(string + "\n"*(50-final_height), end="") 
				#printing one string at once, instead of continuously printing the characters, produces non flickering console output.
				#we're also printing (50-final_height) number of "\n" so as to keep the ASCII art non flickering. It's very annoying when it flickers.
				#you might think why don't we just add a time.sleep(xyz), but that doesn't work, it'll just fuck up your framerate, and overall its a huge pain
				#not to mention, flickering will still exist, just not as much as before. It's WAY easier (and fucking CLEANER) to just print one bloody string at a time.

			if show_output: #we defined this variable earlier as well.
				cv.imshow("Bad Apple", cv.resize(imageobject, None, fx=outputratio, fy=outputratio, interpolation = cv.INTER_AREA))
				#you can use cv.putText() to print the framerate in the output player. it sometimes helps with debugging and you can turn it on or off by just using a variable.
				#on the contrary if you print the framerate in console, it might fuck up the ASCII, and overall its way cleaner to just use cv.putText().
				
				if cv.waitKey(1) & 0xFF == ord('q'): #press q in the miniplayer to exit() the script. very helpful lol.
					break

	cap.release()
	cv.destroyAllWindows()

if __name__ == '__main__': #you don't really need if __name__ == '__main__' but i used it here to look professional lmfao.
	Bad_Apple()
