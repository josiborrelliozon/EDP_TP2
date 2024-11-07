import csv

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

if __name__=='__main__':
    print(Category)
    print('\n')
    print(Current_Ver)
    print('\n')

