#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import schedule
import datetime
import subprocess
import time

def rec_agqr(url, time, name):
    rtmpdump = "/usr/bin/rtmpdump"
    ffmpeg = "/usr/bin/ffmpeg"
    today = datetime.datetime.now().strftime('%Y%m%d')
    print("{}: {}の録音を開始します...".format(datetime.datetime.now().strftime('%Y/%m/%d %H:%M', name)))
    p1 = subprocess.Popen([rtmpdump, "-v", "-r", url, "-m", "60", "-B", str(time), "-o", "-"], stdout = subprocess.PIPE, stderr= subprocess.DEVNULL)
    p2 = subprocess.Popen([ffmpeg, "-y", "-i", "-", "{}-{}.mp4".format(name, today)], stdin = p1.stdout, stderr = subprocess.DEVNULL)
    p2.communicate()

def rec_radiko(name, station, duration):
    radigo = "/usr/local/bin/go/bin/radigo"
    print("{}: {}の録音を開始します...".format(datetime.datetime.now().strftime('%Y/%m/%d %H:%M', name)))
    subprocess.call([radigo, "rec-live", "-id={}".format(station), "-t={}".format(duration), "-o=mp3"])

if __name__ == '__main__':
    json_path = "/home/hsrmy/bin/program.json"
    agqr_url = "rtmp://fms-base1.mitene.ad.jp/agqr/aandg1"

    with open(json_path) as file:
        programs = json.load(file)
    for i in range(0,7):
        if len(programs[str(i)]) != 0:
            for prog in programs[str(i)]:
                if i == 0:
                    if prog['station'] == "agqr":
                        schedule.every().monday.at(prog['start']).do(rec_agqr, agqr_url, prog['minute'], prog['name'])
                    else:
                        schedule.every().monday.at(prog['start']).do(rec_radiko, prog['name'], prog['station'], prog['minute'])
                elif i == 1:
                    if prog['station'] == "agqr":
                        schedule.every().tuesday.at(prog['start']).do(rec_agqr, agqr_url, prog['minute'], prog['name'])
                    else:
                        schedule.every().tuesday.at(prog['start']).do(rec_radiko, prog['name'], prog['station'], prog['minute'])
                elif i == 2:
                    if prog['station'] == "agqr":
                        schedule.every().wednesday.at(prog['start']).do(rec_agqr, agqr_url, prog['minute'], prog['name'])
                    else:
                        schedule.every().wednesday.at(prog['start']).do(rec_radiko, prog['name'], prog['station'], prog['minute'])
                elif i == 3:
                    if prog['station'] == "agqr":
                        schedule.every().thursday.at(prog['start']).do(rec_agqr, agqr_url, prog['minute'], prog['name'])
                    else:
                        schedule.every().thursday.at(prog['start']).do(rec_radiko, prog['name'], prog['station'], prog['minute'])
                elif i == 4:
                    if prog['station'] == "agqr":
                        schedule.every().friday.at(prog['start']).do(rec_agqr, agqr_url, prog['minute'], prog['name'])
                    else:
                        schedule.every().friday.at(prog['start']).do(rec_radiko, prog['name'], prog['station'], prog['minute'])
                elif i == 5:
                    if prog['station'] == "agqr":
                        schedule.every().saturday.at(prog['start']).do(rec_agqr, agqr_url, prog['minute'], prog['name'])
                    else:
                        schedule.every().saturday.at(prog['start']).do(rec_radiko, prog['name'], prog['station'], prog['minute'])
                elif i == 6:
                    if prog['station'] == "agqr":
                        schedule.every().sunday.at(prog['start']).do(rec_agqr, agqr_url, prog['minute'], prog['name'])
                    else:
                        schedule.every().sunday.at(prog['start']).do(rec_radiko, prog['name'], prog['station'], prog['minute'])
    print("Jobs: {}".format(schedule.jobs))
    while True:
        schedule.run_pending()
        time.sleep(1)
