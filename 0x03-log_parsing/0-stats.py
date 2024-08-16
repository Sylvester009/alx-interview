#!/usr/bin/python3

""" Python script that reads stdin line by line and computes metrics:
  - Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
  - After every 10 lines and/or a keyboard interruption (CTRL + C),
"""

import sys
import signal

# Initialize variables
total_file_size = 0
status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

def print_statistics():
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def parse_line(line):
    parts = line.split()
    if len(parts) >= 7:
        try:
            file_size = int(parts[-1])
            status_code = parts[-2]
            if status_code in status_counts:
                return file_size, status_code
        except ValueError:
            return None, None
    return None, None

def handle_interrupt(signum, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        file_size, status_code = parse_line(line)
        if file_size is not None and status_code is not None:
            total_file_size += file_size
            status_counts[status_code] += 1
        
        if line_count == 10:
            print_statistics()
            line_count = 0

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

finally:
    print_statistics()
