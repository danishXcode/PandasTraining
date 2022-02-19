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


class BenchmarkJob(object):
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
        'algo': 'AlgoName',
        'rank': 'int',
        'recommended': 'bool'
    }

    attribute_map = {
        'algo': 'algo',
        'rank': 'rank',
        'recommended': 'recommended'
    }

    def __init__(self, algo=None, rank=None, recommended=None, _configuration=None):  # noqa: E501
        """BenchmarkJob - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._algo = None
        self._rank = None
        self._recommended = None
        self.discriminator = None

        if algo is not None:
            self.algo = algo
        if rank is not None:
            self.rank = rank
        if recommended is not None:
            self.recommended = recommended

    @property
    def algo(self):
        """Gets the algo of this BenchmarkJob.  # noqa: E501


        :return: The algo of this BenchmarkJob.  # noqa: E501
        :rtype: AlgoName
        """
        return self._algo

    @algo.setter
    def algo(self, algo):
        """Sets the algo of this BenchmarkJob.


        :param algo: The algo of this BenchmarkJob.  # noqa: E501
        :type: AlgoName
        """

        self._algo = algo

    @property
    def rank(self):
        """Gets the rank of this BenchmarkJob.  # noqa: E501

        Popularity of this algo. Lower is better.  # noqa: E501

        :return: The rank of this BenchmarkJob.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this BenchmarkJob.

        Popularity of this algo. Lower is better.  # noqa: E501

        :param rank: The rank of this BenchmarkJob.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def recommended(self):
        """Gets the recommended of this BenchmarkJob.  # noqa: E501

        This algo is mined by another Hive users with the same GPUs.  # noqa: E501

        :return: The recommended of this BenchmarkJob.  # noqa: E501
        :rtype: bool
        """
        return self._recommended

    @recommended.setter
    def recommended(self, recommended):
        """Sets the recommended of this BenchmarkJob.

        This algo is mined by another Hive users with the same GPUs.  # noqa: E501

        :param recommended: The recommended of this BenchmarkJob.  # noqa: E501
        :type: bool
        """

        self._recommended = recommended

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
        if issubclass(BenchmarkJob, dict):
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
        if not isinstance(other, BenchmarkJob):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BenchmarkJob):
            return True

        return self.to_dict() != other.to_dict()