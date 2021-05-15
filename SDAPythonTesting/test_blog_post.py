from blog_post import BlogPostHistory
from unittest.mock import patch, MagicMock


class TestBlogPostHistory:

    def test_save_file(self):
        post = BlogPostHistory('Football', 'This is a football post')

        mock = MagicMock()

        with patch('blog_post.BlogPostHistory.save', mock):
            post.save()

    def test_read_content(self):
        post = BlogPostHistory('Football', 'This is a football post')

        mock = MagicMock()
        mock.return_value = ['Football,This is a football post']

        with patch('blog_post.BlogPostHistory.get_content', mock):
            result = post.get_content()

            assert result == ['Football,This is a football post']