from PIL import Image, ImageDraw, ImageFont
from django.core.files.storage import default_storage
import io

STRINGS = ['E', 'A', 'D', 'G', 'B', 'e']

class ChordGenerator:

    def __init__(self, tab, name="", capo=None, size=(256, 512), instrument="guitar", strings=6, guess_name=False):

        self.tab = tab
        self.name = name
        self.capo = capo if capo != 0 else None
        self.size = size
        self.instrument = instrument
        self.strings = strings
        
        self._create_fretboard()
        self._generate_fingering()

    def __str__(self):
        return self.name

    def _create_fretboard(self):

        self.padding = {
            "top": 0.1 * self.size[1],
            "right": 0.1 * self.size[0],
            "bottom": 0.1 * self.size[1],
            "left": 0.2 * self.size[0] if self.capo else 0.1 * self.size[0]
        }

        self.name_font_size = int(0.1 * self.size[1])
        self.nut_markers_size = int(0.07 * self.size[1])
        self.header_height = self.name_font_size + self.nut_markers_size + self.padding['bottom']/4

        self.neck_width = self.size[0] - self.padding['left'] - self.padding['right']
        self.space_between_strings = self.neck_width / ( self.strings - 1 )
        
        self.fret_num = 4
        self.fret_size = ( self.size[1] - self.padding['top'] - self.padding['bottom'] - self.header_height ) / self.fret_num

        self.finger_radius = self.space_between_strings / 3

        self.chord = Image.new('RGBA', self.size, (255,255,255,255))

        draw = ImageDraw.Draw(self.chord)

        # Nut
        nut_start = (self.padding['left'], self.header_height + self.padding['top'])
        nut_end = (self.size[0] - self.padding['right'], self.header_height + self.padding['top'])
        draw.line([nut_start, nut_end], fill="black", width=10)

        if self.capo:
            font = ImageFont.truetype("staticfiles/fonts/Verdana.ttf", int(self.nut_markers_size*0.7))
            width, height = draw.textsize(str(self.capo), font=font)

            center = (self.padding['left'] - 2*width, self.header_height + self.padding['top'] - height/2)

            draw.text(center, str(self.capo), font=font, fill="black")

        # Strings
        for i in range(self.strings):
            string_start = (self.padding['left'] + i * self.space_between_strings, self.header_height + self.padding['top'])
            string_end = (self.padding['left'] + i * self.space_between_strings, self.size[1] - self.padding['bottom'])
            draw.line([string_start, string_end], fill="black", width=2)

        # Frets
        for j in range(1, self.fret_num+1):
            fret_start = (self.padding['left'], self.header_height + self.padding['top'] + j * self.fret_size)
            fret_end = (self.padding['left'] + self.neck_width , self.header_height + self.padding['top'] + j * self.fret_size)
            draw.line([fret_start, fret_end], fill="black", width=2)

        del draw


    def _generate_fingering(self):
        
        draw = ImageDraw.Draw(self.chord)

        # Name
        if self.name:
            font = ImageFont.truetype("staticfiles/fonts/Verdana.ttf", self.name_font_size)
            draw.text((self.padding['top'], self.padding['left']), self.name, font=font, fill="black") 

        # Fingers
        for string, field in self.tab.items():

            string_index = STRINGS.index(string)

            # If it is a pressed note
            if field['fret'] not in (0, None, ""):

                center = ( self.padding['left'] + string_index * self.space_between_strings, self.header_height + self.padding['top'] + int(field['fret']) * self.fret_size - self.fret_size/2 )

                x0 = center[0] - self.finger_radius
                y0 = center[1] - self.finger_radius
                x1 = center[0] + self.finger_radius
                y1 = center[1] + self.finger_radius

                draw.ellipse((x0,y0,x1,y1), fill="black")

                # Finger markers
                font = ImageFont.truetype("staticfiles/fonts/Verdana.ttf", int(self.nut_markers_size/2))

                width, height = draw.textsize(field['finger'], font=font)
                text_center = (center[0] - width/2, center[1] - height/2)
                draw.text(text_center, field['finger'], font=font, fill="white")

            # If empty string
            else:
                x = self.padding['left'] + string_index * self.space_between_strings
                y = self.padding['top'] + self.name_font_size 
                sign = 'O' if field['fret'] == "0" else "X"

                font = ImageFont.truetype("staticfiles/fonts/Verdana.ttf", int(self.nut_markers_size))
                width, height = draw.textsize("O", font=font)
                draw.text((x - width/2, y), sign, font=font, fill="black")

        del draw

    def get_image(self):
        return self.chord

    def get_name(self):
        return self.name

    def output(self, filename):

        if not default_storage.exists(filename):
            self.chord.save("media/" + filename, format="JPEG")

        return filename
