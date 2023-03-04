import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

font_path = '/home/Sophia.Huang.24/twitter_coronavirus/NotoSansTC-Regular.otf'
font_family = 'Noto Sans TC'

if fm.findfont(font_family) is None:
    print(f'Font family {font_family} is not installed.')
else:
    print(f'Font family {font_family} is installed.')

font = plt.matplotlib.font_manager.FontProperties(fname='NotoSansTC-Regular.otf')
font.set_family('Noto Sans TC')

# Print the font family
print(font.get_family())
