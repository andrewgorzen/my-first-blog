# volume = 9

#Change the volume if too loud or too quiet
#if volume < 20 or volume > 80:
#    volume = 50

#Display the volume
#print("Volume is now at " + str(volume))

def hi(name):
    if name == "Drew":
        print('Hi, me.')
    elif name == "Sonya":
        print('hey turd')
    else:
        print('Hello, ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Sonya']
i = 1

for name in girls:
    hi(name)
    print(i)
    i = i + 1