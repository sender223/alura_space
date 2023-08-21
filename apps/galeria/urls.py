# AQUI VC CRIA O CAMINHO DAS URLS DE NOVAS PAGINAS.

from django.urls import path
#DEPOIS DE IMPORTAR, PRECISA SER CRIADO DENTRO DE VIEWS.PY A NOVA CLASSE (VIEW)
from apps.galeria.views import \
    index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem, filtro


urlpatterns = [ 
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    #caminho(nome_do_path/parametro_da_url, nome_da_view, e o nome será filtro
    path('filtro/<str:categoria>', filtro, name='filtro'),
]
