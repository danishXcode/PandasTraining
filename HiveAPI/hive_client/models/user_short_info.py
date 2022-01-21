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


class UserShortInfo(object):
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
        'login': 'str',
        'name': 'str',
        'me': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'login': 'login',
        'name': 'name',
        'me': 'me'
    }

    def __init__(self, id=None, login=None, name=None, me=None, _configuration=None):  # noqa: E501
        """UserShortInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._login = None
        self._name = None
        self._me = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if login is not None:
            self.login = login
        if name is not None:
            self.name = name
        if me is not None:
            self.me = me

    @property
    def id(self):
        """Gets the id of this UserShortInfo.  # noqa: E501

        User ID  # noqa: E501

        :return: The id of this UserShortInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserShortInfo.

        User ID  # noqa: E501

        :param id: The id of this UserShortInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this UserShortInfo.  # noqa: E501

        User login  # noqa: E501

        :return: The login of this UserShortInfo.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this UserShortInfo.

        User login  # noqa: E501

        :param login: The login of this UserShortInfo.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def name(self):
        """Gets the name of this UserShortInfo.  # noqa: E501

        User full name  # noqa: E501

        :return: The name of this UserShortInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserShortInfo.

        User full name  # noqa: E501

        :param name: The name of this UserShortInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def me(self):
        """Gets the me of this UserShortInfo.  # noqa: E501

        Is me  # noqa: E501

        :return: The me of this UserShortInfo.  # noqa: E501
        :rtype: bool
        """
        return self._me

    @me.setter
    def me(self, me):
        """Sets the me of this UserShortInfo.

        Is me  # noqa: E501

        :param me: The me of this UserShortInfo.  # noqa: E501
        :type: bool
        """

        self._me = me

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
        if issubclass(UserShortInfo, dict):
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
        if not isinstance(other, UserShortInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserShortInfo):
            return True

        return self.to_dict() != other.to_dict()
