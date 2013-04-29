#!/usr/bin/env python
#cobbler_crack.py - a quick hack to speed up
#the built in cobbler ENC
import fapws._evwsgi as evwsgi
from fapws import base

import json
import yaml

def start():
	evwsgi.start('0.0.0.0', '80') 
	evwsgi.set_base_module(base)
	
	#TODO - should read /etc/cobbler/settings and provide
	#any global parameters
	#settings = open(fileloc, 'r')
	#parse the file
	#settings.close()
	
	def sysname(environ, start_response):
		#you might need to strip fully qualified domain
		#if you don't have them in your cobbler install
		hostname = str(environ['PATH_INFO']).split('.')[0]

		fileloc = '/var/lib/cobbler/config/systems.d/' \
			+ hostname + '.json'
		out = {}
		try:	
			sys = open(fileloc, 'r')
			system = json.load(sys)
			sys.close()
			mp = system['mgmt_parameters']
			km = system['ks_meta']
			mp.update(km)
			out['parameters'] = mp
			out['classes'] = system['mgmt_classes']
			out['classes'] = system['mgmt_classes']
		except IOError, e:
			out['parameters'] = []
			out['classes'] = []
			
		outprint = yaml.safe_dump(out, default_flow_style=True)
		start_response('200 OK', [('Content-Type','text/html')])
		return[outprint]

	evwsgi.wsgi_cb(('/enc/', sysname))

	evwsgi.set_debug(0)	   
	evwsgi.run()
 
if __name__ == '__main__':
	start()
