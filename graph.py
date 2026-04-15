from node import Node
from edge import Edge

class Graph:
    def __init__(self,id="grafo", directed=False, auto=False):
        """
        Constructor
        """
        self.id=id
        self.nodes={}
        self.edges={}
        self.directed= directed
        self.auto=auto


    def addNode(self, id):
        """
        Agrega nodo al grafo, en caso de que no exista lo crea, si existe, regresa el nodo
        encontrado en el diccionario
        :param id= Node Id
        :return: node
        """
        new_node=self.nodes.get(id)
        if new_node is None:
            new_node=Node(id)
            self.nodes[new_node.id]=new_node
        return new_node

    def addEdge(self, source, target):
        """
        Agregar una arista al grafo, los nodos deben ser agregados con anterioridad, si no,
        levanta una excepcion
        :param source: Node source
        :param target: Node target
        """

        #Si los nodos no se encuentran en el grafo, levantar excepcion
        if self.nodes.get(source) is None or self.nodes.get(target) is None:
            raise Exception("Nodes are not in the graph, please add them to the graph")

        #nodos en grafo
        nodeSource=self.nodes[source]
        nodeTarget=self.nodes[target]

        #crear el id de la arista
        idAux=str(source)+' -> '+str(target)

        #Si el grafo es no dirigido, checar que no se repitan los vertices en el diccionario
        repeated=False
        autoAux=False
        if not self.directed:
            idAuxNotDirected=str(target) + ' -> ' +str(source)
            aux=self.edges.get(idAuxNotDirected)
            if not(aux is None):
                repeated=True
        
        #Si el grafo es no autociclico, checar que source y target no sean iguales
        if not self.auto:
            if source is target:
                #print(source, target)
                autoAux=True
        
        new_edge= self.edges.get(idAux)
        
        """
        chequeo para grafo no dirigido y no autociclico.
        si la arista es nueva (no se encuentra en el grafo) y los nodos no son repetidos
        agrega nueva arista
        """
        if new_edge is None and repeated is False and autoAux is False:
            new_edge= Edge(idAux, nodeSource, nodeTarget)
            self.edges[new_edge.id]=new_edge
            nodeSource.attr.get("neighbors").append(nodeTarget)
            nodeTarget.attr.get("neighbors").append(nodeSource)
            nodeSource.attr.get("edges").append(new_edge)
            nodeTarget.attr.get("edges").append(new_edge)
            
        return new_edge


    def getDegree(self, id):
        """
        Obtener el grado de nodo
        :param: id: Node id
        :return: Node degree
        """
        node=self.nodes.get(id)
        if node is None:
            return 0
        return len(node.attr["neighbors"])
    
    def getNode(self, id):
        """
        Encontrar nodo en el grafo
        :param id: Node id to find
        :return: found node
        """
        return self.nodes.get(id)

    def getTotalNodes(self):
        """
        Obtener el total de nodos en el grafo
        :return: total nodes
        """
        nodes=self.nodes
        if nodes is None:
            return 0
        return len(self.nodes)
    
    def getTotalEdges(self):
        """
        Obtener el total de aristas del grafo
        :return: total edges
        """
        edges=self.edges
        if edges is None:
            return 0
        return len(self.edges)

    def saveGV(self):
        """
        Crea el archivo .gv que posteriormente sera usado para la creacion de los grafos
        :return: total edges
        """

        #creacion del string gv
        graph=''
        graph+='digraph '+self.id+' {\n'
        
        for nodo in self.nodes:
            graph+=str(nodo)+';\n'

        for key, value in self.edges.items():
            graph+= value.id+';\n'

        graph+='}'

        #se escribe y salva el archivo
        name=self.id+'.gv'
        file = open(name, "w")
        file.write(graph)
        file.close()
        #se imprime q el file fue creado para saber cuando termina
        print('File GraphViz: '+name+' was created\n')
    
    #Proyecto 2 (BFS, DFS iterativo y DFS recursivo)
    
    #BFS
    def BFS(self,s):
        """
        BFS
        :param s: nodo raiz
        """
        try:
            name = self.id + '_BFS_'+str(s)
            #Objeto grafo bfs
            bfsGraph = Graph(name)
            #Fila para el algoritmo BFS
            queue = []
            #Obtener objeto nodo a partir de nodo raiz
            s=self.nodes[s]
            # Agreagr nodo a la fila 
            queue.append(s)
            #Poner al nodo como visitado
            s.attr["visitedBFS"] = True
            #Agregar nodo a grafo BFS
            bfsGraph.addNode(s.id) 
            #Mientras encuentre nodos en la fila
            while queue: 
                #Sacar el primer objeto nodo de la fila 
                s = queue.pop(0)               
                #Obtener los vecinos del nodo s
                neighbors = s.attr["neighbors"]
                #Iterar los vecinos del nodo s
                for nodeNeighbor in neighbors:
                    #Si el nodo aún no ha sido visitado
                    if not (nodeNeighbor.attr["visitedBFS"]):
                        #Agregar nodo a la fila
                        queue.append(nodeNeighbor)
                        #Poner al nodo como visitado
                        nodeNeighbor.attr["visitedBFS"] = True
                        #Agregar nodo a grafo BFS
                        bfsGraph.addNode(nodeNeighbor.id) 
                        #Agregar arista a grafo BFS
                        bfsGraph.addEdge(s.id,nodeNeighbor.id) 
            return bfsGraph
        except:
            print("Por favor agrega un nodo raiz valido")


    #DFS iterativo
    def DFS_I(self,s):
        """
        DFS iterativo
        :param s: nodo raiz
        """
        try:              
            name =  self.id +'_DFS_I_'+str(s)
            #Generar objeto grafo
            dfs_i_Graph = Graph(name)
            # Pila para el algoritmo DFS
            stack = []
            #Obtener objeto nodo a partir de nodo raiz
            s=self.nodes[s]
            #Agregar nodo a la pila
            stack.append(s)
            #agregar nodo s al grafo DFSI
            dfs_i_Graph.addNode(s.id)
            while stack:
                # Remover un elemento de la pila y asignarlo a s
                s = stack.pop()
                # Si no ha sido visitado marcarlo como visitado
                if not s.attr["visitedDFSI"]:
                    s.attr["visitedDFSI"] = True
                #Obtener los vecinos del nodo s
                neighbors = s.attr["neighbors"]
                #Iterar vecinos
                for neighbor in neighbors:
                    # Si un vecino no ha sido visitado, entrar
                    if not neighbor.attr["visitedDFSI"]:
                        #Agregar nodo al grafo DFSI
                        dfs_i_Graph.addNode(neighbor.id)
                        #Agregar nodo a la pila
                        stack.append(neighbor)
                        #Agregar el nodo raiz del actual nodo al atributo rootNodeDFSI 
                        neighbor.attr["rootNodeDFSI"]=s.id
                        ##dfs_i_Graph.addEdge(s.id,neighbor.id)
            #Iterar nodos para agregar aristas a los nodos
            for key, node in self.nodes.items():
                if node.attr["rootNodeDFSI"]>-1:
                    #Agregar arista
                    dfs_i_Graph.addEdge(key,node.attr["rootNodeDFSI"])
            return dfs_i_Graph
        except:
            print("Por favor agrega un nodo raiz valido")


    #DFS recursivo
    def DFS_R(self,s):
        """
        DFS recursivo usuario
        :param s: nodo raiz
        """
        try: 
            name = self.id +'_DFS_R_'+str(s)
            #Generar objeto grafo
            dfs_r_Graph = Graph(name)
            # Crear un conjunto de nodos visitados vacio
            visited = set()
            #Obtener objeto nodo a partir de nodo raiz
            s=self.nodes[s]
            # Llamar la funcion recursiva dfsRecursive
            self.dfsRecursive(visited,s,dfs_r_Graph)
            return dfs_r_Graph
        except:
            print("Por favor agrega un nodo raiz valido")

    def dfsRecursive(self,visited,node,dfs_r_Graph):
        """
        Auxiliar DFS recursivo 
        :param visited: nodos visitados
        :param node: nodo a trabajar
        :param dfs_r_Graph: grafica final
        """
        # Marcar el nodo como visitado
        visited.add(node.id)
        #Agregar nodo a grafo DFS    
        dfs_r_Graph.addNode(node.id) 
        #Obtener los vecinos del nodo s
        neighbors = node.attr["neighbors"]

        #Recorrer de manera recursiva los vecinos del nodo
        for neighbor in neighbors:
            #Si nodo no esta en el conjunto visitado
            if neighbor.id not in visited:
                #llamer recursivamente a dfsRecursive
                self.dfsRecursive(visited, neighbor, dfs_r_Graph)
                #Agregar arista
                dfs_r_Graph.addEdge(node.id,neighbor.id)