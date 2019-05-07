# -*- coding: utf8 -*-

"""
method resolution order

https://makina-corpus.com/blog/metier/2014/python-tutorial-understanding-python-mro-class-search-path
https://www.python.org/download/releases/2.3/mro/

each time a class is found in built search path, Python asked the question « Is it a good head ? »
and if not, it removes the class from the final search path.
So, what is a « good head »?
A class is said as being a « good head » if there is no other class in the tail of the search path which inherits from it.
In this case it is more natural to use the method defined by its derived class.

6
                         ---
Level 3                 | O |                  (more general)
                      /  ---  \
                     /    |    \                      |
                    /     |     \                     |
                   /      |      \                    |
                  ---    ---    ---                   |
Level 2        3 | D | 4| E |  | F | 5                |
                  ---    ---    ---                   |
                   \  \ _ /       |                   |
                    \    / \ _    |                   |
                     \  /      \  |                   |
                      ---      ---                    |
Level 1            1 | B |    | C | 2                 |
                      ---      ---                    |
                        \      /                      |
                         \    /                      \ /
                           ---
Level 0                 0 | A |                (more specialized)
                           ---

L[O] = O
L[D] = D O
L[E] = E O
L[F] = F O
L[B] = B + merge(DO, EO, DE) = B D E O
L[C] = C + merge(DO,FO,DF)
     = C + D + merge(O,FO,F)
     = C + D + F + merge(O,O)
     = C D F O
L[A] = A + merge(BDEO,CDFO,BC)
     = A + B + merge(DEO,CDFO,C)
     = A + B + C + merge(DEO,DFO)
     = A + B + C + D + merge(EO,FO)
     = A + B + C + D + E + merge(O,FO)
     = A + B + C + D + E + F + merge(O,O)
     = A B C D E F O


6
                          ---
Level 3                  | O |
                       /  ---  \
                      /    |    \
                     /     |     \
                    /      |      \
                  ---     ---    ---
Level 2        2 | E | 4 | D |  | F | 5
                  ---     ---    ---
                   \      / \     /
                    \    /   \   /
                     \  /     \ /
                      ---     ---
Level 1            1 | B |   | C | 3
                      ---     ---
                       \       /
                        \     /
                          ---
Level 0                0 | A |
                          ---
"""


class F:
    def who_am_i(self):
        print("I am a F")


class E:
    def who_am_i(self):
        print("I am a E")


class D:
    def who_am_i(self):
        print("I am a D")


class C(D, F):
    def who_am_i(self):
        print("I am a C")


class B(E, D):
    def who_am_i(self):
        print("I am a B")


class A(B, C):
    def who_am_i(self):
        print("I am a A")


if __name__ == '__main__':
    print(A.mro())
