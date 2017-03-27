#!/usr/bin/python2

import threading
import subprocess
import re

start_frame_re = re.compile(r'^APRS: (.*)')

class Kenwood:
	def __init__(self, frame_handler, config):
		self.frame_handler = frame_handler
		self.config = config
		self.subprocs = {}
		self._start()
		self._running = True
		self._worker = threading.Thread(target=self._kw_worker)
		self._worker.setDaemon(True)
		self._worker.start()

	def exit(self):
		self._running = False
		self._stop()
		
		
	def _start(self):
#		if self.config['source'] = 'kenwood':

	def _stop(self):
#		for name in ['mm', 'src']:
#			try:
#				proc = self.subprocs[name]
#				proc.terminate()
#			except:
#				pass


	def _kw_worker(self):
		while self._running:
			line = stdin.readline()
			line = line.strip()
			m = start_frame_re.match(line)
			if m:
				tnc2_frame = m.group(1)
				self.frame_handler(tnc2_frame)
