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


class OCConfig(object):
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
        'default': 'object',
        'by_algo': 'list[object]'
    }

    attribute_map = {
        'default': 'default',
        'by_algo': 'by_algo'
    }

    def __init__(self, default=None, by_algo=None, _configuration=None):  # noqa: E501
        """OCConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._default = None
        self._by_algo = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if by_algo is not None:
            self.by_algo = by_algo

    @property
    def default(self):
        """Gets the default of this OCConfig.  # noqa: E501

        Default overclock. This overclock will be applied if there is no configuration for needed algo.   # noqa: E501

        :return: The default of this OCConfig.  # noqa: E501
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this OCConfig.

        Default overclock. This overclock will be applied if there is no configuration for needed algo.   # noqa: E501

        :param default: The default of this OCConfig.  # noqa: E501
        :type: object
        """

        self._default = default

    @property
    def by_algo(self):
        """Gets the by_algo of this OCConfig.  # noqa: E501


        :return: The by_algo of this OCConfig.  # noqa: E501
        :rtype: list[object]
        """
        return self._by_algo

    @by_algo.setter
    def by_algo(self, by_algo):
        """Sets the by_algo of this OCConfig.


        :param by_algo: The by_algo of this OCConfig.  # noqa: E501
        :type: list[object]
        """

        self._by_algo = by_algo

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
        if issubclass(OCConfig, dict):
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
        if not isinstance(other, OCConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OCConfig):
            return True

        return self.to_dict() != other.to_dict()
