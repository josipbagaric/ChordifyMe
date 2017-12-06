from django.shortcuts import render, get_object_or_404

from .generator import ChordGenerator, STRINGS

from django.contrib.auth.models import User, Group


def index(request):

    image_sizes = [
        (256, 512)
    ]

    context = {
        "instruments": [
            'Guitar'
        ],
        "image_sizes": image_sizes,
        "strings": [ (string, None) for string in reversed(STRINGS) ],
        "guess": False,
        "capo": 0
    }    

    if request.POST:

        tab = {}
        filename = "chord_"

        for idx, string_props in enumerate(context['strings']):

            string = string_props[0]

            fret = request.POST[string] if request.POST[string] else ""
            finger = request.POST[string+'_finger'] if request.POST[string+'_finger'] else ""

            # Save it into a tab dictionary which will be used
            # to generate the image
            tab[string] = {
                "fret": fret,
                "finger": finger
            }

            filename += string + fret + finger

            # Remember what the user inputted
            context['strings'][idx] = (string, tab[string])

        guess_name = None #request.POST['guess']      

        context['capo'] = int(request.POST['capo'])
        context['chord_name'] = request.POST['name'] if 'name' in request.POST.keys() else ""
        filename += request.POST['capo'] + "_" + context['chord_name']

        chord = ChordGenerator(tab=tab, capo=context['capo'], guess_name=guess_name, name=context['chord_name'])
        url = chord.output("generated_chords/" + filename + ".jpg")        

        context["image"] = "/media/" +  url
        context["image_url"] = "https://chordify.me/media/" +  url

    else:
        context['strings'] = [('e', {'finger': '', 'fret': '0'}), ('B', {'finger': '', 'fret': '1'}), ('G', {'finger': '', 'fret': '0'}), ('D', {'finger': '', 'fret': '2'}), ('A', {'finger': '3', 'fret': '3'}), ('E', {'finger': '', 'fret': ''})]

    return render(request, 'index.html', context)


def api(request):
    context = {}
    return render(request, 'api.html', context)