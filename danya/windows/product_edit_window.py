# windows/product_edit_window.py — форма добавления/редактирования товара
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
from config import (
    COLOR_MAIN_BG, COLOR_SECONDARY_BG, COLOR_ACCENT,
    FONT_FAMILY, get_resources_dir,
)
from PIL import Image, ImageTk


class ProductEditFrame(tk.Frame):
    def __init__(self, master, db, product=None, on_save=None, on_cancel=None):
        """
        product=None — режим добавления
        product=dict — режим редактирования
        on_save(article) — колбэк после сохранения
        on_cancel() — колбэк при отмене
        """
        super().__init__(master, bg=COLOR_MAIN_BG)
        self.master = master
        self.db = db
        self.product = product  # None для добавления
        self.on_save = on_save
        self.on_cancel = on_cancel
        self.is_edit = product is not None
        self.selected_photo_path = None  # путь к выбранному фото
        self.photo_data = None  # имя файла для сохранения

        # Находим папку для сохранения фото
        self.photos_dir = get_resources_dir()

        self._build_ui()
        if self.is_edit:
            self._load_product()

    def _build_ui(self):
        # Верхняя панель
        top = tk.Frame(self, bg=COLOR_SECONDARY_BG, height=40)
        top.pack(fill="x")
        top.pack_propagate(False)

        # Логотип
        logo_path = os.path.join(get_resources_dir(), "icon.png")
        if os.path.exists(logo_path):
            try:
                img = Image.open(logo_path)
                img.thumbnail((28, 28), Image.LANCZOS)
                logo_img = ImageTk.PhotoImage(img)
                tk.Label(top, image=logo_img, bg=COLOR_SECONDARY_BG).pack(side="left", padx=(10, 5))
                # храним ссылку
                self._logo_img = logo_img
            except Exception:
                pass

        tk.Label(
            top, text="ЧитайГород", font=(FONT_FAMILY, 16, "bold"),
            bg=COLOR_SECONDARY_BG, fg=COLOR_ACCENT,
        ).pack(side="left")

        title = "Редактирование товара" if self.is_edit else "Добавление товара"
        tk.Label(
            top, text=title, font=(FONT_FAMILY, 12),
            bg=COLOR_SECONDARY_BG, fg="black",
        ).pack(side="left", padx=20)

        # Основной контент
        main = tk.Frame(self, bg=COLOR_MAIN_BG)
        main.pack(fill="both", expand=True, padx=20, pady=10)

        # Левая колонка — фото
        left = tk.Frame(main, bg=COLOR_MAIN_BG, width=320)
        left.pack(side="left", fill="y", padx=(0, 20))
        left.pack_propagate(False)

        tk.Label(left, text="Фото товара:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").pack(anchor="w")

        self.photo_preview = tk.Label(left, bg="#FFFFFF", relief="solid", bd=1)
        self.photo_preview.pack(pady=(5, 10))

        # Показываем заглушку или текущее фото
        self._show_photo_preview(None)

        tk.Button(
            left, text="Загрузить фото", font=(FONT_FAMILY, 10),
            bg=COLOR_ACCENT, fg="white", relief="flat",
            command=self._choose_photo,
        ).pack(fill="x")

        if self.is_edit:
            tk.Label(left, text=f"Артикул: {self.product['article']}",
                     font=(FONT_FAMILY, 10), bg=COLOR_MAIN_BG, fg="#666").pack(pady=(10, 0))

        # Правая колонка — поля
        right = tk.Frame(main, bg=COLOR_MAIN_BG)
        right.pack(side="right", fill="both", expand=True)

        row = 0
        # Артикул (только при добавлении)
        if not self.is_edit:
            tk.Label(right, text="Артикул:", font=(FONT_FAMILY, 11),
                     bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
            self.entry_article = tk.Entry(right, font=(FONT_FAMILY, 11))
            self.entry_article.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
            row += 1

        # Наименование
        tk.Label(right, text="Наименование:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        self.entry_name = tk.Entry(right, font=(FONT_FAMILY, 11))
        self.entry_name.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        row += 1

        # Категория (выпадающий список)
        tk.Label(right, text="Категория:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        categories = self.db.get_categories()
        self.cat_combo = ttk.Combobox(
            right, values=[c["name"] for c in categories],
            state="readonly", font=(FONT_FAMILY, 11), width=30,
        )
        self.cat_combo.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        if categories:
            self.cat_combo.set(categories[0]["name"])
        # Сохраняем id по имени
        self.cat_map = {c["name"]: c["id"] for c in categories}
        row += 1

        # Производитель (выпадающий)
        tk.Label(right, text="Производитель:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        manufacturers = self.db.get_manufacturers()
        self.man_combo = ttk.Combobox(
            right, values=[m["name"] for m in manufacturers],
            state="readonly", font=(FONT_FAMILY, 11), width=30,
        )
        self.man_combo.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        if manufacturers:
            self.man_combo.set(manufacturers[0]["name"])
        self.man_map = {m["name"]: m["id"] for m in manufacturers}
        row += 1

        # Поставщик (выпадающий)
        tk.Label(right, text="Поставщик:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        suppliers = self.db.get_suppliers()
        self.sup_combo = ttk.Combobox(
            right, values=[s["name"] for s in suppliers],
            state="readonly", font=(FONT_FAMILY, 11), width=30,
        )
        self.sup_combo.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        if suppliers:
            self.sup_combo.set(suppliers[0]["name"])
        self.sup_map = {s["name"]: s["id"] for s in suppliers}
        row += 1

        # Цена
        tk.Label(right, text="Цена (руб.):", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        self.entry_price = tk.Entry(right, font=(FONT_FAMILY, 11))
        self.entry_price.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        row += 1

        # Единица измерения
        tk.Label(right, text="Ед. изм.:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        self.entry_unit = tk.Entry(right, font=(FONT_FAMILY, 11))
        self.entry_unit.insert(0, "шт.")
        self.entry_unit.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        row += 1

        # Количество
        tk.Label(right, text="Кол-во на складе:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        self.entry_quantity = tk.Entry(right, font=(FONT_FAMILY, 11))
        self.entry_quantity.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        row += 1

        # Скидка
        tk.Label(right, text="Скидка (%):", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="w", pady=3)
        self.entry_discount = tk.Entry(right, font=(FONT_FAMILY, 11))
        self.entry_discount.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        row += 1

        # Описание
        tk.Label(right, text="Описание:", font=(FONT_FAMILY, 11),
                 bg=COLOR_MAIN_BG, fg="#000").grid(row=row, column=0, sticky="nw", pady=3)
        self.text_description = tk.Text(right, font=(FONT_FAMILY, 11),
                                         height=5, width=40, wrap="word")
        self.text_description.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=3)
        row += 1

        right.grid_columnconfigure(1, weight=1)

        # Кнопки внизу
        btn_frame = tk.Frame(self, bg=COLOR_MAIN_BG)
        btn_frame.pack(fill="x", padx=20, pady=(0, 15))

        tk.Button(
            btn_frame, text="Назад", font=(FONT_FAMILY, 11),
            bg=COLOR_SECONDARY_BG, fg="black", relief="flat",
            command=self._on_cancel,
        ).pack(side="left", padx=(0, 10))

        if self.is_edit:
            tk.Button(
                btn_frame, text="Удалить товар", font=(FONT_FAMILY, 11),
                bg="#CC0000", fg="white", relief="flat",
                command=self._on_delete,
            ).pack(side="left")

        tk.Button(
            btn_frame, text="Сохранить", font=(FONT_FAMILY, 11),
            bg=COLOR_ACCENT, fg="white", relief="flat",
            command=self._on_save,
        ).pack(side="right", padx=(10, 0))

    def _show_photo_preview(self, photo_path):
        """Показать превью фото 300x200"""
        if photo_path and os.path.exists(photo_path):
            try:
                img = Image.open(photo_path)
                img.thumbnail((300, 200), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.photo_preview.config(image=photo)
                self.photo_preview.image = photo
                return
            except Exception:
                pass
        # Заглушка
        img = Image.new("RGB", (300, 200), "#CCCCCC")
        photo = ImageTk.PhotoImage(img)
        self.photo_preview.config(image=photo)
        self.photo_preview.image = photo

    def _choose_photo(self):
        path = filedialog.askopenfilename(
            title="Выберите фото товара",
            filetypes=[("Изображения", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")],
        )
        if path:
            self.selected_photo_path = path
            self._show_photo_preview(path)

    def _load_product(self):
        """Заполнить поля из данных товара (режим редактирования)"""
        p = self.product
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, p["name"] or "")

        if p.get("category_name") and p["category_name"] in self.cat_map:
            self.cat_combo.set(p["category_name"])

        if p.get("manufacturer_name") and p["manufacturer_name"] in self.man_map:
            self.man_combo.set(p["manufacturer_name"])

        if p.get("supplier_name") and p["supplier_name"] in self.sup_map:
            self.sup_combo.set(p["supplier_name"])

        self.entry_price.delete(0, tk.END)
        self.entry_price.insert(0, str(p["price"]))

        self.entry_unit.delete(0, tk.END)
        self.entry_unit.insert(0, p["unit"] or "шт.")

        self.entry_quantity.delete(0, tk.END)
        self.entry_quantity.insert(0, str(p["quantity"]))

        self.entry_discount.delete(0, tk.END)
        self.entry_discount.insert(0, str(p["discount"]))

        self.text_description.delete("1.0", tk.END)
        if p["description"]:
            self.text_description.insert("1.0", p["description"])

        # Фото — ищем в ресурсах
        if p["photo"]:
            photo_path = os.path.join(self.photos_dir, p["photo"])
            if os.path.exists(photo_path):
                self._show_photo_preview(photo_path)
                self.selected_photo_path = photo_path

    def _save_photo(self, article):
        """Сохранить фото, вернуть имя файла"""
        if not self.selected_photo_path:
            return self.product["photo"] if self.is_edit else None

        # Определяем расширение
        ext = os.path.splitext(self.selected_photo_path)[1] or ".jpg"
        # Имя файла = артикул + расширение
        new_name = f"{article}{ext}"
        dest = os.path.join(self.photos_dir, new_name)

        try:
            # Открываем, ресайзим до 300x200 и сохраняем
            img = Image.open(self.selected_photo_path)
            img.thumbnail((300, 200), Image.LANCZOS)
            # Если фото было другое — удаляем старое
            if self.is_edit and self.product.get("photo"):
                old_photo = os.path.join(self.photos_dir, self.product["photo"])
                if os.path.exists(old_photo) and old_photo != dest:
                    os.remove(old_photo)
            img.save(dest)
            return new_name
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить фото:\n{e}")
            return None

    def _validate(self):
        """Проверить поля перед сохранением"""
        errors = []

        if not self.is_edit:
            article = self.entry_article.get().strip()
            if not article:
                errors.append("Артикул не может быть пустым")
            elif self.db.get_product(article):
                errors.append(f"Товар с артикулом '{article}' уже существует")

        name = self.entry_name.get().strip()
        if not name:
            errors.append("Наименование не может быть пустым")

        price_str = self.entry_price.get().strip()
        if not price_str:
            errors.append("Цена не может быть пустой")
        else:
            try:
                price = float(price_str)
                if price < 0:
                    errors.append("Цена не может быть отрицательной")
            except ValueError:
                errors.append("Цена должна быть числом")

        qty_str = self.entry_quantity.get().strip()
        if not qty_str:
            errors.append("Количество не может быть пустым")
        else:
            try:
                qty = int(qty_str)
                if qty < 0:
                    errors.append("Количество не может быть отрицательным")
            except ValueError:
                errors.append("Количество должно быть целым числом")

        disc_str = self.entry_discount.get().strip()
        if disc_str:
            try:
                disc = float(disc_str)
                if disc < 0 or disc > 100:
                    errors.append("Скидка должна быть от 0 до 100")
            except ValueError:
                errors.append("Скидка должна быть числом")

        if errors:
            messagebox.showerror(
                "Ошибка валидации",
                "\n".join(errors),
            )
            return False
        return True

    def _on_save(self):
        if not self._validate():
            return

        article = self.entry_article.get().strip() if not self.is_edit else self.product["article"]

        data = {
            "article": article,
            "name": self.entry_name.get().strip(),
            "unit": self.entry_unit.get().strip() or "шт.",
            "price": float(self.entry_price.get().strip()),
            "supplier_id": self.sup_map.get(self.sup_combo.get(), 1),
            "manufacturer_id": self.man_map.get(self.man_combo.get(), 1),
            "category_id": self.cat_map.get(self.cat_combo.get(), 1),
            "discount": float(self.entry_discount.get().strip() or 0),
            "quantity": int(self.entry_quantity.get().strip() or 0),
            "description": self.text_description.get("1.0", tk.END).strip(),
            "photo": None,
        }

        # Сохраняем фото
        photo_name = self._save_photo(article)
        data["photo"] = photo_name

        try:
            if self.is_edit:
                self.db.update_product(self.product["article"], data)
                msg = "Товар обновлён"
            else:
                self.db.add_product(data)
                msg = "Товар добавлен"

            messagebox.showinfo("Успешно", msg)
            if self.on_save:
                self.on_save(article)
        except Exception as e:
            messagebox.showerror("Ошибка БД", str(e))

    def _on_delete(self):
        if not messagebox.askyesno(
            "Подтверждение",
            f"Удалить товар '{self.product['name']}'?",
        ):
            return

        if self.db.product_in_orders(self.product["article"]):
            messagebox.showerror(
                "Ошибка",
                "Нельзя удалить товар — он присутствует в заказе",
            )
            return

        try:
            self.db.delete_product(self.product["article"])
            messagebox.showinfo("Успешно", "Товар удалён")
            if self.on_save:
                self.on_save(None)  # None — сигнал что товар удалён
        except Exception as e:
            messagebox.showerror("Ошибка БД", str(e))

    def _on_cancel(self):
        if self.on_cancel:
            self.on_cancel()
