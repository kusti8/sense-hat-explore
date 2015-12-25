from sense_hat import SenseHat
sense = SenseHat()

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    print(t)
    t = 9.0/5.0*t+32

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    msg = "Temperature = %s F, Pressure=%s mb, Humidity=%s%%" % (t,p,h)
    print(t,p,h)

    sense.show_message(msg)
