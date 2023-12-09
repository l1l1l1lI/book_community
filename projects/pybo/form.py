from django import forms

from pybo.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['subject', 'content']
        labels = {
            'book_name': '책 제목',
            'subject': '주제',
            'writer': '작가',
            'number_of_pages': '쪽 수'
        }