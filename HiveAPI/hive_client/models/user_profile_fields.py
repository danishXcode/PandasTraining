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


class UserProfileFields(object):
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
        'name': 'str',
        'email': 'str',
        'timezone': 'str',
        'phone': 'str',
        'telegram': 'str',
        'skype': 'str',
        'company_info': 'str'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'timezone': 'timezone',
        'phone': 'phone',
        'telegram': 'telegram',
        'skype': 'skype',
        'company_info': 'company_info'
    }

    def __init__(self, name=None, email=None, timezone=None, phone=None, telegram=None, skype=None, company_info=None, _configuration=None):  # noqa: E501
        """UserProfileFields - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._email = None
        self._timezone = None
        self._phone = None
        self._telegram = None
        self._skype = None
        self._company_info = None
        self.discriminator = None

        self.name = name
        self.email = email
        self.timezone = timezone
        if phone is not None:
            self.phone = phone
        if telegram is not None:
            self.telegram = telegram
        if skype is not None:
            self.skype = skype
        if company_info is not None:
            self.company_info = company_info

    @property
    def name(self):
        """Gets the name of this UserProfileFields.  # noqa: E501


        :return: The name of this UserProfileFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserProfileFields.


        :param name: The name of this UserProfileFields.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this UserProfileFields.  # noqa: E501


        :return: The email of this UserProfileFields.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserProfileFields.


        :param email: The email of this UserProfileFields.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def timezone(self):
        """Gets the timezone of this UserProfileFields.  # noqa: E501


        :return: The timezone of this UserProfileFields.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UserProfileFields.


        :param timezone: The timezone of this UserProfileFields.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

    @property
    def phone(self):
        """Gets the phone of this UserProfileFields.  # noqa: E501


        :return: The phone of this UserProfileFields.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UserProfileFields.


        :param phone: The phone of this UserProfileFields.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def telegram(self):
        """Gets the telegram of this UserProfileFields.  # noqa: E501


        :return: The telegram of this UserProfileFields.  # noqa: E501
        :rtype: str
        """
        return self._telegram

    @telegram.setter
    def telegram(self, telegram):
        """Sets the telegram of this UserProfileFields.


        :param telegram: The telegram of this UserProfileFields.  # noqa: E501
        :type: str
        """

        self._telegram = telegram

    @property
    def skype(self):
        """Gets the skype of this UserProfileFields.  # noqa: E501


        :return: The skype of this UserProfileFields.  # noqa: E501
        :rtype: str
        """
        return self._skype

    @skype.setter
    def skype(self, skype):
        """Sets the skype of this UserProfileFields.


        :param skype: The skype of this UserProfileFields.  # noqa: E501
        :type: str
        """

        self._skype = skype

    @property
    def company_info(self):
        """Gets the company_info of this UserProfileFields.  # noqa: E501


        :return: The company_info of this UserProfileFields.  # noqa: E501
        :rtype: str
        """
        return self._company_info

    @company_info.setter
    def company_info(self, company_info):
        """Sets the company_info of this UserProfileFields.


        :param company_info: The company_info of this UserProfileFields.  # noqa: E501
        :type: str
        """

        self._company_info = company_info

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
        if issubclass(UserProfileFields, dict):
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
        if not isinstance(other, UserProfileFields):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserProfileFields):
            return True

        return self.to_dict() != other.to_dict()
