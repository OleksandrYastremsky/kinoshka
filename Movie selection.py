import pandas as pd
from prettytable import PrettyTable

class БібліотекаФільмів:
    def __init__(self, шлях_до_файлу):
        self.df = pd.read_csv(шлях_до_файлу)
        
    def показати_фільми(self, фільтр_жанр=None, фільтр_рік=None, сортувати_за='популярність', зростання=False):
        df_фільтрований = self.df
        
        if фільтр_жанр:
            df_фільтрований = df_фільтрований[df_фільтрований['жанр'].str.contains(фільтр_жанр, case=False)]
        
        if фільтр_рік:
            df_фільтрований = df_фільтрований[df_фільтрований['рік'] == фільтр_рік]
        
        df_фільтрований = df_фільтрований.sort_values(by=сортувати_за, ascending=зростання)
        
        таблиця = PrettyTable()
        таблиця.field_names = ["Назва", "Рік", "Жанр", "Популярність"]
        
        for index, row in df_фільтрований.iterrows():
            таблиця.add_row([row['назва'], row['рік'], row['жанр'], row['популярність']])
        
        print(таблиця)

    def додати_фільм(self, назва, рік, жанр, популярність):
        новий_фільм = pd.DataFrame([[назва, рік, жанр, популярність]], columns=['назва', 'рік', 'жанр', 'популярність'])
        self.df = pd.concat([self.df, новий_фільм], ignore_index=True)
        self.df.to_csv('фільми.csv', index=False)

    def видалити_фільм(self, назва):
        self.df = self.df[self.df['назва'] != назва]
        self.df.to_csv('фільми.csv', index=False)

    def отримати_фільм(self, назва):
        фільм = self.df[self.df['назва'] == назва]
        if not фільм.empty:
            return фільм.iloc[0].to_dict()
        else:
            return None

# Використання бібліотеки
бібліотека = БібліотекаФільмів('фільми.csv')

print("Всі фільми:")
бібліотека.показати_фільми()

print("\nФільми жанру 'Бойовик':")
бібліотека.показати_фільми(фільтр_жанр='Бойовик')

print("\nДодавання нового фільму:")
бібліотека.додати_фільм('Фільм Е', 2017, 'Жахи', 90)
бібліотека.показати_фільми()

print("\nВидалення фільму 'Фільм Б':")
бібліотека.видалити_фільм('Фільм Б')
бібліотека.показати_фільми()

print("\nОтримання інформації про фільм 'Фільм В':")
інформація_про_фільм = бібліотека.отримати_фільм('Фільм В')
print(інформація_про_фільм)

