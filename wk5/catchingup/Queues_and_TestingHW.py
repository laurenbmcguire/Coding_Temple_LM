class Node:
                                                        #Initialize node object
    def __init__(self, element):
        self.element = element                          # Assign element value
        self.next = None                                # Initialize next as null
        self.prev = None                                # Initialize prev as null
        
class Queue:                                                 
   
                                                        # Function to initialize queue
    def __init__(self):
        self.frontofLine = None
        self.last= None
           
   
                                                        # Enqueue element
    def enqueue(self, element):
        if self.last is None:                           #If there's no element 
            self.frontofLine = Node(element)            #The front of the line of the queue is formed
            self.last = self.frontofLine                #make the last element the front of the line
        else:
            self.last.next = Node(element)              #node after the back of the line 
            self.last.next.prev=self.last               #node for next node 
            self.last = self.last.next                  #node for element that is ahead in the line
               
               
                                                        #  Function to dequeue 
    def dequeue(self):
   
        if self.frontofLine is None:                    #if there's no front of the line, return nothing
            return None
        else:
            frontOfLineValue = self.frontofLine.element               #value of the front of the line holds the data of the first element
            self.frontofLine = self.frontofLine.next                  #second element is not first element
            self.frontofLine.prev = None                                #the "next" of the new front of the line is now none
            return frontOfLineValue                                   #return the value of the orinigial first element
   
   

   
                                                        # Function to print the queue 
    def printqueue(self):
           
        sentence = ("People in your queue are:")
        frontOfLine=self.frontofLine                    #get the front of the line of the queue
        while frontOfLine is not None:                  #if it's not none
            name = (frontOfLine.element)         #print the element of the front of the line
            sentence = sentence + name + ", "
            frontOfLine=frontOfLine.next                #make the next item the front of the line until it's none
        return sentence
           

   
class Main:
    def run(self):
        queue = Queue()
        decision =""
        while decision != "9":
            decision = input("Would you like to enqueue, dequeue or see the queue? Click 9 to exit ").lower()
            if decision == "enqueue":
                queue.enqueue(input("Who are we adding to the list? "))
            elif decision == "dequeue":
                queue.dequeue()
            elif decision == "see the queue":
                print(queue.printqueue())
            elif decision == "9":
                break