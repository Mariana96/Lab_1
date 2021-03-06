import matplotlib.pyplot as plt, pandas as  ps


#Cargue el dataset referido por el preparador.
mydata=ps.read_csv("student-por.csv", sep=';')

#Calcule y muestre algunas propiedades de los datos.
print("Se muestran algunas propiedades sumarizadas de los datos presentados")
print(mydata.describe())

#Grafique el histograma de, al menos, una variable numerica en los datos.
plt.hist(mydata['Dalc'])
plt.title("Histograma del Consumo Diario de Alcohol")
plt.xlabel("DALC")
plt.ylabel("Frecuencia")
plt.show()

print("En el histograma Se puede observar la frecuencia de cada uno de los grados de consumo del alcohol diario")

#-Realice un diagrama de dispersion entre un par de variables numericas y presente una hipotesis de acuerdo a los resultados.

x = mydata['G1']
y = mydata['G3']
plt.scatter(x, y, c='blue')
plt.title("Diagrama de Dispersion de notas del Primer y Ultimo periodo")
plt.xlabel("Notas G1")
plt.ylabel("Notas G3")
plt.show()

print("En el grafico puede observarse que existe una correlacion positiva, es decir en este caso, mientras aumentan los valores del eje x (Notas en los primeros grados del periodo mas aumentan los valores del eje Y (Aumenta la nota final del curso.HIPOTESIS: los estudiantes que obtienen buenas calificaciones los primeros grados,terminan obteniendo buenas calificaciones al final del curso")
#-Explore, usando lo aprendido en el laboratorio, los datos provistos.

print("Se muestra la cantidad de personas por edad en los distintos niveles de consumo de alcohol diario")
print(mydata.groupby(['Dalc','age']).size())
print("Puede notarse que predominan las edades entre 16 y 17 en cualquiera de los niveles de consumo diario de alcohol, con esto podemos definir la hipotesis de que: los jovenes menores de edad son los que consumen mas alcohol diariamente")



print("Se muestra la cantidad de personas por sexo en los distintos niveles de consumo de alcohol los fines de semana")
print(mydata.groupby(['Walc','sex']).size())
print("Mediante la observacion de los resultados puede observarse que las personas de sexo femenino tienen una tendencia a tener un consumo entre bajo a mediano los fines de semana mientras que las personas de sexo masculino tienden a tener un consumo alto los fines de semana, esta hipotesis podria platearse como : los hombres toman mas que las muejeres los fines de semana")

#Plantee al menos 3 preguntas sobre que puedan ser respondidas con #los datos provistos y postule el codigo (o algoritmo) necesario #para responderla.

#Cual es el promedio de edad de los hombres que consumen mucho alcohol diariamente (Dalc>4)

print("Cual es el promedio de edad de los hombres que tienen un consumo alto de alcohol diariamente?")
hombres=mydata[mydata['sex']=="M"]
consumo_mayor=hombres[hombres['Dalc']>4]
promedio_edad_h=consumo_mayor['age'].mean()
print(promedio_edad_h)

#El promedio anterior es menor al de las mujeres
print("El promedio anterior es menor al de las mujeres?")
mujeres=mydata[mydata['sex']=="F"]
consumo_mayor=mujeres[mujeres['Dalc']>4]
promedio_edad_f=consumo_mayor['age'].mean()
print(promedio_edad_h<promedio_edad_f)


#promedio de edad de los estudiantes cuyos padres son profesores que tienen un consumo de alcohol diario elevado
print("Cual es el promedio de edad de los estudiantes cuyos padres son profesores que tienen un consumo de alcohol diario elevado?")

profes=mydata[mydata['Fjob']=="teacher"]
consumo_elevado=profes[profes['Dalc']>4]
promedio_profes=consumo_elevado['age'].mean();
print(promedio_profes)














