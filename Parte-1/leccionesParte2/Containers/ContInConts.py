


lists = []

Rap = ["Migos","JuL","Eminem","Drake","2 Pac"]

Hard_Techno = ["Shlømo","I Hate Models","Parfait","Clara Cuvé","Nastia","SNTS"]

Funk = ["Aretha Franklyn","Funckadellic","Luther Vandross","Gwen McCrae"]

DrumandBass = ["Dj Marky","LSB","Sub Focus"]


lists.append(Rap)
lists.append(Hard_Techno)
lists.append(Funk)
lists.append(DrumandBass)



Rap.append("Snoop Dogg")
print("This is a rap list:      ", Rap)
print("This is a Funky list                     ", lists[2])

locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 876298)

locations.append(la)
locations.append(chicago)

print("Here you cansee the coordinates of Los Angeles and Chicago respectively:         ", locations)

eights = ["Edgar Allan Poe","Charles Dickens"]
nines = ["Hemingway","Orwell","Fitzergald"]

authors = (eights,nines)

print("and these are some authors:      ", authors)



bday = {"Hemingway": "7/21/1899","Fitzergald":"9/24/1896"}

tuple_bday = (bday,)
print("Some where born:     ",tuple_bday)

ny = {"location":(40.7128,740059),

    "celebrities":["W. Allen","Jay Z","K. Bacon"],
    
    "facts":{"state":"NY","country":"United States"}
    }

print("These are some New York Celebrities:     ",ny["celebrities"])