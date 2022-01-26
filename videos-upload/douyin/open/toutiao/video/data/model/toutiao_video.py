# coding: utf-8

"""

    通过头条视频id批量获取已分享视频数据信息

    
"""

import pprint
import re  # noqa: F401

import six


class ToutiaoVideo(object):
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
        'item_id': 'str',
        'title': 'str',
        'cover': 'str',
        'create_time': 'int',
        'statistics': 'ToutiaoVideoStatistics'
    }

    attribute_map = {
        'item_id': 'item_id',
        'title': 'title',
        'cover': 'cover',
        'create_time': 'create_time',
        'statistics': 'statistics'
    }

    def __init__(self, item_id=None, title=None, cover=None, create_time=None, statistics=None):  # noqa: E501
        """ToutiaoVideo - a model defined in Swagger"""  # noqa: E501
        self._item_id = None
        self._title = None
        self._cover = None
        self._create_time = None
        self._statistics = None
        self.discriminator = None
        self.item_id = item_id
        self.title = title
        self.cover = cover
        self.create_time = create_time
        self.statistics = statistics

    @property
    def item_id(self):
        """Gets the item_id of this ToutiaoVideo.  # noqa: E501

        视频id  # noqa: E501

        :return: The item_id of this ToutiaoVideo.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this ToutiaoVideo.

        视频id  # noqa: E501

        :param item_id: The item_id of this ToutiaoVideo.  # noqa: E501
        :type: str
        """
        if item_id is None:
            raise ValueError("Invalid value for `item_id`, must not be `None`")  # noqa: E501

        self._item_id = item_id

    @property
    def title(self):
        """Gets the title of this ToutiaoVideo.  # noqa: E501

        视频标题  # noqa: E501

        :return: The title of this ToutiaoVideo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ToutiaoVideo.

        视频标题  # noqa: E501

        :param title: The title of this ToutiaoVideo.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def cover(self):
        """Gets the cover of this ToutiaoVideo.  # noqa: E501

        视频封面  # noqa: E501

        :return: The cover of this ToutiaoVideo.  # noqa: E501
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """Sets the cover of this ToutiaoVideo.

        视频封面  # noqa: E501

        :param cover: The cover of this ToutiaoVideo.  # noqa: E501
        :type: str
        """
        if cover is None:
            raise ValueError("Invalid value for `cover`, must not be `None`")  # noqa: E501

        self._cover = cover

    @property
    def create_time(self):
        """Gets the create_time of this ToutiaoVideo.  # noqa: E501

        视频创建时间戳  # noqa: E501

        :return: The create_time of this ToutiaoVideo.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ToutiaoVideo.

        视频创建时间戳  # noqa: E501

        :param create_time: The create_time of this ToutiaoVideo.  # noqa: E501
        :type: int
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def statistics(self):
        """Gets the statistics of this ToutiaoVideo.  # noqa: E501


        :return: The statistics of this ToutiaoVideo.  # noqa: E501
        :rtype: ToutiaoVideoStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this ToutiaoVideo.


        :param statistics: The statistics of this ToutiaoVideo.  # noqa: E501
        :type: ToutiaoVideoStatistics
        """
        if statistics is None:
            raise ValueError("Invalid value for `statistics`, must not be `None`")  # noqa: E501

        self._statistics = statistics

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
        if issubclass(ToutiaoVideo, dict):
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
        if not isinstance(other, ToutiaoVideo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
