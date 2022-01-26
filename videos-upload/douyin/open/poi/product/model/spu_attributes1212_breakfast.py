# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class SpuAttributes1212Breakfast(object):
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
        'type': 'int',
        'price': 'int'
    }

    attribute_map = {
        'type': 'type',
        'price': 'price'
    }

    def __init__(self, type=None, price=None):  # noqa: E501
        """SpuAttributes1212Breakfast - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._price = None
        self.discriminator = None
        self.type = type
        self.price = price

    @property
    def type(self):
        """Gets the type of this SpuAttributes1212Breakfast.  # noqa: E501

        加早类型; 0 - 不支持加早; 1 - 早餐; 2 - 自助早餐  # noqa: E501

        :return: The type of this SpuAttributes1212Breakfast.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SpuAttributes1212Breakfast.

        加早类型; 0 - 不支持加早; 1 - 早餐; 2 - 自助早餐  # noqa: E501

        :param type: The type of this SpuAttributes1212Breakfast.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = [0, 1, 2]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def price(self):
        """Gets the price of this SpuAttributes1212Breakfast.  # noqa: E501

        加早费用/每人，单位人民币分 不支持加早填0  # noqa: E501

        :return: The price of this SpuAttributes1212Breakfast.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SpuAttributes1212Breakfast.

        加早费用/每人，单位人民币分 不支持加早填0  # noqa: E501

        :param price: The price of this SpuAttributes1212Breakfast.  # noqa: E501
        :type: int
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

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
        if issubclass(SpuAttributes1212Breakfast, dict):
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
        if not isinstance(other, SpuAttributes1212Breakfast):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
