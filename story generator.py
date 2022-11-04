import random
person=["brother","friend","sister","cousin"]
place=["Dubai","Delhi","Rajasthan","TamilNadu"]
adj=["hot","plesent","nice","warm"]

someplace=["Dubai","Delhi","Rajasthan","TamilNadu"]
hasmany=["beaches","parks","hotels",""]
goto=["the mountains","the seas ","forests"]
actionverb=["for hiking","for surfing"]
pluralnoun=["dolphins","skeying","boating"]
eat=["Dark Green Vegetables","Cakes","Kofta","Biryani"]
likketo=["play football","play batmintin","play tabletenis"]
print("last summer, my mom and dad took me and ",random.choice(person),"on a trip to",random.choice(place),".the weather is very",random.choice(adj),"nothern ",random.choice(someplace),"has many",random.choice(hasmany),"many people go to",random.choice(goto)," to ",random.choice(actionverb),
    "or see the ",random.choice(pluralnoun),"the people that live there love to eat",random.choice(eat),"they also like to ",random.choice(likketo) )