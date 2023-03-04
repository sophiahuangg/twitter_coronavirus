import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Replace "/path/to/font" with the actual path to the font file on your Mac.
font_path = "/Users/sophia/Library/Fonts/NotoSansCJK.ttc "

# Register the font with Matplotlib.
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()

# Use the font in a plot.
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel('横轴', fontproperties=prop)
plt.ylabel('纵轴', fontproperties=prop)
plt.title('标题', fontproperties=prop)
plt.savefig('characters.png')
