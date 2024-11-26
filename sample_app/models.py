"""このモジュールは、ソーシャルメディアの投稿を管理するためのDjangoモデルを定義します。

クラス:
    Post: ユーザーが投稿するソーシャルメディアの投稿を表すモデル。
"""

from django.db import models


class Post(models.Model):
    """ユーザーが投稿したソーシャルメディアの投稿を表すモデル。

    属性:
        name: 投稿者の名前を表します。
        micropost: 投稿内容を表します。
    """

    name: str = models.CharField("user name", max_length=15)
    micropost: str = models.CharField("tweet", max_length=140, blank=True)

    def __str__(self) -> str:
        """投稿者の名前を文字列として返します。

        戻り値:
            str: 投稿者の名前。
        """
        return self.name
