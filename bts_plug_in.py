# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:41:42 2017

@author: device
"""

class Bug(object):
    def __init__(self, idBug, idProject, idCluster, rawBugDescription,
                 processedBugDescription, hasSTR, hasEOB, hasConfigFilesOrLogs,
                 hasImages, hasStackTrace, hasJavaCode):
        self.idBug = idBug
        self.idProject = idProject
        self.idCluster = idCluster
        self.rawBugDescription = rawBugDescription
        self.processedBugDescription = processedBugDescription
        self.hasSTR = hasSTR
        self.hasEOB = hasEOB
        self.hasConfigFilesOrLogs = hasConfigFilesOrLogs
        self.hasImages = hasImages
        self.hasStackTrace = hasStackTrace
        self.hasJavaCode = hasJavaCode

class Project(object):
    def __init__(self, idProject, nameProject):
        self.idProject = idProject
        self.nameProject = nameProject

class Parameters(object):
    def __init__(self, numClustersForFirstStep, numClustersForSecondStep,
                 numWordsWithMaxTfidf, percentWordsFromClusterToExpandFeatures,
                 percentSTRtoDecideSTR, percentEOBtoDecideEOB):
        self.numClustersForFirstStep = numClustersForFirstStep
        self.numClustersForSecondStep = numClustersForSecondStep
        self.numWordsWithMaxTfidf = numWordsWithMaxTfidf
        self.percentWordsFromClusterToExpandFeatures = percentWordsFromClusterToExpandFeatures
        self.percentSTRtoDecideSTR = percentSTRtoDecideSTR
        self.percentEOBtoDecideEOB = percentEOBtoDecideEOB
        
        
class Project_parameters(object):
    def __init__(self, idProject, idParameter, paramsValue):
        #paramsValue - объект класса Parameters
        self.idProject = idProject
        self.idParameter = idParameter
        self.paramsValue = paramsValue
        
        
class Cluster(object):
    def __init__(self, idCluster, percentageHasSTR, percentageHasEOB,
                 percentageHasConfigFilesOrLogs, percentageHasImages,
                 percentageHasStackTrace, percentageHasJavaCode,
                 percentageBugsInClusterInProject, wordsInClusterRankedByTfidf):
        self.idCluster = idCluster
        self.percentageHasSTR = percentageHasSTR
        self.percentageHasEOB = percentageHasEOB
        self.percentageHasConfigFilesOrLogs = percentageHasConfigFilesOrLogs
        self.percentageHasImages = percentageHasImages
        self.percentageHasStackTrace = percentageHasStackTrace
        self.percentageHasJavaCode = percentageHasJavaCode
        self.percentageBugsInClusterInProject = percentageBugsInClusterInProject
        self.wordsInClusterRankedByTfidf = wordsInClusterRankedByTfidf

class Recommendation(object):        
    def __init__(self, idRecommendation, textRecommendation):
        self.idRecommendation = idRecommendation
        self.textRecommendation = textRecommendation
        
class Cluster_recommendation(object):
    def __init__(self, idCluster, idRecommendation):
        #idRecommendation - массив id рекомендаций, соответствующих данному кластеру
        self.idCluster = idCluster
        self.idRecommendation = idRecommendation        

class Cluster_project(object):
    def __init__(self, idProject, idCluster):
        #idCluster - массив id кластеров, соответствующих данному проекту
        self.idProject = idProject
        self.idCluster = idCluster
        
class Bts_plug_in_system(object):
    def __init__(self):
        self.list_of_projects = list()
        self.list_of_bugs = list()
        self.list_of_clusters = list()
        self.list_of_recommendations = list()
        
    def choose_the_action():
        print()
        
    def load_project_in_system():
        print()
    
    def learning():
        print()
        
    def create_recommendations():
        print()
        
    def set_params():
        print()
        
    def show_project_list(): #аргумент - id проекта
        print()
    
    def show_project_params(): #аргумент - id проекта
        print()
        
    def export_xls_for_STR_EOB_marking():
        print()
        
    def import_xls_for_STR_EOB_marking():
        print()
        
    def load_bug_and_get_recommendations():
        print()
        
    def continue_or_save_or_exit():
        print()
        
system = Bts_plug_in_system()

while True:
    #определяем, кто перед нами
    role = system.who_are_you()
    
    #запускаем действие актора
    if role == "admin":
        action = system.choose_the_action(role)
        if action == "load_project_in_system":
            system.load_project_in_system()
        if action == "system_learning":
            system.learning()
        if action == "create_recommendations":
            system.create_recommendations()
    if role == "analyst":
        action = system.choose_the_action(role)
        if action == "setting_system_params": #сохранять в текстовый файл отдельный
        #создать структуру папка-файлы
        #сырой дескр отдельным файлом
            system.set_params()
        if action == "show_project_list": 
            system.show_project_list()
        if action == "show_project_params":
            system.show_project_params()
        if action == "export_excel_file_for_STR_EOB_marking":
            system.export_xls_for_STR_EOB_marking()
        if action == "import_excel_file_for_STR_EOB_marking":
            system.import_xls_for_STR_EOB_marking()
    if role == "user":
        system.load_bug_and_get_recommendations()

    #запрашиваем, что делать дальше    
    if system.continue_or_save_or_exit():
        break
    