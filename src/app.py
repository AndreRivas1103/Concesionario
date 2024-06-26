
from abc import ABC
import tkinter
import tkinter.messagebox
import tkinter.ttk
from tkcalendar import DateEntry
from typing import Literal, Optional
from src.models.purchase import Purchase
from src.db.database import Database
from src.exceptions import db_exceptions
from src.models.user import User
from src.utils.color import Color
from src.models.car import Car

class UILog:

    FORMAT: tuple[str, int] = ("Arial", 14)

    def __init__(self) -> None:
        self.__window: tkinter.Tk = tkinter.Tk()
        self.__window.title("Concesionario de Carros")
        self.__window.config(padx=35, pady=35)

        # Ingresar Nombre
        self.__label_name: tkinter.Label = tkinter.Label(text="Ingresa tu nombre", font=self.FORMAT)
        self.__label_name.grid(column=0, row=1)

        self.__box_name: tkinter.Entry = tkinter.Entry(width=20, font=self.FORMAT)
        self.__box_name.grid(column=0, row=2)

        # Ingresar Numero
        self.__label_phone: tkinter.Label = tkinter.Label(text="Ingresa tu número de teléfono", font=self.FORMAT)
        self.__label_phone.grid(column=0, row=3)

        # valida numero
        vcmd: tuple[str, Literal['%P']] = (self.__window.register(self.__validate_numeric), '%P')
        self.__box_phone: tkinter.Entry = tkinter.Entry(width=20, font=self.FORMAT, validate='key', validatecommand=vcmd)
        self.__box_phone.grid(column=0, row=4)

        self.__button_send: tkinter.Button = tkinter.Button(text="Send", font=self.FORMAT, command=self.save_data)
        self.__button_send.grid(column=0, row=5)

        self.__user: Optional[User] = None
        self.__window.mainloop()

    def __validate_numeric(self, P: str) -> bool:
        return P.isdigit() or P == ""

    def save_data(self) -> None:
        name: str = self.__box_name.get()
        phone: int = self.__box_phone.get()

        if phone == "":
            tkinter.messagebox.showerror(message="Debes ingresar un numero.")
        else:
            try:
                if not Database.user_exist(name, phone):
                    Database.add_user(name=name, phone_number=phone)

                self.__user = Database.get_user(name=name, phone_number=phone)
                UISelectEvent(self.__user)

            except db_exceptions.PhoneNumberRepeated:
                tkinter.messagebox.showerror(message="Los datos ingresados no coinciden. Verifica Nuevamente")


class UISelectEvent:

    def __init__(self, user: User) -> None:
        self.__window: tkinter.Toplevel = tkinter.Toplevel()
        self.__window.config(padx=35, pady=35)
        self.__window.title("Welcome")

        self.__driver_test: tkinter.ttk.Button = tkinter.ttk.Button(self.__window, text="Test Drive", command=self.open_driver_test)
        self.__driver_test.grid(column=0, row=1)

        self.__purchase: tkinter.ttk.Button = tkinter.ttk.Button(self.__window, text="Pre-compra", command=self.open_purchase)
        self.__purchase.grid(column=1, row=1)
        self.__window.focus()
        self.__window.grab_set()
        self.__user: User = user

    def open_driver_test(self) -> None:
        UIDriver_test(self.__user)
        self.__window.destroy()

    def open_purchase(self) -> None:
        UIPurchase(self.__user)
        self.__window.destroy()


class Event(ABC):

    def __init__(self, user: User) -> None:
        self._user: User = user
        self._window: tkinter.Toplevel = tkinter.Toplevel()
        self._window.config(padx=35, pady=35)
        self._window.focus()
        self._undo: tkinter.ttk.Button = tkinter.ttk.Button(self._window, text="Undo", command=self.return_page)

    def return_page(self) -> None:
        UISelectEvent(self._user)
        self._window.destroy()


class UIPurchase(Event):
    def __init__(self, user: User) -> None:
        super().__init__(user)
        self._window.title("Pre-compra")
        self._undo.grid(column=0, row=2)

        # Opciones de carro
        self._label_car: tkinter.Label = tkinter.Label(self._window, text="Selecciona el tipo ")
        self._label_car.grid(column=0, row=0)
        self._types_car: tkinter.Listbox = tkinter.Listbox(self._window, selectmode=tkinter.SINGLE, exportselection=False)
        for i in Purchase.TYPES_CAR:
            self._types_car.insert(tkinter.END, i)
        self._types_car.grid(column=1, row=0)

        # Rin
        self._label_rim: tkinter.Label = tkinter.Label(self._window, text="Selecciona el tipo de rin ")
        self._label_rim.grid(column=0, row=1)
        self._types_rim: tkinter.Listbox = tkinter.Listbox(self._window, selectmode=tkinter.SINGLE, exportselection=False)
        for i in Purchase.TYPES_RIM:
            self._types_rim.insert(tkinter.END, i)
        self._types_rim.grid(column=1, row=1)

        # Motor
        self._label_engine: tkinter.Label = tkinter.Label(self._window, text="Selecciona el cilindraje ")
        self._label_engine.grid(column=3, row=0)
        self._engine_displacement: tkinter.Listbox = tkinter.Listbox(self._window, selectmode=tkinter.SINGLE, exportselection=False)
        for i in Purchase.ENGINE_DISPLACEMENT:
            self._engine_displacement.insert(tkinter.END, i)
        self._engine_displacement.grid(column=4, row=0)

        self._label_color: tkinter.Label = tkinter.Label(self._window, text="Escribe tu codigo de color (r, g, b)")
        self._label_color.grid(column=3, row=1)
        # Sedes
        self._label_sede: tkinter.Label = tkinter.Label(self._window, text="Selecciona tu sede mas cercana")
        self._label_sede.grid(column=5, row=0)
        self._sedes: tkinter.Listbox = tkinter.Listbox(self._window, selectmode=tkinter.SINGLE, exportselection=False)
        for i in Purchase.SEDES:
            self._sedes.insert(tkinter.END, i)
        self._sedes.grid(column=6, row=0)

        vcmd = (self._window.register(self.validate_color), '%P')
        self._color_r: tkinter.ttk.Entry = tkinter.ttk.Entry(self._window, validate='key', validatecommand=vcmd)
        self._color_r.grid(column=4, row=1)
        self._color_g: tkinter.ttk.Entry = tkinter.ttk.Entry(self._window, validate='key', validatecommand=vcmd)
        self._color_g.grid(column=5, row=1)
        self._color_b: tkinter.ttk.Entry = tkinter.ttk.Entry(self._window, validate='key', validatecommand=vcmd)
        self._color_b.grid(column=6, row=1)

        self._submit: tkinter.Button = tkinter.Button(self._window, text="Enviar", command=self.submit)
        self._submit.grid(column=5, row=2)

        self._label_pay: tkinter.Label = tkinter.Label(self._window, text="Selecciona metodo de pago. ")
        self._label_pay.grid(column=3, row=2)
        self._pay: tkinter.Listbox = tkinter.Listbox(self._window, selectmode=tkinter.SINGLE, exportselection=False)
        for i in Purchase.PAY_METHODS:
            self._pay.insert(tkinter.END, i)
        self._pay.grid(column=4, row=2)

        self.resul: Optional[Purchase] = None
        self._car: Optional[Car] = None

    def validate_color(self, P: str):
        if P == '':
            return True
        if P.isdigit():
            num = int(P)
            if 0 <= num <= 255:
                return True
        return False

    def submit(self):
        try:
            r: int = int(self._color_r.get())
            g: int = int(self._color_g.get())
            b: int = int(self._color_b.get())
        except ValueError:
            tkinter.messagebox.showerror("Error. ", "Por favor un numero dentro del rango establecido. ")
            return

        color: Color = Color(r, g, b)

        type_car = self._types_car.curselection()
        type_rim = self._types_rim.curselection()
        engine_displacement = self._engine_displacement.curselection()
        pay_method = self._pay.curselection()
        sede = self._sedes.curselection()
        if not type_car or not type_rim or not engine_displacement or not pay_method or not pay_method:
            tkinter.messagebox.showerror("Error. ", "Debes escoger todos los campos")
            return

        type_car = Purchase.TYPES_CAR[type_car[0]]
        type_rim = Purchase.TYPES_RIM[type_rim[0]]
        engine_displacement = Purchase.ENGINE_DISPLACEMENT[engine_displacement[0]]
        pay_method = Purchase.PAY_METHODS[pay_method[0]]
        sede = Purchase.SEDES[sede[0]]

        self._car = Car(type_car, type_rim, color, engine_displacement, color)
        self.resul = Purchase(user=self._user, car=self._car, pay_method=pay_method)
        tkinter.messagebox.showinfo("Resumen", f"Nombre: {self._user.get_name()} \nTelefono: {self._user.get_number()}\n"f"tipo de carro: {type_car}\n"
                                    f"Tipo de rin: {type_rim}\nCilindraje: {engine_displacement}\nColor: {color}\nMétodo de pago: {pay_method}\nSede: {sede}\n"" \nSe le mando la solicitud al concesionario en 48 horas puedes acercarte a la sede que seleccionaste a recibir el asesoriamiento.")

class UIDriver_test(Event):
    def __init__(self, user: User) -> None:
        super().__init__(user)
        self._window.title("Test Drive")
        self._window.focus()
        self._undo.grid(column=0, row=2)

        # Seleccionar Fecha
        self._date: DateEntry = DateEntry(self._window,
                                           width=12,
                                           background='darkblue',
                                           foreground='white',
                                           borderwidth=2)
        self._date.grid(column=0, row=0)

        # Seleccionar Hora
        self._hour_label = tkinter.ttk.Label(self._window, text="Selecciona la hora:")
        self._hour_label.grid(column=1, row=0)
        self._hour_combo = tkinter.ttk.Combobox(self._window, values=["08:00", "09:00", "10:00", "11:00", "12:00", "13:00"])
        self._hour_combo.grid(column=2, row=0)

        # Seleccionar tipo de carro
        self._car_type_label = tkinter.ttk.Label(self._window, text="Selecciona el tipo de carro:")
        self._car_type_label.grid(column=1, row=1)
        self._car_type_combo = tkinter.ttk.Combobox(self._window, values=Purchase.TYPES_CAR)
        self._car_type_combo.grid(column=2, row=1)

        # Enviar
        self._send_button = tkinter.ttk.Button(self._window, text="Enviar", command=self.submit)
        self._send_button.grid(column=1, row=2)

    def submit(self):
        date = self._date.get_date()
        hour = self._hour_combo.get()
        car_type = self._car_type_combo.get()

        if not date or not hour or not car_type:
            tkinter.messagebox.showerror("Error. ", "Llena todos los campos")
        else:
            tkinter.messagebox.showinfo(
                "Cita Registrada, informacion enviada al concesionario.",
                "El dia de la cita dirigete al concesionario y llega 15 minutos antes."
            )

if __name__ == "__main__":
    ui_log = UILog()
