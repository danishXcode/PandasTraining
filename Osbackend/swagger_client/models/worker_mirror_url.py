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


class WorkerMirrorUrl(object):
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
        'mirror_url': 'MirrorUrl'
    }

    attribute_map = {
        'mirror_url': 'mirror_url'
    }

    def __init__(self, mirror_url=None, _configuration=None):  # noqa: E501
        """WorkerMirrorUrl - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mirror_url = None
        self.discriminator = None

        if mirror_url is not None:
            self.mirror_url = mirror_url

    @property
    def mirror_url(self):
        """Gets the mirror_url of this WorkerMirrorUrl.  # noqa: E501


        :return: The mirror_url of this WorkerMirrorUrl.  # noqa: E501
        :rtype: MirrorUrl
        """
        return self._mirror_url

    @mirror_url.setter
    def mirror_url(self, mirror_url):
        """Sets the mirror_url of this WorkerMirrorUrl.


        :param mirror_url: The mirror_url of this WorkerMirrorUrl.  # noqa: E501
        :type: MirrorUrl
        """

        self._mirror_url = mirror_url

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
        if issubclass(WorkerMirrorUrl, dict):
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
        if not isinstance(other, WorkerMirrorUrl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkerMirrorUrl):
            return True

        return self.to_dict() != other.to_dict()