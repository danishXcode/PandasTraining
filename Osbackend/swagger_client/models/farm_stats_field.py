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


class FarmStatsField(object):
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
        'stats': 'FarmStats'
    }

    attribute_map = {
        'stats': 'stats'
    }

    def __init__(self, stats=None, _configuration=None):  # noqa: E501
        """FarmStatsField - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._stats = None
        self.discriminator = None

        if stats is not None:
            self.stats = stats

    @property
    def stats(self):
        """Gets the stats of this FarmStatsField.  # noqa: E501


        :return: The stats of this FarmStatsField.  # noqa: E501
        :rtype: FarmStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this FarmStatsField.


        :param stats: The stats of this FarmStatsField.  # noqa: E501
        :type: FarmStats
        """

        self._stats = stats

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
        if issubclass(FarmStatsField, dict):
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
        if not isinstance(other, FarmStatsField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FarmStatsField):
            return True

        return self.to_dict() != other.to_dict()