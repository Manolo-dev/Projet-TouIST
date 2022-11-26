@echo off
touist --sat --solve %1>output.txt
py filter.py
type output.txt