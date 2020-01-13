#!/usr/bin/env python
import os
import json
import datetime
class update_time():
    def __init__(self,name,min_update_day=30,command='',config_file='/home/pwnht/crontab/json/update_date.json'):
        self.file=config_file
        self.date=json.load(open(self.file))
        self.now=datetime.date.today()
        self.json_name=name
        self.min_update_day=min_update_day
        self.command=command
        try:
            self.name=json.loads(self.date[name])
        except:
            self.name={}
            self.sub_time=1
            self.min_update_day=0
            if self.update_name():
                print("--------------")
                print(self.json_name+" init succeed")
                print("--------------")
            else:
                print("--------------")
                print(self.json_name+" init fail")
                print("--------------")
        else:
            self.update_day=(self.name['update_day'])
            self.update_time=datetime.date(int((self.update_day.split('-'))[0]),int((self.update_day.split('-'))[1]),int((self.update_day.split('-'))[2]))
            self.sub_time=self.now.__sub__(self.update_time).days
    def update_name(self):
        if self.sub_time>self.min_update_day:
            if os.system(self.command):
                print("--------------")
                print(self.json_name+" exec fail")
                print("--------------")
                return 0
            self.name['update_day']=self.now
            self.date[self.json_name]=json.dumps(self.name,cls=DateTimeEncoder)
            json.dump(self.date,open(self.file,'w'),sort_keys=True, indent=4, separators=(',', ':'))
            return 1
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)