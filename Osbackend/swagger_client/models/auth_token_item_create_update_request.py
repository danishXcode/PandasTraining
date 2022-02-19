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


class AuthTokenItemCreateUpdateRequest(object):
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
        'name': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'active': 'active'
    }

    def __init__(self, name=None, active=None, _configuration=None):  # noqa: E501
        """AuthTokenItemCreateUpdateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._active = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if active is not None:
            self.active = active

    @property
    def name(self):
        """Gets the name of this AuthTokenItemCreateUpdateRequest.  # noqa: E501

        Display name  # noqa: E501

        :return: The name of this AuthTokenItemCreateUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthTokenItemCreateUpdateRequest.

        Display name  # noqa: E501

        :param name: The name of this AuthTokenItemCreateUpdateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def active(self):
        """Gets the active of this AuthTokenItemCreateUpdateRequest.  # noqa: E501

        Is active  # noqa: E501

        :return: The active of this AuthTokenItemCreateUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AuthTokenItemCreateUpdateRequest.

        Is active  # noqa: E501

        :param active: The active of this AuthTokenItemCreateUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._active = active

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
        if issubclass(AuthTokenItemCreateUpdateRequest, dict):
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
        if not isinstance(other, AuthTokenItemCreateUpdateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthTokenItemCreateUpdateRequest):
            return True

        return self.to_dict() != other.to_dict()
