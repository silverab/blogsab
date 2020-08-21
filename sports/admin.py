from django.contrib import admin
from .models import Category, LPost, RPost, CPost, MiniCPost, AsiaPost



admin.site.register(Category)

class AsiaPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = AsiaPost

admin.site.register(AsiaPost, AsiaPostAdmin)

class LPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = LPost

admin.site.register(LPost, LPostAdmin)

class CPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = CPost

admin.site.register(CPost, CPostAdmin)

class MiniCPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = MiniCPost

admin.site.register(MiniCPost, MiniCPostAdmin)

class RPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = RPost

admin.site.register(RPost, RPostAdmin)