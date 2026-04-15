class Node:

    def __init__(self,id):
        """
        Constructor
        :param id: node identifier
        """
        self.id=id
        self.attr = {
            "edges":[],
            "neighbors":[],
            "geoX_Y":[],
            "visitedBFS":False,
            "visitedDFSI":False,
            "rootNodeDFSI":-1
        }
    
    def __str__(self):
        """
        Convert node to str
        """
        return str(self.id) + str(self.attr["neighbors"])