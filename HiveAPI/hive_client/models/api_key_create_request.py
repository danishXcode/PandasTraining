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


class ApiKeyCreateRequest(object):
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
        'api_secret': 'str',
        'source_type': 'str',
        'source_name': 'str'
    }

    attribute_map = {
        'api_secret': 'api_secret',
        'source_type': 'source_type',
        'source_name': 'source_name'
    }

    def __init__(self, api_secret=None, source_type=None, source_name=None, _configuration=None):  # noqa: E501
        """ApiKeyCreateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_secret = None
        self._source_type = None
        self._source_name = None
        self.discriminator = None

        if api_secret is not None:
            self.api_secret = api_secret
        if source_type is not None:
            self.source_type = source_type
        if source_name is not None:
            self.source_name = source_name

    @property
    def api_secret(self):
        """Gets the api_secret of this ApiKeyCreateRequest.  # noqa: E501

        API secret  # noqa: E501

        :return: The api_secret of this ApiKeyCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret):
        """Sets the api_secret of this ApiKeyCreateRequest.

        API secret  # noqa: E501

        :param api_secret: The api_secret of this ApiKeyCreateRequest.  # noqa: E501
        :type: str
        """

        self._api_secret = api_secret

    @property
    def source_type(self):
        """Gets the source_type of this ApiKeyCreateRequest.  # noqa: E501


        :return: The source_type of this ApiKeyCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ApiKeyCreateRequest.


        :param source_type: The source_type of this ApiKeyCreateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["pool", "exchange"]  # noqa: E501
        if (self._configuration.client_side_validation and
                source_type not in allowed_values):
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def source_name(self):
        """Gets the source_name of this ApiKeyCreateRequest.  # noqa: E501

        Pool name or exchange name. For supported pools and exchanges see /hive/wallet_sources endpoint.   # noqa: E501

        :return: The source_name of this ApiKeyCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this ApiKeyCreateRequest.

        Pool name or exchange name. For supported pools and exchanges see /hive/wallet_sources endpoint.   # noqa: E501

        :param source_name: The source_name of this ApiKeyCreateRequest.  # noqa: E501
        :type: str
        """

        self._source_name = source_name

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
        if issubclass(ApiKeyCreateRequest, dict):
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
        if not isinstance(other, ApiKeyCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiKeyCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
