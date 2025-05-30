# 👕 WeatherStyleAI

**WeatherStyleAI** — это веб-приложение, которое сочетает прогноз погоды с искусственным интеллектом, чтобы дать вам персональные советы:  
**что надеть в ближайшие 5 часов**, основываясь на текущей и ожидаемой погоде.

---

## 🌟 Возможности

- 🌤️ Прогноз погоды на 5 часов вперёд (через **Yandex Weather API**)
- 🧠 Советы по одежде, сгенерированные **OpenAI GPT**
- ⚡ Быстрая серверная логика на **FastAPI**
- 💻 Простая и адаптивная фронтенд-страница на **HTML / CSS / JavaScript**

---

## 🔧 Технологии

| Технология           | Назначение                            |
|----------------------|----------------------------------------|
| `Python`             | Основной язык бэкенда                 |
| `FastAPI`            | Создание и запуск API сервиса         |
| `HTML / CSS / JS`    | Фронтенд интерфейс пользователя       |
| `Yandex Weather API` | Получение погодных данных             |
| `OpenAI API`         | Генерация советов по стилю одежды     |

---

💡 Как это работает?

Приложение делает запрос к Yandex Weather API для получения прогноза на ближайшие 5 часов.

Эти данные передаются в OpenAI, где модель генерирует рекомендации по одежде.

Результат отображается на странице: погода и совет по стилю!



