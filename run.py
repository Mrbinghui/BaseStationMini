# !/usr/bin/env python
# -*- coding:utf-8 -*-
#
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('BaseStationMini')

from multiprocessing import Process
from BaseStationMini import EchoServer


if __name__ == '__main__':

    print('strat')
    ProcessMptServer = Process(target=EchoServer.run)
    ProcessMptServer.start()
    print("waiting")
    ProcessMptServer.join()
    print("end")
