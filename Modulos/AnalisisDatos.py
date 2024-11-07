import csv
import matplotlib.pyplot as plt
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
    Rating.pop(0)

if __name__=='__main__':
    apps_ratings = list(zip(app, Rating))
    top_apps = sorted(apps_ratings, key=lambda x: x[1], reverse=True)
    apps = []
    rating = []
    for i in range(5):
        apps.append(top_apps[i][0])
        rating.append(float(top_apps[i][1]))
    print(apps)
    print(rating)
    plt.bar(apps, rating)
    plt.title('Ratings de Aplicaciones')
    plt.xlabel('Aplicaciones')
    plt.ylabel('Ratings')
    plt.show()


