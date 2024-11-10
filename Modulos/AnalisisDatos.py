import csv
import matplotlib.pyplot as plt
import math
from wordcloud import WordCloud
from scipy.stats import pearsonr
app =[]
Category =[]
Rating = []
Reviews = []
Size = []
Installs = []
Type =[]
Price = []
Content_Rating =[]
Genres=[]
Last_Updated=[]
Current_Ver =[]
Android_Ver = []

with open('Play Store Data.csv', newline='', encoding='utf-8') as archivo:
    lector_csv = csv.reader(archivo)

    for fila in lector_csv:
        app.append(fila[0])
        Category.append(fila[1])
        Rating.append(fila[2])
        Reviews.append(fila[3])
        Size.append(fila[4])
        Installs.append(fila[5])
        Type.append(fila[6])
        Price.append(fila[7])
        Content_Rating.append(fila[8])
        Genres.append(fila[9])
        Last_Updated.append(fila[10])
        Current_Ver.append(fila[11])
        Android_Ver.append(fila[12])
    app.pop(0)
    Category.pop(0)
    Rating.pop(0)
    Reviews.pop(0)
    Size.pop(0)
    Installs.pop(0)
    Type.pop(0)
    Price.pop(0)
    Content_Rating.pop(0)
    Genres.pop(0)
    Last_Updated.pop(0)
    Current_Ver.pop(0)
    Android_Ver.pop(0)

if __name__=='__main__':
    apps_ratings = list(zip(app, Rating))
    filtered = [x for x in apps_ratings if not math.isnan(float(x[1]))]
    top_apps = sorted(filtered, key=lambda x: x[1], reverse=True)
    apps = []
    rating = []
    cadena_unida = ''
    for i in range(300):
        apps.append(top_apps[i][0])
        rating.append(float(top_apps[i][1]))
    apps_filtradas = [palabra for palabra in apps if len(palabra) > 10]
    cadena_unida = ' '.join(apps_filtradas)
    print(cadena_unida)
    nube = WordCloud(width=800, height=400, background_color='white').generate(cadena_unida)
    plt.figure(figsize=(10, 5))
    plt.imshow(nube, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    #piechart con las instalaciones de las categorias
    piechart = list(zip(Category, Installs))
    categorias = list(set(Category))
    r = len(Installs)
    c = len(categorias)
    instalaciones = [0]*c
    for j in range(c):
        for i in range(r):
            if piechart[i][0] == categorias[j]:
                instalaciones[j] += float((((piechart[i][1])[:-1]).replace(",", "")).replace('','0'))
    sortear = list(zip(categorias, instalaciones))
    top_ins = sorted(sortear, key=lambda x: x[1], reverse=True)
    cate = []
    dw = []
    tot = 0
    for i in range(5):
        cate.append(top_ins[i][0])
        dw.append(float(top_ins[i][1]))
    for i in range(5, c):
        tot += float(top_ins[i][1])
    cate.append('otras')
    dw.append(tot)
    plt.pie(dw, labels=cate, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de instalaciones por Categoría')
    plt.show()

    #
    # t = len(Rating)
    # ratio = []
    # y = len(Price)
    # ins = []
    # for i in range(t):
    #     ratio.append(float(Rating[i]))
    #
    # for i in range(y):
    #     ins.append(float(Price[i].replace("$",'')))
    #
    # correlation, p_value = pearsonr(ratio, ins)
    # print("Correlación de Pearson:", correlation)
    # print("Valor p:", p_value)
    # plt.scatter(ratio, ins)
    # plt.xlabel('Variable 1')
    # plt.ylabel('Variable 2')
    # plt.title('Gráfico de dispersión entre las dos variables')
    # plt.show()



