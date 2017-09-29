import subprocess

def playWav(file_path):
	subprocess.call(["aplay", "-D", "hw:2,0", file_path])