#!/usr/bin/env python3
'''
use this via the command-line
or via import changy

uses watchdog
'''
from watchdog.observers import Observer as FSObserver
from watchdog.events import FileSystemEventHandler as FSEventHandler
import time

class Error(Exception): pass

FILE_NAME = ".changy"

def doFuncs(events, folder, time_space=5):
    '''
    schedule functions to happen on any file system
    change (in the folder)

    :param events: a list of functions that will be executed on any change
    :param time_space: delay between changes
    :param folder: folder to watch
    '''
    last_reset = -30
    class EventHandler(FSEventHandler):
        '''
        the changy event handler
        '''
        def on_any_event(self, event):
            nonlocal last_reset
            curr_time  = time.time()
            is_over_time_space = curr_time - last_reset > time_space
            if is_over_time_space: 
                for f in events: f()
                last_reset = curr_time

    eh = EventHandler()
    observer = FSObserver()
    observer.schedule(eh, folder, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    import os
    import yaml
    import subprocess
    from orchid66 import printn, printc

    printn('*running* *changy*!', ['orange', 'green']

    if not os.path.isfile(FILE_NAME):
        raise Error(f"{FILE_NAME} file not found!")
    
    with open(FILE_NAME) as cf:
        details = yaml.load(cf, Loader=yaml.FullLoader)

    tasks = details.get('tasks')
    time_space = details.get("delay", 5)
    if not tasks: raise Error('no tasks specified')

    def performTasks():
        for task in tasks:
            printn(f'*doing task* - *{task}*', ['lime green', 'maroon'])
            subprocess.call(task, shell=True)

    doFuncs([performTasks], '.', time_space)
