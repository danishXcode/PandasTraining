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


class FarmConfigFiles(object):
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
        'rig_conf': 'str'
    }

    attribute_map = {
        'rig_conf': 'rig.conf'
    }

    def __init__(self, rig_conf=None, _configuration=None):  # noqa: E501
        """FarmConfigFiles - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rig_conf = None
        self.discriminator = None

        if rig_conf is not None:
            self.rig_conf = rig_conf

    @property
    def rig_conf(self):
        """Gets the rig_conf of this FarmConfigFiles.  # noqa: E501

        rig.conf file contents  # noqa: E501

        :return: The rig_conf of this FarmConfigFiles.  # noqa: E501
        :rtype: str
        """
        return self._rig_conf

    @rig_conf.setter
    def rig_conf(self, rig_conf):
        """Sets the rig_conf of this FarmConfigFiles.

        rig.conf file contents  # noqa: E501

        :param rig_conf: The rig_conf of this FarmConfigFiles.  # noqa: E501
        :type: str
        """

        self._rig_conf = rig_conf

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
        if issubclass(FarmConfigFiles, dict):
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
        if not isinstance(other, FarmConfigFiles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FarmConfigFiles):
            return True

        return self.to_dict() != other.to_dict()