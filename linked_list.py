# -*- coding: utf8 -*-


import time
from data_structure import LinkedList


class AnimalShelter:
    """
    3.7, 用链表模仿宠物收容所
    """

    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def add_dog(self, name):
        data = (name, time.time())
        self.dogs.add_last(data)

    def add_cat(self, name):
        data = (name, time.time())
        self.cats.add_last(data)

    def adopt_any(self):
        dog = self.dogs.peek_first()
        cat = self.cats.peek_first()
        if dog[1] < cat[1]:
            return self.adopt_dog()
        else:
            return self.adopt_cat()

    def adopt_dog(self):
        return self.dogs.remove_first()

    def adopt_cat(self):
        return self.cats.remove_first()


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.add_dog('d1')
    shelter.add_cat('c1')
    shelter.add_cat('c2')
    shelter.add_cat('c3')
    shelter.add_dog('d2')
    shelter.add_dog('d3')
    print(shelter.adopt_cat())
    print(shelter.adopt_any())
    print(shelter.adopt_dog())
    shelter.cats.print_list()
    shelter.dogs.print_list()
