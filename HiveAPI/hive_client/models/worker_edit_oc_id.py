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


class WorkerEditOCId(object):
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
        'oc_id': 'int',
        'oc_apply_mode': 'str'
    }

    attribute_map = {
        'oc_id': 'oc_id',
        'oc_apply_mode': 'oc_apply_mode'
    }

    def __init__(self, oc_id=None, oc_apply_mode='replace', _configuration=None):  # noqa: E501
        """WorkerEditOCId - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._oc_id = None
        self._oc_apply_mode = None
        self.discriminator = None

        if oc_id is not None:
            self.oc_id = oc_id
        if oc_apply_mode is not None:
            self.oc_apply_mode = oc_apply_mode

    @property
    def oc_id(self):
        """Gets the oc_id of this WorkerEditOCId.  # noqa: E501

        Overclocking profile ID  # noqa: E501

        :return: The oc_id of this WorkerEditOCId.  # noqa: E501
        :rtype: int
        """
        return self._oc_id

    @oc_id.setter
    def oc_id(self, oc_id):
        """Sets the oc_id of this WorkerEditOCId.

        Overclocking profile ID  # noqa: E501

        :param oc_id: The oc_id of this WorkerEditOCId.  # noqa: E501
        :type: int
        """

        self._oc_id = oc_id

    @property
    def oc_apply_mode(self):
        """Gets the oc_apply_mode of this WorkerEditOCId.  # noqa: E501

        How to apply overclocking profile: - replace - means copy entire per-brand configurations of both default and per-algo sets; - merge - means copy only individual fields of per-brand configurations of both default and per-algo sets.   # noqa: E501

        :return: The oc_apply_mode of this WorkerEditOCId.  # noqa: E501
        :rtype: str
        """
        return self._oc_apply_mode

    @oc_apply_mode.setter
    def oc_apply_mode(self, oc_apply_mode):
        """Sets the oc_apply_mode of this WorkerEditOCId.

        How to apply overclocking profile: - replace - means copy entire per-brand configurations of both default and per-algo sets; - merge - means copy only individual fields of per-brand configurations of both default and per-algo sets.   # noqa: E501

        :param oc_apply_mode: The oc_apply_mode of this WorkerEditOCId.  # noqa: E501
        :type: str
        """
        allowed_values = ["replace", "merge"]  # noqa: E501
        if (self._configuration.client_side_validation and
                oc_apply_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `oc_apply_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(oc_apply_mode, allowed_values)
            )

        self._oc_apply_mode = oc_apply_mode

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
        if issubclass(WorkerEditOCId, dict):
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
        if not isinstance(other, WorkerEditOCId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkerEditOCId):
            return True

        return self.to_dict() != other.to_dict()