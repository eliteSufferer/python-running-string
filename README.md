## Инструкция по запуску:

1. Если работаете под Windows, необходимо перед клонированием прописать команду `git config --global core.autocrlf input`
1. Клонируете репозиторий через `git clone`
2. Если работаете на Windows, то открываете клиент Docker, на Linux не нужно
3. В корне проекта открываете терминал и пишете
`docker-compose up --build` (добавив sudo перед командой, если открываете с Linux)
4. Приложение запустится на порту 8000, доступно при открытии в браузере по ссылке http://localhost:8000/
