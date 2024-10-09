from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv(find_dotenv())

client = OpenAI()

def generate_milestones(task_description):
    prompt = f"""
        Раздели следующую задачу на более мелкие этапы (milestones):
        \n\n
        {task_description}
        \n\nЭтапы (milestones):
            Будь уверен, что ответ будет в таком вот формате:
                Отлично, давайте разделим вашу задачу на этапы для более эффективного обучения Python для бэкенд-разработки:

                ### Этап 1: Начало
                1. **Месяц 1-3** 
                   - Установка Python и настройка окружения (IDE/редактор кода).
                   - Изучение базовых конструкций (переменные, типы данных, операторы).
                  
                2. **Месяц 3-4**  
                   - Условные операторы: if, else, elif.
                   - Циклы: for, while.
                
                3. **Месяц 4-5** 
                   - Определение и использование функций.
                   - Импортирование библиотек и модулей.
                
                ### Этап 2: Применение Python
                4. **Месяц 5-6**
                   - Изучение списков, кортежей, множеств и словарей.
                   - Основы обработки строк и работы с файлами.
                
                5. **Месяц 6-7**
                   - Понимание классов и объектов.
                   - Наследование и инкапсуляция.
                
                ### Этап 3: Основы веб-разработки
                6. **Месяц 7-8**
                   - Понять, как работают HTTP-запросы и ответы.
                   - Изучение принципов RESTful API.
                
                7. **Месяц 8-9**
                   - Выбор фреймворка (Django или Flask).
                   - Изучение основ выбранного фреймворка.
                
                ### Этап 4: Практика разработки
                8. **Месяц 9-10**
                   - Разработка простого REST API (например, ToDo приложение).
                   - Взаимодействие с базой данных (выбор SQL или NoSQL).
                
                9. **Месяц 10-11**
                   - Основы написания тестов.
                   - Знакомство с библиотеками для тестирования (например, unittest или pytest).
                
                ### Этап 5: Продвинутые темы
                10. **Месяц 11-12**
                    - Изучение SQL и работы с реляционными базами данных (например, PostgreSQL).
                    - Использование ORM (например, SQLAlchemy или Django ORM).
                
                11. **Месяц 12-13**
                    - Изучение методов аутентификации (JWT, OAuth).
                
                12. **Месяц 13-14**
                    - Знакомство с инструментами деплоя (Heroku, Docker).
                    - Развертывание собственного приложения.
                
                ### Этап 6: Поддержка и развитие
                13. **Месяц 14-15**
                    - Участие в open source проектах на GitHub.
                
                14. **Месяц 15-16**
                    - Чтение книг, прохождение курсов, участие в сообществах.
                
                Следуя этим этапам, вы сможете структурированно и эффективно изучать Python для бэкенд-разработки. Удачи на вашем пути!
    """

    try:
        completion = client.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=[
                {
                    "role": "system",
                    "content": "Ты эффективный, целеустремленный и успешный человек. Ты помог миллионам людей стать более продуктивными и добиться своих целей в жизни. Ориентируйся на конкретные задачи пользователя, предоставляя структурированные и полезные ответы. Отвечай кратко, но с детальной проработкой, чтобы улучшить понимание и результативность. Старайся поддерживать позитивный тон, способствующий мотивации и достижению целей."
                },
                {
                    "role": "user",
                    "content": f"{prompt}"
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

def streamlit_app():
   st.title("AI Task Breakdown Generator")
   task_description = st.text_area("Введи свою цель или задание, которое ты хочешь разделить на этапы: ")
   if st.button("Генерировать этапы"):
        if task_description:
            with st.spinner("Генерация этапов..."):
                milestones = generate_milestones(task_description)
            st.markdown("### Этапы:")
            st.write(milestones)
        else:
            st.error("Пожалуйста, введи свою цель в текстовом поле выше.")


def console_app():
    print("AI Task Breakdown Generator\n")
    task_description = input("Введи свою цель или задание, которое ты хочешь разделить на этапы: ")

    if task_description:
        print("\nGenerating milestones...")
        milestones = generate_milestones(task_description)
        if milestones:
            print("\nЭтапы (milestones):")
            print(milestones)
        else:
            print("\nAn error occurred. Please try again.")
    else:
        print("No task description provided.")

def main():
    # console_app()
    streamlit_app()


if __name__ == "__main__":
    main()
