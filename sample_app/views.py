"""このモジュールは、Djangoアプリケーション「sample_app」のビューを定義します。

ユーザーが投稿データを操作するための機能を提供します。

クラス:
    PostForm: Postモデルに基づくフォームを提供します。

関数:
    create_post: 新しい投稿を作成します。
    read_post: 投稿データの一覧を表示します。
    edit_post: 指定された投稿を編集します。
    delete_post: 指定された投稿を削除します。
"""

from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from sample_app.models import Post


def create_post(request: HttpRequest) -> HttpResponse:
    """新規に投稿を作成する。

    Args:
        request: HTTPリクエストオブジェクト。

    Returns:
        HttpResponse: テンプレートをレンダリングしたレスポンス。

    """
    # オブジェクトを新規作成する
    post = Post()

    # ページロード時
    if request.method == "GET":
        # 新規作成オブジェクトにより form を作成
        form = PostForm(instance=post)

        # ページロード時は form を Template に渡す
        return render(
            request,
            "sample_app/post_form.html",  # 呼び出す Template
            {"form": form},
        )  # Template に渡すデータ

    # 実行ボタン押下時
    if request.method == "POST":
        # POST されたデータにより form を作成
        form = PostForm(request.POST, instance=post)

        # 入力されたデータのバリデーション
        if form.is_valid():
            # チェック結果に問題なければデータを作成する
            post = form.save(commit=False)
            post.save()

        return redirect("sample_app:read_post")
    return None


def read_post(request: HttpRequest) -> HttpResponse:
    """データの一覧を表示する。

    Args:
        request: HTTPリクエストオブジェクト。

    Returns:
        HttpResponse: テンプレートをレンダリングしたレスポンス。

    """
    # 全オブジェクトを取得
    posts = Post.objects.all().order_by("id")
    return render(
        request,
        "sample_app/post_list.html",  # 呼び出す Template
        {"posts": posts},
    )  # Template に渡すデータ


def edit_post(request: HttpRequest, post_id: int) -> HttpResponse:
    """指定された投稿を更新し、投稿一覧画面にリダイレクトする。

    Args:
        request: HTTPリクエストオブジェクト。
        post_id: 更新対象の投稿のID。

    Returns:
        HttpResponse: 投稿一覧画面へのリダイレクトレスポンス。

    """
    # IDを引数に、対象オブジェクトを取得
    post = get_object_or_404(Post, pk=post_id)

    # ページロード時
    if request.method == "GET":
        # 対象オブジェクトにより form を作成
        form = PostForm(instance=post)

        # ページロード時は form とデータIDを Template に渡す
        return render(
            request,
            "sample_app/post_form.html",  # 呼び出す Template
            {"form": form, "post_id": post_id},
        )  # Template に渡すデータ

    # 実行ボタン押下時
    if request.method == "POST":
        # POST されたデータにより form を作成
        form = PostForm(request.POST, instance=post)

        # 入力されたデータのバリデーション
        if form.is_valid():
            # チェック結果に問題なければデータを更新する
            post = form.save(commit=False)
            post.save()

        # 実行ボタン押下時は処理実行後、一覧画面にリダイレクトする
        return redirect("sample_app:read_post")
    return None


def delete_post(_request: HttpRequest, post_id: int) -> HttpResponse:
    """指定された投稿を削除し、投稿一覧画面にリダイレクトする。

    Args:
        request: HTTPリクエストオブジェクト。
        post_id: 削除対象の投稿のID。

    Returns:
        HttpResponse: 投稿一覧画面へのリダイレクトレスポンス。

    """
    # 対象のオブジェクトを取得
    post = get_object_or_404(Post, pk=post_id)
    post.delete()

    # 削除リクエスト時は削除実行後、一覧表示画面へリダイレクトする
    return redirect("sample_app:read_post")


class PostForm(ModelForm):
    """フォーム定義"""

    class Meta:
        """Postモデルと連携するフォームの設定を定義する内部クラス。"""

        model = Post
        # fields は models.py で定義している変数名
        fields = ("name", "micropost")
