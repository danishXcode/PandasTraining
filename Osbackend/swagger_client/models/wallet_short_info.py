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


class WalletShortInfo(object):
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
        'id': 'int',
        'farm_id': 'int',
        'user_id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'farm_id': 'farm_id',
        'user_id': 'user_id',
        'name': 'name'
    }

    def __init__(self, id=None, farm_id=None, user_id=None, name=None, _configuration=None):  # noqa: E501
        """WalletShortInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._farm_id = None
        self._user_id = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if farm_id is not None:
            self.farm_id = farm_id
        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this WalletShortInfo.  # noqa: E501


        :return: The id of this WalletShortInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WalletShortInfo.


        :param id: The id of this WalletShortInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def farm_id(self):
        """Gets the farm_id of this WalletShortInfo.  # noqa: E501


        :return: The farm_id of this WalletShortInfo.  # noqa: E501
        :rtype: int
        """
        return self._farm_id

    @farm_id.setter
    def farm_id(self, farm_id):
        """Sets the farm_id of this WalletShortInfo.


        :param farm_id: The farm_id of this WalletShortInfo.  # noqa: E501
        :type: int
        """

        self._farm_id = farm_id

    @property
    def user_id(self):
        """Gets the user_id of this WalletShortInfo.  # noqa: E501


        :return: The user_id of this WalletShortInfo.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this WalletShortInfo.


        :param user_id: The user_id of this WalletShortInfo.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this WalletShortInfo.  # noqa: E501

        Display name  # noqa: E501

        :return: The name of this WalletShortInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WalletShortInfo.

        Display name  # noqa: E501

        :param name: The name of this WalletShortInfo.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(WalletShortInfo, dict):
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
        if not isinstance(other, WalletShortInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WalletShortInfo):
            return True

        return self.to_dict() != other.to_dict()