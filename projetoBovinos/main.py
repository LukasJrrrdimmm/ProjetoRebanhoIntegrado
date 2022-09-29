import numpy as np

altura_brac = []
altura_massai = []
altura_momb = []

peso_brac, peso_massai, peso_momb = list(map(float, input().split(" ")))
pct_mat_seca_brac, pct_mat_seca_massai, pct_mat_seca_momb = list(map(float, input().split(" ")))
peso_med_rebanho = float(input())
# nº de piquetes = periodo_descanso(n+1)/periodo_ocupação(max=7d)

try:
	print("\n>>> Brachiária:")
	altura_brac = list(map(int, input().split(" ")))
	med_altura_brac = np.array(altura_brac).mean()
	peso_forra_brac = (peso_brac*pct_mat_seca_brac)*10000
	tx_lota_brac = peso_forra_brac/peso_med_rebanho
	print(f"média altura brachiária {med_altura_brac} cm")
	print(f"peso forragem brachiaria {peso_forra_brac} Kgms/ha")	
	print(f"taxa lotação brachiária {tx_lota_brac} cab/ha")
	
	print("\n>>> Massai")
	altura_massai = list(map(int, input().split(" ")))
	med_altura_massai = np.array(altura_massai).mean()
	peso_forra_massai = (peso_massai*pct_mat_seca_massai)*10000
	tx_lota_massai = peso_forra_massai/peso_med_rebanho
	print(f"média altura massai {med_altura_massai} cm")
	print(f"peso forragem massai {peso_forra_massai} Kgms/ha")
	print(f"taxa lotação massai {tx_lota_massai} cab/ha")
	
	print("\n>>> Mombassa")
	altura_momb = list(map(int, input().split(" ")))
	med_altura_momb = np.array(altura_momb).mean()
	peso_forra_momb = (peso_momb*pct_mat_seca_momb)*10000
	tx_lota_momb = peso_forra_momb/peso_med_rebanho
	print(f"média altura mombassa {med_altura_momb} cm")
	print(f"peso forragem mombassa {peso_forra_momb} Kgms/ha")
	print(f"taxa lotação mombassa {tx_lota_momb} cab/ha")
except EOFError:
	print("Programa Finalizado!");


# Projeto: dia 13, 5 pontos (Trios)
# Ecolher um sistema de produção (leite ou carne: definir nº de animais e funções de cada um, sistemas de ordenha, confinamento, cercas, etc.): fazer um projeto de instalações (desenhar as instalações, custos)
# Prova: dia 08 (Multiprovas), 5 pontos (intro, sistemas)
