# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:12:56 2020

@author: sosboy888
"""
import sqlite3
import joblib
class AttendanceMark:
    conn=sqlite3.connect("Personnel.db")
    def __init__(self):
        pass
    def markAttendance(self,id):
        cursor=self.conn.execute("select Name from Students where id="+str(id))
        for row in cursor:
            print(row[0])
        