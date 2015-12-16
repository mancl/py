#!/usr/bin/python
#coding=utf8

import threading

class MyLocal(threading.local):
    def __init__(self):
        self.name = "base";


class MyThread(threading.Thread):
    def __init__(self, thread_local):
        super(MyThread, self).__init__()
        self._local = thread_local;

    def run(self):
        self._local.name = self.getName();
        print self._local.name;


if __name__ == "__main__":
    thread_local = MyLocal();
    a = MyThread(thread_local);
    a.start();
    b = MyThread(thread_local);
    b.start();

    a.join();
    b.join();
    print "ok";

