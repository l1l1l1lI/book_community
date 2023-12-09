from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Book


def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어


    # 검색
    if kw:
        book_list = book_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(book_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'book_list': page_obj, 'page': page, 'kw': kw}  # <------ so 추가
    return render(request, 'pybo/book_list.html', context)


def detail(request, book_id):
    """
    pybo 내용 출력
    """
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'pybo/book_detail.html', context)