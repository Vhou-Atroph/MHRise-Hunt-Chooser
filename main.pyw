from tkinter import *
import random

'''
VERSION 1

CONTRIBUTORS:
-VhouAtroph
'''

#Lists
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
'Great Izuchi','Kulu-Ya-Ku','Great Baggi','Lagombi','Great Wroggi','Aknosom',
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
'Rakna-Kadaki','Goss Harag','Magnamalo','Almudron','Diablos','Tigrex','Rajang','Thunder Serpent Narwa'
]
weapons=['Hammer','Charge Blade','Greatsword','Hunting Horn','Longsword','Lance','Gunlance','Insect Glaive','Switch Axe','Dual Blades','Sword and Shield','Bow','Light Bowgun','Heavy Bowgun'
]

#Window
global window
window=Tk()
window.title("Monster Hunter Rise: Random Hunt Chooser")
window.geometry('180x150')
window.resizable(0,0)

#Dropdown
selection=Frame(window)
questtypes=['Low Rank Village','Low Rank Hub','High Rank Hub']
defaultquest=StringVar(window)
defaultquest.set('Low Rank Village')
choose=OptionMenu(selection,defaultquest,*questtypes)
rollbtn=Button(selection,text="Roll Hunt")

#Chosen Hunt
hunt=Label(selection,text="Your rolled hunt \nwill go here!")
wpnchance=Label(selection)

#Command
def rolltime():
  if defaultquest.get()=='Low Rank Village':
    hunt.configure(text="Low Rank Village:\n"+random.choice(vilLR))
    wpnchance.configure(text="")
  if defaultquest.get()=='Low Rank Hub':
    hunt.configure(text="Low Rank Village:\n"+random.choice(hubLR))
    wpnchance.configure(text="")
  if defaultquest.get()=='High Rank Hub':
    hunt.configure(text="Low Rank Village:\n"+random.choice(hubHR))
    wpnchance.configure(text="")
  if random.randint(0,9)>7:
    wpnchance.configure(text="Why not also try out\n"+random.choice(weapons)+"?")
    
rollbtn.configure(command=rolltime)

#Packing time!!!
selection.pack(pady=2,padx=2)
choose.pack()
rollbtn.pack(pady=2)
hunt.pack(pady=3)
wpnchance.pack()

window.mainloop()