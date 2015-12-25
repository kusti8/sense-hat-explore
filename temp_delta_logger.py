from sense_hat import SenseHat
from subprocess import call

sense = SenseHat()
sense.clear()
f = open('temp.log', 'w')
while True:
    temp = sense.get_temperature()
    cpu = call('''vcgencmd measure_temp | sed -e "s/temp=\(.*\)'C/\1/"''', shell=True)
    delta = cpu-temp
    f.write(str(delta)+'\n')
    sense.show_message(str(round(delta,1)))
