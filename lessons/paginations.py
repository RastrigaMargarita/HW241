from rest_framework import pagination


class PagePagination(pagination.PageNumberPagination):
    page_size = 10  # Количество элементов на странице
    page_size_query_param = 'page_size'
    max_page_size = 15  # Максимальное количество элементов
