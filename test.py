import urllib.parse

url = "https://www.google.com/maps/place/Anytime+Fitness/@38.859691,-94.7507246,12z/data=!4m6!3m5!1s0x87c0c1a24b58163b:0x518415eefd7cb2c!8m2!3d38.859691!4d-94.6683271!16s%2Fg%2F11c6q33cnq?entry=ttu"
print(urllib.parse.quote(url))