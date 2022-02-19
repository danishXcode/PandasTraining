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


class Tag(object):
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
        'color': 'int',
        'farms_count': 'int',
        'workers_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'color': 'color',
        'farms_count': 'farms_count',
        'workers_count': 'workers_count'
    }

    def __init__(self, name=None, color=None, farms_count=None, workers_count=None, _configuration=None):  # noqa: E501
        """Tag - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._color = None
        self._farms_count = None
        self._workers_count = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if color is not None:
            self.color = color
        if farms_count is not None:
            self.farms_count = farms_count
        if workers_count is not None:
            self.workers_count = workers_count

    @property
    def name(self):
        """Gets the name of this Tag.  # noqa: E501

        Display name  # noqa: E501

        :return: The name of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.

        Display name  # noqa: E501

        :param name: The name of this Tag.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 50):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def color(self):
        """Gets the color of this Tag.  # noqa: E501

        Display color ID  # noqa: E501

        :return: The color of this Tag.  # noqa: E501
        :rtype: int
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Tag.

        Display color ID  # noqa: E501

        :param color: The color of this Tag.  # noqa: E501
        :type: int
        """

        self._color = color

    @property
    def farms_count(self):
        """Gets the farms_count of this Tag.  # noqa: E501

        Amount of farms that use this tag  # noqa: E501

        :return: The farms_count of this Tag.  # noqa: E501
        :rtype: int
        """
        return self._farms_count

    @farms_count.setter
    def farms_count(self, farms_count):
        """Sets the farms_count of this Tag.

        Amount of farms that use this tag  # noqa: E501

        :param farms_count: The farms_count of this Tag.  # noqa: E501
        :type: int
        """

        self._farms_count = farms_count

    @property
    def workers_count(self):
        """Gets the workers_count of this Tag.  # noqa: E501

        Amount of workers that use this tag  # noqa: E501

        :return: The workers_count of this Tag.  # noqa: E501
        :rtype: int
        """
        return self._workers_count

    @workers_count.setter
    def workers_count(self, workers_count):
        """Sets the workers_count of this Tag.

        Amount of workers that use this tag  # noqa: E501

        :param workers_count: The workers_count of this Tag.  # noqa: E501
        :type: int
        """

        self._workers_count = workers_count

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
        if issubclass(Tag, dict):
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
        if not isinstance(other, Tag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tag):
            return True

        return self.to_dict() != other.to_dict()