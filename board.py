"""
This will contain the risk board
"""
import territory as terr
import continent as c
import player as play
import random

class board():

    def __init__(self, continentsId = None, map = None, player = ["red", "blue"]) -> None:
        
        print("Creating Board")
        self.create_board(continentsId, map)

        self.player = []
        for p in player:
            self.player.append(play.player(p))
        
        #This shuffle will determine turn order
        random.shuffle(self.player)
        self.turn = 0

        return

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

            #need to check what this does or if i made a mistake somewhere
            for i in self.map:
                self.map[i].append(terr.territory(i))
            return
        
        else:
            self.continentsId = continentsId
            self.map = map
            for t in self.map:
                self.map.append(terr.territory(t))

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

    #the purpose of this function is to search the map for strategic points
    #this is done by finding cycles with the highest troop income divided by links out of cycle
    #highest value cycle must come from areas with troop bonus (continents) else 
    #individual territories being 1
    #therefore finding the value of each continent then trying to find if a territory add will decrease links
    #in and increase the value of controlling the cycle
    def find_best_areas(self):
        
        #self.cycle = continentid to match index [[territories in cycle], {territory : links out}, 
        #[[links out],[boarder]]]
        self.cycles = [[[],{},[[],[]]] for _ in range(len(self.continentsId))]
        
        #start with the continents as the starting point for each cycle then optimize

        #go through each one of the territories (i) on the map
        for i in self.map:

            #add each territory to an individual continent for a cycle
            #self.cycle = continentid to match index [[territories in cycle], {territory : links out}, 
            #[[links out],[boarder]]]
            self.cycles[self.map[i][0]][0].append(i)

            #makes a empty list to hold links out of continent
            self.cycles[self.map[i][0]][1][i] = []
            
            #finds the links out of the continent
            # j is links out to the territory i
            for j in self.map[i][1]:
                #find the continent of j
                check = self.map[j][0]
                if check != self.map[i][0]:
                    #adds to list out for each continent
                    self.cycles[self.map[i][0]][1][i].append(j)


        for idx, c in enumerate(self.cycles):
            links_out, links_in = self.count_links(c)
            #self.cycle = continentid to match index [[territories in cycle], {territory : links out}, 
            #[[links out],[boarder]]]
            self.cycles[idx][2] = [[links_out], [links_in]]
            


            #optimize by checking to see if there is any strategic point that would decrease the number of
            #way to attack the cycle of territories
            unchanged = False
            while (unchanged == False):
                unchanged = True
                for l in links_out:
                    temp = c
                    temp.append([])
                    #add l to temp
                    temp[0].append(l)
                    temp[1][l] = []
                    for li in self.map[l][1]:
                        if not (li in temp[0]):
                            temp[1][l].append(li)
                    #check if by add l to c if temp is better than the original
                    c[2], c[3] = self.count_links(temp)
                    
                    if len(c[3]) < len(links_in):
                        #temp is better
                        temp[0] = list(set(temp[0]))
                        temp[2] = list(set(temp[2]))
                        temp[3] = list(set(temp[3]))                        
                        self.cycles[idx] = temp
                        c = self.cycles[idx]
                        unchanged = False
        return self.cycles
    

    # given a list cycle [[territories], {territory: link out}] this function will return the number of
    # links out of the cycle
    def count_links(self, cycle):
        links_out = []
        links_in = []

        # t is the name of the territory being evaluated
        for t in cycle[1]:
            #i is the name of the connecting territory
            for i in cycle[1][t]:
                #if i is not in the cycle then it must be out side the cycle
                #i is then added to links out and count
                if not ( i in cycle[0]):
                    links_out.append(i)
                    links_in.append(t)

                    #save territory that is on the edge of the cycle
                    if not (t in links_in):
                        links_in.append(t)

        return (links_out, links_in)

    
    #tries to make claim in best areas with least competition
    def claims_ai(self):
        pass
    
    def claims_human(self):
        pass
    
    def place_troops(self):
        pass

    def assign_starting_troops(self):
        pass
 
    def start_game(self):
        self.claims_ai()
        self.assign_starting_troops()
        self.place_troops()

        return
