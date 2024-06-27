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
    PERSONAL_AREA_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')

    # кнопка Войти/Зарегистрироваться/Восстановить/Сохранить в аккаунт на экране авторизации
    AUTH_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

    # кнопка Войти/Оформить заказ на главной
    COME_IN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')

    # Ошибка Некорректный пароль на экране авторизации
    INCORRECT_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')

    # Кнопка восстановить пароль на экране авторизации
    BUTTON_RECOVERY = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')

    # Кнопка Войти на экране Восстановления пароля и на экране регистрации
    BUTTON_LOGIN = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')

    # Кнопка Выход в личном кабинете
    BUTTON_EXIT = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')

    # Кнопка Конструктор
    BUTTON_CONSTRUCTOR = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a')

    # Текст Соберите бургер на главной
    TEXT_HOME = (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')

    # Логотип сайта
    LOGO = (By.XPATH, '//*[@id="root"]/div/header/nav/div')

    # Тег Булки на главной
    TAG_1 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')

    # Тег Соусы на главной
    TAG_2 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')

    # Тег Начинки на главной
    TAG_3 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')

    # Заголовок Булки на главной
    TITLE_1 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')

    # Заголовок Соусы на главной
    TITLE_2 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]')

    # Заголовок Начинки  на главной
    TITLE_3 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]')

    # Кнопка Зарегистрироваться на экране авторизации
    REGISTRATION_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')
