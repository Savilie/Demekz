# windows/order_edit_window.py — форма добавления/редактирования заказа
import os
import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from config import (
    COLOR_MAIN_BG, COLOR_SECONDARY_BG, COLOR_ACCENT,
    FONT_FAMILY, get_resources_dir,
)


class OrderEditFrame(tk.Frame):
    def __init__(self, master, db, order=None, on_save=None, on_cancel=None):
        super().__init__(master, bg=COLOR_MAIN_BG)
        self.master = master
        self.db = db
        self.order = order
        self.on_save = on_save
        self.on_cancel = on_cancel
        self.is_edit = order is not None

        self._build_ui()
        if self.is_edit:
            self._load_order()

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

        title = "Редактирование заказа" if self.is_edit else "Добавление заказа"
        tk.Label(
            top, text=title, font=(FONT_FAMILY, 12),
            bg=COLOR_SECONDARY_BG, fg="black",
        ).pack(side="left", padx=20)

        # Форма
        main = tk.Frame(self, bg=COLOR_MAIN_BG)
        main.pack(fill="both", expand=True, padx=20, pady=10)

        if self.is_edit:
            tk.Label(main, text=f"Номер заказа: {self.order['id']}",
                     font=(FONT_FAMILY, 11, "bold"),
                     bg=COLOR_MAIN_BG, fg="#000").grid(row=0, column=0, columnspan=2,
                                                       sticky="w", pady=(0, 10))

        row = 1 if not self.is_edit else 0

        # Клиент
        tk.Label(main, text="Клиент:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        users = self.db.execute("SELECT id, full_name FROM users WHERE role = 'Авторизированный клиент' ORDER BY full_name")
        self.client_combo = ttk.Combobox(
            main, values=[u["full_name"] for u in users],
            state="readonly", font=(FONT_FAMILY, 11), width=35,
        )
        self.client_combo.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        self.client_map = {u["full_name"]: u["id"] for u in users}
        if users:
            self.client_combo.set(users[0]["full_name"])
        row += 1

        # Статус
        tk.Label(main, text="Статус:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        self.status_combo = ttk.Combobox(
            main, values=["Новый", "Завершен", "Отменен"],
            state="readonly", font=(FONT_FAMILY, 11), width=35,
        )
        self.status_combo.set("Новый")
        self.status_combo.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        row += 1

        # Пункт выдачи
        tk.Label(main, text="Пункт выдачи:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        pp_points = self.db.get_pickup_points()
        self.pp_combo = ttk.Combobox(
            main, values=[p["address"] for p in pp_points],
            state="readonly", font=(FONT_FAMILY, 11), width=35,
        )
        self.pp_combo.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        self.pp_map = {p["address"]: p["id"] for p in pp_points}
        if pp_points:
            self.pp_combo.set(pp_points[0]["address"])
        row += 1

        # Дата заказа
        tk.Label(main, text="Дата заказа (ГГГГ-ММ-ДД):", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        self.entry_order_date = tk.Entry(main, font=(FONT_FAMILY, 11))
        self.entry_order_date.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        self.entry_order_date.insert(0, datetime.date.today().isoformat())
        row += 1

        # Дата доставки
        tk.Label(main, text="Дата выдачи (ГГГГ-ММ-ДД):", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        self.entry_delivery_date = tk.Entry(main, font=(FONT_FAMILY, 11))
        self.entry_delivery_date.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        row += 1

        # Код получения
        tk.Label(main, text="Код получения:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        self.entry_code = tk.Entry(main, font=(FONT_FAMILY, 11))
        self.entry_code.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        import random
        self.entry_code.insert(0, str(random.randint(100, 999)))
        row += 1

        main.grid_columnconfigure(1, weight=1)

        # Товары в заказе
        items_frame = tk.LabelFrame(main, text="Товары в заказе",
                                     font=(FONT_FAMILY, 11),
                                     bg=COLOR_MAIN_BG)
        items_frame.grid(row=row, column=0, columnspan=2,
                         sticky="nsew", pady=(15, 5))
        main.grid_rowconfigure(row, weight=1)

        # Список товаров
        self.items_tree = ttk.Treeview(
            items_frame, columns=("article", "name", "quantity"),
            show="headings", height=6,
        )
        self.items_tree.heading("article", text="Артикул")
        self.items_tree.heading("name", text="Наименование")
        self.items_tree.heading("quantity", text="Кол-во")
        self.items_tree.column("article", width=80)
        self.items_tree.column("name", width=250)
        self.items_tree.column("quantity", width=60)
        self.items_tree.pack(fill="both", expand=True, padx=5, pady=5)

        # Кнопка добавления товара в заказ
        btn_frame = tk.Frame(items_frame, bg=COLOR_MAIN_BG)
        btn_frame.pack(fill="x", padx=5, pady=(0, 5))

        tk.Label(btn_frame, text="Артикул:", font=(FONT_FAMILY, 10),
                 bg=COLOR_MAIN_BG).pack(side="left")
        self.entry_item_article = tk.Entry(btn_frame, font=(FONT_FAMILY, 10), width=12)
        self.entry_item_article.pack(side="left", padx=5)

        tk.Label(btn_frame, text="Кол-во:", font=(FONT_FAMILY, 10),
                 bg=COLOR_MAIN_BG).pack(side="left")
        self.entry_item_qty = tk.Entry(btn_frame, font=(FONT_FAMILY, 10), width=5)
        self.entry_item_qty.insert(0, "1")
        self.entry_item_qty.pack(side="left", padx=5)

        tk.Button(
            btn_frame, text="+", font=(FONT_FAMILY, 10),
            bg=COLOR_ACCENT, fg="white", relief="flat",
            command=self._add_item,
        ).pack(side="left", padx=5)

        tk.Button(
            btn_frame, text="Удалить", font=(FONT_FAMILY, 10),
            bg="#CC0000", fg="white", relief="flat",
            command=self._remove_item,
        ).pack(side="left", padx=5)

        # Кнопки внизу
        btn_main = tk.Frame(self, bg=COLOR_MAIN_BG)
        btn_main.pack(fill="x", padx=20, pady=(0, 15))

        tk.Button(
            btn_main, text="Назад", font=(FONT_FAMILY, 11),
            bg=COLOR_SECONDARY_BG, fg="black", relief="flat",
            command=self._on_cancel,
        ).pack(side="left", padx=(0, 10))

        if self.is_edit:
            tk.Button(
                btn_main, text="Удалить заказ", font=(FONT_FAMILY, 11),
                bg="#CC0000", fg="white", relief="flat",
                command=self._on_delete,
            ).pack(side="left")

        tk.Button(
            btn_main, text="Сохранить", font=(FONT_FAMILY, 11),
            bg=COLOR_ACCENT, fg="white", relief="flat",
            command=self._on_save,
        ).pack(side="right")

        # Данные для items
        self.order_items_data = []  # список dict: {article, name, quantity}

    def _load_order(self):
        o = self.order
        # Клиент
        for name, uid in self.client_map.items():
            if uid == o["user_id"]:
                self.client_combo.set(name)
                break

        self.status_combo.set(o["status"])

        for addr, pid in self.pp_map.items():
            if pid == o["pickup_point_id"]:
                self.pp_combo.set(addr)
                break

        self.entry_order_date.delete(0, tk.END)
        self.entry_order_date.insert(0, str(o["order_date"]) if o["order_date"] else "")

        self.entry_delivery_date.delete(0, tk.END)
        self.entry_delivery_date.insert(0, str(o["delivery_date"]) if o["delivery_date"] else "")

        self.entry_code.delete(0, tk.END)
        self.entry_code.insert(0, str(o["pickup_code"]))

        # Загружаем товары в заказе
        items = self.db.get_order_items(o["id"])
        self.order_items_data = []
        for item in items:
            self.order_items_data.append({
                "article": item["product_article"],
                "name": item["product_name"],
                "quantity": item["quantity"],
            })
        self._refresh_items_tree()

    def _add_item(self):
        article = self.entry_item_article.get().strip()
        qty_str = self.entry_item_qty.get().strip()
        if not article:
            messagebox.showwarning("Ошибка", "Введите артикул товара")
            return
        try:
            qty = int(qty_str) if qty_str else 1
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Ошибка", "Количество должно быть положительным числом")
            return

        # Проверяем существование товара
        p = self.db.get_product(article)
        if not p:
            messagebox.showerror("Ошибка", f"Товар с артикулом '{article}' не найден")
            return

        # Проверяем, нет ли уже такого товара
        for item in self.order_items_data:
            if item["article"] == article:
                messagebox.showwarning("Ошибка", "Этот товар уже добавлен в заказ")
                return

        # Также проверяем, если это редактирование — может товар уже есть в БД
        if self.is_edit:
            existing = self.db.execute(
                "SELECT * FROM order_items WHERE order_id = %s AND product_article = %s",
                (self.order["id"], article),
            )
            if existing:
                messagebox.showwarning("Ошибка", "Этот товар уже есть в заказе")
                return

        self.order_items_data.append({
            "article": article,
            "name": p["name"],
            "quantity": qty,
        })
        self._refresh_items_tree()
        self.entry_item_article.delete(0, tk.END)
        self.entry_item_qty.delete(0, tk.END)
        self.entry_item_qty.insert(0, "1")

    def _remove_item(self):
        selected = self.items_tree.selection()
        if not selected:
            return
        idx = self.items_tree.index(selected[0])
        if 0 <= idx < len(self.order_items_data):
            del self.order_items_data[idx]
            self._refresh_items_tree()

    def _refresh_items_tree(self):
        for item in self.items_tree.get_children():
            self.items_tree.delete(item)
        for d in self.order_items_data:
            self.items_tree.insert("", "end", values=(d["article"], d["name"], d["quantity"]))

    def _validate(self):
        errors = []
        if not self.client_combo.get():
            errors.append("Выберите клиента")

        if not self.entry_order_date.get().strip():
            errors.append("Введите дату заказа")
        else:
            try:
                datetime.date.fromisoformat(self.entry_order_date.get().strip())
            except ValueError:
                errors.append("Дата заказа должна быть в формате ГГГГ-ММ-ДД")

        dd = self.entry_delivery_date.get().strip()
        if dd:
            try:
                datetime.date.fromisoformat(dd)
            except ValueError:
                errors.append("Дата выдачи должна быть в формате ГГГГ-ММ-ДД")

        if not self.order_items_data:
            errors.append("Добавьте хотя бы один товар в заказ")

        if errors:
            messagebox.showerror("Ошибка валидации", "\n".join(errors))
            return False
        return True

    def _on_save(self):
        if not self._validate():
            return

        data = {
            "order_date": self.entry_order_date.get().strip(),
            "delivery_date": self.entry_delivery_date.get().strip() or None,
            "pickup_point_id": self.pp_map.get(self.pp_combo.get(), 1),
            "user_id": self.client_map.get(self.client_combo.get(), 1),
            "pickup_code": int(self.entry_code.get().strip() or 0),
            "status": self.status_combo.get(),
        }

        try:
            if self.is_edit:
                self.db.update_order(self.order["id"], data)
                # Обновляем состав — удаляем старый, вставляем новый
                self.db.execute("DELETE FROM order_items WHERE order_id = %s",
                                (self.order["id"],))
                for item in self.order_items_data:
                    self.db.execute(
                        "INSERT INTO order_items (order_id, product_article, quantity) VALUES (%s, %s, %s)",
                        (self.order["id"], item["article"], item["quantity"]),
                    )
                msg = "Заказ обновлён"
            else:
                order_id = self.db.add_order(data)
                for item in self.order_items_data:
                    self.db.execute(
                        "INSERT INTO order_items (order_id, product_article, quantity) VALUES (%s, %s, %s)",
                        (order_id, item["article"], item["quantity"]),
                    )
                msg = f"Заказ №{order_id} добавлен"

            messagebox.showinfo("Успешно", msg)
            if self.on_save:
                self.on_save()
        except Exception as e:
            messagebox.showerror("Ошибка БД", str(e))

    def _on_delete(self):
        if not messagebox.askyesno(
            "Подтверждение",
            f"Удалить заказ №{self.order['id']}?",
        ):
            return
        try:
            self.db.delete_order(self.order["id"])
            messagebox.showinfo("Успешно", "Заказ удалён")
            if self.on_save:
                self.on_save()
        except Exception as e:
            messagebox.showerror("Ошибка БД", str(e))

    def _on_cancel(self):
        if self.on_cancel:
            self.on_cancel()
