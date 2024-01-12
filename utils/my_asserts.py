import allure


def check_current_url(current_url: str, exp_url: str):
    with allure.step(f'Проверка текущего урла {current_url} c ожидаемым: {exp_url}'):
        assert current_url == exp_url, f'Урл {current_url} не совпадает с {exp_url}'
