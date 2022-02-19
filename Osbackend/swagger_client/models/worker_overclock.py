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


class WorkerOverclock(object):
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
        'overclock': 'object'
    }

    attribute_map = {
        'overclock': 'overclock'
    }

    def __init__(self, overclock=None, _configuration=None):  # noqa: E501
        """WorkerOverclock - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._overclock = None
        self.discriminator = None

        if overclock is not None:
            self.overclock = overclock

    @property
    def overclock(self):
        """Gets the overclock of this WorkerOverclock.  # noqa: E501

        Actually applied overclock  # noqa: E501

        :return: The overclock of this WorkerOverclock.  # noqa: E501
        :rtype: object
        """
        return self._overclock

    @overclock.setter
    def overclock(self, overclock):
        """Sets the overclock of this WorkerOverclock.

        Actually applied overclock  # noqa: E501

        :param overclock: The overclock of this WorkerOverclock.  # noqa: E501
        :type: object
        """

        self._overclock = overclock

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
        if issubclass(WorkerOverclock, dict):
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
        if not isinstance(other, WorkerOverclock):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkerOverclock):
            return True

        return self.to_dict() != other.to_dict()
