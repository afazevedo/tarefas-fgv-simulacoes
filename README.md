# Tarefa de aprendizado: Modelagem NEWAVE



## INFRAESTRUTURA 
#### Base PMO 08/2020 

- **arquivos.dat** – nome arquivos de entrada utilizados
- **agrint.dat** - agrupamento de intercâmbios e seus limites – altera anos e meses do PMO
- **hidr.dat** – dados usinas hidrelétricas 
- **penalid.dat** – penalidade ao não atendimento as restrições de Q mín., etc.
- **postos.dat** – dados dos postos fluviométricos
- **ree.dat** – Reservatórios Equivalentes e Submercados
- **selcor.dat** – parâmetros de seleção de cortes 
- **shist.dat** – tipo de simulação da série histórica
- **vazoes.dat** – dados históricos de vazões

# Sazonalidade 
#### Base PMO 02/2020 (úmido) e 10/2020 (seco)
##### altera os anos no PMO - inicia simulação em 2015 (úmido) e inicia simulação em 2017 (seco))

- **adterm.dat**  - despacho GNL (não precisa alterar)
- **c_adic.dat** – carga/oferta adicional
- **clast.dat** – classes das usinas térmicas, tipo de combustível e custo
- **curva.dat** – curva de aversão a risco, penalização das violações
- **cvar.dat** – aversão a risco
- **dsvagua.dat** – dados para outros usos da água
- **exph.dat** – dados de expansão usinas hidroelétricas
- **ghmin.dat** – geração hidro mínima
- **modif.dat** – altera configuração das hidroelétricas, restrições
- **patamar.dat** – patamares de carga, fator da demanda, fator do intercâmbio
- **re.dat** – restrição de capacidade máx. de geração de conj. de hidrelétricas
- **sistema.dat**– custo de déficit, limite intercâmbio, carga do sistema e pequenas usinas

-----

- **confhd.dat** - configuração hidrologia: volume armazenado 2015 para úmido e 2017 para seco
- **conft.dat** – configuração das termoelétricas, geração térmica mínima de acordo com TEIF IP – altera usinas listadas como manutenção em EXPT.dat (EE) e passam a EX. 
- **dger.dat** – dados gerais – altera linha 33 para não considerar o MANUTT
- **expt.dat** – dados de expansão usinas termoelétricas, manutenção, modificações na configuração - altera anos e meses do PMO
- **term.dat ** - dados das usinas termoelétricas – cálculo do Gtmin de acordo com o TEIF IP
- **manutt.dat**  - dados de manutenção - não considerado por ser conjuntural
- **term.dat**  - dados das usinas termoelétricas – cálculo do Gtmin de acordo com o TEIF IP
- **vazpast.dat**  - tendência hidrológica por posto de medição –
utiliza dados de fev 2014 a jan 2015 para úmido e out 2016 a set 2017 para seco















