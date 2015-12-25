from sense_hat import SenseHat
import subprocess

sense = SenseHat()
sense.clear()
f = open('temp.log', 'w')
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
while True:
    temp = sense.get_temperature()
    process = subprocess.Popen(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print out
    cpu = float(find_between(out, 'temp=', "'C"))
    print temp, cpu
    delta = cpu-temp
    f.write(str(delta)+'\n')
    sense.show_message(str(round(delta,1)))
