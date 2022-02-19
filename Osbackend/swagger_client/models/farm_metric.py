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


class FarmMetric(object):
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
        'time': 'int',
        'rigs': 'int',
        'gpus': 'int',
        'asics': 'int',
        'boards': 'int',
        'hashrates': 'list[object]'
    }

    attribute_map = {
        'time': 'time',
        'rigs': 'rigs',
        'gpus': 'gpus',
        'asics': 'asics',
        'boards': 'boards',
        'hashrates': 'hashrates'
    }

    def __init__(self, time=None, rigs=None, gpus=None, asics=None, boards=None, hashrates=None, _configuration=None):  # noqa: E501
        """FarmMetric - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._time = None
        self._rigs = None
        self._gpus = None
        self._asics = None
        self._boards = None
        self._hashrates = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if rigs is not None:
            self.rigs = rigs
        if gpus is not None:
            self.gpus = gpus
        if asics is not None:
            self.asics = asics
        if boards is not None:
            self.boards = boards
        if hashrates is not None:
            self.hashrates = hashrates

    @property
    def time(self):
        """Gets the time of this FarmMetric.  # noqa: E501


        :return: The time of this FarmMetric.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this FarmMetric.


        :param time: The time of this FarmMetric.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def rigs(self):
        """Gets the rigs of this FarmMetric.  # noqa: E501

        Rigs online  # noqa: E501

        :return: The rigs of this FarmMetric.  # noqa: E501
        :rtype: int
        """
        return self._rigs

    @rigs.setter
    def rigs(self, rigs):
        """Sets the rigs of this FarmMetric.

        Rigs online  # noqa: E501

        :param rigs: The rigs of this FarmMetric.  # noqa: E501
        :type: int
        """

        self._rigs = rigs

    @property
    def gpus(self):
        """Gets the gpus of this FarmMetric.  # noqa: E501

        GPUs online  # noqa: E501

        :return: The gpus of this FarmMetric.  # noqa: E501
        :rtype: int
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """Sets the gpus of this FarmMetric.

        GPUs online  # noqa: E501

        :param gpus: The gpus of this FarmMetric.  # noqa: E501
        :type: int
        """

        self._gpus = gpus

    @property
    def asics(self):
        """Gets the asics of this FarmMetric.  # noqa: E501

        ASICs online  # noqa: E501

        :return: The asics of this FarmMetric.  # noqa: E501
        :rtype: int
        """
        return self._asics

    @asics.setter
    def asics(self, asics):
        """Sets the asics of this FarmMetric.

        ASICs online  # noqa: E501

        :param asics: The asics of this FarmMetric.  # noqa: E501
        :type: int
        """

        self._asics = asics

    @property
    def boards(self):
        """Gets the boards of this FarmMetric.  # noqa: E501

        ASIC boards online  # noqa: E501

        :return: The boards of this FarmMetric.  # noqa: E501
        :rtype: int
        """
        return self._boards

    @boards.setter
    def boards(self, boards):
        """Sets the boards of this FarmMetric.

        ASIC boards online  # noqa: E501

        :param boards: The boards of this FarmMetric.  # noqa: E501
        :type: int
        """

        self._boards = boards

    @property
    def hashrates(self):
        """Gets the hashrates of this FarmMetric.  # noqa: E501

        Hashrates by algorithm  # noqa: E501

        :return: The hashrates of this FarmMetric.  # noqa: E501
        :rtype: list[object]
        """
        return self._hashrates

    @hashrates.setter
    def hashrates(self, hashrates):
        """Sets the hashrates of this FarmMetric.

        Hashrates by algorithm  # noqa: E501

        :param hashrates: The hashrates of this FarmMetric.  # noqa: E501
        :type: list[object]
        """

        self._hashrates = hashrates

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
        if issubclass(FarmMetric, dict):
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
        if not isinstance(other, FarmMetric):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FarmMetric):
            return True

        return self.to_dict() != other.to_dict()