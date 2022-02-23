## @file Shape.py
#  @author Mark Procopio 400344315
#  @brief Shape interface module
#  @date Feb 12, 2021

from abc import ABC, abstractmethod

class Shape(ABC):
    # @brief Shape Interface module
    ## @details The method in the interface are abstract and need to be
    #  overridden by the modules that inherit this interface

    # @brief x centermass abstractmethod
    # @return pass
    @abstractmethod
    def cm_x(self):
        pass
    
    # @brief y centermass abstractmethod
    # @return pass
    @abstractmethod
    def cm_y(self):
        pass

    # @brief mass abstractmethod
    # @return pass
    @abstractmethod
    def mass(self):
        pass

    # @brief m_inert abstractmethod
    # @return pass
    @abstractmethod
    def m_inert(self):
        pass