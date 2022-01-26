# coding: utf-8

"""
    获取应用推送事件订阅状态

    通过access_token查询该应用事件订阅状态

    
"""

import pprint
import re  # noqa: F401

import six


class PersonalTabContact(object):
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
        'event': 'str',
        'from_user_id': 'str',
        'to_user_id': 'str',
        'client_key': 'str'
    }

    attribute_map = {
        'event': 'event',
        'from_user_id': 'from_user_id',
        'to_user_id': 'to_user_id',
        'client_key': 'client_key'
    }

    def __init__(self, event=None, from_user_id=None, to_user_id=None, client_key=None):  # noqa: E501
        """PersonalTabContact - a model defined in Swagger"""  # noqa: E501
        self._event = None
        self._from_user_id = None
        self._to_user_id = None
        self._client_key = None
        self.discriminator = None
        if event is not None:
            self.event = event
        if from_user_id is not None:
            self.from_user_id = from_user_id
        if to_user_id is not None:
            self.to_user_id = to_user_id
        if client_key is not None:
            self.client_key = client_key

    @property
    def event(self):
        """Gets the event of this PersonalTabContact.  # noqa: E501

        事件名为personal_tab_contact  # noqa: E501

        :return: The event of this PersonalTabContact.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this PersonalTabContact.

        事件名为personal_tab_contact  # noqa: E501

        :param event: The event of this PersonalTabContact.  # noqa: E501
        :type: str
        """

        self._event = event

    @property
    def from_user_id(self):
        """Gets the from_user_id of this PersonalTabContact.  # noqa: E501

        事件发起用户user_id  # noqa: E501

        :return: The from_user_id of this PersonalTabContact.  # noqa: E501
        :rtype: str
        """
        return self._from_user_id

    @from_user_id.setter
    def from_user_id(self, from_user_id):
        """Sets the from_user_id of this PersonalTabContact.

        事件发起用户user_id  # noqa: E501

        :param from_user_id: The from_user_id of this PersonalTabContact.  # noqa: E501
        :type: str
        """

        self._from_user_id = from_user_id

    @property
    def to_user_id(self):
        """Gets the to_user_id of this PersonalTabContact.  # noqa: E501

        事件接收用户user_id  # noqa: E501

        :return: The to_user_id of this PersonalTabContact.  # noqa: E501
        :rtype: str
        """
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, to_user_id):
        """Sets the to_user_id of this PersonalTabContact.

        事件接收用户user_id  # noqa: E501

        :param to_user_id: The to_user_id of this PersonalTabContact.  # noqa: E501
        :type: str
        """

        self._to_user_id = to_user_id

    @property
    def client_key(self):
        """Gets the client_key of this PersonalTabContact.  # noqa: E501

        使用应用的client_key  # noqa: E501

        :return: The client_key of this PersonalTabContact.  # noqa: E501
        :rtype: str
        """
        return self._client_key

    @client_key.setter
    def client_key(self, client_key):
        """Sets the client_key of this PersonalTabContact.

        使用应用的client_key  # noqa: E501

        :param client_key: The client_key of this PersonalTabContact.  # noqa: E501
        :type: str
        """

        self._client_key = client_key

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
        if issubclass(PersonalTabContact, dict):
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
        if not isinstance(other, PersonalTabContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
