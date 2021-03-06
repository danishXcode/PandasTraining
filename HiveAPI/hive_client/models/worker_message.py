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


class WorkerMessage(object):
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
        'id': 'int',
        'title': 'str',
        'type': 'MessageType',
        'time': 'int',
        'cmd_id': 'int',
        'command': 'str',
        'command_result': 'object',
        'has_payload': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'type': 'type',
        'time': 'time',
        'cmd_id': 'cmd_id',
        'command': 'command',
        'command_result': 'command_result',
        'has_payload': 'has_payload'
    }

    def __init__(self, id=None, title=None, type=None, time=None, cmd_id=None, command=None, command_result=None, has_payload=None, _configuration=None):  # noqa: E501
        """WorkerMessage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._title = None
        self._type = None
        self._time = None
        self._cmd_id = None
        self._command = None
        self._command_result = None
        self._has_payload = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if time is not None:
            self.time = time
        if cmd_id is not None:
            self.cmd_id = cmd_id
        if command is not None:
            self.command = command
        if command_result is not None:
            self.command_result = command_result
        if has_payload is not None:
            self.has_payload = has_payload

    @property
    def id(self):
        """Gets the id of this WorkerMessage.  # noqa: E501


        :return: The id of this WorkerMessage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkerMessage.


        :param id: The id of this WorkerMessage.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this WorkerMessage.  # noqa: E501


        :return: The title of this WorkerMessage.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WorkerMessage.


        :param title: The title of this WorkerMessage.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this WorkerMessage.  # noqa: E501


        :return: The type of this WorkerMessage.  # noqa: E501
        :rtype: MessageType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkerMessage.


        :param type: The type of this WorkerMessage.  # noqa: E501
        :type: MessageType
        """

        self._type = type

    @property
    def time(self):
        """Gets the time of this WorkerMessage.  # noqa: E501


        :return: The time of this WorkerMessage.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this WorkerMessage.


        :param time: The time of this WorkerMessage.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def cmd_id(self):
        """Gets the cmd_id of this WorkerMessage.  # noqa: E501

        Command ID for which this message is related to  # noqa: E501

        :return: The cmd_id of this WorkerMessage.  # noqa: E501
        :rtype: int
        """
        return self._cmd_id

    @cmd_id.setter
    def cmd_id(self, cmd_id):
        """Sets the cmd_id of this WorkerMessage.

        Command ID for which this message is related to  # noqa: E501

        :param cmd_id: The cmd_id of this WorkerMessage.  # noqa: E501
        :type: int
        """

        self._cmd_id = cmd_id

    @property
    def command(self):
        """Gets the command of this WorkerMessage.  # noqa: E501

        Command name for which this message is related to  # noqa: E501

        :return: The command of this WorkerMessage.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this WorkerMessage.

        Command name for which this message is related to  # noqa: E501

        :param command: The command of this WorkerMessage.  # noqa: E501
        :type: str
        """

        self._command = command

    @property
    def command_result(self):
        """Gets the command_result of this WorkerMessage.  # noqa: E501

        Result of executed command  # noqa: E501

        :return: The command_result of this WorkerMessage.  # noqa: E501
        :rtype: object
        """
        return self._command_result

    @command_result.setter
    def command_result(self, command_result):
        """Sets the command_result of this WorkerMessage.

        Result of executed command  # noqa: E501

        :param command_result: The command_result of this WorkerMessage.  # noqa: E501
        :type: object
        """

        self._command_result = command_result

    @property
    def has_payload(self):
        """Gets the has_payload of this WorkerMessage.  # noqa: E501


        :return: The has_payload of this WorkerMessage.  # noqa: E501
        :rtype: bool
        """
        return self._has_payload

    @has_payload.setter
    def has_payload(self, has_payload):
        """Sets the has_payload of this WorkerMessage.


        :param has_payload: The has_payload of this WorkerMessage.  # noqa: E501
        :type: bool
        """

        self._has_payload = has_payload

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
        if issubclass(WorkerMessage, dict):
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
        if not isinstance(other, WorkerMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkerMessage):
            return True

        return self.to_dict() != other.to_dict()
