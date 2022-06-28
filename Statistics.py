# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:39:45 2021

@author: PC
"""

import ReadTermFromTermsModule
import SearchForTermInStatModule
# import CalcStatModule
import AddRecordToTermStatModule
# indTerm - Индекс по основной таблице Term, полный обход, 1 раз
# indRest - Индекс по таблице TermStat 
# FirstTerm - адрес термина в таблице Term, записывается в TernmStat
# Совпадающие значения в колонке FirstTerm - это количество вхождений термина 
# FirstTerm в таблицу Terms - Статистика встречаемости
indTerm = 0; Term = ''; EqualFlag = 0
while Term != 'EndOfTerms': # Конец записей в таблице, цикл по всем записям в БД
# Не добавляется второе слово к термину
# Смотри завершение чтения таблицы - из корпус
#    i2 = 0
    Term = ''
    indTerm = indTerm + 1   
    Res = ReadTermFromTermsModule.ReadTermFromTermsTable(indTerm)
    if Res[0] == 'EndOfTerms':
        break
    else:
        Term = Res[0]
    if len(Res[1]) >= 4: 
        Year = Res[1][0:4]
    else:
        Year = ''
    indRest = 0; FirstTerm = 0; # Индекс и номер термина из Terms
    while FirstTerm != 'EndOfFirstTerm':
        indRest = indRest + 1
        Res = SearchForTermInStatModule.SearchForTermIdInStat(indRest)
        FirstTerm = Res[0]
        RestTerm  = Res[1]
        if RestTerm == 'EndOfRestTerm' and EqualFlag != 1:
            AddRecordToTermStatModule.AddRecordToTermStat(indTerm,indTerm,Year) 
            break
        else:
            Term2 = ''
            Term2 = ReadTermFromTermsModule.ReadTermFromTermsTable(FirstTerm)
            Term2 = Term2[0]
        EqualFlag = 0
        if Term == Term2:
            AddRecordToTermStatModule.AddRecordToTermStat(FirstTerm,indTerm,Year)
            EqualFlag =1 # Чтобы не записать еще раз, если таблица TermStat закончилась
            break        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if indTerm % 100 == 0:
        wait = input("PRESS ENTER TO CONTINUE.222222")
