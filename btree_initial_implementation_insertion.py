class BNode:
    def __init__(self,leaf=False):
        self.leaf=leaf
        self.parent=None
        self.keys=[]
        self.children=[]
class BTree:
    def __init__(self,deg):
        self.root=BNode(True)
        self.deg=deg
    def insert(self,val):
        pos,i=self.find(val)
        if len(pos.keys)==self.deg-1:

            self.split(pos,val)

        else:
            # i=0
            # while i<len(pos.keys) and val<pos.keys[i]:
            #     i+=1
            pos.keys.insert(i,val)
    def split(self,pos,val=None): 
        if val!=None:
            i=0
            while i<len(pos.keys) and val>pos.keys[i]:
                i+=1
            pos.keys.insert(i+1,val)
        mid=pos.keys[len(pos.keys)//2]
        
        if pos.parent!=None: 
            
            if len(pos.parent.keys)<self.deg-1:
                # if val!=None:
                i=0
                while i<len(pos.parent.keys) and mid>pos.parent.keys[i]:
                    i+=1
                pos.parent.keys.insert(i+1,mid)
            
                a=BNode(pos.leaf)
                a.keys=pos.keys[0:len(pos.keys)//2]
                a.children=pos.children[0:len(pos.children)//2]
                a.parent=pos.parent

                b=BNode(pos.leaf)
                b.keys=pos.keys[(len(pos.keys)//2)+1:len(pos.keys)]
                b.children=pos.children[(len(pos.children)//2):len(pos.children)]
                b.parent=pos.parent

                index=pos.parent.children.index(pos)
                pos.parent.children[index]=a
                pos.parent.children.insert(index+1,b)
                # pos.parent.keys.remove(mid)
            else:
                i=0
                while i<len(pos.parent.keys) and mid>pos.parent.keys[i]:
                    i+=1
                pos.parent.keys.insert(i+1,mid)
                mid=pos.parent.keys[len(pos.parent.keys)//2]
                self.childsplit(pos)
                self.split(pos.parent)
        else:
            par=BNode()
            if pos==self.root:
                self.root=par

            a=BNode(True)
            a.keys=pos.keys[0:len(pos.keys)//2]
            a.children=pos.children[0:len(pos.children)//2]
            a.parent=par

            b=BNode(True)
            b.keys=pos.keys[(len(pos.keys)//2)+1:len(pos.keys)]
            b.children=pos.children[(len(pos.children)//2):len(pos.children)]
            b.parent=par

            par.keys.append(mid)

            par.children.append(a)
            par.children.append(b)
    
    def childsplit(self,pos):
                a=BNode(pos.leaf)
                a.keys=pos.keys[0:len(pos.keys)//2]
                a.children=pos.children[0:len(pos.children)//2 ]
                a.parent=pos.parent

                b=BNode(pos.leaf)
                b.keys=pos.keys[(len(pos.keys)//2)+1:len(pos.keys)]
                b.children=pos.children[(len(pos.children)//2):len(pos.children)]
                b.parent=pos.parent

                index=pos.parent.children.index(pos)
                pos.parent.children[index]=a
                pos.parent.children.insert(index+1,b)

    def find(self,item,pos=None):
        if pos==None:
            pos=self.root
        i=0
        while i<len(pos.keys) and item>pos.keys[i]:
            i+=1
        if i<len(pos.keys) and item==pos.keys[i]:
            return pos,i
        elif len(pos.children)>0:
            return self.find(item,pos.children[i])
        return pos,i
    def display(self,pos=None,lev=0):
        if pos==None:
            pos=self.root
        print("Level",lev,end=":")
        for i in pos.keys:
            print(i,end=" ")
        print("\n")
        lev+=1
        if len(pos.children)>0:
            for j in pos.children:
                self.display(j,lev)
b=BTree(3)
print(b.find(12))
b.insert(2)
b.insert(13)
b.insert(25)
b.insert(26)
b.insert(12)
b.insert(27)
b.insert(28)
b.insert(29)
b.display()