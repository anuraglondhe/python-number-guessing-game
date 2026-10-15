
import tkinter as tk
import random

# ---------- Colors ----------
BG = "#0B1420"
PANEL = "#101F31"
CARD = "#172B44"
BORDER = "#203D5F"
WHITE = "#F4F7FB"
MUTED = "#86A6CC"
BLUE = "#50A8FF"
GREEN = "#08C994"
YELLOW = "#FFC247"
RED = "#FF7373"


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("900x650")
        self.root.minsize(650, 600)
        self.root.configure(bg=BG)

        self.best_score = None
        self.new_game()
        self.create_ui()

        self.root.bind("<Return>", lambda event: self.check_guess())

    def new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.game_over = False

        if hasattr(self, "attempts_label"):
            self.attempts_label.config(text="Attempts: 0")
            self.best_label.config(
                text=f"Best Score: {self.best_score if self.best_score is not None else '-'}"
            )
            self.message_label.config(
                text="💡  Enter a number to start!",
                fg=MUTED
            )
            self.status_label.config(
                text="I'm thinking of a number between 1 and 100.",
                fg=WHITE
            )
            self.guess_entry.config(state="normal")
            self.guess_entry.delete(0, tk.END)
            self.guess_entry.focus_set()
            self.guess_button.config(state="normal", bg=GREEN)

    def create_ui(self):
        # ---------- Header ----------
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=25, pady=(22, 18))

        tk.Label(
            header,
            text="🎮  NUMBER GUESSING GAME",
            font=("Segoe UI", 23, "bold"),
            bg=BG,
            fg=WHITE
        ).pack()

        tk.Label(
            header,
            text="A little logic. A little luck. Can you win?",
            font=("Segoe UI", 11),
            bg=BG,
            fg=MUTED
        ).pack(pady=(6, 0))

        # ---------- Main content ----------
        content = tk.Frame(self.root, bg=BG)
        content.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        game_panel = tk.Frame(
            content, bg=PANEL,
            highlightbackground=BORDER, highlightthickness=1
        )
        game_panel.pack(side="left", fill="both", expand=True, padx=(0, 12))

        side_panel = tk.Frame(
            content, bg=PANEL, width=230,
            highlightbackground=BORDER, highlightthickness=1
        )
        side_panel.pack(side="right", fill="y")
        side_panel.pack_propagate(False)

        # ---------- Game panel ----------
        tk.Label(
            game_panel,
            text="YOUR CHALLENGE",
            font=("Segoe UI", 10, "bold"),
            bg=PANEL, fg=BLUE
        ).pack(pady=(28, 12))

        self.status_label = tk.Label(
            game_panel,
            text="I'm thinking of a number between 1 and 100.",
            font=("Segoe UI", 14, "bold"),
            bg=CARD, fg=WHITE,
            wraplength=450, justify="center",
            padx=20, pady=25
        )
        self.status_label.pack(fill="x", padx=22)

        tk.Label(
            game_panel,
            text="YOUR GUESS",
            font=("Segoe UI", 10, "bold"),
            bg=PANEL, fg=MUTED
        ).pack(anchor="w", padx=25, pady=(24, 8))

        input_row = tk.Frame(game_panel, bg=PANEL)
        input_row.pack(fill="x", padx=22)

        self.guess_entry = tk.Entry(
            input_row,
            font=("Segoe UI", 16),
            bg=BG, fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER,
            highlightcolor=BLUE
        )
        self.guess_entry.pack(
            side="left", fill="x", expand=True,
            ipady=12, padx=(0, 10)
        )
        self.guess_entry.insert(0, "")

        self.guess_button = tk.Button(
            input_row,
            text="GUESS  ➜",
            command=self.check_guess,
            font=("Segoe UI", 11, "bold"),
            bg=GREEN, fg=BG,
            activebackground="#06B583",
            activeforeground=BG,
            relief="flat", cursor="hand2",
            padx=16, pady=12
        )
        self.guess_button.pack(side="right")

        # ---------- Statistics ----------
        stats = tk.Frame(game_panel, bg=PANEL)
        stats.pack(fill="x", padx=22, pady=22)

        self.attempts_label = tk.Label(
            stats, text="Attempts: 0",
            font=("Segoe UI", 12, "bold"),
            bg=PANEL, fg=BLUE
        )
        self.attempts_label.pack(side="left")

        self.best_label = tk.Label(
            stats, text="Best Score: -",
            font=("Segoe UI", 12, "bold"),
            bg=PANEL, fg=YELLOW
        )
        self.best_label.pack(side="right")

        self.message_label = tk.Label(
            game_panel,
            text="💡  Enter a number to start!",
            font=("Segoe UI", 11),
            bg=CARD, fg=MUTED,
            anchor="w", padx=15, pady=16,
            wraplength=480
        )
        self.message_label.pack(fill="x", padx=22, pady=(0, 20))

        tk.Button(
            game_panel,
            text="↻   NEW GAME",
            command=self.new_game,
            font=("Segoe UI", 11, "bold"),
            bg=CARD, fg=WHITE,
            activebackground=BORDER,
            activeforeground=WHITE,
            relief="flat", cursor="hand2",
            padx=24, pady=12
        ).pack(pady=(0, 22))

        # ---------- Information panel ----------
        tk.Label(
            side_panel, text="📊  GAME INFO",
            font=("Segoe UI", 13, "bold"),
            bg=PANEL, fg=WHITE
        ).pack(anchor="w", padx=18, pady=(25, 18))

        self.info_item(side_panel, "🎯", "NUMBER RANGE", "1 - 100")
        self.info_item(side_panel, "🔄", "ATTEMPTS", "Try your luck!")
        self.info_item(side_panel, "🏆", "BEST SCORE", "Fewer attempts win")

        tk.Frame(
            side_panel, bg=BORDER, height=1
        ).pack(fill="x", padx=18, pady=18)

        tk.Label(
            side_panel, text="✨  HOW TO PLAY",
            font=("Segoe UI", 12, "bold"),
            bg=PANEL, fg=WHITE
        ).pack(anchor="w", padx=18, pady=(0, 12))

        tips = [
            "• Guess a number from 1 to 100.",
            "• Too low? Try higher.",
            "• Too high? Try lower.",
            "• Find it in fewer attempts!"
        ]

        for tip in tips:
            tk.Label(
                side_panel, text=tip,
                font=("Segoe UI", 10),
                bg=PANEL, fg=MUTED,
                wraplength=190, justify="left",
                anchor="w"
            ).pack(fill="x", padx=18, pady=6)

    def info_item(self, parent, icon, title, value):
        item = tk.Frame(parent, bg=PANEL)
        item.pack(fill="x", padx=18, pady=8)

        tk.Label(
            item, text=icon, font=("Segoe UI Emoji", 17),
            bg=PANEL, fg=WHITE
        ).pack(side="left", padx=(0, 10))

        details = tk.Frame(item, bg=PANEL)
        details.pack(side="left", fill="x", expand=True)

        tk.Label(
            details, text=title,
            font=("Segoe UI", 9, "bold"),
            bg=PANEL, fg=MUTED
        ).pack(anchor="w")

        tk.Label(
            details, text=value,
            font=("Segoe UI", 11, "bold"),
            bg=PANEL, fg=WHITE,
            wraplength=150, justify="left"
        ).pack(anchor="w", pady=(3, 0))

    def check_guess(self):
        if self.game_over:
            return

        text = self.guess_entry.get().strip()

        try:
            guess = int(text)
        except ValueError:
            self.message_label.config(
                text="⚠️  Please enter a valid whole number.",
                fg=RED
            )
            return

        if not 1 <= guess <= 100:
            self.message_label.config(
                text="⚠️  Your number must be between 1 and 100.",
                fg=RED
            )
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.secret_number:
            self.status_label.config(
                text="📈  Too low! Try a HIGHER number.",
                fg=YELLOW
            )
            self.message_label.config(
                text="💡  Think bigger. You've got this!",
                fg=MUTED
            )

        elif guess > self.secret_number:
            self.status_label.config(
                text="📉  Too high! Try a LOWER number.",
                fg=YELLOW
            )
            self.message_label.config(
                text="💡  Go a little lower this time.",
                fg=MUTED
            )

        else:
            score = max(0, 100 - (self.attempts - 1) * 10)

            if self.best_score is None or score > self.best_score:
                self.best_score = score

            self.game_over = True

            self.status_label.config(
                text=f"🎉  YOU WON!\nThe number was {self.secret_number}.",
                fg=GREEN
            )
            self.message_label.config(
                text=f"🏆  Score: {score}  |  Attempts: {self.attempts}",
                fg=GREEN
            )
            self.best_label.config(text=f"Best Score: {self.best_score}")
            self.guess_entry.config(state="disabled")
            self.guess_button.config(state="disabled", bg=BORDER)
            return

        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
