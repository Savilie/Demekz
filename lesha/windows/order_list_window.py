# windows/order_list_window.py — список заказов
import os
import tkinter as tk
from tkinter import ttk, messagebox
from config import (
    COLOR_MAIN_BG, COLOR_SECONDARY_BG, COLOR_ACCENT,
    FONT_FAMILY, get_resources_dir,
)


class OrderListFrame(tk.Frame):
    def __init__(self, master, db, user=None,
                 on_logout=None, on_add_order=None,
                 on_edit_order=None, on_back=None):
        super().__init__(master, bg=COLOR_MAIN_BG)
        self.master = master
        self.db = db
        self.user = user
        self.role = user["role"] if user else "Гость"
        self.user_name = user["full_name"] if user else "Гость"
        self.on_logout = on_logout
        self.on_add_order = on_add_order
        self.on_edit_order = on_edit_order
        self.on_back = on_back
        self._all_orders = []

        self._build_ui()
        self._load_orders()

    def _build_ui(self):
        top = tk.Frame(self, bg=COLOR_SECONDARY_BG, height=40)
        top.pack(fill="x")
        top.pack_propagate(False)

        # Логотип
        logo_path = os.path.join(get_resources_dir(), "icon.png")
        if os.path.exists(logo_path):
            try:
                from PIL import Image, ImageTk
                img = Image.open(logo_path)
                img.thumbnail((28, 28), Image.LANCZOS)
                logo_img = ImageTk.PhotoImage(img)
                tk.Label(top, image=logo_img, bg=COLOR_SECONDARY_BG).pack(side="left", padx=(10, 5))
                self._logo_img = logo_img
            except Exception:
                pass

        tk.Label(
            top, text="ЧитайГород", font=(FONT_FAMILY, 16, "bold"),
            bg=COLOR_SECONDARY_BG, fg=COLOR_ACCENT,
        ).pack(side="left")

        tk.Label(
            top, text=f"{self.role}: {self.user_name}",
            font=(FONT_FAMILY, 11), bg=COLOR_SECONDARY_BG, fg="black",
        ).pack(side="right", padx=15)

        tk.Button(
            top, text="Выход", font=(FONT_FAMILY, 10),
            bg=COLOR_ACCENT, fg="white", relief="flat",
            command=self._on_logout,
        ).pack(side="right", padx=(0, 10))

        # Панель кнопок
        toolbar = tk.Frame(self, bg=COLOR_MAIN_BG)
        toolbar.pack(fill="x", padx=10, pady=(10, 5))

        tk.Button(
            toolbar, text="← Назад к товарам", font=(FONT_FAMILY, 10),
            bg=COLOR_SECONDARY_BG, fg="black", relief="flat",
            command=self._on_back,
        ).pack(side="left")

        if self.role == "Администратор":
            tk.Button(
                toolbar, text="Добавить заказ", font=(FONT_FAMILY, 10),
                bg=COLOR_ACCENT, fg="white", relief="flat",
                command=self._add_order,
            ).pack(side="right", padx=5)

        # Таблица заказов
        frame = tk.Frame(self, bg=COLOR_MAIN_BG)
        frame.pack(fill="both", expand=True, padx=10, pady=5)

        v_scroll = tk.Scrollbar(frame, orient="vertical")

        self.columns = ("id", "order_date", "delivery_date", "status",
                        "pickup_point", "user_name", "pickup_code")
        col_labels = {
            "id": "№ заказа", "order_date": "Дата заказа",
            "delivery_date": "Дата выдачи", "status": "Статус",
            "pickup_point": "Пункт выдачи", "user_name": "Клиент",
            "pickup_code": "Код получения",
        }
        col_widths = [70, 100, 100, 100, 300, 180, 90]

        self.tree = ttk.Treeview(
            frame, columns=self.columns, show="headings",
            yscrollcommand=v_scroll.set, selectmode="browse", height=20,
        )
        v_scroll.config(command=self.tree.yview)

        for i, col in enumerate(self.columns):
            self.tree.heading(col, text=col_labels[col])
            self.tree.column(col, width=col_widths[i], minwidth=50)

        self.tree.pack(side="left", fill="both", expand=True)
        v_scroll.pack(side="right", fill="y")

        if self.role == "Администратор":
            self.tree.bind("<Double-1>", self._edit_order)

    def _load_orders(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        orders = self.db.get_orders()
        self._all_orders = orders
        # Карта ПВ
        pp_points = self.db.get_pickup_points()
        pp_map = {p["id"]: p["address"] for p in pp_points}

        for o in orders:
            pp_address = pp_map.get(o["pickup_point_id"], str(o["pickup_point_id"]))
            values = (
                o["id"],
                str(o["order_date"]) if o["order_date"] else "",
                str(o["delivery_date"]) if o["delivery_date"] else "",
                o["status"],
                pp_address,
                o["user_name"],
                o["pickup_code"],
            )
            self.tree.insert("", "end", values=values)

    def _add_order(self):
        if self.on_add_order:
            self.on_add_order()

    def _edit_order(self, event):
        selected = self.tree.selection()
        if not selected or not self.on_edit_order:
            return
        item = self.tree.item(selected[0])
        vals = item["values"]
        if not vals:
            return
        order_id = vals[0]
        o = None
        for order in self._all_orders:
            if order["id"] == order_id:
                o = order
                break
        if o:
            self.on_edit_order(o)

    def _on_back(self):
        if self.on_back:
            self.on_back()

    def _on_logout(self):
        if messagebox.askyesno("Выход", "Выйти из учетной записи?"):
            if self.on_logout:
                self.on_logout()
