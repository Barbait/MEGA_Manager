##
# Created by: Curtis Szmania
# Date: 7/2/2017
# Initial Creation.
# Sync Profile class. Used for sync profile data.
###

from account import Account
from logging import getLogger
from os import path
from pathMapping import PathMapping

__author__ = 'szmania'

SCRIPT_DIR = path.dirname(path.realpath(__file__))

class SyncProfile(Account):
    def __init__(self, profileName, username, password, rootMappings, logLevel='DEBUG'):
        """
        Library for ffmpeg converter and encoder interaction.

        Args:
            profileName (str): Unique profile name
            username (str): MEGA account user name
            password (str): MEGA account password
            rootMappings (list): dictionary of local and remote root mappings.
            logLevel (str): Logging level setting ie: "DEBUG" or "WARN"
        """

        Account.__init__(self, username=username, password=password, logLevel=logLevel)

        self.__profileName = profileName
        self.__rootMappings = rootMappings

        self.__local_usedSpace = None
        self.__remote_usedSpace = None

    @property
    def local_usedSpace(self):
        """
        Getter for MEGA profile local used space.

        Returns:
            String: Returns MEGA profile local used space
        """

        logger = getLogger('SyncProfile.local_usedSpace')
        logger.setLevel(self.__logLevel)

        return self.__local_usedSpace

    @local_usedSpace.setter
    def local_usedSpace(self, value):
        """
        Setter for MEGA profile local used space.

        Args:
            value (str): value to set profile local used space to.
        """

        logger = getLogger('SyncProfile.local_usedSpace')
        logger.setLevel(self.__logLevel)

        self.__local_usedSpace = value

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

    @property
    def remote_usedSpace(self):
        """
        Getter for MEGA profile remote used space.

        Returns:
            String: Returns MEGA profile remote  used space
        """

        logger = getLogger('SyncProfile.remote_usedSpace')
        logger.setLevel(self.__logLevel)

        return self.__remote_usedSpace

    @remote_usedSpace.setter
    def remote_usedSpace(self, value):
        """
        Setter for MEGA profile remote used space.

        Args:
            value (str): value to set profile remote used space to.
        """

        logger = getLogger('SyncProfile.remote_usedSpace')
        logger.setLevel(self.__logLevel)

        self.__remote_usedSpace = value

    def add_root_mapping(self, localRoot, remoteRoot):
        """
        Add root mapping to profile root mappings list.

        Args:
            localRoot (str): Local root of pair.
            remoteRoot (str): Remote root of pair.
        """

        logger = getLogger('SyncProfile.add_root_mapping')
        logger.setLevel(self.__logLevel)

        logger.debug(' Adding root mapping to profile.')

        try:
            pathMapObj = PathMapping(localPath=localRoot, remotePath=remoteRoot)
            self.__rootMappings[self.get_root_mappings_count()] = pathMapObj
            return True
        except Exception as e:
            logger.error(' Exception: %s' % str(e))
            return False

    def get_root_mapping_local_root(self, index=None):
        """
        Getter for profile local root path.

        Args:
            index (int): index of root mapping to get local root of.
        
        Returns:
            String: Returns local root path.
        """

        logger = getLogger('SyncProfile.get_root_mapping_local_root')
        logger.setLevel(self.__logLevel)
        
        logger.debug(' Returning root mapping local root path.')
        
        if index:
            if not index + 1 > len(self.__rootMappings):
                return self.__rootMappings[index].localPath
            else:
                logger.error(' Error, given index of "%d" is larger than root mappings list for profile.' % index)
                return None
        else:
            if len(self.__rootMappings) > 0:
                logger.debug(' No index given. Returning first item.')
                return self.__rootMappings[0].localPath
            else:
                logger.error(' Error, no root mappings exist for this profile!')
                return None

    def get_root_mapping_remote_root(self, index=None):
        """
        Getter for profile remote root path.

        Args:
            index (int): index of root mapping to get remote root of.

        Returns:
            String: Returns remote root path.
        """

        logger = getLogger('SyncProfile.get_root_mapping_remote_root')
        logger.setLevel(self.__logLevel)

        logger.debug(' Returning root mapping remote root path.')

        if index:
            if not index + 1 > len(self.__rootMappings):
                return self.__rootMappings[index].remotePath
            else:
                logger.error(' Error, given index of "%d" is larger than root mappings list for profile.' % index)
                return None
        else:
            if len(self.__rootMappings) > 0:
                logger.debug(' No index given. Returning first item.')
                return self.__rootMappings[0].remotePath
            else:
                logger.error(' Error, no root mappings exist for this profile!')
                return None

    def get_root_mappings_count(self):
        """
        Return root mappings list size.

        Returns:
            integer: size of root mappings list.
        """

        logger = getLogger('SyncProfile.get_root_mappings_count')
        logger.setLevel(self.__logLevel)

        return len(self.__rootMappings)

    def set_root_mapping_local_root(self, value, index=None):
        """
        Setter for profile local root path.

        Args:
            index (int): index of root mapping to set local root of.
            value (str): value to set local root to.
        """

        logger = getLogger('SyncProfile.set_root_mapping_local_root')
        logger.setLevel(self.__logLevel)

        logger.debug(' Setting root mapping local root path.')

        # if index:
        if not index + 1 > len(self.__rootMappings):
            self.__rootMappings[index].localPath = value
            return True
        else:
            logger.error(' Error, given index of "%d" is larger than root mappings list for profile.' % index)
            return False
        # else:
        #     if len(self.__rootMappings) > 0:
        #         logger.debug(' No index given. Adding new item.')
        #         self.__rootMappings[self.get_root_mappings_count()]['localRoot'] = value
        #         return True
        #     else:
        #         logger.error(' Error, no root mappings exist for this profile!')
        #         return False

    def set_root_mapping_remote_root(self, index, value):
        """
        Setter for profile remote root path.

        Args:
            index (int): index of root mapping to set remote root of.
            value (str): value to set remote root to.
        """

        logger = getLogger('SyncProfile.set_root_mapping_remote_root')
        logger.setLevel(self.__logLevel)

        logger.debug(' Setting root mapping remote root path.')

        if not index + 1 > len(self.__rootMappings):
            self.__rootMappings[index].remotePath = value
            return True
        else:
            logger.error(' Error, given index of "%d" is larger than root mappings list for profile.' % index)
            return False
        # else:
        #     if len(self.__rootMappings) > 0:
        #         logger.debug(' No index given. Adding new item.')
        #         self.__rootMappings[self.get_root_mappings_count()]['remoteRoot'] = value
        #         return True
        #     else:
        #         logger.error(' Error, no root mappings exist for this profile!')
        #         return False
        #         
                

