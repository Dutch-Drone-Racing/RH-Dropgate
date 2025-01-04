# RH-Plugin-Dropgate
Rotorhazard plugin to add functionality for an automatic dropgate.

## Installation
1. Setup a Rotorhazard instalion on the Raspberry Pi (Zero)
2. Place the whole contents (RH-Dropgate-Plugin) in the Rotorhazard Plugin directory on your Rotorhazard 
3. Set the GPIO in the settings menu on your Rotorhazard installion when another GPIO then 12 is used.
4. Optional to set the timer device as mirror timer [Rotorhazard mirror documentation](https://github.com/RotorHazard/RotorHazard/blob/main/doc/Cluster.md). 

## Hardware Needed

### Raspberry Pi Zero W / Raspberry Pi Zero W 2 recommended
RPI3/4/5 are also usable but will require another casing and are more expensive

### 12V BEC
Recommend to be able to deliver at least 5A for the electromagnets. For the project XL4015 or XL4005 are good options.

### 5V BEC
To power the RPi. For the project Mateksys 30 to 5V BEC is used. 

### 12V Relais
12V and at least 5A (higher is better to be sure). I use [this one](https://www.tinytronics.nl/nl/schakelaars/relais/12v-relais-1-channel-hoog-actief-of-laag-actief-30a).


### 12V 40mm Electro Magnet
You need 2 electro magnets that work on 12V. The available 3D prints are made for 40mm version. In my example 25KG version is used. As the dropgate will contain of a round bar the magnet can not use it full potential so its recommend to take a stronger magnet then needed. You could try to use a magnet with less strength on your own risk.
Product used: [JF-XP4020](https://www.tinytronics.nl/nl/mechanica-en-actuatoren/elektromagneten/elektromagneet-25kg-12v-dc-jf-xp4020)

### XT60E Connectors
2x XT60EF (Female) and 3x XT60E (Male)


### Double Sided Tape
I used some double sided tape to stick the relay, 5V BEC and 12V BEC to the case as not all dimensions are universal. I'd recommend the thicker heat resistant tape also known as 'gecko-tape'.


### M3 Screws
To mount the RPI Zero W, XT60 connectors and lid of the casing. 
4x M3x6mm  for the lid
4x M3x16mm for the RPI Zero W Bracket
6x M3x12mm for the XT60 connectors

### 3D Prints
1x Casing
2x Magnet/Pole holder

You can find the 3D files in the /prints folder.


### Other hardware
32mm tubes in lengts/heights you'd like.
Aluminium rod in the length of your drop gate banner
Metal rod for the ends of the aluminium rod that sticks to the magnet

