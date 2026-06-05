# windows/main_window.py — главный фрейм (список товаров)
import tkinter as tk
from tkinter import ttk, messagebox
import os
from config import (
    COLOR_MAIN_BG, COLOR_SECONDARY_BG, COLOR_ACCENT,
    COLOR_DISCOUNT_HIGH, COLOR_OUT_OF_STOCK,
    COLOR_DISCOUNTED_PRICE, COLOR_FINAL_PRICE,
    FONT_FAMILY, get_resources_dir, get_app_dir,
)
from PIL import Image, ImageTk


class MainFrame(tk.Frame):
    def __init__(self, master, db, user=None, on_logout=None,
                 on_add_product=None, on_edit_product=None,
                 on_open_orders=None):
        super().__init__(master, bg=COLOR_MAIN_BG)
        self.master = master
        self.db = db
        self.on_logout = on_logout
        self.on_add_product = on_add_product
        self.on_edit_product = on_edit_product
        self.on_open_orders = on_open_orders
        self.role = user["role"] if user else "Гость"
        self.user_name = user["full_name"] if user else "Гость"
        self._all_products = []

        self.image_cache = {}
        self._find_resources()

        self._build_ui()
        self._load_products()

    def _find_resources(self):
        self.photos_dir = get_resources_dir()
        app_dir = get_app_dir()
        import_dir = os.path.normpath(os.path.join(app_dir, "..", "Модуль 1", "import_data", "import"))
        if os.path.exists(import_dir):
            self.import_dir = import_dir
        else:
            self.import_dir = None

    def _get_photo(self, photo_name, size=(50, 70)):
        if not photo_name:
            return self._get_placeholder(size)
        cache_key = f"{photo_name}_{size}"
        if cache_key in self.image_cache:
            return self.image_cache[cache_key]
        for base_dir in (self.photos_dir, self.import_dir):
            if base_dir:
                path = os.path.join(base_dir, photo_name)
                if os.path.exists(path):
                    try:
                        img = Image.open(path)
                        img.thumbnail(size, Image.LANCZOS)
                        photo = ImageTk.PhotoImage(img)
                        self.image_cache[cache_key] = photo
                        return photo
                    except Exception:
                        pass
        return self._get_placeholder(size)

    def _get_placeholder(self, size=(50, 70)):
        key = f"ph_{size}"
        if key not in self.image_cache:
            for base_dir in (self.photos_dir, self.import_dir):
                if base_dir:
                    path = os.path.join(base_dir, "picture.png")
                    if os.path.exists(path):
                        try:
                            img = Image.open(path)
                            img.thumbnail(size, Image.LANCZOS)
                            self.image_cache[key] = ImageTk.PhotoImage(img)
                            return self.image_cache[key]
                        except Exception:
                            pass
            img = Image.new("RGB", size, "#CCCCCC")
            self.image_cache[key] = ImageTk.PhotoImage(img)
        return self.image_cache[key]

    def _build_ui(self):
        # Верхняя панель
        top = tk.Frame(self, bg=COLOR_SECONDARY_BG, height=40)
        top.pack(fill="x")
        top.pack_propagate(False)

        # Логотип в топбаре
        self._top_logo = None
        logo_path = os.path.join(self.photos_dir, "icon.png")
        if os.path.exists(logo_path):
            try:
                img = Image.open(logo_path)
                img.thumbnail((28, 28), Image.LANCZOS)
                self._top_logo = ImageTk.PhotoImage(img)
                tk.Label(top, image=self._top_logo, bg=COLOR_SECONDARY_BG).pack(side="left", padx=(10, 5))
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

        # Панель инструментов (только для менеджера и админа)
        toolbar = tk.Frame(self, bg=COLOR_MAIN_BG)
        toolbar.pack(fill="x", padx=10, pady=(10, 5))

        if self.role in ("Менеджер", "Администратор"):
            tk.Label(toolbar, text="Поиск:", font=(FONT_FAMILY, 10), bg=COLOR_MAIN_BG).pack(side="left")
            self.entry_search = tk.Entry(toolbar, font=(FONT_FAMILY, 10), width=30)
            self.entry_search.pack(side="left", padx=(5, 15))
            self.entry_search.bind("<KeyRelease>", lambda e: self._reload())

            tk.Label(toolbar, text="Сортировка:", font=(FONT_FAMILY, 10), bg=COLOR_MAIN_BG).pack(side="left")
            self.sort_combo = ttk.Combobox(
                toolbar, values=["Нет", "Цена ↑", "Цена ↓", "Кол-во ↑", "Кол-во ↓"],
                state="readonly", font=(FONT_FAMILY, 10), width=12,
            )
            self.sort_combo.set("Нет")
            self.sort_combo.pack(side="left", padx=5)
            self.sort_combo.bind("<<ComboboxSelected>>", lambda e: self._reload())

            tk.Label(toolbar, text="Скидка:", font=(FONT_FAMILY, 10), bg=COLOR_MAIN_BG).pack(side="left", padx=(15, 5))
            self.discount_combo = ttk.Combobox(
                toolbar, values=["Все диапазоны", "0-12.99%", "13-16.99%", "17% и более"],
                state="readonly", font=(FONT_FAMILY, 10), width=16,
            )
            self.discount_combo.set("Все диапазоны")
            self.discount_combo.pack(side="left", padx=5)
            self.discount_combo.bind("<<ComboboxSelected>>", lambda e: self._reload())

        if self.role == "Администратор":
            tk.Button(
                toolbar, text="Добавить товар", font=(FONT_FAMILY, 10),
                bg=COLOR_ACCENT, fg="white", relief="flat",
                command=self._add_product,
            ).pack(side="right", padx=5)

        if self.role in ("Менеджер", "Администратор"):
            tk.Button(
                toolbar, text="Заказы", font=(FONT_FAMILY, 10),
                bg=COLOR_ACCENT, fg="white", relief="flat",
                command=self._open_orders,
            ).pack(side="right", padx=5)

        # ===== Основная область: только таблица (на всю ширину) =====
        main_area = tk.Frame(self, bg=COLOR_MAIN_BG)
        main_area.pack(fill="both", expand=True, padx=10, pady=5)

        v_scroll = tk.Scrollbar(main_area, orient="vertical")
        h_scroll = tk.Scrollbar(main_area, orient="horizontal")

        self.columns = ("article", "name", "category",
                        "manufacturer", "supplier", "price", "discount", "quantity")
        col_labels = {
            "article": "Артикул", "name": "Наименование",
            "category": "Категория", "manufacturer": "Производитель",
            "supplier": "Поставщик", "price": "Цена",
            "discount": "Скидка%", "quantity": "Кол-во",
        }
        col_widths = [80, 280, 150, 150, 150, 120, 70, 70]

        style = ttk.Style()
        style.configure("Treeview", rowheight=60)

        self.tree = ttk.Treeview(
            main_area, columns=self.columns, show="tree headings",
            yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set,
            selectmode="browse", height=22,
        )
        v_scroll.config(command=self.tree.yview)
        h_scroll.config(command=self.tree.xview)

        self.tree.column("#0", width=55, minwidth=40)

        for i, col in enumerate(self.columns):
            self.tree.heading(col, text=col_labels[col])
            self.tree.column(col, width=col_widths[i], minwidth=50)

        self.tree.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")
        main_area.grid_rowconfigure(0, weight=1)
        main_area.grid_columnconfigure(0, weight=1)

        # Клик — открывает всплывающее окно с деталями
        self.tree.bind("<Double-1>", self._show_detail_popup)

        if self.role == "Администратор":
            self.tree.bind("<Double-1>", self._show_detail_popup)

    def _reload(self):
        if hasattr(self, 'entry_search'):
            self.search_text = self.entry_search.get().strip()
        self._load_products()

    def _load_products(self):
        sort_by, sort_order = None, "ASC"
        if hasattr(self, 'sort_combo'):
            sort_map = {
                "Цена ↑": ("price", "ASC"),
                "Цена ↓": ("price", "DESC"),
                "Кол-во ↑": ("quantity", "ASC"),
                "Кол-во ↓": ("quantity", "DESC"),
            }
            val = self.sort_combo.get()
            if val in sort_map:
                sort_by, sort_order = sort_map[val]

        discount_val = None
        if hasattr(self, 'discount_combo'):
            discount_map = {
                "0-12.99%": "0-12.99",
                "13-16.99%": "13-16.99",
                "17% и более": "17+",
            }
            discount_val = discount_map.get(self.discount_combo.get())

        search_text = None
        if hasattr(self, 'entry_search'):
            search_text = self.entry_search.get().strip() or None

        products = self.db.get_products(
            search=search_text,
            sort_by=sort_by,
            sort_order=sort_order,
            discount_range=discount_val,
        )
        self._all_products = products

        for item in self.tree.get_children():
            self.tree.delete(item)

        for p in products:
            is_high = p["discount"] > 25
            is_out = p["quantity"] == 0
            has_discount = p["discount"] > 0

            if has_discount:
                final_price = round(p["price"] * (1 - p["discount"] / 100), 2)
                price_text = f"{p['price']:.2f} → {final_price:.2f}"
            else:
                price_text = f"{p['price']:.2f}"

            # Фото для колонки (первая колонка с image)
            photo_img = self._get_photo(p["photo"], size=(40, 56))

            values = (
                p["article"], p["name"], p["category_name"],
                p["manufacturer_name"], p["supplier_name"],
                price_text, f"{p['discount']:.1f}%", p["quantity"],
            )
            item_id = self.tree.insert("", "end", image=photo_img, values=values)

            tags = []
            if is_out:
                tags.append("out_of_stock")
            if is_high:
                tags.append("high_discount")
            if tags:
                self.tree.item(item_id, tags=tags)

        self.tree.tag_configure("out_of_stock", background=COLOR_OUT_OF_STOCK)
        self.tree.tag_configure("high_discount", background=COLOR_DISCOUNT_HIGH)

    def _on_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        item = self.tree.item(selected[0])
        vals = item["values"]
        if not vals or not vals[0]:  # vals[0] = артикул
            return
        article = vals[0]
        # Ищем товар в _all_products
        p = None
        for prod in self._all_products:
            if prod["article"] == article:
                p = prod
                break
        if p is None:
            return

        # Скрываем плейсхолдер
        self.detail_placeholder.grid_remove()

        # Фото
        photo_img = self._get_photo(p["photo"], size=(120, 168))
        self.detail_photo_label.config(image=photo_img)
        self.detail_photo_label.image = photo_img  # keep ref
        self.detail_photo_label.grid(row=0, column=0, pady=(10, 5))

        # Название
        self.detail_name.config(text=p["name"])
        self.detail_name.grid(row=1, column=0, pady=(0, 5), padx=10)

        has_discount = p["discount"] > 0
        if has_discount:
            final_price = round(p["price"] * (1 - p["discount"] / 100), 2)
            self.detail_old_price.config(text=f"{p['price']:.2f} руб.")
            self.detail_old_price.grid()  # показываем
            self.detail_new_price.config(text=f"{final_price:.2f} руб.")
        else:
            self.detail_old_price.grid_remove()  # скрываем, но ряд остаётся
            self.detail_new_price.config(text=f"{p['price']:.2f} руб.")

        # Инфо
        info = f"Категория: {p['category_name']}\n"
        info += f"Производитель: {p['manufacturer_name']}\n"
        info += f"Поставщик: {p['supplier_name']}\n"
        info += f"На складе: {p['quantity']} шт.\n"
        info += f"Скидка: {p['discount']:.1f}%\n"
        if p["unit"]:
            info += f"Ед. изм.: {p['unit']}\n"
        if p["description"]:
            desc = p["description"]
            if len(desc) > 200:
                desc = desc[:200] + "..."
            info += f"\n{desc}"
        self.detail_info.config(text=info)
        self.detail_info.grid(row=4, column=0, pady=(0, 10), padx=10)

    def _add_product(self):
        if self.on_add_product:
            self.on_add_product()

    def _show_detail_popup(self, event):
        """Всплывающее окно с деталями товара"""
        selected = self.tree.selection()
        if not selected:
            return
        item = self.tree.item(selected[0])
        vals = item["values"]
        if not vals or not vals[0]:
            return
        article = vals[0]
        p = None
        for prod in self._all_products:
            if prod["article"] == article:
                p = prod
                break
        if p is None:
            return

        popup = tk.Toplevel(self.master)
        popup.title(f"Товар — {p['name']}")
        popup.geometry("520x680")
        popup.configure(bg="#FFFFFF")
        popup.resizable(False, False)
        popup.transient(self.master)
        popup.grab_set()

        popup.update_idletasks()
        x = (popup.winfo_screenwidth() // 2) - 260
        y = (popup.winfo_screenheight() // 2) - 340
        popup.geometry(f"+{x}+{y}")

        # Canvas с прокруткой для всего содержимого
        canvas = tk.Canvas(popup, bg="#FFFFFF", highlightthickness=0)
        scrollbar = tk.Scrollbar(popup, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#FFFFFF")

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=500)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Привязка колесика мыши
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind("<MouseWheel>", _on_mousewheel)

        frame = tk.Frame(scroll_frame, bg="#FFFFFF")
        frame.pack(fill="both", expand=True, padx=15, pady=15)

        photo_img = self._get_photo(p["photo"], size=(150, 210))
        photo_label = tk.Label(frame, image=photo_img, bg="#FFFFFF")
        photo_label.image = photo_img
        photo_label.pack(pady=(0, 10))

        tk.Label(frame, text=p["name"], font=(FONT_FAMILY, 14, "bold"),
                 bg="#FFFFFF", fg="#000", wraplength=400).pack(pady=(0, 5))

        has_discount = p["discount"] > 0
        if has_discount:
            final_price = round(p["price"] * (1 - p["discount"] / 100), 2)
            tk.Label(frame, text=f"{p['price']:.2f} руб.",
                     font=(FONT_FAMILY, 12, "overstrike"),
                     bg="#FFFFFF", fg=COLOR_DISCOUNTED_PRICE).pack()
            tk.Label(frame, text=f"{final_price:.2f} руб.",
                     font=(FONT_FAMILY, 18, "bold"),
                     bg="#FFFFFF", fg=COLOR_FINAL_PRICE).pack(pady=(2, 10))
        else:
            tk.Label(frame, text=f"{p['price']:.2f} руб.",
                     font=(FONT_FAMILY, 18, "bold"),
                     bg="#FFFFFF", fg=COLOR_FINAL_PRICE).pack(pady=(2, 10))

        info = f"Категория: {p['category_name']}\n"
        info += f"Производитель: {p['manufacturer_name']}\n"
        info += f"Поставщик: {p['supplier_name']}\n"
        info += f"На складе: {p['quantity']} шт.\n"
        info += f"Скидка: {p['discount']:.1f}%\n"
        if p["unit"]:
            info += f"Ед. изм.: {p['unit']}\n"
        if p["description"]:
            desc = p["description"]
            if len(desc) > 300:
                desc = desc[:300] + "..."
            info += f"\n{desc}"

        tk.Label(frame, text=info, font=(FONT_FAMILY, 10),
                 bg="#FFFFFF", fg="#333", justify="left",
                 wraplength=400).pack(pady=(0, 10))

        btn_frame = tk.Frame(frame, bg="#FFFFFF")
        btn_frame.pack()

        if self.role == "Администратор":
            tk.Button(btn_frame, text="Редактировать", font=(FONT_FAMILY, 10),
                      bg=COLOR_ACCENT, fg="white", relief="flat",
                      command=lambda a=article: [popup.destroy(), self._edit_product_by_article(a)],
                      ).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Закрыть", font=(FONT_FAMILY, 10),
                  bg=COLOR_SECONDARY_BG, fg="black", relief="flat",
                  command=popup.destroy,
                  ).pack(side="left", padx=5)

    def _edit_product_by_article(self, article):
        """Редактировать товар по артикулу"""
        if not self.on_edit_product:
            return
        for prod in self._all_products:
            if prod["article"] == article:
                self.on_edit_product(prod)
                return

    def _edit_product(self, event):
        selected = self.tree.selection()
        if not selected or not self.on_edit_product:
            return
        item = self.tree.item(selected[0])
        vals = item["values"]
        if not vals or not vals[0]:
            return
        article = vals[0]
        p = None
        for prod in self._all_products:
            if prod["article"] == article:
                p = prod
                break
        if p:
            self.on_edit_product(p)

    def _open_orders(self):
        if self.on_open_orders:
            self.on_open_orders()

    def _on_logout(self):
        if messagebox.askyesno("Выход", "Выйти из учетной записи?"):
            if self.on_logout:
                self.on_logout()
