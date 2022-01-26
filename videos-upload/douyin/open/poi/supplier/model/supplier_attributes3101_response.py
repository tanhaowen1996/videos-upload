# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class SupplierAttributes3101Response(object):
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
        'population': 'str',
        'condition': 'str',
        'discount': 'str'
    }

    attribute_map = {
        'population': 'population',
        'condition': 'condition',
        'discount': 'discount'
    }

    def __init__(self, population=None, condition=None, discount=None):  # noqa: E501
        """SupplierAttributes3101Response - a model defined in Swagger"""  # noqa: E501
        self._population = None
        self._condition = None
        self._discount = None
        self.discriminator = None
        if population is not None:
            self.population = population
        if condition is not None:
            self.condition = condition
        if discount is not None:
            self.discount = discount

    @property
    def population(self):
        """Gets the population of this SupplierAttributes3101Response.  # noqa: E501

        优待政策-人群(婴儿、儿童、老人、军人、残障人士，不超过30个汉字)  # noqa: E501

        :return: The population of this SupplierAttributes3101Response.  # noqa: E501
        :rtype: str
        """
        return self._population

    @population.setter
    def population(self, population):
        """Sets the population of this SupplierAttributes3101Response.

        优待政策-人群(婴儿、儿童、老人、军人、残障人士，不超过30个汉字)  # noqa: E501

        :param population: The population of this SupplierAttributes3101Response.  # noqa: E501
        :type: str
        """

        self._population = population

    @property
    def condition(self):
        """Gets the condition of this SupplierAttributes3101Response.  # noqa: E501

        优待政策-适用条件(不超过200个汉字)  # noqa: E501

        :return: The condition of this SupplierAttributes3101Response.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this SupplierAttributes3101Response.

        优待政策-适用条件(不超过200个汉字)  # noqa: E501

        :param condition: The condition of this SupplierAttributes3101Response.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def discount(self):
        """Gets the discount of this SupplierAttributes3101Response.  # noqa: E501

        优待政策-优待内容(免费、优惠、半价)  # noqa: E501

        :return: The discount of this SupplierAttributes3101Response.  # noqa: E501
        :rtype: str
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this SupplierAttributes3101Response.

        优待政策-优待内容(免费、优惠、半价)  # noqa: E501

        :param discount: The discount of this SupplierAttributes3101Response.  # noqa: E501
        :type: str
        """

        self._discount = discount

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
        if issubclass(SupplierAttributes3101Response, dict):
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
        if not isinstance(other, SupplierAttributes3101Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
