from screeninfo import get_monitors
print(get_monitors()[0].width)
for m in get_monitors():
    print(str(m))
