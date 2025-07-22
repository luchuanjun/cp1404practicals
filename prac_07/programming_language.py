class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, pointer_arithmetic):
        """
        :param name: str
        :param typing: str (e.g. 'Dynamic', 'Static')
        :param reflection: bool
        :param pointer_arithmetic: bool, indicates if language supports pointer arithmetic
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        reflection_str = "Yes" if self.reflection else "No"
        pointer_str = "Yes" if self.pointer_arithmetic else "No"
        return f"{self.name} ({self.typing} typing), Reflection: {reflection_str}, Pointer Arithmetic: {pointer_str}"
