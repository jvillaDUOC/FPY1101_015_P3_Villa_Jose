
Personas=[]

def Buscar():
    while True:
        try:
            print("""------------
                  Buscar de persona
                  """)
            NIF = input("Favor ingrese el NIF de la persona a buscar: ")
            if (len(NIF)>12):
                for persona in Personas:
                    persona["NIF"]==NIF
                    return persona
                break
            else:
                return False
        except:
            print("Ingrese dato valido!!!")            
    #fin while
#fin funcion BuscarPersona
      
#funcion para buscar persona
def BuscarPersona():
    #llamarmos funcion para buscar Persona
    Buscar()
    #validamos datos regresados por funcion
    if(Buscar()==False):
        print("no se encuentra en los registros la persona")
    else:
        print(Buscar())
        
    
#fin funcion buscar Persona
    
#funcion para Ingresar Persona
def IngresarPersona():
    while True:        
        try:
            print("""
                  Ingresar de persona
                  -------------------
                  """)
            #while para ingreso y validacion de datos para el NIF de la persona
            while True:
                try:
                    NIF = input("ingrese NIF de la persona: ")                        
                    if (len(NIF)>=12):
                        #ingreso de dato desde diccionario a arreglo
                        #Personas.append(persona["NIF":NIF])
                        break
                    else:
                        print(f"""{NIF} : digito ingresado no es un formato valido!!
                              Debe ser 12 digitos ej: 99999999-ABC
                              """)
                except:
                    "Dato no valido.."    
            #endwhile
            #while para ingreso y validacion de datos para el NOMBRE de la persona
            while True:
                try:
                    nombre = input("ingrese NOMBRE de la persona: ")
                    if ( nombre!="" or len(nombre)>=8):
                        #ingreso de dato desde diccionario a arreglo
                        #Personas.append(persona["nombre":nombre])
                        break
                    else:
                        print(f"{nombre} :Nombre no valido, debe contener caracteres.")
                except:
                    "Dato no valido.."    
            #endwhile
            #while para ingreso y validacion de datos para la EDAD de la persona
            while True:
                try:
                    edad = int(input("ingrese EDAD de la persona: "))
                    if (edad>=0):
                        #ingreso de dato desde diccionario a arreglo
                        #Personas.append(persona["edad":edad])
                        break
                    else:
                        print(f"{edad} : No es valida, debe ser igual o mayor a 0")
                except:
                    "Dato no valido, debe ser numerico.."    
            #endwhile  
            
            persona={
                    "NIF":NIF,
                    "nombre":nombre,
                    "edad":edad,
                    #"nacionalidad": nacionalidad
               }
            
            #ingresando datos al arreglo
            
            Personas.append({"NIF": NIF, "nombre":nombre,"edad": edad})
            print(Personas)
            break         
        except:
            print("Dato no valido.....")
        #end try        
    #fin while
    
#funcion Imprimir certificado:
def imprimirCertificado():
    print("""
            Imprimir Certificado de persona
            -------------------
        """)
    Buscar()
    if(Buscar!=False):
        
        while True:
            try:
                print("""
              1.- Certificado Nacimiento
              2.- Estado Conyugal
              3.- Pertenencia a la Union Europea
              """)
                certificado = int(input("Seleccione certifcado a imprimir"))
                if( certificado<1 or certificado>3):
                    while True:
                        try:
                            precio=int(input("ingrese valor de Certificado: "))
                            if(precio <1500 or precio>2000):
                                print(f"Certificado tiene un valor de {precio}")
                                break
                            else:
                                print("precio no corresponde...")
                        except:
                            print("Formato de precio no valido...")                        
                    #end while
                    if(certificado==1):
                        print("certificado de nacimiento")
                        print(Buscar())
                    elif(certificado==2):
                        print("certificado de Estado Conyugal")
                        print(Buscar())
                    elif(certificado==3):
                        print("certificado de Pertenencia a la Union Europea")
                        print(Buscar())
                    else:
                        print("no se pudo imprimir certificado")
                else:
                    print("Seleccion de certificado no valida")
                #end if            
            except:
                print("Dato no valida")    
            #end try
        #end while
    else:
        print("No se encuentran datos para imprimir certificado")    
    

while True:
    try:
        print("""
          Bienvenido a su aplicacion de idenficicion fiscal
          =================================================

          1.- Grabar datos
          2.- Buscar datos
          3.- Imprimir certificado
          4.- Salir
          """)
        opcion = int(input("Seleccione opcion: "))
        if(opcion==1):
            IngresarPersona()
        elif (opcion==2):
            Buscar()
        elif (opcion==3):
            imprimirCertificado()
        elif (opcion ==4):
            print("""PROGRAMA FINALIZADO 
                  Desarrollado por JOSE VILLA
                  seccion 15V
                  Version de programa 03072024.1
                  """)
            break
        else:
            print("opcion no valida")
        #end if
    except:
        print("opcion no valida.. reintente")
     #end try
#end while