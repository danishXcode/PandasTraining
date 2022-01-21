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


class HiveVersion(object):
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
        'system_type': 'str',
        'version': 'str',
        '_date': 'str',
        'image': 'bool',
        'beta': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'system_type': 'system_type',
        'version': 'version',
        '_date': 'date',
        'image': 'image',
        'beta': 'beta',
        'description': 'description'
    }

    def __init__(self, system_type=None, version=None, _date=None, image=None, beta=None, description=None, _configuration=None):  # noqa: E501
        """HiveVersion - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._system_type = None
        self._version = None
        self.__date = None
        self._image = None
        self._beta = None
        self._description = None
        self.discriminator = None

        if system_type is not None:
            self.system_type = system_type
        if version is not None:
            self.version = version
        if _date is not None:
            self._date = _date
        if image is not None:
            self.image = image
        if beta is not None:
            self.beta = beta
        if description is not None:
            self.description = description

    @property
    def system_type(self):
        """Gets the system_type of this HiveVersion.  # noqa: E501

        System type (only for Hive release)  # noqa: E501

        :return: The system_type of this HiveVersion.  # noqa: E501
        :rtype: str
        """
        return self._system_type

    @system_type.setter
    def system_type(self, system_type):
        """Sets the system_type of this HiveVersion.

        System type (only for Hive release)  # noqa: E501

        :param system_type: The system_type of this HiveVersion.  # noqa: E501
        :type: str
        """
        allowed_values = ["linux", "asic", "windows"]  # noqa: E501
        if (self._configuration.client_side_validation and
                system_type not in allowed_values):
            raise ValueError(
                "Invalid value for `system_type` ({0}), must be one of {1}"  # noqa: E501
                .format(system_type, allowed_values)
            )

        self._system_type = system_type

    @property
    def version(self):
        """Gets the version of this HiveVersion.  # noqa: E501

        Version number (Hive, Asic Hub beta, Asic Hub)  # noqa: E501

        :return: The version of this HiveVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this HiveVersion.

        Version number (Hive, Asic Hub beta, Asic Hub)  # noqa: E501

        :param version: The version of this HiveVersion.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def _date(self):
        """Gets the _date of this HiveVersion.  # noqa: E501

        Release date  # noqa: E501

        :return: The _date of this HiveVersion.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this HiveVersion.

        Release date  # noqa: E501

        :param _date: The _date of this HiveVersion.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def image(self):
        """Gets the image of this HiveVersion.  # noqa: E501

        Is new image released (only for Hive release)  # noqa: E501

        :return: The image of this HiveVersion.  # noqa: E501
        :rtype: bool
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this HiveVersion.

        Is new image released (only for Hive release)  # noqa: E501

        :param image: The image of this HiveVersion.  # noqa: E501
        :type: bool
        """

        self._image = image

    @property
    def beta(self):
        """Gets the beta of this HiveVersion.  # noqa: E501

        Indicates that released image (Hive) or release itself (Asic Hub) is beta  # noqa: E501

        :return: The beta of this HiveVersion.  # noqa: E501
        :rtype: bool
        """
        return self._beta

    @beta.setter
    def beta(self, beta):
        """Sets the beta of this HiveVersion.

        Indicates that released image (Hive) or release itself (Asic Hub) is beta  # noqa: E501

        :param beta: The beta of this HiveVersion.  # noqa: E501
        :type: bool
        """

        self._beta = beta

    @property
    def description(self):
        """Gets the description of this HiveVersion.  # noqa: E501

        Version description  # noqa: E501

        :return: The description of this HiveVersion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HiveVersion.

        Version description  # noqa: E501

        :param description: The description of this HiveVersion.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(HiveVersion, dict):
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
        if not isinstance(other, HiveVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HiveVersion):
            return True

        return self.to_dict() != other.to_dict()