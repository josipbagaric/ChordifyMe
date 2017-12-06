from django.db import models

class ChordName(models.Model):

    """CHORDS = (
        ('C','C'), ('C#','C#'), ('Db','Db'), ('D','D'), ('D#','D#'), ('Eb','Eb'), ('E','E'), ('F','F'), 
        ('F#','F#'), ('Gb','Gb'), ('G','G'), ('G#','G#'), ('Ab','Ab'), ('A ','A'), ('A#','A#'), ('Bb','Bb'), ('B','B'), 
        ('A/C#','A/C#'), ('A/E','A/E'), ('A/F','A/F'), ('A/G','A/G'), ('A/G#','A/G#'), ('Am/C','Am/C'), ('Am/E','Am/E'), 
        ('Am/F','Am/F'), ('Am/F#','Am/F#'), ('Am/G','Am/G'), ('Am/G#','Am/G#'), 
        ('C/E','C/E'), ('C/F','C/F'), ('C/G','C/G'), ('D/A','D/A'), ('D/B','D/B'), ('D/Bb','D/Bb'), ('D/C','D/C'), ('D/F#','D/F#'), 
        ('E/B','E/B'), ('E/C#','E/C#'), ('E/D','E/D'), ('E/D#','E/D#'), ('E/F','E/F'), ('E/F#','E/F#'), ('E/G','E/G'), ('E/G#','E/G#'), 
        ('Em/B','Em/B'), ('Em/C#','Em/C#'), ('Em/D','Em/D'), ('Em/D#','Em/D#'), ('Em/F','Em/F'), ('Em/F#','Em/F#'), 
        ('Em/G','Em/G'), ('Em/G#','Em/G#'), ('F/A','F/A'), ('F/C','F/C'), ('F/D','F/D'), ('F/D#','F/D#'), 
        ('F/E','F/E'), ('F/G','F/G'), ('Fm/C','F/C'), ('G/B','G/B'), ('G/D','G/D'), ('G/E','G/E'), ('G/F','G/F'), ('G/F#', 'G/F#'),
        ('', '')
    )"""

    name = models.CharField(null=False, unique=True, max_length=100)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Created on')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last updated')

    class Meta:
        ordering = ('created',)


class ChordModifier(models.Model):

    """MODIFIERS = (
        ('m', 'minor'), ('M', 'major'), ('aug', 'aug'), ('dim', 'dim'),
        ('sus', 'sus'), ('add9', 'add9'), ('m6', 'm6'), ('m7', 'm7'), ('m9', 'm9'),
        ('mmaj7', 'mmaj7'), ('-5', '-5'), ('11', '11'), ('13', '13'), ('5','5'),
        ('6', '6'), ('6add9', '6add9'), ('7', '7'), ('7-5', '7-5'), ('7maj5', '7maj5'),
        ('7sus4', '7sus4'), ('9', '9'), 
        ('', '')
    )"""

    name = models.CharField(null=False, unique=True, max_length=100)
    short_name = models.CharField(null=False, max_length=100)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Created on')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last updated')

    class Meta:
        ordering = ('created',)

        
class GuitarChord(models.Model):

    def __str__(self):
        return "{}{}: {}{}{}{}{}{}".format(self.name, self.modifier, self.high_e_string, self.b_string, 
            self.g_string, self.d_string, self.a_string, self.low_e_string)

    FRETS = (
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
        ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'),
        ('','')
    )
    FINGERS = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("", "")
    )

    name = models.ForeignKey(ChordName, related_name='chord_name', on_delete=models.CASCADE)
    modifier = models.ForeignKey(ChordModifier, related_name='chord_modifier', on_delete=models.CASCADE)
    capo = models.IntegerField(null=False, default=0)

    high_e_string = models.CharField(choices=FRETS, default="", max_length=100)
    high_e_string_finger = models.CharField(choices=FINGERS, default="", max_length=100)
    b_string = models.CharField(choices=FRETS, default="", max_length=100)
    b_string_finger = models.CharField(choices=FINGERS, default="", max_length=100)
    g_string = models.CharField(choices=FRETS, default="", max_length=100)
    g_string_finger = models.CharField(choices=FINGERS, default="", max_length=100)
    d_string = models.CharField(choices=FRETS, default="", max_length=100)
    d_string_finger = models.CharField(choices=FINGERS, default="", max_length=100)
    a_string = models.CharField(choices=FRETS, default="", max_length=100)
    a_string_finger = models.CharField(choices=FINGERS, default="", max_length=100)
    low_e_string = models.CharField(choices=FRETS, default="", max_length=100)
    low_e_string_finger = models.CharField(choices=FINGERS, default="", max_length=100)

    image = models.ImageField(upload_to="chords/img/", null=True, blank=True)

    owner = models.ForeignKey('auth.User', related_name='guitar_chords', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created on')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last updated')

    class Meta:
        ordering = ('created',)

