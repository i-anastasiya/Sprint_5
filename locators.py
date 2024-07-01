from selenium.webdriver.common.by import By


class Locators:
    # поле ввода email на экране авторизации
    EMAIL = (By.XPATH, './/form/fieldset[1]/div/div/input')

    # поле ввода email на экране регистрации
    EMAIL_REGISTRATION = (By.XPATH, './/form/fieldset[2]/div/div/input')

    # поле ввода пароля на экране авторизации
    PASSWORD = (By.XPATH, './/form/fieldset[2]/div/div/input')

    # поле ввода пароля на экране регистрации
    PASSWORD_REGISTRATION = (By.XPATH, './/form/fieldset[3]/div/div/input')

    # поле ввода имени на экране регистрации
    NAME_REGISTRATION = (By.XPATH, './/form/fieldset[1]/div/div/input')

    # кнопка Личный Кабинет на главной
    PERSONAL_AREA_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    # кнопка Зарегистрироваться на экране авторизации
    AUTH_BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    # кнопка Войти в аккаунт на экране авторизации
    AUTH_BUTTON_ACCOUNT = (By.XPATH, ".//button[text()='Войти']")

    # кнопка Войти в аккаунт на главной
    AUTH_BUTTON_ACCOUNT_1 = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    # кнопка Оформить заказ на главной
    COME_IN_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    # Ошибка Некорректный пароль на экране авторизации
    INCORRECT_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")

    # Кнопка восстановить пароль на экране авторизации
    BUTTON_RECOVERY = (By.XPATH, ".//a[text()='Восстановить пароль']")

    # Кнопка Войти на экране Восстановления пароля и на экране регистрации
    BUTTON_LOGIN = (By.XPATH, ".//a[text()='Войти']")

    # Кнопка Выход в личном кабинете
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")

    # Кнопка Конструктор
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")

    # Текст Соберите бургер на главной
    TEXT_HOME = (By.XPATH, ".//h1[text()='Соберите бургер']")

    # Логотип сайта
    LOGO = (By.CSS_SELECTOR, 'div.AppHeader_header__logo__2D0X2')

    # Тег Булки на главной
    TAG_1 = (By.XPATH, ".//span[text()='Булки']")

    # Тег Соусы на главной
    TAG_2 = (By.XPATH, ".//span[text()='Соусы']")

    # Тег Начинки на главной
    TAG_3 = (By.XPATH, ".//span[text()='Начинки']")

    # Заголовок Булки на главной
    TITLE_1 = (By.XPATH, ".//h2[text()='Булки']")

    # Заголовок Соусы на главной
    TITLE_2 = (By.XPATH, ".//h2[text()='Соусы']")

    # Заголовок Начинки  на главной
    TITLE_3 = (By.XPATH, ".//h2[text()='Начинки']")

    # Кнопка Зарегистрироваться на экране авторизации
    REGISTRATION_BUTTON = (By.XPATH, ".//a[text()='Зарегистрироваться']")
