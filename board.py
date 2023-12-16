"""
This will contain the risk board
"""
import territory
import continent as c


class board():

    def __init__(self, continentsId = None, map = None) -> None:
        
        print("Creating Board")
        self.create_board(continentsId, map)

        


    #creates board and if not given both continents and a map with default to basic risk map
    def create_board(self, continentsId = None, map = None):
        if continentsId == None or map == None:
            print("default risk map")

            self.continentsId = [c.continent(5, "North America"),
                    c.continent(2, "South America"),
                    c.continent(3, "Africa"),
                    c.continent(5, "Europe"),
                    c.continent(7, "Asia"),
                    c.continent(2, "Oceania")]
            
            #This is a dictionary of {name : [countinentId, [link territories]]}
            self.map = {"Alaska" : [0, ["Kamchatka","Northwest Territory", "Alberta"]],
                "Alberta" : [0, ["Alaska", "Northwest Territory", "Ontario", "Western United States"]],
                "Northwest Territory" : [0, ["Alaska", "Alberta", "Greenland", "Ontario"]],
                "Greenland" : [0, ["Northwest Territory", "Quebec", "Ontario", "Iceland"]],
                "Quebec" : [0, ["Greenland", "Ontario", "Eastern United States"]],
                "Ontario" : [0, ["Alberta", "Northwest Territory", 
                                    "Greenland", "Quebec", "Eastern United States",
                                    "Western United States"]],
                "Eastern United States" : [0, ["Quebec", "Ontario", "Western United States",
                                                "Central America"]],
                "Western United States" : [0, ["Alberta", "Ontario", "Eastern United States",
                                                "Central America"]],
                "Central America" : [0, ["Western United States", "Eastern United States",
                                            "Venezuela"]],
                "Venezuela" : [1, ["Central America", "Peru", "Brazil"]],
                "Brazil" : [1, ["Venezuela", "Peru", "Argentina", "North Africa"]],
                "Peru" : [1, ["Venezuela", "Brazil", "Argentina"]],
                "Argentina" : [1, [ "Brazil", "Peru"]],
                "North Africa" : [2, ["Brazil", "Egypt", "East Africa", "Congo", "Western Europe", 
                                    "Southern Europe"]],
                "Congo" : [2, ["North Africa", "East Africa", "Congo", "South Africa"]],
                "South Africa" : [2, ["East Africa", "Congo", "Madagascar"]],
                "Madagascar" : [2, ["East Africa", "South Africa"]],
                "East Africa" : [2, ["Madagascar", "South Africa", "Congo", "North Africa",
                                    "Middle East", "Egypt"]],
                "Egypt" : [2, ["Southern Europe", "North Africa", "Middle East", "East Africa"]],
                "Iceland" : [3, ["Greenland", "Great Britain", "Scandinavia"]],
                "Scandinavia" : [3, ["Ukraine", "Northern Europe", "Great Britain", "Iceland"]],
                "Ukraine" : [3, ["Scandinavia", "Northern Europe", "Southern Europe", "Ural", 
                                "Afghanistan", "Middle East"]],
                "Great Britain" : [3, ["Iceland", "Scandinavia", "Northern Europe",
                                    "Western Europe"]],
                "Northern Europe" : [3, ["Southern Europe", "Scandinavia", "Ukraine", 
                                        "Great Britain", "Western Europe"]],
                "Southern Europe" : [3, ["Northern Europe", "Western Europe", "Ukraine", "Egypt", 
                                        "Middle East", "North Africa"]],
                "Western Europe" : [3, ["North Africa", "Great Britain", "Southern Europe",
                                        "Northern Europe"]],
                "Siam" : [4, ["Indonesia", "China", "India"]],
                "India" : [4, ["Middle East", "Afghanistan", "China", "Siam"]],
                "China" : [4, ["Siam", "India", "Afghanistan", "Ural", "Siberia", "Mongolia"]],
                "Mongolia" : [4, ["China", "Siberia", "Irkutsk", "Kamchatka", "Japan"]],
                "Japan" : [4, ["Kamchatka", "Mongolia"]],
                "Irkutsk" : [4, ["Mongolia", "Siberia", "Yakutsk", "Kamchatka"]],
                "Middle East" : [4, ["East Africa", "Southern Europe", "Egypt", "Ukraine",
                                    "India", "Afghanistan"]],
                "Ural" : [4, ["Ukraine", "Afghanistan", "Siberia","China"]],
                "Afghanistan" : [4, ["Ukraine", "Ural", "China", "India", "Middle East"]],
                "Siberia" : [4, ["Yakutsk", "Irkutsk", "Mongolia", "China", "Ural"]],
                "Kamchatka" : [4, ["Alaska", "Yakutsk", "Irkutsk", "Mongolia", "Japan"]],
                "Yakutsk" : [4, ["Siberia", "Irkutsk", "Kamchatka"]],
                "Indonesia" : [5, ["Siam", "New Guinea", "Western Australia"]],
                "New Guinea" : [5, ["Indonesia", "Western Australia", "Eastern Australia"]],
                "Western Australia" : [5, ["Indonesia", "New Guinea", "Eastern Australia"]],
                "Eastern Australia" : [5, ["New Guinea", "Western Australia"]]
                }

            return
        else:
            self.continentsId = continentsId
            self.map = map
            return

    def check_map_is_nondirectional(self, map):
        for t in map:
            for i in map[t][1]:
                print(t)
                print(map[i][1])
                if t in map[i][1]:
                    pass
                else:
                    print("invalid " + i + " is missing " + t)
                    return False
        
        return True

