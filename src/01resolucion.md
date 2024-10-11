# Resolución

1. ¿Qué es un sistema operativo y cuales son sus partes más importantes?

    Un sistema operativo es el software que administra los recursos de una
    computadora. Asimismo, proporciona una interfaz abstracta que permite
    la comunicación entre los programas y el hardware.

    Existe una gran variedad de sistemas operativos destinados a diferentes
    aplicaciones. Pero, la mayoría de ellos comparten los siguientes
    componentes:

    1. **Núcleo:** Es el componente más importante de un sistema operativo.
    Ya que se encarga de interactuar con el hardware directamente. Se puede
    clasificar según su alcance, esto es, la cantidad de funciones que este
    realize.
    2. **Gestor de procesos:** Administra la ejecución de programas y procesos
    en la CPU.
    3. **Gestor de archivos:** Controla a bajo nivel la forma en que se
    almacenan, organizan y acceden a los archivos.
    4. **Interfaz de usuario:** Este componente permite al usuario interactuar
    con el sistema, ya sea mediante una interfaz gráfica o por línea de
    comandos.

2. Mencione al menos 5 comandos de navegación en el Shell de Windows y describe
con tus propias palabras que hace cada uno.

    Antes de listar los comandos, explicaré la diferencias entre los dos shells
    disponibles en Windows: **cmd** y **Powershell**.

    1. **cmd:** Es el intérprete de comandos tradicional en Windows.
    Se enfoca en tareas simples de archivos y ejecución de programas.
    2. **Powershell:** Es una herramienta más moderna y potente. Aparte de
    ejecutar algunos comandos tradicionales de cmd mediante **alias**,
    utiliza un lenguaje de scripting más avanzado basado en objetos .NET.

    Ahora veamos algunos comandos de navegación:

    | **cmd** | **Poweshell** | Descripción |
    | --- | --- | --- |
    |`cd`|`Set-Location`|Cambia el directorio actual. Sirve para moverte entre carpetas|
    |`dir`|`Get-ChildItem`|Lista los archivos y carpetas en el directorio actual|
    |`mkdir`|`New-Item -ItemType Directory`|Crea una nueva carpeta|
    |`rmdir`|`Remove-Item`|Elimina una carpeta vacía. Si no está vacia retorna un error|
    |`cls`|`Clear-Host`|Limpia la pantalla del terminal|

    Como se puede apreciar los comandos de Powershell son más verbosos y largos.
    Pero ofrecer una mayor flexibilidad en comparación a los comandos de cmd.

3. Describa cómo es el proceso de comunicación entre el Usuario - Shell – Kernel.

    En la mayoría de sistemas operativos, los usuarios interactúan con el sistema operativo
    a través de un **shell**, el cual proporciona una interfaz amigable para la ejecución
    de funciones del sistema. Estos componentes interactúan de la siguiente manera:

    1. Usuario: Interactúa con el sistema operativo a través de la línea de comandos.
    2. Shell: Interpreta los comandos ingresados por el usuario y los
    traduce en instrucciones comprensibles para el Kernel. Es la interfaz entre el
    usuario y el núcleo del sistema operativo.
    3. Kernel: Recibe las instrucciones del shell, las ejecuta y devuelve los
    resultados al shell, el cual los presenta al Usuario.

4. De un ejemplo de hilos aplicados en una situación cotidiana distinta a las
mencionadas en clase.

    En el salón, se ha decidido celebrar el cumpleaños de un profesor con un compartir.
    En lugar de que solo una persona se encargue del compartir, se puede dividir la
    tarea entre varios compañeros. Cada una de las tareas representaría un **hilo**:

    - Un compañero se encarga de comprar la torta.
    - Otro más compra los globos y la decoración.
    - Otro se encarga de reservar el lugar.

    Cada persona **("hilo")** está trabajando de manera simultánea en su propia tarea.
    Así, no se tiene que esperar a que uno termine para que el siguiente empiece.

    Si alguien lo hiciera solo, tendría que hacer cada tarea una tras otra,
    lo que te tomaría mucho más tiempo. Gracias a la trabajo en equipo
    **("concurrencia de hilos")**, el compartir estaría listo a tiempo.
