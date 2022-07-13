from django.forms import inlineformset_factory
from photo.models import Album,Photo
#인라인폼셋1:N관계에서 여러레코드불러오는 방법
PhotoInlineFormSet=inlineformset_factory(Album,Photo,
fields=['image','title','description'],extra=3)