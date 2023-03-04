import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = '/home/Sophia.Huang.24/twitter_coronavirus/NotoSansJP-Regular.otf'
font_prop = FontProperties(fname=font)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]


plt.plot(x, y)
plt.xlabel("日本語 X 軸ラベル", fontproperties=font_prop)
plt.ylabel("日本語 Y 軸ラベル", fontproperties=font_prop)
plt.title("日本語タイトル", fontproperties=font_prop)
plt.savefig('test.png')
