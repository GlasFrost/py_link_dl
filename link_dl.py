#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#f.write(urllib.request.urlopen("http://www.heise.de/thema/NSA").read().decode('utf8'))

import os, sys, json, urllib.request
import sqlite3 as lite

class link_dl:
	
	default_config = '{"db_file": "links.sqlite3"}'
	config = {}
	
	def __init__(self, config_file=''):
		
		if config_file == '':
			self.config = json.loads(self.default_config)
		else:
			try:
				f = open(config_file, "r")
				self.config = json.loads(f.read())
				f.close()
			except Exception as e:
				print("[WRN] link_dl.__init__(): Can't read config from file {}: {}".format(config_file, e))
				print("[INF] link_dl.__init__(): using default config")
	
	def insert(self, url='', comment=''):
		if url=='':
			print("[ERR] link_dl.insert(): No URL given!")
			return False
		else:
			if "http://" in url:
				try:
					html = urllib.request.urlopen(url).read().decode('utf8')
				except Exception as e:
					print("[ERR] link_dl.insert(): Unable to download website: {}".format(e))
					return False
				con = None
				try:
					con = lite.connect(self.config["db_file"])
					cur = con.cursor()
					cur.execute("CREATE TABLE IF NOT EXISTS links(id INTEGER PRIMARY KEY, url VARCHAR(255), comment TEXT, html TEXT, dat DATETIME DEFAULT(CURRENT_TIMESTAMP))")
					cur.execute("INSERT INTO links (url, comment, html) VALUES (?, ?, ?)", (url, comment, html))
					con.commit()
				except Exception as e:
					print("[ERR] link_dl.insert(): SQLite error: {}".format(e))
					return False
				finally:
					if con:
						con.close()
				print("[SUC] link_dl.insert(): Done")
				return True
			else:
				print("[ERR] link_dl.insert(): Invalid URL!")
				return False

if __name__ == '__main__':
	if len(sys.argv) > 3:
		if "http://" in sys.argv[1]:
			url = sys.argv[1]
			comment = " ".join(sys.argv[2:])
			operator = link_dl()
			operator.insert(url, comment)
		else:
			sys.exit("Invalid systax!")
	else:
		sys.exit("Give me some more information.")