import csv
import matplotlib.pyplot as plt
import math
from wordcloud import WordCloud
import numpy as np

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
    cadena_unida = ' '.join(apps)
    nube = WordCloud(width=800, height=400, background_color='white', min_word_length = 3).generate(cadena_unida)
    plt.figure(figsize=(10, 5))
    plt.imshow(nube, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # #piechart con las instalaciones de las categorias
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

    #eje x tamaño, eje y rating, el tamaño segun el numero de instalaciones
    installs = [0] * len(Reviews)
    for i in range(len(Reviews)):
        installs = (Reviews[i])[:-1].replace(",", "").replace('','0')
    apps_ratings = list(zip(installs, Rating, Size, app)) #junto lo q me importa en una matrix
    filtro = [x for x in apps_ratings if not math.isnan(float(x[1])) and x[2] != 'Varies with device'] #filtro las q tienen rating y el tamaño no varia segun el dispositivo
    dow =[]
    ratin = []
    tamaño = []
    apli = []
    for i in range(len(filtro)):
        ratin.append(float(filtro[i][1]))
        dow.append(float(filtro[i][0])+1)
        apli.append(filtro[i][3])
        tamaño.append(float(filtro[i][2][:-1]))
    bubble_size = np.array(dow) * 1000
    plt.figure(figsize=(10, 6))
    plt.scatter(tamaño, ratin, s=bubble_size, alpha=0.5, c=dow, cmap='viridis')
    plt.title('Diagrama de Burbujas: Rating vs. Instalaciones vs. Size')
    plt.xlabel('Tamaño de la aplicacion(MB)')
    plt.ylabel('Calificación de la Aplicación')
    plt.colorbar(label='Número de Instalaciones')
    #for i in range(len(apli)):
     #   plt.text(tamaño[i] - 0.5, ratin[i], dow[i], fontsize=9)
    plt.show()

