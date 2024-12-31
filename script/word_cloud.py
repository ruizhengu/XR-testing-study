from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
import random
from matplotlib import cm
from matplotlib.colors import Normalize

def qualitative_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    cmap = cm.get_cmap('tab20b')
    norm = Normalize(vmin=0, vmax=255)
    color_index = random.randint(0, 255)  # Random index for color
    rgba = cmap(norm(color_index))
    return tuple(int(c * 255) for c in rgba[:3])  # Convert RGBA to RGB

# Apply color function


def test_activity():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    test_activity_values = df["test activity"].dropna().astype(str)
    text = " ".join(test_activity_values)
    text = text.replace("runtime testing", "runtime")
    print(text)

    wc = WordCloud(background_color="white", width=1600, height=800).generate(text)
    wc = wc.recolor(color_func=qualitative_color_func)

    plt.figure(figsize=(15, 9))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/ruizhengu/Projects/XR-testing-study/figure/test_activity.png', dpi=300)

test_activity()