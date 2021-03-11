from collections import defaultdict
import pickle

def sort_continte3(listarecorrencias):
    p_pset_pseg = []
    for seg, pos in listarecorrencias:
        posset = {p[0:3] for p in pos}
        for p in pos:
            p_pset_pseg.append((p,tuple(posset),seg))

    #por nome, set, tamanho maior, posicao menor
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[0][3][0]))
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (len(item[2][0])), reverse=True)
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[1]))
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[0][0:3]))
    locpset = defaultdict(list)
    for p, pset, pseg in p_pset_pseg:
        locpset[(p[0:3], pset)].append((p,pseg))
    locpset = [(c[1],v) for c, v in locpset.items()]
    return locpset

def contida3(listaposicoes, posicao):
    for quepassou in listaposicoes:
        if posicao[0:3] == quepassou[0][0:3] and posicao[3][0] >= quepassou[0][3][0] and posicao[3][1] <= quepassou[0][3][1]:
            return True
    return False

def intercalada3(listaposicoes, posicao, distancia=0):
    for quepassou in listaposicoes:
        if posicao[0:3] == quepassou[0][0:3] and posicao[3][0] > quepassou[0][3][0] and posicao[3][0] < quepassou[0][3][1]+distancia and posicao[3][1] > quepassou[0][3][1]:
            return True
        if posicao[0:3] == quepassou[0][0:3] and posicao[3][1] > quepassou[0][3][0]-distancia and posicao[3][1] < quepassou[0][3][1] and posicao[3][0] < quepassou[0][3][0]:
            assert posicao[3][1] - posicao[3][0] < quepassou[0][3][1] - quepassou[0][3][0]
            return True
    return 

def sem_cont_inte3(listarecorrencias, distancia=0):
    listarecorrencias = sort_continte3(listarecorrencias)
    dictrecorrencias = defaultdict(list)
    for grupo in listarecorrencias:
        quepassaram = []
        for posicao in grupo[1]:
            if not contida3(quepassaram, posicao[0]) and not intercalada3(quepassaram, posicao[0], distancia=distancia):
                quepassaram.append(posicao)
        for posicao, segmento in quepassaram:
            dictrecorrencias[(segmento, grupo[0])].append(posicao)
            print(f'\rQuaSegUnicos: {len(dictrecorrencias)} ', end='')
    print()
    return dictrecorrencias

def sorec(dictrecorrencias):
    listarecorrenciaspronta = []
    for chave, valor in dictrecorrencias.items():
        if len(valor) > 1:
            setv = {v[0:3] for v in valor}
            if tuple(setv) == chave[1]:
                listarecorrenciaspronta.append((chave[0], valor))
    return listarecorrenciaspronta

nomes = ('K.1 Musicalion', 'K.10 Musicalion', 'K.11 Musicalion', 'K.12 Musicalion', 'K.13 Musicalion',
        'K.14 Musicalion', 'K.15 Musicalion', 'K.16 Musicalion', 'K.17 Musicalion', 'K.18 Musicalion',
        'K.19 Musicalion', 'K.2 Musicalion', 'K.20 Musicalion', 'K.21 Musicalion', 'K.22 Musicalion',
        'K.23 Musicalion', 'K.24 Musicalion', 'K.25 Musicalion', 'K.26 Musicalion', 'K.27 Musicalion',
        'K.28 Musicalion', 'K.29 Musicalion', 'K.3 Musicalion', 'K.30 Musicalion', 'K.4 Musicalion',
        'K.5 Musicalion', 'K.6 Musicalion', 'K.7 Musicalion', 'K.8 Musicalion', 'K.9 Musicalion')

caractreristicas = (('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1p2'), ('Ptempo', 'p1p2'))
chavearquivo = (nomes, caractreristicas)

with open(r'_segmentacoes_.p', 'rb') as f:
    segmentacao = pickle.loads(f.read())
    segmentacao = segmentacao[chavearquivo]

segmentacao = sem_cont_inte3(segmentacao)
print(f'len list berofe sorec is the same: {len(segmentacao)}')
segmentacao = sorec(segmentacao)
print(f'len list after sorec sometimes changes when the program is restarted: {len(segmentacao)}')

with open(r'_segmentacoes_.p', 'rb') as f:
    segmentacao = pickle.loads(f.read())
    segmentacao = segmentacao[chavearquivo]

segmentacao = sem_cont_inte3(segmentacao)
print(f'len list berofe sorec is the same: {len(segmentacao)}')
segmentacao = sorec(segmentacao)
print(f'len list after sorec sometimes changes when the program is restarted: {len(segmentacao)}')