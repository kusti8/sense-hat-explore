from sense_hat import SenseHat
import subprocess

sense = SenseHat()
sense.clear()
f = open('temp.log', 'w')
while True:
    temp = sense.get_temperature()
    process = subprocess.Popen('''vcgencmd measure_temp | sed -e "s/temp=\(.*\)'C/\1/"''', shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    cpu = float(out)
    print temp, cpu
    delta = cpu-temp
    f.write(str(delta)+'\n')
    sense.show_message(str(round(delta,1)))
