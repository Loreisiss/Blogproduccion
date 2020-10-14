from django.contrib import admin
from .models import Autor,Categoria,Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['nombre']
    list_display=('nombre','estado','fecha_creacion')
    resources_class=CategoriaResource

class AutorResourse(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres','apellidos','correo']
    list_display = ('nombres','apellidos','estado')
    resources_class=AutorResourse

class PostResourse(resources.ModelResource):
    class Meta:
        model = Autor

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','slug','descripcion']
    list_display = ('titulo','slug','descripcion','estado')
    resources_class=PostResourse

# Register your models here.
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)
