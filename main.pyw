from tkinter import *
import random

'''
VERSION 3.3.1

CONTRIBUTORS:
-Vhou-Atroph
-PurpleShad0w
'''

#Lists
quest_types=['Low Rank','High Rank','Master Rank'
]

monsters={"Low Rank":[#1*
'Great Izuchi','Kulu-Ya-Ku','Great Baggi','Lagombi','Great Wroggi','Aknosom','Arzuros',
#2*
'Tetranadon','Bishaten','Pukei-Pukei','Royal Ludroth','Barroth','Khezu','Volvidon','Basarios','Rathian',
#3*
'Magnamalo','Diablos','Tigrex','Barioth','Zinogre','Somnacanth','Goss Harag','Tobi-Kadachi','Almudron','Anjanath','Nargacuga','Mizutsune','Rathalos'],
"High Rank":[#4*
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
'Apex Zinogre','Crimson Glow Valstrax','Narwa the Allmother'],
"Master Rank":[#G1
'Daimyo Hermitaur','Aknosom','Volvidon','Barroth','Great Wroggi','Lagombi','Great Baggi','Kulu-Ya-Ku','Royal Ludroth','Arzuros','Tetranadon','Great Izuchi',
#G2
'Blood Orange Bishaten','Tobi-Kadachi','Basarios','Jyuratodus','Rathian','Khezu','Somnacanth','Pukei-Pukei','Anjanath','Bishaten',
#G3
'Garangolm','Nargacuga','Rakna-Kadaki','Magnamalo','Shogun Ceanataur','Almudron','Barioth','Goss Harag','Aurora Somnacanth',
#G4
'Lunagaron','Gore Magala','Tigrex','Pyre Rakna-Kadaki','Zinogre','Seregios','Magma Almudron','Mizutsune','Diablos','Rathalos','Astalos','Espinas',
#G5
'Malzeno','Chameleos','Teostra','Rajang','Bazelgeuse','Shagaru Magala','Kushala Daora',
#G6
'Gaismagorm','Wind Serpent Ibushi','Narwa the Allmother','Furious Rajang','Crimson Glow Valstrax','Scorned Magnamalo',
#TU1
'Seething Bazelgeuse','Silver Rathalos','Gold Rathian','Lucent Nargacuga',
#TU2
'Flaming Espinas','Violet Mizutsune','Risen Chameleos',
#TU3
'Chaotic Gore Magala','Risen Kushala Daora','Risen Teostra',
#TU4
'Velkhana',#'Risen Crimson Glow Valstrax'
]
}

weapons=['Hammer','Charge Blade','Greatsword','Hunting Horn','Longsword','Lance','Gunlance','Insect Glaive','Switch Axe','Dual Blades','Sword and Shield','Bow','Light Bowgun','Heavy Bowgun'
]

teams=['Solo','1 Palamute and 1 Palico','2 Palamutes','2 Palicos','1 Palamute','1 Palico'
]

#Window
global window
window=Tk()
window.title("MHRise: Random Hunt Chooser") #Fixed the title not showing up by adding in images. So glad I figured that out!
window.geometry('350x260')
window.resizable(0,0) #Window is not resizable.
window.iconbitmap("icons/gargwa.ico")

#Dropdown
selection=Frame(window)
quest_choice=StringVar(window)
quest_choice.set('Low Rank') #Default value for quest_choice
choose=OptionMenu(selection,quest_choice,*quest_types) #Dropdown menu with Low Rank Village as the default value (as mentioned above). The options are taken from quest_types.
roll_hunt=Button(selection,text="Roll Hunt") #Creates a button with text "Roll Hunt"

#Checkboxes!
wep=IntVar(window)
bud=IntVar(window)
wep_check=Checkbutton(selection, text="Random weapon", variable=wep, onvalue=1, offvalue=0) #Checkbox for choosing if a user may want a random weapon in addition to a random monster.
team_check=Checkbutton(selection, text="Random buddies", variable=bud, onvalue=1, offvalue=0) #Checkbox for choosing if a user may want a random team selection in addition to a random monster.

#Chosen Hunt
the_hunt=Frame(selection)

hunt=Label(the_hunt,font=('Arial',8,'bold'),width=20)
quest_monster=Label(the_hunt,text="Your rolled hunt\nwill go here!") #Label before any hunt is rolled.

wep_lbl=Label(the_hunt,text="\n",font=('Arial',8,'bold'))
wep_roll=Label(the_hunt,text="\n")

bud_lbl=Label(the_hunt,text="\n",font=('Arial',8,'bold'))
bud_roll=Label(the_hunt,text="\n\n")

#Monster Icons
default_icon=PhotoImage(file='icons/Unknown.png')
ico=Label(window,image=default_icon)

#Command
def rolltime():
  monster=random.choice(monsters.get(quest_choice.get()))
  new_icon=PhotoImage(file='icons/'+monster+'.png')
  ico.configure(image=new_icon)
  ico.image=new_icon
  hunt.configure(text="\n"+quest_choice.get()+":")
  quest_monster.configure(text=monster)
    
  if wep.get()==1:
    wep_lbl.configure(text="Weapon:")
    wep_roll.configure(text=random.choice(weapons))
    
  elif bud.get()==1 and wep.get()==0:
    wep_lbl.configure(text="")
    wep_roll.configure(text="")
    
  else:
    wep_lbl.configure(text="")
    wep_roll.configure(text="\n")
    
  if bud.get()==1:
    bud_lbl.configure(text="Buddies:")
    bud_roll.configure(text=random.choice(teams))
    
  else:
    bud_lbl.configure(text="")
    bud_roll.configure(text="\n")
    
roll_hunt.configure(command=rolltime)

#Packing time!!!
selection.pack(pady=2,padx=2,side=LEFT)
choose.pack()
wep_check.pack()
team_check.pack()
roll_hunt.pack(pady=3)
the_hunt.pack(pady=3)
hunt.pack()
quest_monster.pack()
wep_lbl.pack(pady=1)
wep_roll.pack()
bud_lbl.pack(pady=1)
bud_roll.pack()
ico.pack(side=RIGHT)

window.mainloop() #Opens the window!