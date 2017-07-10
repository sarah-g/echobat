import subprocess

def playWav(file_path):
	subprocess.call(["aplay", "-D", "mono", file_path])