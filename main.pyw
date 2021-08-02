from tkinter import *
import random

'''
VERSION 2.1

CONTRIBUTORS:
-Vhou-Atroph
'''

#Lists
questtypes=['Low Rank Village','Low Rank Hub','High Rank Hub'
]

#Admittedly this is a little inefficient. I'm pretty sure hubLR and vilLR have exactly the same monsters so I might just merge them into low rank together.
vilLR=[#2*
'Great Izuchi','Arzuros','Great Baggi','Lagombi',
#3*
'Aknosom','Royal Ludroth','Great Wroggi','Barroth','Kulu-Ya-Ku','Tetranadon','Khezu',
#4*
'Bishaten','Somnacanth','Barioth','Rathian','Tobi-Kadachi','Volvidon','Basarios','Pukei-Pukei',
#5*
'Magnamalo','Rathalos','Mizutsune','Anjanath','Zinogre','Nargacuga',
#6*
'Almudron','Goss Harag','Tigrex','Diablos'
]

hubLR=[#1*
'Great Izuchi','Kulu-Ya-Ku','Great Baggi','Lagombi','Great Wroggi','Aknosom','Arzuros',
#2*
'Tetranadon','Bishaten','Pukei-Pukei','Royal Ludroth','Barroth','Khezu','Volvidon','Basarios','Rathian',
#3*
'Magnamalo','Diablos','Tigrex','Barioth','Zinogre','Somnacanth','Goss Harag','Tobi-Kadachi','Almudron','Anjanath','Nargacuga','Mizutsune','Rathalos'
]

hubHR=[#4*
'Apex Arzuros','Great Izuchi','Arzuros','Kulu-Ya-Ku','Great Baggi','Aknosom','Tetranadon','Lagombi','Khezu','Great Wroggi',
#5*
'Apex Rathian','Jyuratodus','Rathian','Basarios','Pukei-Pukei','Bishaten','Volvidon','Barroth','Royal Ludroth',
#6*
'Apex Mizutsune','Mizutsune','Zinogre','Somnacanth','Barioth','Tobi-Kadachi','Anjanath','Nargacuga','Rathalos','Wind Serpent Ibushi',
#7*
'Rakna-Kadaki','Goss Harag','Magnamalo','Almudron','Diablos','Tigrex','Rajang','Thunder Serpent Narwa',
#TU1
'Bazelgeuse','Chameleos','Kushala Daora','Teostra','Apex Rathalos','Apex Diablos',
#TU2
'Apex Zinogre','Crimson Glow Valstrax','Narwa the Allmother'
]

weapons=['Hammer','Charge Blade','Greatsword','Hunting Horn','Longsword','Lance','Gunlance','Insect Glaive','Switch Axe','Dual Blades','Sword and Shield','Bow','Light Bowgun','Heavy Bowgun'
]

teams=['Solo','1 Palamute and 1 Palico','2 Palamutes','2 Palicos','1 Palamute','1 Palico'
]

#Window
global window
window=Tk()
window.title("MHRise: Random Hunt Chooser") #Uhh the full title doesn't show up. At all. Hmm.
window.geometry('180x200')
window.resizable(0,0) #Window is not resizable.

#Dropdown
selection=Frame(window)
defaultquest=StringVar(window)
defaultquest.set('Low Rank Village')
choose=OptionMenu(selection,defaultquest,*questtypes) #Dropdown menu with Low Rank Village as the default value. The options are taken from questtypes.
rollbtn=Button(selection,text="Roll Hunt") #Creates a button with text "Roll Hunt"

#Checkboxes!
wep=IntVar(window)
bud=IntVar(window)
wepCheck=Checkbutton(selection, text="Random weapon?", variable=wep, onvalue=1, offvalue=0)
teamCheck=Checkbutton(selection, text="Random buddies?", variable=bud, onvalue=1, offvalue=0)

#Chosen Hunt
hunt=Label(selection,text="Your rolled hunt \nwill go here!") #Label before any hunt is rolled.
weproll=Label(selection)
budroll=Label(selection)

#Command
def rolltime():
  if defaultquest.get()=='Low Rank Village': #defaultquest is also the variable that is looked at when determining what kind of hunt to do. Kinda dumb, might change the name.
    hunt.configure(text="Low Rank Village:\n"+random.choice(vilLR))
  if defaultquest.get()=='Low Rank Hub':
    hunt.configure(text="Low Rank Hub:\n"+random.choice(hubLR))
  if defaultquest.get()=='High Rank Hub':
    hunt.configure(text="High Rank Hub:\n"+random.choice(hubHR))
  if wep.get()==1:
    weproll.configure(text="Weapon: "+random.choice(weapons))
  else:
    weproll.configure(text="Weapon: Your choice!")
  if bud.get()==1:
    budroll.configure(text="Buddies: "+random.choice(teams))
  else:
    budroll.configure(text="Buddies: Your choice!")
    
rollbtn.configure(command=rolltime)

#Packing time!!!
selection.pack(pady=2,padx=2)
choose.pack()
wepCheck.pack()
teamCheck.pack()
rollbtn.pack(pady=2)
hunt.pack(pady=3)
weproll.pack()
budroll.pack()

window.mainloop() #Opens the window!