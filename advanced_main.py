import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QCheckBox, \
    QHBoxLayout, QGroupBox, QSlider
from PyQt5.QtGui import QIcon, QPixmap, QClipboard, QColor
from PyQt5.QtCore import Qt

import random
import string


class MainInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SecurePass Generator")
        self.setGeometry(200, 200, 400, 400)
        self.setWindowIcon(QIcon('padlock_icon.png'))
        self.setStyleSheet("background-color: #F5F5F5;")

        self.initUI()

    def initUI(self):
        """Initialize the main user interface."""
        # Color Palette
        primary_color = "#003366"  # Deep shade of royal blue
        secondary_color = "#00CC66"  # Contrasting lime green

        # Header Section
        header_label = QLabel("SecurePass Generator")
        header_label.setAlignment(Qt.AlignCenter)
        header_font = header_label.font()
        header_font.setPointSize(20)
        header_label.setFont(header_font)
        header_label.setStyleSheet(f"color: {primary_color};")

        padlock_label = QLabel()
        padlock_label.setPixmap(QPixmap('padlock_icon.png'))
        padlock_label.setAlignment(Qt.AlignCenter)

        # Main Content Area
        main_layout = QVBoxLayout()

        # Settings Section
        settings_groupbox = QGroupBox("Settings")
        settings_layout = QVBoxLayout()

        # Password Length Slider
        self.length_label = QLabel("Password Length:")
        self.length_slider = QSlider(Qt.Horizontal)
        self.length_slider.setMinimum(8)
        self.length_slider.setMaximum(20)
        self.length_slider.setValue(12)
        self.length_slider.setTickInterval(1)
        self.length_slider.setTickPosition(QSlider.TicksBelow)
        self.length_slider.setStyleSheet(f"QSlider::handle:horizontal {{ background-color: {secondary_color}; }}")
        self.length_slider.valueChanged.connect(self.update_length_label)

        self.length_edit = QLineEdit(str(self.length_slider.value()))
        self.length_edit.setFixedWidth(30)
        self.length_edit.setReadOnly(True)

        # Character options
        self.letters_check = QCheckBox("Include Letters")
        self.numbers_check = QCheckBox("Include Numbers")
        self.symbols_check = QCheckBox("Include Symbols")

        # Generate Button
        generate_button = QPushButton("Generate Password")
        generate_button.clicked.connect(self.generate_password)
        generate_button.setStyleSheet(f"background-color: {secondary_color}; color: white;")

        settings_layout.addWidget(self.length_label)
        settings_layout.addWidget(self.length_slider)
        settings_layout.addWidget(self.length_edit)
        settings_layout.addWidget(self.letters_check)
        settings_layout.addWidget(self.numbers_check)
        settings_layout.addWidget(self.symbols_check)
        settings_layout.addWidget(generate_button)

        settings_groupbox.setLayout(settings_layout)

        # Generated Password Section
        generated_groupbox = QGroupBox("Generated Password")
        generated_layout = QVBoxLayout()

        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.copy_to_clipboard)
        copy_button.setStyleSheet(f"background-color: {secondary_color}; color: white;")

        self.strength_label = QLabel("Strength: ")
        self.strength_label.setAlignment(Qt.AlignCenter)

        generated_layout.addWidget(self.password_display)
        generated_layout.addWidget(copy_button)
        generated_layout.addWidget(self.strength_label)

        generated_groupbox.setLayout(generated_layout)

        # Footer Section
        footer_label = QLabel("Create strong, secure passwords effortlessly!")
        footer_label.setAlignment(Qt.AlignCenter)

        privacy_policy_label = QLabel('<a href="privacy_policy.txt">Privacy Policy</a>')
        privacy_policy_label.setAlignment(Qt.AlignCenter)
        privacy_policy_label.setOpenExternalLinks(True)

        main_layout.addWidget(header_label)
        main_layout.addWidget(padlock_label)
        main_layout.addWidget(settings_groupbox)
        main_layout.addWidget(generated_groupbox)
        main_layout.addWidget(footer_label)
        main_layout.addWidget(privacy_policy_label)

        self.setLayout(main_layout)

    def update_length_label(self, value):
        """Update the displayed password length based on the slider value."""
        self.length_edit.setText(str(value))

    def generate_password(self):
        """Generate a password based on user settings."""
        try:
            length = int(self.length_edit.text())
            if length <= 0:
                raise ValueError("Length must be a positive integer")

            use_letters = self.letters_check.isChecked()
            use_numbers = self.numbers_check.isChecked()
            use_symbols = self.symbols_check.isChecked()

            characters = ''
            if use_letters:
                characters += string.ascii_letters
            if use_numbers:
                characters += string.digits
            if use_symbols:
                characters += string.punctuation

            if not characters:
                raise ValueError("Select at least one character type")

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_display.setText(password)

            # Calculate strength
            strength = self.calculate_strength(password)
            self.strength_label.setText(f"Strength: {strength}")

        except ValueError as ve:
            QMessageBox.warning(self, "Error", str(ve))

    def calculate_strength(self, password):
        """Calculate the strength of the generated password."""
        # Dummy implementation, replace with your own logic
        length = len(password)
        if length < 10:
            return "Weak"
        elif length < 15:
            return "Medium"
        else:
            return "Strong"

    def copy_to_clipboard(self):
        """Copy the generated password to the clipboard."""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_display.text())


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(300, 300, 300, 200)
        self.setWindowIcon(QIcon('login_icon.png'))  # Replace 'login_icon.png' with your icon file
        self.setStyleSheet("background-color: #F5F5F5;")

        self.initUI()

    def initUI(self):
        """Initialize the login window."""
        # Username
        self.username_label = QLabel("Username:")
        self.username_edit = QLineEdit()

        # Password
        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.login_button.setStyleSheet(f"background-color: #003366; color: white;")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        """Authenticate the user."""
        username = self.username_edit.text()
        password = self.password_edit.text()
        # Dummy authentication logic (replace with your actual authentication code)
        if username == "admin" and password == "password":
            print("Login successful!")
            # Close the login window
            self.close()
            # Open the main interface window
            self.main_interface = MainInterface()
            self.main_interface.show()
        else:
            # Display an error message
            QMessageBox.warning(self, "Login Error", "Invalid username or password. Please try again.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
