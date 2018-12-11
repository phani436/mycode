#!/usr/bin/env python3

message = 'the movie is about to begin, we recommend setting your video to '
print(message)
speed = float(input('what is your speed ? '))
print(speed)
if speed >= 25:
  message = message + '4k'
elif speed >=10:
  message = message + '1080p'
elif speed >=2:
  message = message + '720p'
else:
  message = 'slow connection'

print(message)
