class Location:     
    def __init__(self,radius):         
        self.radius = radius
        
    def myLocation(self):
        print("Hi, my name is " + self.name + "and I live in " + self.country + ".")

loc1 = Location("Tom","Belgium")
loc1.myLocation()
loc2= Location("Jon","NL")
loc3= Location("Lies","Cz")
loc2.myLocation()
loc3.myLocation()
your_loc = Location("Dec","Beglium")
your_loc.myLocation()
