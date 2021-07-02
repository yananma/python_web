from django.contrib import admin
from .models import Banner, Category, Teacher, XXUser, Course, StarStudent, Blog
from .models import Tags, BlogCategory, Org, Section, Video, Comment

# Register your models here.
# admin.site.site_title = '后台管理'
# C:\Python36\Lib\site-packages\django\contrib\admin\templates\admin\base_site.html

admin.site.site_header = '在线教育平台后台管理系统'


admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Teacher)
admin.site.register(XXUser)
admin.site.register(StarStudent)
admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(BlogCategory)
admin.site.register(Org)
admin.site.register(Section)
admin.site.register(Video)
admin.site.register(Comment)
# admin.site.register(Icon)
# admin.site.register(Star)



class CourseAdmin(admin.ModelAdmin):
    fields = ['category', 'level', 'title', 'body', 'cover', 'attachment',
            'is_free', 'teacher', 'star', 'price', 'recommend', 'published']

admin.site.register(Course, CourseAdmin)
