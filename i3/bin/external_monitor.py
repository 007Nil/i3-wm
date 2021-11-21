#!/usr/bin/python3

import argparse
import subprocess
# xrandr --output VGA1 --right-of LVDS1
#INTERNAL = "eDP1"
INTERNAL = "eDP-1-1"
#EXTERNAL = "HDMI1"
EXTERNAL = "HDMI-1-1"
HDMI_CONNECT = f"{EXTERNAL} connected"
#PRIMARY_CMD = "xrandr --output HDMI-1-1 --right-of LVDS1"


def is_connected():
    xrandr_output = subprocess.check_output("xrandr").decode()
    if HDMI_CONNECT in xrandr_output:
        return True
    else:
        print("HIT")
        return False


def exe_cmd(direction):
    active_internal_cmd = f'xrandr --output {INTERNAL} --primary --mode 1366x768'
    print(active_internal_cmd)
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
    external_cmd = f'xrandr --output {INTERNAL} --off'
    print(external_cmd)
    feh_cmd = "feh --bg-scale /home/$USER/Downloads/anime.jpg"
    subprocess.run(external_cmd,shell=True)
    subprocess.run(feh_cmd,shell=True)
def internal():
    internal_cmd = f'xrandr --output {EXTERNAL} --off'
    subprocess.run(internal_cmd,shell=True)

def dynamic_monitor_name_fetch():
    internal_like = "eDP"
    external_like = "HDMI"
    xrandr_output = subprocess.getoutput("xrandr")

    output_list = xrandr_output.splitlines()

    for each_line in output_list:
        if internal_like in each_line:
            # print("HIT")
            global INTERNAL
            INTERNAL = each_line.split(" ")[0]
            # print(INTERNAL)

        if external_like in each_line:
            global EXTERNAL
            global HDMI_CONNECT
            EXTERNAL = each_line.split(" ")[0]
            HDMI_CONNECT = f"{EXTERNAL} connected"


    # print(INTERNAL)
    # print(EXTERNAL)


def main():
    dynamic_monitor_name_fetch()
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
            print("HIT")
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
