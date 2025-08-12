from django.urls import path
from .views import RegisterAPI, LoginAPI, BookListAPI, BorrowBookAPI, ReturnBookAPI, UserTransactionHistoryAPI, PayFineAPI, BookCreateAPI, BookUpdateAPI, BookDeleteAPI, UserDashboardAPI, OverdueBooksAPI, ExtendDueDateAPI
urlpatterns = [
    path('api/extend-due-date/', ExtendDueDateAPI.as_view(), name='api-extend-due-date'),
    path('api/books/create/', BookCreateAPI.as_view(), name='api-book-create'),
    path('api/books/<int:pk>/update/', BookUpdateAPI.as_view(), name='api-book-update'),
    path('api/books/<int:pk>/delete/', BookDeleteAPI.as_view(), name='api-book-delete'),
    path('api/register/', RegisterAPI.as_view(), name='api-register'),
    path('api/login/', LoginAPI.as_view(), name='api-login'),
    path('api/books/', BookListAPI.as_view(), name='api-books'),
    path('api/borrow/', BorrowBookAPI.as_view(), name='api-borrow'),
    path('api/return/', ReturnBookAPI.as_view(), name='api-return'),
    path('api/transactions/', UserTransactionHistoryAPI.as_view(), name='api-transactions'),
    path('api/pay-fine/', PayFineAPI.as_view(), name='api-pay-fine'),
    path('api/dashboard/', UserDashboardAPI.as_view(), name='api-dashboard'),
    path('api/overdue/', OverdueBooksAPI.as_view(), name='api-overdue'),

]

# urlpatterns += [
    
# ]
