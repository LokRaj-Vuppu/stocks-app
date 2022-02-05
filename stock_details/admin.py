from django.contrib import admin
from stock_details.models import Stocks, StockUser, Song, Album, Director, Movie

admin.site.register(Stocks)
# admin.site.register(StockUser)
# admin.site.register(Album)
# admin.site.register(Song)
admin.site.register(Director)
admin.site.register(Movie)

@admin.register(StockUser)
class UserAdminListView(admin.ModelAdmin):
    list_display = ('user_name', 'age', 'salary', 'city', 'state')


# @admin.register(NewsItem)
# class NewsItemAdminView(admin.ModelAdmin):
#     list_display = ('source', 'link', 'title','published_date')
