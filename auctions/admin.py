from django.contrib import admin

from .models import Comment, DashboardPreferences, User, UserProfile



# For the UserProfile model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username',)

admin.site.register(UserProfile, UserProfileAdmin)

# For the DashboardPreferences model
class DashboardPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user', 'preference')
    search_fields = ('user__username', 'preference')

admin.site.register(DashboardPreferences, DashboardPreferencesAdmin)

# For the Comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'content')
    search_fields = ('user__username', 'content')
    list_filter = ('timestamp',)
    date_hierarchy = 'timestamp'

admin.site.register(Comment, CommentAdmin)


# admin.site.register(Watchlist)

# admin.site.register(Category)

# admin.site.register(AuctionListing)

# class BidAdmin(admin.ModelAdmin):
#     list_display = ("id", "listing", "amount")
    
# admin.site.register(Bid, BidAdmin)

