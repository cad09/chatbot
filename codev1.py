import random

class Materia:
    def __init__(self, nombre, creditos, dias_disponibles, ya_vista=False):
        self.nombre = nombre
        self.creditos = creditos
        self.dias_disponibles = dias_disponibles
        self.ya_vista = ya_vista

# Lista de materias disponibles
materias_disponibles = [
    Materia("Matemáticas I", 3, ["Lunes", "Miércoles"], ya_vista=False),
    Materia("Física I", 4, ["Martes", "Jueves"], ya_vista=True),
    Materia("Química I", 3, ["Lunes", "Miércoles"], ya_vista=False),
    Materia("Literatura", 2, ["Viernes"], ya_vista=False),
    Materia("Programación", 5, ["Lunes", "Viernes"], ya_vista=False)
]

def calcular_probabilidad_cancelacion(materias_matriculadas):
    # Calcula la probabilidad de cancelar una materia según la cantidad de materias matriculadas
    # A mayor cantidad de materias, mayor probabilidad de cancelar una materia
    # Por ejemplo, 10% por cada materia matriculada
    probabilidad = len(materias_matriculadas) * 0.1
    return min(probabilidad, 1.0)  # Limita la probabilidad al 100%

def mostrar_materias_disponibles(creditos_disponibles, dias_disponibles):
    print("\nChatbot: Materias disponibles:")
    for i, materia in enumerate(materias_disponibles):
        if not materia.ya_vista and set(materia.dias_disponibles).intersection(set(dias_disponibles)):
            print(f"{i + 1}. {materia.nombre} - {materia.creditos} créditos - Días disponibles: {', '.join(materia.dias_disponibles)}")

def proponer_matricula(creditos_disponibles, dias_disponibles):
    print("\nChatbot: Propuestas de matrícula:")
    propuestas = []
    creditos_totales = 0
    for materia in materias_disponibles:
        if not materia.ya_vista and set(materia.dias_disponibles).issubset(set(dias_disponibles)) and creditos_totales + materia.creditos <= creditos_disponibles:
            propuestas.append(materia)
            creditos_totales += materia.creditos
            print(f"- {materia.nombre}: {materia.creditos} créditos (Días disponibles: {', '.join(materia.dias_disponibles)})")
    return propuestas

def main():
    # Ingreso de datos por parte del usuario con interacciones del chatbot
    print("Chatbot: Hola, bienvenido al sistema de matrícula. Empecemos.")
    
    creditos_disponibles = int(input("\nChatbot: Ingrese los créditos comprados: "))
    
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

    print("\nChatbot: Matrícula finalizada con las siguientes materias:")
    for num in seleccion_materias:
        materia = propuestas[num - 1]  # Los números comienzan desde 1 en la lista de propuestas
        print(f"- {materia.nombre}")

    print("\nChatbot: Gracias por usar el sistema de matrícula. ¡Que tengas un excelente semestre!")

if __name__ == "__main__":
    main()
