import pickle

def sorec(dictrecorrencias):
    listarecorrenciaspronta = []
    for chave, valor in dictrecorrencias.items():
        if len(valor) > 1:
            setv = {v[0:3] for v in valor}
            if tuple(setv) == chave[1]:
                listarecorrenciaspronta.append((chave[0], valor))
    print(f'len list after sorec changes when the program is restarted: {len(listarecorrenciaspronta)}')
    return listarecorrenciaspronta

def sorec_corrected(dictrecorrencias):
    listarecorrenciaspronta = []
    for chave, valor in dictrecorrencias.items():
        if len(valor) > 1:
            setv = {v[0:3] for v in valor}
            if sorted(tuple(setv)) == sorted(chave[1]):
                listarecorrenciaspronta.append((chave[0], valor))
    print(f'with sorted stays the same: {len(listarecorrenciaspronta)}')
    return listarecorrenciaspronta


with open(r'segmentacao.p', 'rb') as f:
    segmentacao = pickle.loads(f.read())

sorec(segmentacao)
sorec(segmentacao)
sorec(segmentacao)
sorec_corrected(segmentacao)
sorec_corrected(segmentacao)
sorec_corrected(segmentacao)