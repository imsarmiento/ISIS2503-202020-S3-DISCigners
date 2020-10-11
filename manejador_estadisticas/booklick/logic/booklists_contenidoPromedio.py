from manejador_contenido.models import Booklist

def get_all_booklists():
    booklists = Booklist.objects.all()
    return booklists
    
    