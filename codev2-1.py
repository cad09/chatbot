class Materia:
    def __init__(self, nombre, creditos, disponibilidad, ya_vista=False):
        self.nombre = nombre
        self.creditos = creditos
        self.disponibilidad = disponibilidad  # Diccionario de disponibilidad de días y horarios
        self.ya_vista = ya_vista

# Lista de materias disponibles con horarios específicos
materias_disponibles = [
    Materia("Matemáticas I", 3, {"Lunes": "08:00-10:00", "Miércoles": "10:00-12:00"}, ya_vista=False),
    Materia("Física I", 4, {"Martes": "08:00-10:00", "Jueves": "10:00-12:00"}, ya_vista=True),
    Materia("Química I", 3, {"Lunes": "10:00-12:00", "Miércoles": "14:00-16:00"}, ya_vista=False),
    Materia("Literatura", 2, {"Viernes": "10:00-12:00", "Viernes": "14:00-16:00"}, ya_vista=False),
    Materia("Programación", 5, {"Lunes": "14:00-16:00", "Viernes": "16:00-18:00"}, ya_vista=False),
    Materia("Biología", 3, {"Martes": "10:00-12:00", "Jueves": "14:00-16:00"}, ya_vista=False),
    Materia("Historia", 2, {"Miércoles": "14:00-16:00", "Viernes": "16:00-18:00"}, ya_vista=False),
    Materia("Geografía", 3, {"Lunes": "16:00-18:00", "Viernes": "14:00-16:00"}, ya_vista=False),
    Materia("Química Orgánica", 4, {"Martes": "14:00-16:00", "Jueves": "16:00-18:00"}, ya_vista=False),
    Materia("Álgebra", 3, {"Lunes": "08:00-10:00", "Miércoles": "08:00-10:00"}, ya_vista=False)
]

# Función para calcular la probabilidad de cancelar una materia
def calcular_probabilidad_cancelacion(materias_matriculadas):
    # Calcula la probabilidad de cancelar una materia según la cantidad de materias matriculadas
    # A mayor cantidad de materias, mayor probabilidad de cancelar una materia
    # Por ejemplo, 10% por cada materia matriculada
    probabilidad = len(materias_matriculadas) * 0.1
    return min(probabilidad, 1.0)  # Limita la probabilidad al 100%

# Función para mostrar las materias disponibles según los créditos y días disponibles
def mostrar_materias_disponibles(creditos_disponibles, dias_disponibles):
    print("\nChatbot: Materias disponibles:")
    for i, materia in enumerate(materias_disponibles):
        dias_intersectados = set(materia.disponibilidad.keys()).intersection(set(dias_disponibles))
        if not materia.ya_vista and dias_intersectados:
            horarios = []
            for dia in dias_intersectados:
                horarios.append(f"{dia}: {materia.disponibilidad[dia]}")
            print(f"{i + 1}. {materia.nombre} - {materia.creditos} créditos - Horarios: {', '.join(horarios)}")

# Función para proponer matrícula según los créditos disponibles y los días disponibles
def proponer_matricula(creditos_disponibles, dias_disponibles):
    print("\nChatbot: Propuestas de matrícula:")
    propuestas = []
    creditos_totales = 0
    for materia in materias_disponibles:
        dias_intersectados = set(materia.disponibilidad.keys()).issubset(set(dias_disponibles))
        if not materia.ya_vista and dias_intersectados and creditos_totales + materia.creditos <= creditos_disponibles:
            propuestas.append(materia)
            creditos_totales += materia.creditos
            horarios = []
            for dia in dias_intersectados:
                horarios.append(f"{dia}: {materia.disponibilidad[dia]}")
        print(f"- {materia.nombre}: {materia.creditos} créditos (Horarios: {', '.join(horarios)})")
    return propuestas

# Función principal del chatbot
def main():
    # Ingreso de datos por parte del usuario con interacciones del chatbot
    print("Chatbot: Hola, bienvenido al sistema de matrícula. Empecemos.")
    
    # Solicitud de créditos comprados
    creditos_disponibles = int(input("\nChatbot: Ingrese los créditos comprados: "))
    
    # Solicitud de días disponibles para estudiar
    dias_disponibles = input("Chatbot: Ingrese los días disponibles para estudiar (separados por comas): ").split(",")
    dias_disponibles = [dia.strip() for dia in dias_disponibles]  # Eliminar espacios en blanco

    # Mostrar las materias disponibles que el estudiante no ha visto
    mostrar_materias_disponibles(creditos_disponibles, dias_disponibles)

    # Proponer matrícula según los créditos disponibles y los días disponibles
    propuestas = proponer_matricula(creditos_disponibles, dias_disponibles)

    # Calcular la probabilidad de cancelar una materia
    probabilidad_cancelacion = calcular_probabilidad_cancelacion(propuestas)
    print(f"\nChatbot: La probabilidad de cancelar una materia es de {probabilidad_cancelacion * 100:.2f}%.")

    # Selección de materias para la matrícula final
    seleccion_materias = input("\nChatbot: Seleccione los números de las materias que desea matricular (separados por comas): ").split(",")
    seleccion_materias = [int(num.strip()) for num in seleccion_materias]

    # Mostrar la matrícula finalizada con las materias seleccionadas
    print("\nChatbot: Matrícula finalizada con las siguientes materias:")
    for num in seleccion_materias:
        materia = propuestas[num - 1]  # Los números comienzan desde 1 en la lista de propuestas
        horarios = []
        for dia in dias_intersectados:
            horarios.append(f"{dia}: {materia.disponibilidad[dia]}")
        print(f"- {materia.nombre} ({materia.creditos} créditos) - Horarios: {', '.join(horarios)}")

    # Mensaje final de agradecimiento
    print("\nChatbot: Gracias por usar el sistema de matrícula. ¡Que tengas un excelente semestre!")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
