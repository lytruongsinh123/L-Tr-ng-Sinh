from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from django.utils.html import mark_safe
# Register your models here.
from .models import Post, Comment
class CommentInline(admin.TabularInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date','image_thumbnail']
    list_filter = ['date']
    search_fields = ['title','id']
    inlines = [CommentInline]

    def image_thumbnail(self, obj):
        if obj.image:  # Kiểm tra xem đối tượng có ảnh hay không
            return mark_safe('<img src="{}" style="height: 100px;" />'.format(obj.image.url))
        else:
            return '(No image)'  # Nếu không có ảnh, trả về chuỗi "(No image)"

    image_thumbnail.allow_tags = True
class CustomUserAdmin(UserAdmin):
    # Define the fields to be used in displaying the User model.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'birth_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'bio', 'birth_date'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post,PostAdmin)