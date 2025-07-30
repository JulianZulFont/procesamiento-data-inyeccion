import pandas as pd

df0 = pd.read_csv("Archivo1.csv")
#crear columna de indice
indice = pd.Series(range(0,len(df0)))
#insertar la columna indices en el dataframe inicial
df0.insert(loc = 0, column="Id-produccion", value=indice) #Este método no sirve asignando una nueva variable, si no solo modificando la existente en un método de mutación no se porque

#/-/-/-/-/
#tabla de cavidades disponibles
df1 = pd.concat([df0.iloc[:,0],df0.iloc[:,3:8]], axis=1)
#Crear un dataframe donde se guardará toda la información de los accesorios, con el id de la producción asignado
df2 = pd.DataFrame(columns=["Id-produccion", "acceosorio", "Cavidades disponibles"])
#se itera en para cada fila primeramente y después para cada columna de la fila seleccionada, si la casilla es distinto a "nan" entonces se guarda el valor junto al id
for i in range(0,len(df1)):
    for j in range(1,len(df1.columns)):
        if str(df1.iloc[i,j]) != "nan":
            Id_acc = str(df1.iloc[i,0])  #Id del accesorio
            N_acc = str(df1.iloc[i,j])   #Nombre del accesorio
            Cav_disp = ((str(df1.columns[j]))[44:46]).strip()  #toma el título de la columna de donde salen las cavidades disponibles y extrae los caracteres de las cavidades disponibles
            df2.loc[len(df2)] = [Id_acc, N_acc, Cav_disp]
#print(df2.columns)

#/-/-/-/-/
#Tabla de cavidades taponadas
df3 = pd.concat([df0.iloc[:,0],df0.iloc[:,29:33]], axis=1)
print(df3.columns)
df4 = pd.DataFrame(columns=["Id-produccion", "acceosorio", "Cavidades taponadas"])
for i in range(0,len(df3)):
    for j in range(1,len(df3.columns)):
        if str(df3.iloc[i,j]) != "nan":
            Id_acc2 = str(df3.iloc[i,0])
            N_acc2 = str(df3.iloc[i,j])
            Cav_tap = ((str(df3.columns[j]))[42:44]).strip()
            df4.loc[len(df4)] = [Id_acc2, N_acc2, Cav_tap]
print(df4)

#Unión de la tabla
df5 = (pd.merge(df2,df4,on="Id-produccion",how="left"))
df5 = df5.drop(df5.columns[3],axis=1)
print(df5.columns)
df0_1 = pd.concat([df0.iloc[:,0:3],df0.iloc[:,9:29]], axis=1)
print(df0_1.columns)

with pd.ExcelWriter("Excel1.xlsx") as writer:
    df5.to_excel(writer, sheet_name="Hoja1", index=True)
    df0_1.to_excel(writer, sheet_name="Hoja2", index=True)