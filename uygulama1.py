#2.Haftanın uygulaması

#Karekök hesabını yapabilmek için kütüphane yüklemesi.
import math

#2D uzaydaki noktaları temsil eden (type)tuple bir liste
points =[(1,2), (8,3), (7,4), (5,3), (2,9)]

#Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1,point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

#Mesafeleri saklamak için bir liste
distances=[]

#Noktalar arasındaki mesafeleri hesaplamamızı sağlayan döngü.
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

#Minimum mesafeyi bulma.
min_distance=min(distances)

#Sonuçları yazdırma.
print("Hesaplanan mesafeler:", distances)
print("Minimum mesafe:", min_distance)