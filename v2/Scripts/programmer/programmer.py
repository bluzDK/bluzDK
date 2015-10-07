import subprocess
import sys
import argparse
import os

parser = argparse.ArgumentParser(description='Programs and provisions bluz-based boards for test and production')
parser.add_argument('-m', '--mode', default='test', help='mode to program, either test or prod')
parser.add_argument('-p', '--programmer', default='jlink', help='programmer, either stlink or jlink')
opts = parser.parse_args()
print opts

programmer = opts.programmer
mode = opts.mode

print "Welcome to bluz programmer!"
print "Running in mode " + mode + " with programmer " + programmer

#output = os.system("adalink nrf51822 --programmer " + programmer + " --info")

#subprocess.call("adalink nrf51822 --programmer " + programmer + " --info")

#p = subprocess.call(['adalink'], [' nrf51822 ', ' --programmer ', programmer + ' --info'])

args = ["adalink"]
args.append('nrf51822')
args.append('--programmer')
args.append(programmer)
args.append('--info')


#p = subprocess.Popen(args, stdout=subprocess.PIPE)
#
##out, err = p.communicate()
#out = p.wait()

out = subprocess.check_output(args)
print "---------------------------------------"
print "Getting Hardware ID"
print "---------------------------------------"
print out
print ""

for line in out.split('\n'):
    if ':' in line:
        if line.split(':')[0].strip() == 'Device ID':
            hwIDReversed = str(line.split(':')[1].strip())


hwID = "b1e2"
f = open('bluz_id.txt', 'rw')
idCounter = int('0x' + f.read().strip(), 16)
f.close()

hwID += str(hex(idCounter))[2:].zfill(4)

i = len(hwIDReversed)
for val in range(len(hwIDReversed)/2):
    hwID += hwIDReversed[i-2:i]
    i -= 2

hwID = hwID.lower()
print "PARTICLE ID: " + hwID
print ""

if mode == "test":
    print "---------------------------------------"
    print "Sending ID to Cloud"
    print "---------------------------------------"
    args = ["particle"]
    args.append('keys')
    args.append('send')
    args.append(hwID)
    args.append('/Users/eely/workspace/spark_core/keys/sparkle_core.pub.pem')

    out = subprocess.check_output(args)
    print out
    print ""

    f = open('provisioned_boards.txt', 'a')
    f.write(hwID)
    f.write('\n')
    f.close()


print "---------------------------------------"
print "Wiping Hardware Flash"
print "---------------------------------------"
args = ["adalink"]
args.append('nrf51822')
args.append('--programmer')
args.append(programmer)
args.append('--wipe')
out = subprocess.check_output(args)
print out
print ""

print "---------------------------------------"
print "Programming Firmware"
print "---------------------------------------"
if mode == "test":
    f = open('int.bin', 'w')
    counter = str(hex(idCounter))[2:].zfill(4)
    first = int('0x' + counter[2:], 16)
    second = int('0x' + counter[:2], 16)
    idArray = bytearray([first, second])
    f.write(idArray)
    f.close()

args = ["adalink"]
args.append('nrf51822')
args.append('--programmer')
args.append(programmer)
if mode == "test":
    args.append('--program-bin')
    args.append('./int.bin')
    args.append('0x3F000')

args.append('--program-hex')
args.append('./s110/s110_softdevice.hex')
if mode == "test":
    args.append('--program-hex')
    args.append('./test/main.hex')
elif mode == "prod":
    args.append('--program-hex')
    args.append('./prod/main.hex')


out = subprocess.check_output(args)
print out
print ""

print "---------------------------------------"
print "Cleaning Up"
print "---------------------------------------"
if mode == "test":
    os.remove('int.bin')
    os.remove('bluz_id.txt')
    f = open('bluz_id.txt', 'w')
    idCounter += 1
    f.write(str(hex(idCounter))[2:])
    f.close()


