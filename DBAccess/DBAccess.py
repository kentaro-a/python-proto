# -*- coding: utf-8 -*-

import MySQLdb as msc


"""
Accesser Class of Mysql Database.
	env:
		- python(3.5.1)
		- mysqlclient
"""
class DBAccess:
	
	"""
	Initialize
		config: {
			"user":"dbuser(required)",
			"password":"your db password(required)",
			"database":"database name(required)",
			"host":"database placed on(default=localhost)",
			"port":"database port(default=3306)",
			"charset","databse charset(default=utf8)"
			}
		...type of value is all string
	
	"""
	def __init__(self, config={}):
		requiredKeys = ["user", "password", "database"]
		for key in requiredKeys:
			if not key in config:
				raise Exception("Invalid config.")
	
		if not "host" in config: config["host"] = "localhost"
		if not "port" in config: config["port"] = "3306" 
		if not "charset" in config: config["charset"] = "utf8" 
		self.config = config	


	"""
	Get connection of Database
	"""
	def getDbConnection(self):
		return msc.connect(**self.config)
		
	
	"""
	Execute your query and get its result 
		If the query is "select" ,rows is returned as result of query, 
		On the others, dict of rowCount that iscount of affected row and insertedRowId is returned.
		
		query(str,required): sql includes placeholders like as %s...
		params(list): optional parameters of query
	"""
	def query(self, query, params=[]):
		con = self.getDbConnection()
		cursor = con.cursor(dictionary=True)
	
		if len(params) > 0:
			cursor.execute(query, tuple(params))
		else:
			cursor.execute(query)
		
		if cursor.with_rows:
			ret = {"row": cursor.fetchall()}
		else:
			ret = {"rowCount": cursor.rowcount,
					"insertedRowId": cursor.lastrowid,
				}
			con.commit()
	
		cursor.close()
		con.close()
		return ret

