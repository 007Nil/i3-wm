#!/usr/bin/python3

import argparse
import subprocess
# xrandr --output VGA1 --right-of LVDS1
INTERNAL = "eDP-1"
EXTERNAL = "HDMI-1"
HDMI_CONNECT = "HDMI-1 connected"
PRIMARY_CMD = "xrandr --output HDMI-1 --right-of LVDS1"


def is_connected():
    xrandr_output = subprocess.check_output("xrandr").decode()
    if HDMI_CONNECT in xrandr_output:
        return True
    else:
        return False


def exe_cmd(direction):
    active_internal_cmd = 'xrandr --output eDP-1 --primary --mode 1366x768'
    PRIMARY_CMD = "xrandr --output {} --{}-of {} --mode 1920x1080".format(
        EXTERNAL, direction, INTERNAL)
    feh_cmd = "feh --bg-scale /home/$USER/Downloads/anime.jpg"
    subprocess.run(active_internal_cmd,shell=True)
    subprocess.run(PRIMARY_CMD, shell=True)
    subprocess.run(feh_cmd, shell=True)


def left():
    if is_connected():
        exe_cmd("left")


def right():
    if is_connected():
        exe_cmd("right")

def external():
    external_cmd = 'xrandr --output eDP-1 --off'
    feh_cmd = "feh --bg-scale /home/$USER/Downloads/anime.jpg"
    subprocess.run(external_cmd,shell=True)
    subprocess.run(feh_cmd,shell=True)
def internal():
    internal_cmd = 'xrandr --output HDMI-1 --off'
    subprocess.run(internal_cmd,shell=True)


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--left", '-l', help="set monitor in left", action="store_true")
        parser.add_argument(
            "--right", '-r', help="set monitor in right", action="store_true")
        parser.add_argument(
            '--external' ,'-e', help='Only external activated', action='store_true'
        )
        parser.add_argument(
            '--internal', '-i', help='only ldaptop display activated', action='store_true'
        )
        args = parser.parse_args()

        if args.left:
            left()
        elif args.right:
            right()
        elif args.external:
            external()
        elif args.internal:
            internal()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
