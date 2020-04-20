#!/usr/bin/env python3
weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
print('days in week: {}'.format(len(weekdays)))

workdays = weekdays[0:5]
weekend = weekdays[5:]
print('workdays: {}'.format(workdays))
print('weekend: {}'.format(weekend))
