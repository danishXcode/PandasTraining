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


class OCConfigAmd(object):
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
        'core_clock': 'str',
        'core_state': 'str',
        'core_vddc': 'str',
        'mem_clock': 'str',
        'mem_state': 'str',
        'mem_mvdd': 'str',
        'mem_vddci': 'str',
        'fan_speed': 'str',
        'power_limit': 'str',
        'tref_timing': 'str',
        'soc_clock': 'str',
        'soc_vddmax': 'str',
        'aggressive': 'bool'
    }

    attribute_map = {
        'core_clock': 'core_clock',
        'core_state': 'core_state',
        'core_vddc': 'core_vddc',
        'mem_clock': 'mem_clock',
        'mem_state': 'mem_state',
        'mem_mvdd': 'mem_mvdd',
        'mem_vddci': 'mem_vddci',
        'fan_speed': 'fan_speed',
        'power_limit': 'power_limit',
        'tref_timing': 'tref_timing',
        'soc_clock': 'soc_clock',
        'soc_vddmax': 'soc_vddmax',
        'aggressive': 'aggressive'
    }

    def __init__(self, core_clock=None, core_state=None, core_vddc=None, mem_clock=None, mem_state=None, mem_mvdd=None, mem_vddci=None, fan_speed=None, power_limit=None, tref_timing=None, soc_clock=None, soc_vddmax=None, aggressive=None, _configuration=None):  # noqa: E501
        """OCConfigAmd - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._core_clock = None
        self._core_state = None
        self._core_vddc = None
        self._mem_clock = None
        self._mem_state = None
        self._mem_mvdd = None
        self._mem_vddci = None
        self._fan_speed = None
        self._power_limit = None
        self._tref_timing = None
        self._soc_clock = None
        self._soc_vddmax = None
        self._aggressive = None
        self.discriminator = None

        if core_clock is not None:
            self.core_clock = core_clock
        if core_state is not None:
            self.core_state = core_state
        if core_vddc is not None:
            self.core_vddc = core_vddc
        if mem_clock is not None:
            self.mem_clock = mem_clock
        if mem_state is not None:
            self.mem_state = mem_state
        if mem_mvdd is not None:
            self.mem_mvdd = mem_mvdd
        if mem_vddci is not None:
            self.mem_vddci = mem_vddci
        if fan_speed is not None:
            self.fan_speed = fan_speed
        if power_limit is not None:
            self.power_limit = power_limit
        if tref_timing is not None:
            self.tref_timing = tref_timing
        if soc_clock is not None:
            self.soc_clock = soc_clock
        if soc_vddmax is not None:
            self.soc_vddmax = soc_vddmax
        if aggressive is not None:
            self.aggressive = aggressive

    @property
    def core_clock(self):
        """Gets the core_clock of this OCConfigAmd.  # noqa: E501

        Core Clock (Mhz)  # noqa: E501

        :return: The core_clock of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._core_clock

    @core_clock.setter
    def core_clock(self, core_clock):
        """Sets the core_clock of this OCConfigAmd.

        Core Clock (Mhz)  # noqa: E501

        :param core_clock: The core_clock of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._core_clock = core_clock

    @property
    def core_state(self):
        """Gets the core_state of this OCConfigAmd.  # noqa: E501

        Core State (Index)  # noqa: E501

        :return: The core_state of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._core_state

    @core_state.setter
    def core_state(self, core_state):
        """Sets the core_state of this OCConfigAmd.

        Core State (Index)  # noqa: E501

        :param core_state: The core_state of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._core_state = core_state

    @property
    def core_vddc(self):
        """Gets the core_vddc of this OCConfigAmd.  # noqa: E501

        Core Voltage (mV)  # noqa: E501

        :return: The core_vddc of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._core_vddc

    @core_vddc.setter
    def core_vddc(self, core_vddc):
        """Sets the core_vddc of this OCConfigAmd.

        Core Voltage (mV)  # noqa: E501

        :param core_vddc: The core_vddc of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._core_vddc = core_vddc

    @property
    def mem_clock(self):
        """Gets the mem_clock of this OCConfigAmd.  # noqa: E501

        Memory Clock (Mhz)  # noqa: E501

        :return: The mem_clock of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._mem_clock

    @mem_clock.setter
    def mem_clock(self, mem_clock):
        """Sets the mem_clock of this OCConfigAmd.

        Memory Clock (Mhz)  # noqa: E501

        :param mem_clock: The mem_clock of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._mem_clock = mem_clock

    @property
    def mem_state(self):
        """Gets the mem_state of this OCConfigAmd.  # noqa: E501

        Mem State (Index)  # noqa: E501

        :return: The mem_state of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._mem_state

    @mem_state.setter
    def mem_state(self, mem_state):
        """Sets the mem_state of this OCConfigAmd.

        Mem State (Index)  # noqa: E501

        :param mem_state: The mem_state of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._mem_state = mem_state

    @property
    def mem_mvdd(self):
        """Gets the mem_mvdd of this OCConfigAmd.  # noqa: E501

        Memory voltage (mV)  # noqa: E501

        :return: The mem_mvdd of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._mem_mvdd

    @mem_mvdd.setter
    def mem_mvdd(self, mem_mvdd):
        """Sets the mem_mvdd of this OCConfigAmd.

        Memory voltage (mV)  # noqa: E501

        :param mem_mvdd: The mem_mvdd of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._mem_mvdd = mem_mvdd

    @property
    def mem_vddci(self):
        """Gets the mem_vddci of this OCConfigAmd.  # noqa: E501

        Memory bus voltage (mV)  # noqa: E501

        :return: The mem_vddci of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._mem_vddci

    @mem_vddci.setter
    def mem_vddci(self, mem_vddci):
        """Sets the mem_vddci of this OCConfigAmd.

        Memory bus voltage (mV)  # noqa: E501

        :param mem_vddci: The mem_vddci of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._mem_vddci = mem_vddci

    @property
    def fan_speed(self):
        """Gets the fan_speed of this OCConfigAmd.  # noqa: E501

        Fan (%)  # noqa: E501

        :return: The fan_speed of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._fan_speed

    @fan_speed.setter
    def fan_speed(self, fan_speed):
        """Sets the fan_speed of this OCConfigAmd.

        Fan (%)  # noqa: E501

        :param fan_speed: The fan_speed of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._fan_speed = fan_speed

    @property
    def power_limit(self):
        """Gets the power_limit of this OCConfigAmd.  # noqa: E501

        Power Limit (W) (0 for stock value)  # noqa: E501

        :return: The power_limit of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._power_limit

    @power_limit.setter
    def power_limit(self, power_limit):
        """Sets the power_limit of this OCConfigAmd.

        Power Limit (W) (0 for stock value)  # noqa: E501

        :param power_limit: The power_limit of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._power_limit = power_limit

    @property
    def tref_timing(self):
        """Gets the tref_timing of this OCConfigAmd.  # noqa: E501


        :return: The tref_timing of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._tref_timing

    @tref_timing.setter
    def tref_timing(self, tref_timing):
        """Sets the tref_timing of this OCConfigAmd.


        :param tref_timing: The tref_timing of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._tref_timing = tref_timing

    @property
    def soc_clock(self):
        """Gets the soc_clock of this OCConfigAmd.  # noqa: E501

        SoC clock (MHz)  # noqa: E501

        :return: The soc_clock of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._soc_clock

    @soc_clock.setter
    def soc_clock(self, soc_clock):
        """Sets the soc_clock of this OCConfigAmd.

        SoC clock (MHz)  # noqa: E501

        :param soc_clock: The soc_clock of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._soc_clock = soc_clock

    @property
    def soc_vddmax(self):
        """Gets the soc_vddmax of this OCConfigAmd.  # noqa: E501

        SoC maximum voltage (mV)  # noqa: E501

        :return: The soc_vddmax of this OCConfigAmd.  # noqa: E501
        :rtype: str
        """
        return self._soc_vddmax

    @soc_vddmax.setter
    def soc_vddmax(self, soc_vddmax):
        """Sets the soc_vddmax of this OCConfigAmd.

        SoC maximum voltage (mV)  # noqa: E501

        :param soc_vddmax: The soc_vddmax of this OCConfigAmd.  # noqa: E501
        :type: str
        """

        self._soc_vddmax = soc_vddmax

    @property
    def aggressive(self):
        """Gets the aggressive of this OCConfigAmd.  # noqa: E501

        Aggressive undervolting (set OC for each DPM state)  # noqa: E501

        :return: The aggressive of this OCConfigAmd.  # noqa: E501
        :rtype: bool
        """
        return self._aggressive

    @aggressive.setter
    def aggressive(self, aggressive):
        """Sets the aggressive of this OCConfigAmd.

        Aggressive undervolting (set OC for each DPM state)  # noqa: E501

        :param aggressive: The aggressive of this OCConfigAmd.  # noqa: E501
        :type: bool
        """

        self._aggressive = aggressive

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
        if issubclass(OCConfigAmd, dict):
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
        if not isinstance(other, OCConfigAmd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OCConfigAmd):
            return True

        return self.to_dict() != other.to_dict()