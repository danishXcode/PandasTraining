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


class ReferralPayoutRequest(object):
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
        'currency': 'ReferralCurrency',
        'amount': 'float',
        'all': 'bool'
    }

    attribute_map = {
        'currency': 'currency',
        'amount': 'amount',
        'all': 'all'
    }

    def __init__(self, currency=None, amount=None, all=None, _configuration=None):  # noqa: E501
        """ReferralPayoutRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._currency = None
        self._amount = None
        self._all = None
        self.discriminator = None

        self.currency = currency
        if amount is not None:
            self.amount = amount
        if all is not None:
            self.all = all

    @property
    def currency(self):
        """Gets the currency of this ReferralPayoutRequest.  # noqa: E501


        :return: The currency of this ReferralPayoutRequest.  # noqa: E501
        :rtype: ReferralCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ReferralPayoutRequest.


        :param currency: The currency of this ReferralPayoutRequest.  # noqa: E501
        :type: ReferralCurrency
        """
        if self._configuration.client_side_validation and currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this ReferralPayoutRequest.  # noqa: E501

        Amount in currency to withdraw  # noqa: E501

        :return: The amount of this ReferralPayoutRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ReferralPayoutRequest.

        Amount in currency to withdraw  # noqa: E501

        :param amount: The amount of this ReferralPayoutRequest.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def all(self):
        """Gets the all of this ReferralPayoutRequest.  # noqa: E501

        If TRUE - the whole referral balance in this currency will be withdrawn and \"amount\" will be ignored  # noqa: E501

        :return: The all of this ReferralPayoutRequest.  # noqa: E501
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this ReferralPayoutRequest.

        If TRUE - the whole referral balance in this currency will be withdrawn and \"amount\" will be ignored  # noqa: E501

        :param all: The all of this ReferralPayoutRequest.  # noqa: E501
        :type: bool
        """

        self._all = all

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
        if issubclass(ReferralPayoutRequest, dict):
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
        if not isinstance(other, ReferralPayoutRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReferralPayoutRequest):
            return True

        return self.to_dict() != other.to_dict()
