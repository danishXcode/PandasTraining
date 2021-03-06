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


class FarmStats(object):
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
        'workers_total': 'int',
        'workers_online': 'int',
        'workers_offline': 'int',
        'workers_overheated': 'int',
        'workers_overloaded': 'int',
        'workers_invalid': 'int',
        'workers_low_asr': 'int',
        'rigs_total': 'int',
        'rigs_online': 'int',
        'rigs_offline': 'int',
        'gpus_total': 'int',
        'gpus_online': 'int',
        'gpus_offline': 'int',
        'gpus_overheated': 'int',
        'asics_total': 'int',
        'asics_online': 'int',
        'asics_offline': 'int',
        'boards_total': 'int',
        'boards_online': 'int',
        'boards_offline': 'int',
        'boards_overheated': 'int',
        'cpus_online': 'int',
        'devices_total': 'int',
        'devices_online': 'int',
        'devices_offline': 'int',
        'power_draw': 'float',
        'power_cost': 'float',
        'asr': 'float'
    }

    attribute_map = {
        'workers_total': 'workers_total',
        'workers_online': 'workers_online',
        'workers_offline': 'workers_offline',
        'workers_overheated': 'workers_overheated',
        'workers_overloaded': 'workers_overloaded',
        'workers_invalid': 'workers_invalid',
        'workers_low_asr': 'workers_low_asr',
        'rigs_total': 'rigs_total',
        'rigs_online': 'rigs_online',
        'rigs_offline': 'rigs_offline',
        'gpus_total': 'gpus_total',
        'gpus_online': 'gpus_online',
        'gpus_offline': 'gpus_offline',
        'gpus_overheated': 'gpus_overheated',
        'asics_total': 'asics_total',
        'asics_online': 'asics_online',
        'asics_offline': 'asics_offline',
        'boards_total': 'boards_total',
        'boards_online': 'boards_online',
        'boards_offline': 'boards_offline',
        'boards_overheated': 'boards_overheated',
        'cpus_online': 'cpus_online',
        'devices_total': 'devices_total',
        'devices_online': 'devices_online',
        'devices_offline': 'devices_offline',
        'power_draw': 'power_draw',
        'power_cost': 'power_cost',
        'asr': 'asr'
    }

    def __init__(self, workers_total=None, workers_online=None, workers_offline=None, workers_overheated=None, workers_overloaded=None, workers_invalid=None, workers_low_asr=None, rigs_total=None, rigs_online=None, rigs_offline=None, gpus_total=None, gpus_online=None, gpus_offline=None, gpus_overheated=None, asics_total=None, asics_online=None, asics_offline=None, boards_total=None, boards_online=None, boards_offline=None, boards_overheated=None, cpus_online=None, devices_total=None, devices_online=None, devices_offline=None, power_draw=None, power_cost=None, asr=None, _configuration=None):  # noqa: E501
        """FarmStats - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._workers_total = None
        self._workers_online = None
        self._workers_offline = None
        self._workers_overheated = None
        self._workers_overloaded = None
        self._workers_invalid = None
        self._workers_low_asr = None
        self._rigs_total = None
        self._rigs_online = None
        self._rigs_offline = None
        self._gpus_total = None
        self._gpus_online = None
        self._gpus_offline = None
        self._gpus_overheated = None
        self._asics_total = None
        self._asics_online = None
        self._asics_offline = None
        self._boards_total = None
        self._boards_online = None
        self._boards_offline = None
        self._boards_overheated = None
        self._cpus_online = None
        self._devices_total = None
        self._devices_online = None
        self._devices_offline = None
        self._power_draw = None
        self._power_cost = None
        self._asr = None
        self.discriminator = None

        if workers_total is not None:
            self.workers_total = workers_total
        if workers_online is not None:
            self.workers_online = workers_online
        if workers_offline is not None:
            self.workers_offline = workers_offline
        if workers_overheated is not None:
            self.workers_overheated = workers_overheated
        if workers_overloaded is not None:
            self.workers_overloaded = workers_overloaded
        if workers_invalid is not None:
            self.workers_invalid = workers_invalid
        if workers_low_asr is not None:
            self.workers_low_asr = workers_low_asr
        if rigs_total is not None:
            self.rigs_total = rigs_total
        if rigs_online is not None:
            self.rigs_online = rigs_online
        if rigs_offline is not None:
            self.rigs_offline = rigs_offline
        if gpus_total is not None:
            self.gpus_total = gpus_total
        if gpus_online is not None:
            self.gpus_online = gpus_online
        if gpus_offline is not None:
            self.gpus_offline = gpus_offline
        if gpus_overheated is not None:
            self.gpus_overheated = gpus_overheated
        if asics_total is not None:
            self.asics_total = asics_total
        if asics_online is not None:
            self.asics_online = asics_online
        if asics_offline is not None:
            self.asics_offline = asics_offline
        if boards_total is not None:
            self.boards_total = boards_total
        if boards_online is not None:
            self.boards_online = boards_online
        if boards_offline is not None:
            self.boards_offline = boards_offline
        if boards_overheated is not None:
            self.boards_overheated = boards_overheated
        if cpus_online is not None:
            self.cpus_online = cpus_online
        if devices_total is not None:
            self.devices_total = devices_total
        if devices_online is not None:
            self.devices_online = devices_online
        if devices_offline is not None:
            self.devices_offline = devices_offline
        if power_draw is not None:
            self.power_draw = power_draw
        if power_cost is not None:
            self.power_cost = power_cost
        if asr is not None:
            self.asr = asr

    @property
    def workers_total(self):
        """Gets the workers_total of this FarmStats.  # noqa: E501

        Total amount of workers  # noqa: E501

        :return: The workers_total of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._workers_total

    @workers_total.setter
    def workers_total(self, workers_total):
        """Sets the workers_total of this FarmStats.

        Total amount of workers  # noqa: E501

        :param workers_total: The workers_total of this FarmStats.  # noqa: E501
        :type: int
        """

        self._workers_total = workers_total

    @property
    def workers_online(self):
        """Gets the workers_online of this FarmStats.  # noqa: E501

        Amount of online workers  # noqa: E501

        :return: The workers_online of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._workers_online

    @workers_online.setter
    def workers_online(self, workers_online):
        """Sets the workers_online of this FarmStats.

        Amount of online workers  # noqa: E501

        :param workers_online: The workers_online of this FarmStats.  # noqa: E501
        :type: int
        """

        self._workers_online = workers_online

    @property
    def workers_offline(self):
        """Gets the workers_offline of this FarmStats.  # noqa: E501

        Amount of offline workers  # noqa: E501

        :return: The workers_offline of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._workers_offline

    @workers_offline.setter
    def workers_offline(self, workers_offline):
        """Sets the workers_offline of this FarmStats.

        Amount of offline workers  # noqa: E501

        :param workers_offline: The workers_offline of this FarmStats.  # noqa: E501
        :type: int
        """

        self._workers_offline = workers_offline

    @property
    def workers_overheated(self):
        """Gets the workers_overheated of this FarmStats.  # noqa: E501

        Amount of overheated workers (GPUs/boards exceeds red value)  # noqa: E501

        :return: The workers_overheated of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._workers_overheated

    @workers_overheated.setter
    def workers_overheated(self, workers_overheated):
        """Sets the workers_overheated of this FarmStats.

        Amount of overheated workers (GPUs/boards exceeds red value)  # noqa: E501

        :param workers_overheated: The workers_overheated of this FarmStats.  # noqa: E501
        :type: int
        """

        self._workers_overheated = workers_overheated

    @property
    def workers_overloaded(self):
        """Gets the workers_overloaded of this FarmStats.  # noqa: E501

        Amount of overloaded workers (15m CPU load average exceeds red value)  # noqa: E501

        :return: The workers_overloaded of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._workers_overloaded

    @workers_overloaded.setter
    def workers_overloaded(self, workers_overloaded):
        """Sets the workers_overloaded of this FarmStats.

        Amount of overloaded workers (15m CPU load average exceeds red value)  # noqa: E501

        :param workers_overloaded: The workers_overloaded of this FarmStats.  # noqa: E501
        :type: int
        """

        self._workers_overloaded = workers_overloaded

    @property
    def workers_invalid(self):
        """Gets the workers_invalid of this FarmStats.  # noqa: E501

        Amount of workers with invalid shares  # noqa: E501

        :return: The workers_invalid of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._workers_invalid

    @workers_invalid.setter
    def workers_invalid(self, workers_invalid):
        """Sets the workers_invalid of this FarmStats.

        Amount of workers with invalid shares  # noqa: E501

        :param workers_invalid: The workers_invalid of this FarmStats.  # noqa: E501
        :type: int
        """

        self._workers_invalid = workers_invalid

    @property
    def workers_low_asr(self):
        """Gets the workers_low_asr of this FarmStats.  # noqa: E501

        Amount of workers with low Accepted Shares Ratio (ASR is below red value)  # noqa: E501

        :return: The workers_low_asr of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._workers_low_asr

    @workers_low_asr.setter
    def workers_low_asr(self, workers_low_asr):
        """Sets the workers_low_asr of this FarmStats.

        Amount of workers with low Accepted Shares Ratio (ASR is below red value)  # noqa: E501

        :param workers_low_asr: The workers_low_asr of this FarmStats.  # noqa: E501
        :type: int
        """

        self._workers_low_asr = workers_low_asr

    @property
    def rigs_total(self):
        """Gets the rigs_total of this FarmStats.  # noqa: E501

        Total amount of Rigs  # noqa: E501

        :return: The rigs_total of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._rigs_total

    @rigs_total.setter
    def rigs_total(self, rigs_total):
        """Sets the rigs_total of this FarmStats.

        Total amount of Rigs  # noqa: E501

        :param rigs_total: The rigs_total of this FarmStats.  # noqa: E501
        :type: int
        """

        self._rigs_total = rigs_total

    @property
    def rigs_online(self):
        """Gets the rigs_online of this FarmStats.  # noqa: E501

        Amount of online Rigs  # noqa: E501

        :return: The rigs_online of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._rigs_online

    @rigs_online.setter
    def rigs_online(self, rigs_online):
        """Sets the rigs_online of this FarmStats.

        Amount of online Rigs  # noqa: E501

        :param rigs_online: The rigs_online of this FarmStats.  # noqa: E501
        :type: int
        """

        self._rigs_online = rigs_online

    @property
    def rigs_offline(self):
        """Gets the rigs_offline of this FarmStats.  # noqa: E501

        Amount of offline Rigs  # noqa: E501

        :return: The rigs_offline of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._rigs_offline

    @rigs_offline.setter
    def rigs_offline(self, rigs_offline):
        """Sets the rigs_offline of this FarmStats.

        Amount of offline Rigs  # noqa: E501

        :param rigs_offline: The rigs_offline of this FarmStats.  # noqa: E501
        :type: int
        """

        self._rigs_offline = rigs_offline

    @property
    def gpus_total(self):
        """Gets the gpus_total of this FarmStats.  # noqa: E501

        Total amount of GPUs  # noqa: E501

        :return: The gpus_total of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._gpus_total

    @gpus_total.setter
    def gpus_total(self, gpus_total):
        """Sets the gpus_total of this FarmStats.

        Total amount of GPUs  # noqa: E501

        :param gpus_total: The gpus_total of this FarmStats.  # noqa: E501
        :type: int
        """

        self._gpus_total = gpus_total

    @property
    def gpus_online(self):
        """Gets the gpus_online of this FarmStats.  # noqa: E501

        Amount of online GPUs  # noqa: E501

        :return: The gpus_online of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._gpus_online

    @gpus_online.setter
    def gpus_online(self, gpus_online):
        """Sets the gpus_online of this FarmStats.

        Amount of online GPUs  # noqa: E501

        :param gpus_online: The gpus_online of this FarmStats.  # noqa: E501
        :type: int
        """

        self._gpus_online = gpus_online

    @property
    def gpus_offline(self):
        """Gets the gpus_offline of this FarmStats.  # noqa: E501

        Amount of offline GPUs  # noqa: E501

        :return: The gpus_offline of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._gpus_offline

    @gpus_offline.setter
    def gpus_offline(self, gpus_offline):
        """Sets the gpus_offline of this FarmStats.

        Amount of offline GPUs  # noqa: E501

        :param gpus_offline: The gpus_offline of this FarmStats.  # noqa: E501
        :type: int
        """

        self._gpus_offline = gpus_offline

    @property
    def gpus_overheated(self):
        """Gets the gpus_overheated of this FarmStats.  # noqa: E501

        Amount of overheated GPUs  # noqa: E501

        :return: The gpus_overheated of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._gpus_overheated

    @gpus_overheated.setter
    def gpus_overheated(self, gpus_overheated):
        """Sets the gpus_overheated of this FarmStats.

        Amount of overheated GPUs  # noqa: E501

        :param gpus_overheated: The gpus_overheated of this FarmStats.  # noqa: E501
        :type: int
        """

        self._gpus_overheated = gpus_overheated

    @property
    def asics_total(self):
        """Gets the asics_total of this FarmStats.  # noqa: E501

        Total amount of ASICs  # noqa: E501

        :return: The asics_total of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._asics_total

    @asics_total.setter
    def asics_total(self, asics_total):
        """Sets the asics_total of this FarmStats.

        Total amount of ASICs  # noqa: E501

        :param asics_total: The asics_total of this FarmStats.  # noqa: E501
        :type: int
        """

        self._asics_total = asics_total

    @property
    def asics_online(self):
        """Gets the asics_online of this FarmStats.  # noqa: E501

        Amount of online ASICs  # noqa: E501

        :return: The asics_online of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._asics_online

    @asics_online.setter
    def asics_online(self, asics_online):
        """Sets the asics_online of this FarmStats.

        Amount of online ASICs  # noqa: E501

        :param asics_online: The asics_online of this FarmStats.  # noqa: E501
        :type: int
        """

        self._asics_online = asics_online

    @property
    def asics_offline(self):
        """Gets the asics_offline of this FarmStats.  # noqa: E501

        Amount of offline ASICs  # noqa: E501

        :return: The asics_offline of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._asics_offline

    @asics_offline.setter
    def asics_offline(self, asics_offline):
        """Sets the asics_offline of this FarmStats.

        Amount of offline ASICs  # noqa: E501

        :param asics_offline: The asics_offline of this FarmStats.  # noqa: E501
        :type: int
        """

        self._asics_offline = asics_offline

    @property
    def boards_total(self):
        """Gets the boards_total of this FarmStats.  # noqa: E501

        Total amount of ASIC boards  # noqa: E501

        :return: The boards_total of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._boards_total

    @boards_total.setter
    def boards_total(self, boards_total):
        """Sets the boards_total of this FarmStats.

        Total amount of ASIC boards  # noqa: E501

        :param boards_total: The boards_total of this FarmStats.  # noqa: E501
        :type: int
        """

        self._boards_total = boards_total

    @property
    def boards_online(self):
        """Gets the boards_online of this FarmStats.  # noqa: E501

        Amount of online ASIC boards  # noqa: E501

        :return: The boards_online of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._boards_online

    @boards_online.setter
    def boards_online(self, boards_online):
        """Sets the boards_online of this FarmStats.

        Amount of online ASIC boards  # noqa: E501

        :param boards_online: The boards_online of this FarmStats.  # noqa: E501
        :type: int
        """

        self._boards_online = boards_online

    @property
    def boards_offline(self):
        """Gets the boards_offline of this FarmStats.  # noqa: E501

        Amount of offline ASIC boards  # noqa: E501

        :return: The boards_offline of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._boards_offline

    @boards_offline.setter
    def boards_offline(self, boards_offline):
        """Sets the boards_offline of this FarmStats.

        Amount of offline ASIC boards  # noqa: E501

        :param boards_offline: The boards_offline of this FarmStats.  # noqa: E501
        :type: int
        """

        self._boards_offline = boards_offline

    @property
    def boards_overheated(self):
        """Gets the boards_overheated of this FarmStats.  # noqa: E501

        Amount of overheated ASIC boards  # noqa: E501

        :return: The boards_overheated of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._boards_overheated

    @boards_overheated.setter
    def boards_overheated(self, boards_overheated):
        """Sets the boards_overheated of this FarmStats.

        Amount of overheated ASIC boards  # noqa: E501

        :param boards_overheated: The boards_overheated of this FarmStats.  # noqa: E501
        :type: int
        """

        self._boards_overheated = boards_overheated

    @property
    def cpus_online(self):
        """Gets the cpus_online of this FarmStats.  # noqa: E501

        Amount of online CPUs  # noqa: E501

        :return: The cpus_online of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._cpus_online

    @cpus_online.setter
    def cpus_online(self, cpus_online):
        """Sets the cpus_online of this FarmStats.

        Amount of online CPUs  # noqa: E501

        :param cpus_online: The cpus_online of this FarmStats.  # noqa: E501
        :type: int
        """

        self._cpus_online = cpus_online

    @property
    def devices_total(self):
        """Gets the devices_total of this FarmStats.  # noqa: E501

        Total amount of Devices  # noqa: E501

        :return: The devices_total of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._devices_total

    @devices_total.setter
    def devices_total(self, devices_total):
        """Sets the devices_total of this FarmStats.

        Total amount of Devices  # noqa: E501

        :param devices_total: The devices_total of this FarmStats.  # noqa: E501
        :type: int
        """

        self._devices_total = devices_total

    @property
    def devices_online(self):
        """Gets the devices_online of this FarmStats.  # noqa: E501

        Amount of online Devices  # noqa: E501

        :return: The devices_online of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._devices_online

    @devices_online.setter
    def devices_online(self, devices_online):
        """Sets the devices_online of this FarmStats.

        Amount of online Devices  # noqa: E501

        :param devices_online: The devices_online of this FarmStats.  # noqa: E501
        :type: int
        """

        self._devices_online = devices_online

    @property
    def devices_offline(self):
        """Gets the devices_offline of this FarmStats.  # noqa: E501

        Amount of offline Devices  # noqa: E501

        :return: The devices_offline of this FarmStats.  # noqa: E501
        :rtype: int
        """
        return self._devices_offline

    @devices_offline.setter
    def devices_offline(self, devices_offline):
        """Sets the devices_offline of this FarmStats.

        Amount of offline Devices  # noqa: E501

        :param devices_offline: The devices_offline of this FarmStats.  # noqa: E501
        :type: int
        """

        self._devices_offline = devices_offline

    @property
    def power_draw(self):
        """Gets the power_draw of this FarmStats.  # noqa: E501

        Total power draw of all workers  # noqa: E501

        :return: The power_draw of this FarmStats.  # noqa: E501
        :rtype: float
        """
        return self._power_draw

    @power_draw.setter
    def power_draw(self, power_draw):
        """Sets the power_draw of this FarmStats.

        Total power draw of all workers  # noqa: E501

        :param power_draw: The power_draw of this FarmStats.  # noqa: E501
        :type: float
        """

        self._power_draw = power_draw

    @property
    def power_cost(self):
        """Gets the power_cost of this FarmStats.  # noqa: E501

        Consuming electricity cost per hour (in configured currency)  # noqa: E501

        :return: The power_cost of this FarmStats.  # noqa: E501
        :rtype: float
        """
        return self._power_cost

    @power_cost.setter
    def power_cost(self, power_cost):
        """Sets the power_cost of this FarmStats.

        Consuming electricity cost per hour (in configured currency)  # noqa: E501

        :param power_cost: The power_cost of this FarmStats.  # noqa: E501
        :type: float
        """

        self._power_cost = power_cost

    @property
    def asr(self):
        """Gets the asr of this FarmStats.  # noqa: E501

        Accepted Shares Ratio, % Calculated as: `accepted_shares / total_shares * 100`   # noqa: E501

        :return: The asr of this FarmStats.  # noqa: E501
        :rtype: float
        """
        return self._asr

    @asr.setter
    def asr(self, asr):
        """Sets the asr of this FarmStats.

        Accepted Shares Ratio, % Calculated as: `accepted_shares / total_shares * 100`   # noqa: E501

        :param asr: The asr of this FarmStats.  # noqa: E501
        :type: float
        """

        self._asr = asr

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
        if issubclass(FarmStats, dict):
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
        if not isinstance(other, FarmStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FarmStats):
            return True

        return self.to_dict() != other.to_dict()
