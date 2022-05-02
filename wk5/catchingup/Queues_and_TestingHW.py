class Node:
    def __init__(self, element):
        self.element = element                          
        self.next = None                               
        self.prev = None                                
class Queue:

    def __init__(self):
        self.frontofLine = None
        self.last = None

    def enqueue(self, element):
        if self.last is None:  
            self.frontofLine = Node(element)
            self.last = self.frontofLine  
        else:
            self.last.next = Node(element) 
            self.last.next.prev = self.last  
            self.last = self.last.next  

    def dequeue(self):

        if self.frontofLine is None:  
            return None
        else:
            frontOfLineValue = self.frontofLine.element
            self.frontofLine = self.frontofLine.next  
            self.frontofLine.prev = None  
            return frontOfLineValue 

    def printqueue(self):

        sentence = ("The people in queue are: ")
        frontOfLine = self.frontofLine 
        while frontOfLine is not None:  # if it's not none
            # print the element of the front of the line
            name = (frontOfLine.element)
            sentence = sentence + name + ", "
            # make the next item the front of the line until it's none
            frontOfLine = frontOfLine.next
        return sentence


class Main:
    def run(self):
        queue = Queue()
        decision = ""
        while decision != "quit":
            decision = input(
                "User, woule you like to enqueue, to dequeue or to see your queue? Type 'quit' to exit ").lower()
            if decision == "enqueue":
                queue.enqueue(input("Who would you like to add to the list "))
            elif decision == "dequeue":
                queue.dequeue()
            elif decision == "see your current queue":
                print(queue.printqueue())
            elif decision == "quit":
                break
