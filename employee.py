class Employee:
    _employee_id = 1

    def __init__(self, name_val: str = "anonymous") -> None:
        self.name = name_val
        self.emp_id = self._employee_id
        Employee._employee_id += 1

    def __str__(self) -> str:
        return f"This is the {self.name} that will be found in the {self.emp_id}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name_val: str) -> None:
        self._name = name_val

    def setdata(self) -> None:
        self.name = input(f"Input {self.name}'s name: ")

    def putdata(self) -> None:
        print(self)
