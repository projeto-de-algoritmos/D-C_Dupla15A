
# Desafio Uri: https://www.urionlinejudge.com.br/judge/pt/problems/view/1088
import random
import numpy as np

contSol = 0

def merge(esquerda, direita):

    retMerge = []
    posL = 0
    posR = 0
    global contSol

    while esquerda or direita:

        # Verifica se um dos dois vetores está vazio
        # Caso esteja abaixo considera o vetor que não está vazio, e adiciona ao retorno
        if len(esquerda) and len(direita):
            
            if esquerda[0] < direita[0]:
                popValue = esquerda.pop(0)
                retMerge.append(popValue)

            else:  
                popValue = direita.pop(0)
                retMerge.append(popValue)

                if not popValue == esquerda[0]:
                    contSol = contSol + len(esquerda) #- len(retMerge) + 1

        # Caso um vetor esteja vazio, verifica se o outro está tambem, caso não adiciona o não vazio ao retorno
        if not len(esquerda):
            if len(direita): retMerge.append(direita.pop(0))

        if not len(direita):
            if len(esquerda): retMerge.append(esquerda.pop(0))

    return retMerge

def mergeSort(lista):

    if len(lista) < 2: 
        return lista

    metadeLista = int(len(lista) / 2)
    mergeSort_ret = mergeSort(lista[:metadeLista]) + mergeSort(lista[metadeLista:])
    # Converte o resultado para um inteiro
    metadeLista = int(len(mergeSort_ret)/2)

    return merge(mergeSort_ret[:metadeLista], mergeSort_ret[metadeLista:])

def bolhaBalde(lista):

    global contSol
    returnList = mergeSort(lista)
    returnCont = contSol
    contSol = 0

    return returnList, returnCont
 