import mraa
import player
import time
from threading import Thread

audible_tracks = [
	'./media/sdcard/audio/audible/1_audible.wav', 
	'./media/sdcard/audio/audible/2_audible.wav', 
	'./media/sdcard/audio/audible/3_audible.wav', 
	'./media/sdcard/audio/audible/4_audible.wav',
	'./media/sdcard/audio/audible/5_audible.wav', 
	'./media/sdcard/audio/audible/6_audible.wav'
]

ultra_tracks = [
	'./media/sdcard/audio/ultra/1_ultra.wav', 
	'./media/sdcard/audio/ultra/2_ultra.wav', 
	'./media/sdcard/audio/ultra/3_ultra.wav', 
	'./media/sdcard/audio/ultra/4_ultra.wav',
	'./media/sdcard/audio/ultra/5_ultra.wav', 
	'./media/sdcard/audio/ultra/6_ultra.wav'
]

playing = False

#***************************
#Keep alive loop
#***************************
def loop():
	while True:
		time.sleep(1)


#***************************
#Handler for play button press events
#***************************
def play(args):
	#global tracks
	global playing
	play_button = args[0]
	play_led = args[1]
	toggle_switch = args[2]
	selector_switch = args[3]

	if repr(play_button.read()) == '1':
		print 'Button pressed'

		if not playing:
			#play selected track
			for index, nextSwitch in enumerate(selector_switch):
				print 'checking next selector switch...'
				if repr(nextSwitch.read()) == '1':
					#turn LED on
					play_led.write(1)
					playing = True
					if repr(toggle_switch.read()) == '1':
						print 'playing audible bat call ' + str(index)
						player.playWav(audible_tracks[index])
					else:
						print 'playing ultrasonic bat call ' + str(index)
						player.playWav(ultra_tracks[index])
						player.playWav(ultra_tracks[index])
						player.playWav(ultra_tracks[index])
					play_led.write(0)
					playing = False
					print 'EchoBat ready...'
					break


#***************************
# Start keep-alive thread
#***************************
loopThread = Thread(target=loop)
loopThread.start()


#***************************
#Initialise GPIO pins
#***************************
play_pin = 48 #GP15
led_pin = 14 #GP13
toggle_pin = 36 #GP14
selector_pins = [47,33,46,32,45,31] #(44,45,46,47,48,49)

#***************************
#Define IOs
#***************************
#status led
play_led = mraa.Gpio(led_pin)
play_led.dir(mraa.DIR_OUT)

#toggle switch
toggle_switch = mraa.Gpio(toggle_pin)
toggle_switch.dir(mraa.DIR_IN)

#selector switch
selector_switch = []
for nextPin in selector_pins:
	nextSelector = mraa.Gpio(nextPin)
	nextSelector.dir(mraa.DIR_IN)
	selector_switch.append(nextSelector)

#manual play button
play_button = mraa.Gpio(play_pin)
play_button.dir(mraa.DIR_IN)
play_args = [play_button, play_led, toggle_switch, selector_switch]
play_button.isr(mraa.EDGE_BOTH, play, play_args)

play_led.write(0)
print 'EchoBat ready...'