## Краткое описание
Дипломный проект “Ручное и автоматизированное тестирование веб-приложения “Triangle”: исследовательский подход.”

[Ссылка на приложение “Triangle”](https://testpages.eviltester.com/styled/apps/triangle/triangle001.html)
## Содержание
- [Презентация (PDF)](https://github.com/1stFunt/Autotest_web_applications/blob/dc37103bbdbe17139d23e3a0ba659de8900acf5e/Web_application_Triangle/1_presentation.pdf)
- [Дипломный проект (PDF)](https://github.com/1stFunt/Autotest_web_applications/blob/cccf3a873b255ec4bbfea80833e43353a13b828e/Web_application_Triangle/2_project.pdf)
- [Чек-лист (PDF)](https://github.com/1stFunt/Autotest_web_applications/blob/0284cd5eb494c666aa6c9dedeaf9cb19ebfab6e7/Web_application_Triangle/3_check-list.pdf)


## Файлы для автотестирования
Проект создан с использованием паттерна Page Object.

[BaseApp.py](https://github.com/1stFunt/Autotest_web_applications/blob/0284cd5eb494c666aa6c9dedeaf9cb19ebfab6e7/Web_application_Triangle/BaseApp.py) - файл содержит класс *BasePage*, представляющий базовую
страницу для автотестов веб-приложения “Triangle” с описанием методов, которые
можно будет вызвать через “help(BasePage)”.     
[conftest.py](https://github.com/1stFunt/Autotest_web_applications/blob/0284cd5eb494c666aa6c9dedeaf9cb19ebfab6e7/Web_application_Triangle/conftest.py) - в файле определена фикстура *browser* для создания экземпляра браузера, который будет использоваться в тестах.     
[testpage.py](https://github.com/1stFunt/Autotest_web_applications/blob/0284cd5eb494c666aa6c9dedeaf9cb19ebfab6e7/Web_application_Triangle/testpage.py) - содержит классы для удобной работы с локаторами элементов страницы.