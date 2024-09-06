import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# FUNÇÕES PARA CALCULAR MÉTRICAS
def numeroNosArestas(G):
    print(f"O número de nós é: {G.number_of_nodes()}")
    print(f"O número de arestas é: {G.number_of_edges()}")

def densidade(G):
    print(f"A densidade do grafo é: {nx.density(G):.3f}")

def centralidadeDeGrau(G):
    centralidades = nx.degree_centrality(G)
    for no, valor in centralidades.items():
        print(f"A centralidade de grau do nó {no} é: {valor:.3f}")

def centralidadeDeIntermediacao(G):
    centralidades = nx.betweenness_centrality(G)
    for no, valor in centralidades.items():
        print(f"A centralidade de intermediação do nó {no} é: {valor:.3f}")


def centralidadeDeProximidade(G):
    # Calcula a centralidade de proximidade para todos os nós
    centralidades = nx.closeness_centrality(G)
    
    # Ordena os nós pela centralidade de proximidade em ordem decrescente
    centralidades_ordenadas = sorted(centralidades.items(), key=lambda x: x[1], reverse=True)
    
    # Seleciona os 10 maiores
    top_10_centralidades = centralidades_ordenadas[:10]
    
    # Exibe os 10 maiores
    for no, valor in top_10_centralidades:
        print(f"A centralidade de proximidade do nó {no} é: {valor:.3f}")

def diametro(G):
    print(f"O diâmetro do grafo é {nx.diameter(G)}")

def caminhoMedio(G):
    print(f"O caminho médio do grafo é {nx.average_shortest_path_length(G):.3f}")

def assortividade(G):
    print(f"Assortatividade pelo grau do grafo é {nx.degree_assortativity_coefficient(G):.3f}")


#função furia de titãs

def furia():
    tabela_furia = pd.read_excel("furia.xlsx")
    tabela_furia = tabela_furia.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)
    totalColunas_furia = tabela_furia['A'].count()
    G_furia = nx.Graph()

    #nós furia de titãs
    nos_furia = set()
    for i in range(totalColunas_furia):
        for j in range(2):
            palavra_furia = tabela_furia.iloc[i, j]
            if pd.notna(palavra_furia):  
                nos_furia.add(palavra_furia)
    G_furia.add_nodes_from(nos_furia)

    #arestas furia de titãs
    arestas_furia = set()  
    for i in range(totalColunas_furia):
        palavra_furia = tabela_furia.iloc[i, 0]
        palavra2_furia = tabela_furia.iloc[i, 1]
        if pd.notna(palavra_furia) and pd.notna(palavra2_furia): 
            arestas_furia.add((palavra_furia, palavra2_furia))
    G_furia.add_edges_from(arestas_furia)

    grau_nos_furia = dict(G_furia.degree()) #calcula os graus
    tamanho_nos_furia = [grau * 100 for grau in grau_nos_furia.values()]



    # Configs do grafo
    plt.close('all')
    layout_furia = nx.kamada_kawai_layout(G_furia)
    plt.figure(figsize=(15, 15))  
    nx.draw(G_furia, layout_furia, with_labels=True, node_color="lime", node_size=tamanho_nos_furia,
            font_size=8, font_color="black", font_weight="bold",
            edge_color="gray", linewidths=1.5)

    plt.title("Furia")
    plt.show()
    return G_furia


#função GOW

def GOW():
    tabela_gow = pd.read_excel("gow.xlsx")
    tabela_gow = tabela_gow.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)
    totalColunas_gow = tabela_gow['A'].count()
    G_gow = nx.Graph()

    #nós gow
    nos_gow = set()
    for i in range(totalColunas_gow):
        for j in range(2):
            palavra_gow = tabela_gow.iloc[i, j]
            if pd.notna(palavra_gow):  
                nos_gow.add(palavra_gow)
    G_gow.add_nodes_from(nos_gow)

    #arestas gow
    arestas_gow = set()  
    for i in range(totalColunas_gow):
        palavra_gow = tabela_gow.iloc[i, 0]
        palavra2_gow = tabela_gow.iloc[i, 1]
        if pd.notna(palavra_gow) and pd.notna(palavra2_gow): 
            arestas_gow.add((palavra_gow, palavra2_gow))
    G_gow.add_edges_from(arestas_gow)

    grau_nos_gow = dict(G_gow.degree()) #calcula os graus
    tamanho_nos_gow = [grau * 100 for grau in grau_nos_gow.values()]



    # Configs do grafo
    plt.close('all')
    layout_gow = nx.kamada_kawai_layout(G_gow)
    plt.figure(figsize=(15, 15))  
    nx.draw(G_gow, layout_gow, with_labels=True, node_color="Orchid", node_size=tamanho_nos_gow,
            font_size=8, font_color="black", font_weight="bold",
            edge_color="gray", linewidths=1.5)

    plt.title("GOW")
    plt.show()
    return G_gow


#função Percy J

def percyJ():
    tabela_percyJ = pd.read_excel("percyJ.xlsx")
    tabela_percyJ = tabela_percyJ.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)
    totalColunas_percyJ = tabela_percyJ['A'].count()
    G_percyJ = nx.Graph()

    #nós percyJ
    nos_percyJ = set()
    for i in range(totalColunas_percyJ):
        for j in range(2):
            palavra_percyJ = tabela_percyJ.iloc[i, j]
            if pd.notna(palavra_percyJ):  
                nos_percyJ.add(palavra_percyJ)
    G_percyJ.add_nodes_from(nos_percyJ)

    #arestas percyJ
    arestas_percyJ = set()  
    for i in range(totalColunas_percyJ):
        palavra_percyJ = tabela_percyJ.iloc[i, 0]
        palavra2_percyJ = tabela_percyJ.iloc[i, 1]
        if pd.notna(palavra_percyJ) and pd.notna(palavra2_percyJ): 
            arestas_percyJ.add((palavra_percyJ, palavra2_percyJ))
    G_percyJ.add_edges_from(arestas_percyJ)

    grau_nos_percyJ = dict(G_percyJ.degree()) #calcula os graus
    tamanho_nos_percyJ = [grau * 100 for grau in grau_nos_percyJ.values()]



    # Configs do grafo
    plt.close('all')
    layout_percyJ = nx.kamada_kawai_layout(G_percyJ)
    plt.figure(figsize=(15, 15))  
    nx.draw(G_percyJ, layout_percyJ, with_labels=True, node_color="coral", node_size=tamanho_nos_percyJ,
            font_size=8, font_color="black", font_weight="bold",
            edge_color="gray", linewidths=1.5)

    plt.title("percyJ")
    plt.show()
    return G_percyJ


#função mescla

def Mesclar(G, G_gow, G_percyJ, G_furia):
   
    G_mescla = nx.compose_all([G, G_gow, G_percyJ, G_furia])

    plt.close('all')
    plt.figure(figsize=(15, 15))  

    layout_mescla = nx.spring_layout(G_mescla, seed=42, k=0.9) 


    def tamanhoNos_mescla(degree):
        return max(degree * 20, 50)  
    grau_nos_mescla = dict(G_mescla.degree()) 

    # arestas
    nx.draw_networkx_edges(G_mescla, layout_mescla, alpha=0.5, edge_color="gray", width=1.0)

    # nós
    cores = {'G': 'skyblue', 'G_gow': 'Orchid', 'G_percyJ': 'coral', 'G_furia': 'lime'}

    for node in G_mescla.nodes():
        x, y = layout_mescla[node]
        node_size = tamanhoNos_mescla(grau_nos_mescla[node]) / 9000  # aumentar para diminuir os nós
        participacao = []
        if node in G.nodes():
            participacao.append('G')
        if node in G_gow.nodes():
            participacao.append('G_gow')
        if node in G_percyJ.nodes():
            participacao.append('G_percyJ')
        if node in G_furia.nodes():
            participacao.append('G_furia')

        # cores
        if len(participacao) > 0:
            start_angle = 0
            for part in participacao:
                wedge = patches.Wedge((x, y), node_size, start_angle, start_angle + 360 / len(participacao), color=cores[part], alpha=0.8)
                plt.gca().add_patch(wedge)
                start_angle += 360 / len(participacao)
        else:
            plt.scatter(x, y, s=node_size * 100, c='orange', alpha=0.8)  

    nx.draw_networkx_labels(G_mescla, layout_mescla, font_size=8, font_color="black", font_weight="bold") 

    plt.title("Grafos Mesclados")
    plt.show()
    return G_mescla







#GRAFO PRINCIPAL

tabela = pd.read_excel("CR.xlsx")# Le o arquivo
tabela = tabela.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)

totalColunas = tabela['A'].count()


G = nx.Graph()


# Nós
nos = set()  
for i in range(totalColunas):
    for j in range(2):
        palavra = tabela.iloc[i, j]
        if pd.notna(palavra):  
            nos.add(palavra)
#print(nos)    # conferir nós
G.add_nodes_from(nos)


# Arestas
arestas = set()  
for i in range(totalColunas):
    palavra = tabela.iloc[i, 0]
    palavra2 = tabela.iloc[i, 1]
    if pd.notna(palavra) and pd.notna(palavra2): 
        arestas.add((palavra, palavra2))
#print(arestas)    # conferir arestas
G.add_edges_from(arestas)



grau_nos = dict(G.degree()) #calcula os graus
tamanho_nos = [grau * 100 for grau in grau_nos.values()]



# Configs do grafo
layout = nx.kamada_kawai_layout(G)
plt.figure(figsize=(15, 15))  
nx.draw(G, layout, with_labels=True, node_color="skyblue", node_size=tamanho_nos,
        font_size=8, font_color="black", font_weight="bold",
        edge_color="gray", linewidths=1.5)

plt.title("Mitologia Grega")
plt.show()


G_furia = furia()
G_percyJ = percyJ()
G_gow = GOW()
G_mescla = Mesclar(G,G_gow,G_percyJ, G_furia)



# funções de calcular métrica, é só tirar o # (cuidado para não deixar vários de uma vez só porque vai consumir muita memória)
#colocar nos parametros o nome do grafo (G, G_mescla, G_gow, G_PercyJ ou G_gow)

#numeroNosArestas()
#densidade()
#centralidadeDeGrau()
#centralidadeDeProximidade()
#centralidadeDeIntermediacao()
#diametro()
#caminhoMedio()
#assortividade()










