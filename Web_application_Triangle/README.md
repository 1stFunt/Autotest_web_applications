## Краткое описание
Дипломный проект “Ручное и автоматизированное тестирование веб-приложения “Triangle”: исследовательский подход.”

[Ссылка на приложение “Triangle”](https://testpages.eviltester.com/styled/apps/triangle/triangle001.html)
## Содержание
- [Презентация (PDF)](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/1_presentation.pdf)
- [Дипломная работа (PDF)](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/2_project.pdf)
- [Чек-лист (PDF)](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/3_check-list.pdf)


## Файлы для автотестирования
Проект создан с использованием паттерна Page Object.

[BaseApp.py](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/BaseApp.py) - файл содержит класс *BasePage*, представляющий базовую
страницу для автотестов веб-приложения “Triangle” с описанием методов, которые
можно будет вызвать через “help(BasePage)”.     
[conftest.py](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/conftest.py) - в файле определена фикстура *browser* для создания экземпляра браузера, который будет использоваться в тестах.     
[testpage.py](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/testpage.py) - содержит классы для удобной работы с локаторами элементов страницы.    
[testdata.yaml](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/testdata.yaml) - файл хранит настройки для удобства автоматизированного тестирования.   
[pytest.ini](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/pytest.ini) - хранит настройки логов и отчёта о тестировании.  
[test_app.py](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/test_app.py) - файл содержит автотесты согласно [чек-листу](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/3_check-list.pdf) с использованием среды тестирования *Pytest*.   
[log.txt](https://github.com/1stFunt/Autotest_web_applications/blob/main/Web_application_Triangle/log.txt) - хранение логов.