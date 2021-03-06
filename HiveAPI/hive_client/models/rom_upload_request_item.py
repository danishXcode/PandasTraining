# coding: utf-8

"""
    Hive OS API

    App API for Hive OS 2.0  # noqa: E501

    OpenAPI spec version: 2.1-beta
    Contact: brain@hiveos.farm
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class RomUploadRequestItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'gpus': 'list[object]',
        'rom_id': 'int',
        'force': 'bool',
        'reboot': 'bool'
    }

    attribute_map = {
        'gpus': 'gpus',
        'rom_id': 'rom_id',
        'force': 'force',
        'reboot': 'reboot'
    }

    def __init__(self, gpus=None, rom_id=None, force=None, reboot=None, _configuration=None):  # noqa: E501
        """RomUploadRequestItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._gpus = None
        self._rom_id = None
        self._force = None
        self._reboot = None
        self.discriminator = None

        if gpus is not None:
            self.gpus = gpus
        if rom_id is not None:
            self.rom_id = rom_id
        if force is not None:
            self.force = force
        if reboot is not None:
            self.reboot = reboot

    @property
    def gpus(self):
        """Gets the gpus of this RomUploadRequestItem.  # noqa: E501

        GPUs to flash. Different workers can be mixed here.  # noqa: E501

        :return: The gpus of this RomUploadRequestItem.  # noqa: E501
        :rtype: list[object]
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """Sets the gpus of this RomUploadRequestItem.

        GPUs to flash. Different workers can be mixed here.  # noqa: E501

        :param gpus: The gpus of this RomUploadRequestItem.  # noqa: E501
        :type: list[object]
        """

        self._gpus = gpus

    @property
    def rom_id(self):
        """Gets the rom_id of this RomUploadRequestItem.  # noqa: E501

        Stored Rom ID to use  # noqa: E501

        :return: The rom_id of this RomUploadRequestItem.  # noqa: E501
        :rtype: int
        """
        return self._rom_id

    @rom_id.setter
    def rom_id(self, rom_id):
        """Sets the rom_id of this RomUploadRequestItem.

        Stored Rom ID to use  # noqa: E501

        :param rom_id: The rom_id of this RomUploadRequestItem.  # noqa: E501
        :type: int
        """

        self._rom_id = rom_id

    @property
    def force(self):
        """Gets the force of this RomUploadRequestItem.  # noqa: E501

        Force flashing regardless of security checkings  # noqa: E501

        :return: The force of this RomUploadRequestItem.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this RomUploadRequestItem.

        Force flashing regardless of security checkings  # noqa: E501

        :param force: The force of this RomUploadRequestItem.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def reboot(self):
        """Gets the reboot of this RomUploadRequestItem.  # noqa: E501

        Reboot worker after successful flashing of all GPUs  # noqa: E501

        :return: The reboot of this RomUploadRequestItem.  # noqa: E501
        :rtype: bool
        """
        return self._reboot

    @reboot.setter
    def reboot(self, reboot):
        """Sets the reboot of this RomUploadRequestItem.

        Reboot worker after successful flashing of all GPUs  # noqa: E501

        :param reboot: The reboot of this RomUploadRequestItem.  # noqa: E501
        :type: bool
        """

        self._reboot = reboot

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RomUploadRequestItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RomUploadRequestItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RomUploadRequestItem):
            return True

        return self.to_dict() != other.to_dict()
