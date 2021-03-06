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


class GpuFlashingState(object):
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
        'last_ok': 'object',
        'last_failed': 'object',
        'in_process': 'object'
    }

    attribute_map = {
        'last_ok': 'last_ok',
        'last_failed': 'last_failed',
        'in_process': 'in_process'
    }

    def __init__(self, last_ok=None, last_failed=None, in_process=None, _configuration=None):  # noqa: E501
        """GpuFlashingState - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_ok = None
        self._last_failed = None
        self._in_process = None
        self.discriminator = None

        if last_ok is not None:
            self.last_ok = last_ok
        if last_failed is not None:
            self.last_failed = last_failed
        if in_process is not None:
            self.in_process = in_process

    @property
    def last_ok(self):
        """Gets the last_ok of this GpuFlashingState.  # noqa: E501

        Last successfully flashed ROM  # noqa: E501

        :return: The last_ok of this GpuFlashingState.  # noqa: E501
        :rtype: object
        """
        return self._last_ok

    @last_ok.setter
    def last_ok(self, last_ok):
        """Sets the last_ok of this GpuFlashingState.

        Last successfully flashed ROM  # noqa: E501

        :param last_ok: The last_ok of this GpuFlashingState.  # noqa: E501
        :type: object
        """

        self._last_ok = last_ok

    @property
    def last_failed(self):
        """Gets the last_failed of this GpuFlashingState.  # noqa: E501

        Latest flashing if it failed  # noqa: E501

        :return: The last_failed of this GpuFlashingState.  # noqa: E501
        :rtype: object
        """
        return self._last_failed

    @last_failed.setter
    def last_failed(self, last_failed):
        """Sets the last_failed of this GpuFlashingState.

        Latest flashing if it failed  # noqa: E501

        :param last_failed: The last_failed of this GpuFlashingState.  # noqa: E501
        :type: object
        """

        self._last_failed = last_failed

    @property
    def in_process(self):
        """Gets the in_process of this GpuFlashingState.  # noqa: E501

        Flashing being executed right now  # noqa: E501

        :return: The in_process of this GpuFlashingState.  # noqa: E501
        :rtype: object
        """
        return self._in_process

    @in_process.setter
    def in_process(self, in_process):
        """Sets the in_process of this GpuFlashingState.

        Flashing being executed right now  # noqa: E501

        :param in_process: The in_process of this GpuFlashingState.  # noqa: E501
        :type: object
        """

        self._in_process = in_process

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
        if issubclass(GpuFlashingState, dict):
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
        if not isinstance(other, GpuFlashingState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GpuFlashingState):
            return True

        return self.to_dict() != other.to_dict()
