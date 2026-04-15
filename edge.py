class Edge:

    def __init__(self, id, source, target):
        """
        Constructor
        :param source: source node
        :param target: target node
        :param id: edge id
        """
        self.source=source
        self.target=target
        self.id=id
    
    def __str__(self):
        """
        convert edge to str
        :return: edge textual representation
        """
        return str(self.id)