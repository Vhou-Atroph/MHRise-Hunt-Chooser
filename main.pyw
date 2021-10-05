from tkinter import *
import random

'''
VERSION 3

CONTRIBUTORS:
-Vhou-Atroph
'''

#Lists
questTypes=['Low Rank Village','Low Rank Hub','High Rank Hub'
]

allLR=[#1*
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
window.title("MHRise: Random Hunt Chooser") #Fixed the title not showing up by adding in images. So glad I figured that out!
window.geometry('350x225')
window.resizable(0,0) #Window is not resizable.

#Dropdown
selection=Frame(window)
questChoice=StringVar(window)
questChoice.set('Low Rank Village') #Default value for questChoice
choose=OptionMenu(selection,questChoice,*questTypes) #Dropdown menu with Low Rank Village as the default value (as mentioned above). The options are taken from questTypes.
rollBtn=Button(selection,text="Roll Hunt") #Creates a button with text "Roll Hunt"

#Checkboxes!
wep=IntVar(window)
bud=IntVar(window)
wepCheck=Checkbutton(selection, text="Random weapon?", variable=wep, onvalue=1, offvalue=0) #Checkbox for choosing if a user may want a random weapon in addition to a random monster.
teamCheck=Checkbutton(selection, text="Random buddies?", variable=bud, onvalue=1, offvalue=0) #Checkbox for choosing if a user may want a random team selection in addition to a random monster.

#Chosen Hunt
hunt=Label(selection,text="Your rolled hunt \nwill go here!") #Label before any hunt is rolled.
wepRoll=Label(selection,text="\n\n")
budRoll=Label(selection,text="\n\n")

#Monster Icons
defaultIcon=PhotoImage(file='icons/Unknown.png')
ico=Label(window,image=defaultIcon)

#Command
def rolltime():
  if questChoice.get()=='Low Rank Village': #questChoice is also the variable that is looked at when determining what kind of hunt to do.
    monster=random.choice(allLR)
    newIcon=PhotoImage(file='icons/'+monster+'.png')
    ico.configure(image=newIcon)
    ico.image=newIcon
    hunt.configure(text="Low Rank Village:\n"+monster)
  if questChoice.get()=='Low Rank Hub':
    monster=random.choice(allLR)
    newIcon=PhotoImage(file='icons/'+monster+'.png')
    ico.configure(image=newIcon)
    ico.image=newIcon
    hunt.configure(text="Low Rank Hub:\n"+monster)
  if questChoice.get()=='High Rank Hub':
    monster=random.choice(hubHR)
    newIcon=PhotoImage(file='icons/'+monster+'.png')
    ico.configure(image=newIcon)
    ico.image=newIcon
    hunt.configure(text="High Rank Hub:\n"+monster)
  if wep.get()==1:
    wepRoll.configure(text="Weapon:\n"+random.choice(weapons))
  elif bud.get()==1 and wep.get()==0:
    wepRoll.configure(text="")
  else:
    wepRoll.configure(text="\n\n")
  if bud.get()==1:
    budRoll.configure(text="Buddies:\n"+random.choice(teams))
  else:
    budRoll.configure(text="\n\n")
    
rollBtn.configure(command=rolltime)

#Packing time!!!
selection.pack(pady=2,padx=2,side=LEFT)
choose.pack()
wepCheck.pack()
teamCheck.pack()
rollBtn.pack(pady=2)
hunt.pack(pady=3)
wepRoll.pack()
budRoll.pack()
ico.pack(side=RIGHT)

window.mainloop() #Opens the window!