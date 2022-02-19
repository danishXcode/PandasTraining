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


class WorkerAsicInfo(object):
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
        'asic_info': 'object',
        'asichub_id': 'int'
    }

    attribute_map = {
        'asic_info': 'asic_info',
        'asichub_id': 'asichub_id'
    }

    def __init__(self, asic_info=None, asichub_id=None, _configuration=None):  # noqa: E501
        """WorkerAsicInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._asic_info = None
        self._asichub_id = None
        self.discriminator = None

        if asic_info is not None:
            self.asic_info = asic_info
        if asichub_id is not None:
            self.asichub_id = asichub_id

    @property
    def asic_info(self):
        """Gets the asic_info of this WorkerAsicInfo.  # noqa: E501

        ASIC information  # noqa: E501

        :return: The asic_info of this WorkerAsicInfo.  # noqa: E501
        :rtype: object
        """
        return self._asic_info

    @asic_info.setter
    def asic_info(self, asic_info):
        """Sets the asic_info of this WorkerAsicInfo.

        ASIC information  # noqa: E501

        :param asic_info: The asic_info of this WorkerAsicInfo.  # noqa: E501
        :type: object
        """

        self._asic_info = asic_info

    @property
    def asichub_id(self):
        """Gets the asichub_id of this WorkerAsicInfo.  # noqa: E501

        ID of AsicHUB which manages this ASIC  # noqa: E501

        :return: The asichub_id of this WorkerAsicInfo.  # noqa: E501
        :rtype: int
        """
        return self._asichub_id

    @asichub_id.setter
    def asichub_id(self, asichub_id):
        """Sets the asichub_id of this WorkerAsicInfo.

        ID of AsicHUB which manages this ASIC  # noqa: E501

        :param asichub_id: The asichub_id of this WorkerAsicInfo.  # noqa: E501
        :type: int
        """

        self._asichub_id = asichub_id

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
        if issubclass(WorkerAsicInfo, dict):
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
        if not isinstance(other, WorkerAsicInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkerAsicInfo):
            return True

        return self.to_dict() != other.to_dict()
