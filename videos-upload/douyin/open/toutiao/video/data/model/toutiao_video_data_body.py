# coding: utf-8

"""

    通过头条视频id批量获取已分享视频数据信息

    
"""

import pprint
import re  # noqa: F401

import six


class ToutiaoVideoDataBody(object):
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
        'item_ids': 'list[str]'
    }

    attribute_map = {
        'item_ids': 'item_ids'
    }

    def __init__(self, item_ids=None):  # noqa: E501
        """ToutiaoVideoDataBody - a model defined in Swagger"""  # noqa: E501
        self._item_ids = None
        self.discriminator = None
        self.item_ids = item_ids

    @property
    def item_ids(self):
        """Gets the item_ids of this ToutiaoVideoDataBody.  # noqa: E501

        item_id数组，支持查询授权用户上传的视频。  # noqa: E501

        :return: The item_ids of this ToutiaoVideoDataBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        """Sets the item_ids of this ToutiaoVideoDataBody.

        item_id数组，支持查询授权用户上传的视频。  # noqa: E501

        :param item_ids: The item_ids of this ToutiaoVideoDataBody.  # noqa: E501
        :type: list[str]
        """
        if item_ids is None:
            raise ValueError("Invalid value for `item_ids`, must not be `None`")  # noqa: E501

        self._item_ids = item_ids

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
        if issubclass(ToutiaoVideoDataBody, dict):
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
        if not isinstance(other, ToutiaoVideoDataBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other