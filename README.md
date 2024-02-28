<div align="center">
<h1>
  SpamDestroyerBot
</h1>
</div>

### Задача проекта:
<div>
  Создать телеграм бота, способного детектировать спам в англоязычном тексте и отправлять соответствующее сообщение.
</div>

---

### Технологии:
<div>
  Python(pandas, seaborn, matplotlib, numpy, scikit-learn, pytorch, fasttext, sqlalchemy, aiogram), SQL(postgresql)
</div>

---
### Ссылка на данные для обучения: 
<div>
  <a href="https://www.kaggle.com/datasets/venky73/spam-mails-dataset" target="_blank">
    <img src=https://img.shields.io/badge/kaggle-%2344BAE8.svg?&style=for-the-badge&logo=kaggle&logoColor=white alt=kaggle style="margin-bottom: 5px;" />
  </a> 
</div>

---
### Метрика: 
<div>
  Accuracy@5=0.9915
</div>

---

### Проведенная работа:
<div>
  Текст из данных прошел различные преобразования, был проведен анализ частотности слов в негативных и положительных категориях таргета. Была выбрана архитектура построения модели на основе TextCNN. Была создана база данных с таблицей для данных с текстами. С помощью библиотеки aiogram был разработан телеграм бот.
</div>

---
### Инструкции по развертыванию:
<div>
  
  -  Загрузка данных для обучения с платформы Kaggle(ссылка выше).
  
  -  Работа над данными описанная в .ipynb файле.
  
  -  Создание базы данных и подключение ее в проекту по специальному пути.

  -  Создание специального токена для бота.
  
  -  Запуск проекта.
</div>
