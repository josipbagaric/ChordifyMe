from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import GuitarChord

from io import BytesIO
from django.core.files.base import ContentFile

from core.generator import ChordGenerator

@receiver(post_save, sender=GuitarChord)
def create_image(sender, **kwargs):
    
    if kwargs.pop('created'):
        chord = kwargs.pop('instance')

        tab = {
            'E': {
                'fret': chord.low_e_string, 
                'finger': chord.low_e_string_finger
            }, 
            'A': {
                'fret': chord.a_string,
                'finger': chord.a_string_finger
            }, 
            'D': {
                'fret': chord.d_string,
                'finger': chord.d_string_finger
            },
            'G': {
                'fret': chord.g_string,
                'finger': chord.g_string_finger
            },
            'B': {
                'fret': chord.b_string,
                'finger': chord.b_string_finger
            },
            'e': {
                'fret': chord.high_e_string,
                'finger': chord.high_e_string_finger
            }
        }

        chord_gen = ChordGenerator(tab=tab, capo=chord.capo, name=chord.name+chord.modifier)

        # Temporary image storage before we save it into the model
        f = BytesIO()
        chord_gen.chord.save(f, format='JPEG')
        
        img_name = str(chord.id) + ".jpg"

        chord.image.save(img_name, content=ContentFile(f.getvalue()), save=False)
        f.close()

        chord.save()
