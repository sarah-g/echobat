import mraa
import player
import time
from threading import Thread

#audible_tracks = ['sopranopip_audible.wav', 'commonpip_audible.wav', 'noctule_audible.wav', 'serotine_audible.wav', 'leisler_audible.wav', 'brownlong_audible.wav']
#ultra_tracks = ['sopranopip_ultra.wav', 'commonpip_ultra.wav', 'ultra_bat.wav', 'ultra_bat.wav', 'ultra_bat.wav', 'brownlong_ultra.wav']

audible_tracks = ['recording1.wav', 'recording2.wav', 'recording3.wav', 'recording4.wav', 'recording5.wav', 'recording6.wav']
ultra_tracks = ['recording1.wav', 'recording2.wav', 'recording3.wav', 'recording4.wav', 'recording5.wav', 'recording6.wav']
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
	global tracks
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
						print 'playing audible bat call'
						player.playWav(audible_tracks[index])
					else:
						print 'playing ultrasonic bat call'
						player.playWav(ultra_tracks[index])
					play_led.write(0)
					playing = False
					print 'EdiBat ready...'
					break


#***************************
# Start keep-alive thread
#***************************
loopThread = Thread(target=loop)
loopThread.start()


#***************************
#Initialise GPIO pins
#***************************
play_pin = 14 #(A0)
led_pin = 15 #(A1)
toggle_pin = 4 #(D4)
selector_pins = [6,7,8,9,10,11] #(D6,D7,D8,D9,D10,D11)

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
print 'EdiBat ready...'