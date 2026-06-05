# windows/auth_window.py — фрейм авторизации
import os
import tkinter as tk
from tkinter import messagebox
from config import (
    COLOR_MAIN_BG, COLOR_SECONDARY_BG, COLOR_ACCENT,
    FONT_FAMILY, get_resources_dir,
)
from PIL import Image, ImageTk


class AuthFrame(tk.Frame):
    def __init__(self, master, on_login_success, on_guest):
        super().__init__(master, bg=COLOR_MAIN_BG)
        self.master = master
        self.on_login_success = on_login_success
        self.on_guest = on_guest

        # Загружаем логотип
        logo_path = os.path.join(get_resources_dir(), "icon.png")
        self.logo_img = None
        if os.path.exists(logo_path):
            try:
                img = Image.open(logo_path)
                img.thumbnail((100, 100), Image.LANCZOS)
                self.logo_img = ImageTk.PhotoImage(img)
            except Exception:
                pass

        self._build_ui()
        self._center(500, 400)

    def _center(self, w, h):
        self.master.update_idletasks()
        x = (self.master.winfo_screenwidth() // 2) - (w // 2)
        y = (self.master.winfo_screenheight() // 2) - (h // 2)
        self.master.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self):
        frame = tk.Frame(self, bg=COLOR_MAIN_BG)
        frame.place(relx=0.5, rely=0.5, anchor="center", width=320)

        # Логотип
        if self.logo_img:
            tk.Label(frame, image=self.logo_img, bg=COLOR_MAIN_BG).pack(pady=(0, 10))

        # Название текстом (на случай если лого не загрузится)
        tk.Label(
            frame, text="ЧитайГород", font=(FONT_FAMILY, 22, "bold"),
            bg=COLOR_MAIN_BG, fg=COLOR_ACCENT,
        ).pack(pady=(0, 5))

        tk.Label(
            frame, text="Книжный магазин", font=(FONT_FAMILY, 12),
            bg=COLOR_MAIN_BG, fg=COLOR_ACCENT,
        ).pack(pady=(0, 20))

        # Логин
        tk.Label(frame, text="Логин:", font=(FONT_FAMILY, 11), bg=COLOR_MAIN_BG).pack(anchor="w")
        self.entry_login = tk.Entry(frame, font=(FONT_FAMILY, 11))
        self.entry_login.pack(fill="x", pady=(0, 10))
        self.entry_login.focus()

        # Пароль
        tk.Label(frame, text="Пароль:", font=(FONT_FAMILY, 11), bg=COLOR_MAIN_BG).pack(anchor="w")
        self.entry_pass = tk.Entry(frame, font=(FONT_FAMILY, 11), show="*")
        self.entry_pass.pack(fill="x", pady=(0, 15))

        tk.Button(
            frame, text="Войти", font=(FONT_FAMILY, 11),
            bg=COLOR_ACCENT, fg="white", relief="flat",
            command=self._try_login,
        ).pack(fill="x", pady=(0, 10))

        tk.Button(
            frame, text="Войти как гость", font=(FONT_FAMILY, 11),
            bg=COLOR_SECONDARY_BG, fg="black", relief="flat",
            command=self._guest_login,
        ).pack(fill="x")

        self.master.bind("<Return>", lambda e: self._try_login())

    def _try_login(self):
        login = self.entry_login.get().strip()
        password = self.entry_pass.get().strip()
        if not login or not password:
            messagebox.showwarning("Ошибка", "Введите логин и пароль")
            return

        db = self.master.app.db if hasattr(self.master, 'app') else None
        if db is None:
            messagebox.showerror("Ошибка", "Нет подключения к БД")
            return

        user = db.auth_user(login, password)
        if user:
            self.on_login_success(user)
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")

    def _guest_login(self):
        self.on_guest()
