##
# Created by: Curtis Szmania
# Date: 7/2/2017
# Initial Creation.
# Sync Profile class. Used for sync profile data.
###

from account import Account
from logging import getLogger
from os import path

__author__ = 'szmania'

SCRIPT_DIR = path.dirname(path.realpath(__file__))

class SyncProfile(Account):
    def __init__(self, profileName, username, password, localRoot, remoteRoot, logLevel='DEBUG'):
        """
        Library for ffmpeg converter and encoder interaction.

        Args:
            profileName (str): Unique profile name
            username (str): MEGA account user name
            password (str): MEGA account password
            localRoot (str): MEGA account localRoot
            remoteRoot (str): MEGA account remoteRoot
            logLevel (str): Logging level setting ie: "DEBUG" or "WARN"
        """

        super(SyncProfile, self).__init__(username=username, password=password, logLevel=logLevel)

        self.__profileName = profileName
        self.__localRoot = localRoot
        self.__remoteRoot = remoteRoot

    @property
    def localRoot(self):
        """
        Getter for local root.

        Returns:
            String: Returns local root
        """

        logger = getLogger('SyncProfile.localRoot')
        logger.setLevel(self.__logLevel)

        return self.__localRoot

    @localRoot.setter
    def localRoot(self, value):
        """
        Setter for local root.

        Args:
            value (str): value to set local root to.
        """

        logger = getLogger('SyncProfile.localRoot')
        logger.setLevel(self.__logLevel)

        self.__localRoot = value

    @property
    def profileName(self):
        """
        Getter for profile name.

        Returns:
            String: Returns profile name
        """

        logger = getLogger('SyncProfile.profileName')
        logger.setLevel(self.__logLevel)

        return self.__profileName

    @profileName.setter
    def profileName(self, value):
        """
        Setter for profile name.

        Args:
            value (str): value to set profile name to.
        """

        logger = getLogger('SyncProfile.profileName')
        logger.setLevel(self.__logLevel)

        self.__profileName = value