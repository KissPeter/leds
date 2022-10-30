#!/usr/bin/env sh
export PYTHONPATH=$(pwd)
cd led_control || exit
python3 main.py
