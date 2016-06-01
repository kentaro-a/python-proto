# -*- coding: utf-8 -*-

import logging
	
def initLogger( _filepath="log.txt", isConsoleOutput=False):
	logging.basicConfig(filename=_filepath,
						level=logging.DEBUG,
						format="[%(asctime)s][%(levelname)s][%(filename)s Line:%(lineno)d] %(message)s",
						)
	return logging
