#!/usr/bin/env python
import pyautogui as pg
import time

WIDTH, HEIGHT = pg.size()

def go(n=819200):
    try:
        for _ in range(n):
            pg.click(WIDTH / 8, HEIGHT / 2)

    except pg.FailSafeException:
        print '[FailSafe]',
        time.sleep(4)
        go(n)
