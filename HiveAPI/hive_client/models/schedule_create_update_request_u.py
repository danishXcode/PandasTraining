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


class ScheduleCreateUpdateRequestU(object):
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
        'action': 'object',
        'target': 'object'
    }

    attribute_map = {
        'action': 'action',
        'target': 'target'
    }

    def __init__(self, action=None, target=None, _configuration=None):  # noqa: E501
        """ScheduleCreateUpdateRequestU - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._target = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if target is not None:
            self.target = target

    @property
    def action(self):
        """Gets the action of this ScheduleCreateUpdateRequestU.  # noqa: E501

        Everything defined in this object will be applied to workers  # noqa: E501

        :return: The action of this ScheduleCreateUpdateRequestU.  # noqa: E501
        :rtype: object
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ScheduleCreateUpdateRequestU.

        Everything defined in this object will be applied to workers  # noqa: E501

        :param action: The action of this ScheduleCreateUpdateRequestU.  # noqa: E501
        :type: object
        """

        self._action = action

    @property
    def target(self):
        """Gets the target of this ScheduleCreateUpdateRequestU.  # noqa: E501


        :return: The target of this ScheduleCreateUpdateRequestU.  # noqa: E501
        :rtype: object
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ScheduleCreateUpdateRequestU.


        :param target: The target of this ScheduleCreateUpdateRequestU.  # noqa: E501
        :type: object
        """

        self._target = target

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
        if issubclass(ScheduleCreateUpdateRequestU, dict):
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
        if not isinstance(other, ScheduleCreateUpdateRequestU):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleCreateUpdateRequestU):
            return True

        return self.to_dict() != other.to_dict()
