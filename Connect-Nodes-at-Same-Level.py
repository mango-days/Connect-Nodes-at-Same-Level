# binary tree insertion

class Node :
    def __init__ ( self , data ) :
        self.left = None
        self.data = data
        self.right = None
        self.next = None

class BinaryTree :
    def __init__ ( self ) : self.root = None
    
    def insert ( self , data ) :
        if self.root == None :
            self.root = Node ( data )
            return
        
        temp = self.root
        q = [ temp ]
        index = 0
        while index != len ( q ) :
            
            if temp == None : 
                temp = Node ( data )
                return
        
        
            if temp.left : q.append ( temp.left )
            else :
                temp.left = Node ( data )
                return
            
            if temp.data == data : return # data exists

            if temp.right : q.append ( temp.right )
            else : 
                temp.right = Node ( data )
                return
            
            index += 1
            temp = q [ index ]
            
        print ( " something unfathomable happened! " )
        return

    def printList ( self , node ) :
        if node == None : return
        if node.left : self.printList ( node.left )
        if node.data : print ( node.data ) #data exists
        if node.right : self.printList ( node.right )
        return
    
    def ConnectNodesAtSameLevel ( self , node ) :
        if node == None : return
        if node.right == None : pass
        if node.left and node.right : 
            node.left.next = node.right
            self.ConnectNodesAtSameLevel ( node.left )
        if node.right : 
            self.ConnectNodesAtSameLevel ( node.rightt )
        return
    
    def PrintNodesAtSameLevel ( self , node ) :
        if node == None : return
        if node.left : self.PrintNodesAtSameLevel ( node.left )
        if node.data : 
            print (" ")
            print ( node.data )
            if node.next : print ( "---" , node.next.data )
            else : print ( "--- None" )
        if node.right : self.PrintNodesAtSameLevel ( node.right )
        return

Obj = BinaryTree ()
arr = [ 1 , 2 , 3 , 4 , 5 ]
for index , value in enumerate ( arr ) : Obj.insert ( value )
# Obj.printList ( Obj.root )

Obj.ConnectNodesAtSameLevel ( Obj.root )
Obj.PrintNodesAtSameLevel ( Obj.root )
