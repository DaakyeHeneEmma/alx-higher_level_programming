#!/usr/bin/python3



class Square:


    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        return self.__size**2

    def __eq__(self, o):

        return self.__size == o.__size

    def __ne__(self, o):

        return self.__size != o.__size

    def __gt__(self, o):

        return self.__size > o.__size

    def __ge__(self, o):

        return self.__size >= o.__size

    def __lt__(self, o):

        return self.__size < o.__size

    def __le__(self, o):

        return self.__size <= o.__size
