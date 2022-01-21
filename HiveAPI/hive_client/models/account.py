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


class Account(object):
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
        'user_id': 'int',
        'profile': 'UserProfile',
        'email_confirmed': 'bool',
        'balance': 'float',
        'min_deposit_amount': 'float',
        'referral_reward': 'int',
        'referrers_count': 'int',
        'referrer_workers_count': 'int',
        'promocode': 'str',
        'can_set_promocode': 'bool',
        '_2fa_enabled': 'bool',
        'whitelist_ips': 'list[str]',
        'ip': 'str',
        'recent_commands': 'list[str]',
        'farms': 'list[FarmShortInfoAccount]',
        'meta': 'object'
    }

    attribute_map = {
        'user_id': 'user_id',
        'profile': 'profile',
        'email_confirmed': 'email_confirmed',
        'balance': 'balance',
        'min_deposit_amount': 'min_deposit_amount',
        'referral_reward': 'referral_reward',
        'referrers_count': 'referrers_count',
        'referrer_workers_count': 'referrer_workers_count',
        'promocode': 'promocode',
        'can_set_promocode': 'can_set_promocode',
        '_2fa_enabled': '2fa_enabled',
        'whitelist_ips': 'whitelist_ips',
        'ip': 'ip',
        'recent_commands': 'recent_commands',
        'farms': 'farms',
        'meta': 'meta'
    }

    def __init__(self, user_id=None, profile=None, email_confirmed=None, balance=None, min_deposit_amount=None, referral_reward=None, referrers_count=None, referrer_workers_count=None, promocode=None, can_set_promocode=None, _2fa_enabled=None, whitelist_ips=None, ip=None, recent_commands=None, farms=None, meta=None, _configuration=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_id = None
        self._profile = None
        self._email_confirmed = None
        self._balance = None
        self._min_deposit_amount = None
        self._referral_reward = None
        self._referrers_count = None
        self._referrer_workers_count = None
        self._promocode = None
        self._can_set_promocode = None
        self.__2fa_enabled = None
        self._whitelist_ips = None
        self._ip = None
        self._recent_commands = None
        self._farms = None
        self._meta = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if profile is not None:
            self.profile = profile
        if email_confirmed is not None:
            self.email_confirmed = email_confirmed
        if balance is not None:
            self.balance = balance
        if min_deposit_amount is not None:
            self.min_deposit_amount = min_deposit_amount
        if referral_reward is not None:
            self.referral_reward = referral_reward
        if referrers_count is not None:
            self.referrers_count = referrers_count
        if referrer_workers_count is not None:
            self.referrer_workers_count = referrer_workers_count
        if promocode is not None:
            self.promocode = promocode
        if can_set_promocode is not None:
            self.can_set_promocode = can_set_promocode
        if _2fa_enabled is not None:
            self._2fa_enabled = _2fa_enabled
        if whitelist_ips is not None:
            self.whitelist_ips = whitelist_ips
        if ip is not None:
            self.ip = ip
        if recent_commands is not None:
            self.recent_commands = recent_commands
        if farms is not None:
            self.farms = farms
        if meta is not None:
            self.meta = meta

    @property
    def user_id(self):
        """Gets the user_id of this Account.  # noqa: E501


        :return: The user_id of this Account.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Account.


        :param user_id: The user_id of this Account.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def profile(self):
        """Gets the profile of this Account.  # noqa: E501


        :return: The profile of this Account.  # noqa: E501
        :rtype: UserProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this Account.


        :param profile: The profile of this Account.  # noqa: E501
        :type: UserProfile
        """

        self._profile = profile

    @property
    def email_confirmed(self):
        """Gets the email_confirmed of this Account.  # noqa: E501


        :return: The email_confirmed of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._email_confirmed

    @email_confirmed.setter
    def email_confirmed(self, email_confirmed):
        """Sets the email_confirmed of this Account.


        :param email_confirmed: The email_confirmed of this Account.  # noqa: E501
        :type: bool
        """

        self._email_confirmed = email_confirmed

    @property
    def balance(self):
        """Gets the balance of this Account.  # noqa: E501

        Balance  # noqa: E501

        :return: The balance of this Account.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Account.

        Balance  # noqa: E501

        :param balance: The balance of this Account.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def min_deposit_amount(self):
        """Gets the min_deposit_amount of this Account.  # noqa: E501

        Minimum deposit amount to get 30% bonus  # noqa: E501

        :return: The min_deposit_amount of this Account.  # noqa: E501
        :rtype: float
        """
        return self._min_deposit_amount

    @min_deposit_amount.setter
    def min_deposit_amount(self, min_deposit_amount):
        """Sets the min_deposit_amount of this Account.

        Minimum deposit amount to get 30% bonus  # noqa: E501

        :param min_deposit_amount: The min_deposit_amount of this Account.  # noqa: E501
        :type: float
        """

        self._min_deposit_amount = min_deposit_amount

    @property
    def referral_reward(self):
        """Gets the referral_reward of this Account.  # noqa: E501

        Reward in % from referrer payments  # noqa: E501

        :return: The referral_reward of this Account.  # noqa: E501
        :rtype: int
        """
        return self._referral_reward

    @referral_reward.setter
    def referral_reward(self, referral_reward):
        """Sets the referral_reward of this Account.

        Reward in % from referrer payments  # noqa: E501

        :param referral_reward: The referral_reward of this Account.  # noqa: E501
        :type: int
        """

        self._referral_reward = referral_reward

    @property
    def referrers_count(self):
        """Gets the referrers_count of this Account.  # noqa: E501

        Amount of users who were registered as current user's referral  # noqa: E501

        :return: The referrers_count of this Account.  # noqa: E501
        :rtype: int
        """
        return self._referrers_count

    @referrers_count.setter
    def referrers_count(self, referrers_count):
        """Sets the referrers_count of this Account.

        Amount of users who were registered as current user's referral  # noqa: E501

        :param referrers_count: The referrers_count of this Account.  # noqa: E501
        :type: int
        """

        self._referrers_count = referrers_count

    @property
    def referrer_workers_count(self):
        """Gets the referrer_workers_count of this Account.  # noqa: E501

        Amount of workers that were created as current user's referral  # noqa: E501

        :return: The referrer_workers_count of this Account.  # noqa: E501
        :rtype: int
        """
        return self._referrer_workers_count

    @referrer_workers_count.setter
    def referrer_workers_count(self, referrer_workers_count):
        """Sets the referrer_workers_count of this Account.

        Amount of workers that were created as current user's referral  # noqa: E501

        :param referrer_workers_count: The referrer_workers_count of this Account.  # noqa: E501
        :type: int
        """

        self._referrer_workers_count = referrer_workers_count

    @property
    def promocode(self):
        """Gets the promocode of this Account.  # noqa: E501

        Referral promocode  # noqa: E501

        :return: The promocode of this Account.  # noqa: E501
        :rtype: str
        """
        return self._promocode

    @promocode.setter
    def promocode(self, promocode):
        """Sets the promocode of this Account.

        Referral promocode  # noqa: E501

        :param promocode: The promocode of this Account.  # noqa: E501
        :type: str
        """

        self._promocode = promocode

    @property
    def can_set_promocode(self):
        """Gets the can_set_promocode of this Account.  # noqa: E501

        Only accounts older than 14 days can set promocode  # noqa: E501

        :return: The can_set_promocode of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._can_set_promocode

    @can_set_promocode.setter
    def can_set_promocode(self, can_set_promocode):
        """Sets the can_set_promocode of this Account.

        Only accounts older than 14 days can set promocode  # noqa: E501

        :param can_set_promocode: The can_set_promocode of this Account.  # noqa: E501
        :type: bool
        """

        self._can_set_promocode = can_set_promocode

    @property
    def _2fa_enabled(self):
        """Gets the _2fa_enabled of this Account.  # noqa: E501

        Indicates that Two Factor Authentication (2FA) is enabled for this account  # noqa: E501

        :return: The _2fa_enabled of this Account.  # noqa: E501
        :rtype: bool
        """
        return self.__2fa_enabled

    @_2fa_enabled.setter
    def _2fa_enabled(self, _2fa_enabled):
        """Sets the _2fa_enabled of this Account.

        Indicates that Two Factor Authentication (2FA) is enabled for this account  # noqa: E501

        :param _2fa_enabled: The _2fa_enabled of this Account.  # noqa: E501
        :type: bool
        """

        self.__2fa_enabled = _2fa_enabled

    @property
    def whitelist_ips(self):
        """Gets the whitelist_ips of this Account.  # noqa: E501


        :return: The whitelist_ips of this Account.  # noqa: E501
        :rtype: list[str]
        """
        return self._whitelist_ips

    @whitelist_ips.setter
    def whitelist_ips(self, whitelist_ips):
        """Sets the whitelist_ips of this Account.


        :param whitelist_ips: The whitelist_ips of this Account.  # noqa: E501
        :type: list[str]
        """

        self._whitelist_ips = whitelist_ips

    @property
    def ip(self):
        """Gets the ip of this Account.  # noqa: E501

        Current IP address  # noqa: E501

        :return: The ip of this Account.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Account.

        Current IP address  # noqa: E501

        :param ip: The ip of this Account.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def recent_commands(self):
        """Gets the recent_commands of this Account.  # noqa: E501

        Recently executed custom commands (via exec). Maximum 10 unique commands are stored.  # noqa: E501

        :return: The recent_commands of this Account.  # noqa: E501
        :rtype: list[str]
        """
        return self._recent_commands

    @recent_commands.setter
    def recent_commands(self, recent_commands):
        """Sets the recent_commands of this Account.

        Recently executed custom commands (via exec). Maximum 10 unique commands are stored.  # noqa: E501

        :param recent_commands: The recent_commands of this Account.  # noqa: E501
        :type: list[str]
        """

        self._recent_commands = recent_commands

    @property
    def farms(self):
        """Gets the farms of this Account.  # noqa: E501

        Farms list  # noqa: E501

        :return: The farms of this Account.  # noqa: E501
        :rtype: list[FarmShortInfoAccount]
        """
        return self._farms

    @farms.setter
    def farms(self, farms):
        """Sets the farms of this Account.

        Farms list  # noqa: E501

        :param farms: The farms of this Account.  # noqa: E501
        :type: list[FarmShortInfoAccount]
        """

        self._farms = farms

    @property
    def meta(self):
        """Gets the meta of this Account.  # noqa: E501

        Meta data keyed by namespace  # noqa: E501

        :return: The meta of this Account.  # noqa: E501
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Account.

        Meta data keyed by namespace  # noqa: E501

        :param meta: The meta of this Account.  # noqa: E501
        :type: object
        """

        self._meta = meta

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Account):
            return True

        return self.to_dict() != other.to_dict()
