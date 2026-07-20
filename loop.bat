@echo off
:loop
ping 127.0.0.1 -n 2 > NUL
echo pinged > out3.txt
