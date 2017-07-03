##
# Created by: Curtis Szmania
# Date: 7/2/2017
# Initial Creation.
# MEGA account class. Used for MEGA account details.
###

from logging import getLogger
from .lib import Lib
from os import path

__author__ = 'szmania'

SCRIPT_DIR = path.dirname(path.realpath(__file__))

class Account(object):
    def __init__(self, username, password, logLevel='DEBUG'):
        """
        Library for ffmpeg converter and encoder interaction.

        Args:
            username (str): MEGA account user name
            password (str): MEGA account password
            logLevel (str): Logging level setting ie: "DEBUG" or "WARN"
        """

        self.__username = username
        self.__password = password
        self.__logLevel = logLevel

        self.__lib = Lib(logLevel=logLevel)


    @property
    def username(self):
        """
        Getter for MEGA account username.

        Returns:
            String: Returns MEGA account username
        """

        logger = getLogger('SyncProfile.username')
        logger.setLevel(self.__logLevel)

        return self.__username

    @username.setter
    def username(self, value):
        """
        Setter for MEGA account username.

        Args:
            value (str): value to set username to.
        """

        logger = getLogger('SyncProfile.username')
        logger.setLevel(self.__logLevel)

        self.__uername = value

