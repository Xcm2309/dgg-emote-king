import pickle
import emotes
import re
import os
import datetime

NUMBER_OF_RANKINGS = 25

def load_dictionary(filename):
    with open(filename, 'rb') as d:
        return pickle.load(d)

def parse_macro(emote, rankings, emote_dict, macro):
    macro = macro[len('!!!'):][:-len('!!!')]
    if (macro == 'EMOTE_NAME'):
        return emote
    elif (macro == 'EMOTE_URL'):
        return emotes.getEmoteURL(emote)
    elif (macro == 'GENERATION_DATE'):
        return str(datetime.datetime.today())
    elif (macro.startswith('USERNAME')):
        rank = int(macro[len('USERNAME'):])
        return rankings[rank - 1]
    elif (macro.startswith('USERCOUNT')):
        rank = int(macro[len('USERCOUNT'):])
        return str(emote_dict[rankings[rank - 1]])
    else:
        return macro

def generate_page(emote, emote_dict, template, output):
    """Generates a page for the given emote based off the given template and saved to the given output"""
    filename = output + emote + '.html'
    if (not os.path.isfile(filename)):
        f = open(output + emote + '.html', 'x', encoding='utf-8')
        f.close()

    #https://stackoverflow.com/questions/7197315/5-maximum-values-in-a-python-dictionary
    rankings = sorted(emote_dict, key=emote_dict.get, reverse=True)[:NUMBER_OF_RANKINGS]
    with open(filename, 'w', encoding='utf-8') as f:
        with open(template, 'r', encoding='utf-8') as t:
            tlines = t.readlines()
            for tline in tlines:
                macros = re.findall('!!!\w+!!!', tline)
                fline = tline
                for macro in macros:
                    fline = fline.replace(macro, parse_macro(emote, rankings, emote_dict, macro))
                f.write(fline)


dictionary = load_dictionary('dictionary.bin')
generate_page('Abathur', dictionary['Abathur'], 'template.html', 'generated/')