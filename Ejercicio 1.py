
nacionalidad = input("Ingrese su nacionalidad: ")
renta_anual = float(input("Ingrese su renta anual en  pesos colombianos: "))
if nacionalidad == "colombiano" or nacionalidad == "colombiana" and renta_anual < 10000000:
    indice = (renta_anual*0.05)
elif nacionalidad == "colombiano" or nacionalidad == "colombiana" and renta_anual > 10000000 and renta_anual < 20000000:
    indice = (renta_anual*0.15)
elif nacionalidad == "colombiano" or nacionalidad == "colombiana" and renta_anual > 20000000 and  renta_anual < 35000000 :
    indice = (renta_anual*0.2)
elif nacionalidad == "colombiano" or nacionalidad == "colombiana" and renta_anual > 35000000 and  renta_anual < 60000000:
    indice = (renta_anual*0.3)
elif nacionalidad == "colombiano" or nacionalidad == "colombiana" and  renta_anual > 60000000:
     indice = (renta_anual*0.45)  
if nacionalidad == "mexicano" or nacionalidad == "chileno" or nacionalidad == "peruano" and renta_anual < 10000000:
    indice = (renta_anual*0.1)
elif nacionalidad == "mexicano" or nacionalidad == "chileno" or nacionalidad == "peruano" and renta_anual > 10000000 and renta_anual < 20000000:
    indice = (renta_anual*0.2)
elif nacionalidad == "mexicano" or nacionalidad == "chileno" or nacionalidad == "peruano" and renta_anual > 20000000 and  renta_anual < 35000000 :
    indice = (renta_anual*0.25)
elif nacionalidad == "mexicano" or nacionalidad == "chileno" or nacionalidad == "peruano" and renta_anual > 35000000 and  renta_anual < 60000000:
    indice = (renta_anual*0.35)
elif nacionalidad == "mexicano" or nacionalidad == "chileno" or nacionalidad == "peruano" and  renta_anual > 60000000:
     indice = (renta_anual*0.5)   
elif nacionalidad != "colombiano" or nacionalidad != "chileno" or nacionalidad != "peruano" and renta_anual < 10000000:
    indice = (renta_anual*0.15)
elif nacionalidad != "colombiano" or nacionalidad != "chileno" or nacionalidad != "peruano" and renta_anual > 10000000 and renta_anual < 20000000:
    indice = (renta_anual*0.25)
elif nacionalidad != "mexicano" or nacionalidad != "chileno" or nacionalidad != "peruano" and renta_anual > 20000000 and  renta_anual < 35000000 :
    indice = (renta_anual*0.35)
elif nacionalidad != "mexicano" or nacionalidad != "chileno" or nacionalidad != "peruano" and renta_anual > 35000000 and  renta_anual < 60000000:
    indice = (renta_anual*0.45)
elif nacionalidad != "mexicano" or nacionalidad != "chileno" or nacionalidad != "peruano" and  renta_anual > 60000000:
     indice = (renta_anual*0.6)    
else:
     print( " eso no es un pais ")
print( "usted es ", nacionalidad,"su renta es de ", indice,)