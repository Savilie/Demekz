# main.py — точка входа
import sys
import os
import tkinter as tk

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import Database
from windows.auth_window import AuthFrame
from windows.main_window import MainFrame
from windows.product_edit_window import ProductEditFrame
from windows.order_list_window import OrderListFrame
from windows.order_edit_window import OrderEditFrame


class App:
    def __init__(self):
        self.db = Database()
        self.root = tk.Tk()
        self.root.app = self
        self.root.title("ЧитайГород")
        self.root.geometry("500x400")
        self.root.minsize(400, 300)
        self.current_frame = None
        self.current_user = None
        self._show_auth()

    def _clear(self):
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None

    def _show_auth(self):
        self._clear()
        self.root.geometry("500x400")
        self.current_frame = AuthFrame(
            self.root,
            on_login_success=self._on_login,
            on_guest=self._on_guest,
        )
        self.current_frame.pack(fill="both", expand=True)

    def _on_login(self, user):
        self.current_user = user
        self._show_main()

    def _on_guest(self):
        self.current_user = None
        self._show_main()

    def _show_main(self):
        self._clear()
        self.root.geometry("1200x700")
        self.current_frame = MainFrame(
            self.root, db=self.db, user=self.current_user,
            on_logout=self._show_auth,
            on_add_product=self._show_add_product,
            on_edit_product=self._show_edit_product,
            on_open_orders=self._show_orders,
        )
        self.current_frame.pack(fill="both", expand=True)

    def _show_add_product(self):
        self._clear()
        self.root.geometry("800x650")
        self.current_frame = ProductEditFrame(
            self.root, db=self.db, product=None,
            on_save=self._on_product_saved,
            on_cancel=self._show_main,
        )
        self.current_frame.pack(fill="both", expand=True)

    def _show_edit_product(self, product):
        self._clear()
        self.root.geometry("800x650")
        self.current_frame = ProductEditFrame(
            self.root, db=self.db, product=product,
            on_save=self._on_product_saved,
            on_cancel=self._show_main,
        )
        self.current_frame.pack(fill="both", expand=True)

    def _on_product_saved(self, article):
        # Возвращаемся к списку товаров (он перезагрузится)
        self._show_main()

    def _show_orders(self):
        self._clear()
        self.root.geometry("1200x700")
        self.current_frame = OrderListFrame(
            self.root, db=self.db, user=self.current_user,
            on_logout=self._show_auth,
            on_add_order=self._show_add_order,
            on_edit_order=self._show_edit_order,
            on_back=self._show_main,
        )
        self.current_frame.pack(fill="both", expand=True)

    def _show_add_order(self):
        self._clear()
        self.root.geometry("900x650")
        self.current_frame = OrderEditFrame(
            self.root, db=self.db, order=None,
            on_save=self._show_orders,
            on_cancel=self._show_orders,
        )
        self.current_frame.pack(fill="both", expand=True)

    def _show_edit_order(self, order):
        self._clear()
        self.root.geometry("900x650")
        self.current_frame = OrderEditFrame(
            self.root, db=self.db, order=order,
            on_save=self._show_orders,
            on_cancel=self._show_orders,
        )
        self.current_frame.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    App().run()
