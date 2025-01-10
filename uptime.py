// ERKAN KAVAS @ MIT LICENCE.
// https://github.com/erkankavas/python-server-uptime-checker
// https://www.erkankavas.com

import subprocess

def uptime():
    output = subprocess.check_output(['cat', '/proc/uptime']).decode('utf-8')
    uptime_seconds = float(output.split()[0])
    days = int(uptime_seconds // (3600 * 24))
    hours = int((uptime_seconds % (3600 * 24)) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    seconds = int(uptime_seconds % 60)
    
    return days, hours, minutes, seconds

ut = uptime()
print(f"Uptime: {ut[0]} day(s), {ut[1]} hour(s), {ut[2]} minute(s), {ut[3]} second(s)")

// Respond Example: Uptime: 19 day(s), 0 hour(s), 18 minute(s), 41 second(s)