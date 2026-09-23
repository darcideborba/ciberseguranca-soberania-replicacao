import json, re
"""Gera data/referencias_codificadas.ris (UTF-8) com as referências do estudo e a codificação do Quadro 3."""
A = 'JOUR'
R = []
def add(ty, au, ti, jo=None, py=None, vl=None, is_=None, sp=None, doi=None, ur=None, **kw):
    R.append(dict(TY=ty, AU=au, TI=ti, T2=jo, PY=py, VL=vl, IS=is_, SP=sp, DO=doi, UR=ur, **kw))

# --- Literatura acadêmica e relatórios ---
add(A, ["Adler-Nissen, R.", "Eggeling, K. A."], "The discursive struggle for digital sovereignty: security, economy, rights and the cloud project Gaia-X", "Journal of Common Market Studies", "2024", "62", "4", "993-1011", "10.1111/jcms.13594")
add(A, ["Akçalı Gür, B."], "Cybersecurity, European digital sovereignty and the 5G rollout crisis", "Computer Law & Security Review", "2022", "46", None, "105736", "10.1016/j.clsr.2022.105736")
add('RPRT', ["Banco Interamericano de Desarrollo", "Organización de los Estados Americanos"], "Reporte ciberseguridad 2020: riesgos, avances y el camino a seguir en América Latina y el Caribe", None, "2020", doi="10.18235/0002513", PB="BID", CY="Washington, DC", LA="es")
add('BOOK', ["Bardin, L."], "Análise de conteúdo", None, "2016", PB="Edições 70", CY="São Paulo")
add(A, ["Barrinha, A.", "Christou, G."], "Speaking sovereignty: the EU in the cyber domain", "European Security", "2022", "31", "3", "356-376", "10.1080/09662839.2022.2102895")
add(A, ["Belli, L.", "Magalhães Santos, Larissa Galdino de"], "Editorial: Toward a BRICS stack? Leveraging digital transformation to construct digital sovereignty in the BRICS countries", "Computer Law & Security Review", "2024", "55", None, "106064", "10.1016/j.clsr.2024.106064")
add(A, ["Blancato, F. G.", "Carr, M."], "The trust deficit. EU bargaining for access and control over cloud infrastructures", "Journal of European Public Policy", "2024", doi="10.1080/13501763.2024.2441418", N1="Publicado online em 18 dez. 2024.")
add(A, ["Borba, Darci de", "Brinkhues, Rafael"], "Inteligência artificial no gerenciamento de processos de negócio: desafios, oportunidades e estratégias para alinhamento à ISO 42001", "Review of Artificial Intelligence in Education", "2025", "6", None, "e060", "10.37497/rev.artif.intell.educ.v6ii.60")
add(A, ["Castro, Mario Henrique de Oliveira", "Lanzara, Arnaldo Provasi"], "Capacidades estatais e capacidades dinâmicas para o enfrentamento de crises: o sucesso do Vietnã contra a COVID-19", "Revista do Instituto de Políticas Públicas de Marília", "2023", "9", None, "e023002", "10.36311/2447-780X.2023.v9.e023002")
add('CHAP', ["Cellard, A."], "A análise documental", "A pesquisa qualitativa: enfoques epistemológicos e metodológicos", "2008", sp="295-316", PB="Vozes", CY="Petrópolis", A2=["Poupart, J."])
add('RPRT', ["Check Point Research"], "AI security report 2025", None, "2025", ur="https://engage.checkpoint.com/2025-ai-security-report", PB="Check Point Software Technologies")
add(A, ["Couture, S.", "Toupin, S."], "What does the notion of \"sovereignty\" mean when referring to the digital?", "New Media & Society", "2019", "21", "10", "2305-2322", "10.1177/1461444819865984")
add('RPRT', ["Duarte, A.", "Frost, J.", "Gambacorta, L.", "Koo Wilkens, P.", "Shin, H. S."], "Central banks, the monetary system and public payment infrastructures: lessons from Brazil's Pix", "BIS Bulletin", "2022", is_="52", ur="https://www.bis.org/publ/bisbull52.pdf", PB="Bank for International Settlements", CY="Basel", DA="2022/03/23")
add(A, ["Dunleavy, P.", "Margetts, H.", "Bastow, S.", "Tinkler, J."], "New public management is dead: long live digital-era governance", "Journal of Public Administration Research and Theory", "2006", "16", "3", "467-494", "10.1093/jopart/mui057")
add(A, ["Dunn Cavelty, M.", "Wenger, A."], "Cyber security meets security politics: complex technology, fragmented politics, and networked science", "Contemporary Security Policy", "2020", "41", "1", "5-32", "10.1080/13523260.2019.1678855")
add(A, ["Farrand, B."], "The economy-security nexus: risk, strategic autonomy and the regulation of the semiconductor supply chain", "European Journal of Risk Regulation", "2025", "16", "1", "279-293", "10.1017/err.2024.63")
add(A, ["Farrand, B.", "Carrapico, H."], "Digital sovereignty and taking back control: from regulatory capitalism to regulatory mercantilism in EU cybersecurity", "European Security", "2022", "31", "3", "435-453", "10.1080/09662839.2022.2102896")
add(A, ["Floridi, L."], "The fight for digital sovereignty: what it is, and why it matters, especially for the EU", "Philosophy & Technology", "2020", "33", "3", "369-378", "10.1007/s13347-020-00423-6")
add(A, ["Goldoni, Luiz Rogério Franco", "Rodrigues, Karina Furtado", "Medeiros, Breno Pauli"], "Qual é o futuro da governança de cibersegurança no Brasil?", "Cadernos Gestão Pública e Cidadania", "2024", "29", None, "e90972", "10.12660/cgpc.v29.90972")
add(A, ["Ifeanyi-Ajufo, N."], "Cyber governance in Africa: at the crossroads of politics, sovereignty and cooperation", "Policy Design and Practice", "2023", "6", "2", "146-159", "10.1080/25741292.2023.2199960")
add(A, ["Janowski, T."], "Digital government evolution: from transformation to contextualization", "Government Information Quarterly", "2015", "32", "3", "221-236", "10.1016/j.giq.2015.07.001")
add(A, ["Janowski, T.", "Estévez, E.", "Baguma, R."], "Platform governance for sustainable development: reshaping citizen-administration relationships in the digital age", "Government Information Quarterly", "2018", "35", "4", "S1-S16", "10.1016/j.giq.2018.09.002")
add(A, ["Junqueira, Cesar Augusto de Carvalho"], "A capacidade de coordenação governamental: evolução conceitual, mecanismos institucionais e desafios contemporâneos", "Revista do Instituto de Políticas Públicas de Marília", "2026", "12", None, "e026001", "10.36311/2447-780X.2026.v12.e026001")
add(A, ["Martynova, E.", "Shcherbovich, A."], "Digital transformation in Russia: turning from a service model to ensuring technological sovereignty", "Computer Law & Security Review", "2024", "55", None, "106075", "10.1016/j.clsr.2024.106075")
add(A, ["Mergel, I.", "Edelmann, N.", "Haug, N."], "Defining digital transformation: results from expert interviews", "Government Information Quarterly", "2019", "36", "4", "101385", "10.1016/j.giq.2019.06.002")
add('BOOK', ["Miles, M. B.", "Huberman, A. M."], "Qualitative data analysis: an expanded sourcebook", None, "1994", ET="2", PB="Sage", CY="Thousand Oaks")
add(A, ["Muara, Damião Magido", "Klein, Amarolinda Zanela", "Matos, Celso Augusto de", "Borba, Darci de", "Gonçalves, Bruno Bentes"], "Beyond adoption: how public value drives the success of mobile government: evidence from the Global South", "Telematics and Informatics", "2026", "106", None, "102393", "10.1016/j.tele.2026.102393")
add(A, ["Musiani, F."], "Infrastructuring digital sovereignty: a research agenda for an infrastructure-based sociology of digital self-determination practices", "Information, Communication & Society", "2022", "25", "6", "785-800", "10.1080/1369118X.2022.2049850")
add(A, ["O'Connor, C.", "Joffe, H."], "Intercoder reliability in qualitative research: debates and practical guidelines", "International Journal of Qualitative Methods", "2020", "19", None, "1-13", "10.1177/1609406919899220")
add(A, ["O'Reilly, T."], "Government as a platform", "Innovations: Technology, Governance, Globalization", "2011", "6", "1", "13-40", "10.1162/INOV_a_00056")
add(A, ["Pohle, J.", "Nanni, R.", "Santaniello, M."], "Unthinking digital sovereignty: a critical reflection on origins, objectives, and practices", "Policy & Internet", "2024", "16", "4", "666-671", "10.1002/poi3.437")
add(A, ["Pohle, J.", "Thiel, T."], "Digital sovereignty", "Internet Policy Review", "2020", "9", "4", None, "10.14763/2020.4.1532")
add(A, ["Rodrigues, Jesiélli Santana", "Oliveira, Juliana Alves Nogueira de", "Oliveira, Carlyle"], "Controle social da administração pública no Brasil: perspectivas e desafios", "Revista do Instituto de Políticas Públicas de Marília", "2024", "10", None, "e024001", "10.36311/2447-780X.2024.v10.e024001")
add(A, ["Santos Júnior, Darci de Borba"], "Soberania digital e governança da inteligência artificial: da reivindicação ao instrumento na comparação entre o Plano Brasileiro de IA e o America's AI Action Plan", "SciELO Preprints", "2026", doi="10.1590/SciELOPreprints.17393", ur="https://preprints.scielo.org/index.php/scielo/preprint/view/17393", M3="Preprint")
add(A, ["Santos Júnior, Darci de Borba", "Brinkhues, Rafael Alfonso"], "Plano de ação de IA dos Estados Unidos e governança global: convergências, divergências e implicações teóricas", "Revista de Administração Pública", "2026", "60", None, "e2025-0584", "10.1590/0034-761220250584")
add('BOOK', ["Saunders, M.", "Lewis, P.", "Thornhill, A."], "Research methods for business students", None, "2016", ET="7", PB="Pearson", CY="Harlow")
add('RPRT', ["World Economic Forum"], "Global cybersecurity outlook 2025", None, "2025", ur="https://www.weforum.org/publications/global-cybersecurity-outlook-2025/", PB="WEF", CY="Geneva")

# --- Instrumentos normativos: (tipo, autor, título, ano, data, url, corpus) ---
P = "https://www.planalto.gov.br/ccivil_03/"
def lei(num, ti, py, da, url, corpus=None, au="Brasil", ty='STAT', note=None):
    d = dict(TY=ty, AU=[au], TI=ti, PY=py, DA=da, UR=url, M1=num, CY="Brasília, DF", corpus=corpus)
    if note: d['N1'] = note
    R.append(d)

lei("Decreto n. 8.936/2016", "Decreto n. 8.936, de 19 de dezembro de 2016. Institui a Plataforma de Cidadania Digital e dispõe sobre a oferta dos serviços públicos digitais", "2016", "2016/12/19", P+"_ato2015-2018/2016/decreto/d8936.htm", corpus="caso")
lei("Lei n. 13.709/2018", "Lei n. 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD)", "2018", "2018/08/14", P+"_ato2015-2018/2018/lei/l13709.htm", corpus="LGPD")
lei("Decreto n. 9.637/2018", "Decreto n. 9.637, de 26 de dezembro de 2018. Institui a Política Nacional de Segurança da Informação", "2018", "2018/12/26", P+"_ato2015-2018/2018/decreto/d9637.htm", corpus="revogado", note="Revogado pelo Decreto n. 12.572/2025. Usado apenas para trajetória normativa.")
lei("Decreto n. 9.573/2018", "Decreto n. 9.573, de 22 de novembro de 2018. Aprova a Política Nacional de Segurança de Infraestruturas Críticas", "2018", "2018/11/22", P+"_ato2015-2018/2018/decreto/d9573.htm", corpus="9573")
lei("Decreto n. 9.319/2018", "Decreto n. 9.319, de 21 de março de 2018. Institui o Sistema Nacional para a Transformação Digital e estabelece a estrutura de governança para a implantação da Estratégia Brasileira para a Transformação Digital", "2018", "2018/03/21", P+"_ato2015-2018/2018/decreto/d9319.htm", corpus="revogado", note="Revogado pelo Decreto n. 12.308/2024. Usado apenas para trajetória normativa.")
lei("Decreto n. 10.222/2020", "Decreto n. 10.222, de 5 de fevereiro de 2020. Aprova a Estratégia Nacional de Segurança Cibernética", "2020", "2020/02/05", P+"_ato2019-2022/2020/decreto/d10222.htm", corpus="revogado", note="Revogado pelo Decreto n. 12.573/2025. Usado apenas para trajetória normativa.")
lei("Decreto n. 10.332/2020", "Decreto n. 10.332, de 28 de abril de 2020. Institui a Estratégia de Governo Digital para o período de 2020 a 2022", "2020", "2020/04/28", P+"_ato2019-2022/2020/decreto/d10332.htm", corpus="revogado", note="Revogado (arts. 1º a 6º-A e 13) pelo Decreto n. 12.198/2024. Meta de migração de serviços de ao menos 30 órgãos para nuvem até 2022. Usado apenas para trajetória normativa.")
lei("Decreto n. 10.569/2020", "Decreto n. 10.569, de 9 de dezembro de 2020. Aprova a Estratégia Nacional de Segurança de Infraestruturas Críticas", "2020", "2020/12/09", P+"_ato2019-2022/2020/decreto/d10569.htm", corpus="10569")
lei("IN GSI/PR n. 1/2020", "Instrução Normativa n. 1, de 27 de maio de 2020. Dispõe sobre a Estrutura de Gestão da Segurança da Informação nos órgãos e nas entidades da administração pública federal", "2020", "2020/05/27", "https://www.gov.br/gsi/pt-br/seguranca-da-informacao-e-cibernetica/legislacao/copy_of_IN01_consolidada.pdf", corpus="IN1", au="Brasil. Gabinete de Segurança Institucional")
lei("Lei n. 14.129/2021", "Lei n. 14.129, de 29 de março de 2021. Dispõe sobre princípios, regras e instrumentos para o Governo Digital e para o aumento da eficiência pública", "2021", "2021/03/29", P+"_ato2019-2022/2021/lei/l14129.htm", corpus="14129")
lei("Decreto n. 10.748/2021", "Decreto n. 10.748, de 16 de julho de 2021. Institui a Rede Federal de Gestão de Incidentes Cibernéticos", "2021", "2021/07/16", P+"_ato2019-2022/2021/decreto/d10748.htm", corpus="10748")
lei("IN GSI/PR n. 5/2021", "Instrução Normativa n. 5, de 30 de agosto de 2021. Dispõe sobre os requisitos mínimos de segurança da informação para utilização de soluções de computação em nuvem pelos órgãos e pelas entidades da administração pública federal", "2021", "2021/08/30", "https://www.in.gov.br/en/web/dou/-/instrucao-normativa-n-5-de-30-de-agosto-de-2021-341649684", corpus="IN5", au="Brasil. Gabinete de Segurança Institucional")
lei("Decreto n. 11.856/2023", "Decreto n. 11.856, de 26 de dezembro de 2023. Institui a Política Nacional de Cibersegurança e o Comitê Nacional de Cibersegurança", "2023", "2023/12/26", P+"_ato2023-2026/2023/decreto/d11856.htm", corpus="11856")
lei("Lei n. 14.968/2024", "Lei n. 14.968, de 11 de setembro de 2024. Aperfeiçoa a política industrial para o setor de tecnologias da informação e comunicação e para o setor de semicondutores; cria o Programa Brasil Semicondutores (Brasil Semicon)", "2024", "2024/09/11", P+"_ato2023-2026/2024/lei/l14968.htm", corpus="14968")
lei("Decreto n. 12.198/2024", "Decreto n. 12.198, de 24 de setembro de 2024. Institui a Estratégia Federal de Governo Digital para o período de 2024 a 2027 e a Infraestrutura Nacional de Dados", "2024", "2024/09/24", P+"_ato2023-2026/2024/decreto/d12198.htm", corpus="12198")
lei("Decreto n. 12.308/2024", "Decreto n. 12.308, de 11 de dezembro de 2024. Institui o Comitê Interministerial para a Transformação Digital", "2024", "2024/12/11", P+"_ato2023-2026/2024/decreto/d12308.htm", corpus="12308")
R.append(dict(TY='RPRT', AU=["Brasil. Ministério da Ciência, Tecnologia e Inovação"], TI="Plano Brasileiro de Inteligência Artificial 2024-2028: IA para o bem de todos", PY="2024", PB="MCTI", CY="Brasília, DF", UR="https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/transformacaodigital/plano-brasileiro-de-inteligencia-artificial-pbia-_vf.pdf", corpus="PBIA", N1="Versão de 2024. Total R$ 23,03 bi; infraestrutura R$ 5,79 bi; serviços públicos R$ 1,76 bi; regulação e governança R$ 103,25 mi (0,45%); nuvem soberana R$ 1,4 bi."))
lei("Decreto n. 12.572/2025", "Decreto n. 12.572, de 4 de agosto de 2025. Institui a Política Nacional de Segurança da Informação e dispõe sobre a governança da segurança da informação no âmbito da administração pública federal", "2025", "2025/08/04", P+"_ato2023-2026/2025/decreto/d12572.htm", corpus="12572")
lei("Decreto n. 12.573/2025", "Decreto n. 12.573, de 4 de agosto de 2025. Institui a Estratégia Nacional de Cibersegurança", "2025", "2025/08/04", P+"_ato2023-2026/2025/decreto/d12573.htm", corpus="12573")
lei("IN GSI/PR n. 8/2025", "Instrução Normativa n. 8, de 6 de outubro de 2025. Dispõe sobre os requisitos mínimos de segurança da informação para tratamento de informação classificada em computação em nuvem", "2025", "2025/10/06", None, corpus="IN5", au="Brasil. Gabinete de Segurança Institucional", note="DOU, seção 1, p. 1-2, 7 out. 2025 (verificado em fonte secundária). Altera o art. 17 da IN n. 5/2021.")
lei("PL n. 4.752/2025", "Projeto de Lei n. 4.752, de 2025. Institui o Marco Legal da Cibersegurança, cria o Programa Nacional de Segurança e Resiliência Digital e altera a Lei n. 13.756, de 12 de dezembro de 2018", "2025", "2025/09/24", "https://www25.senado.leg.br/web/atividade/materias/-/materia/170613", corpus="PL", au="Brasil. Senado Federal", ty='BILL', note="Em tramitação; discutido, não codificado.")
R.append(dict(TY='ELEC', AU=["Brasil. Gabinete de Segurança Institucional"], TI="Nota de esclarecimento sobre a Instrução Normativa nº 8/2025 e o Acordo de Cooperação Técnica com a Amazon Web Services", PY="2025", UR="https://www.gov.br/gsi/pt-br/centrais-de-conteudo/noticias/2025/nota-de-esclarecimento-sobre-a-instrucao-normativa-no-8-2025-e-o-acordo-de-cooperacao-tecnica-com-a-amazon-web-services", corpus="caso", N1="Existência confirmada; conteúdo não verificado (página exige autenticação)."))
R.append(dict(TY='ELEC', AU=["Brasil. Ministério da Gestão e da Inovação em Serviços Públicos"], TI="Nuvem de Governo", PY="2025", UR="https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/ambiente-tecnologico/nuvem/nuvem-de-governo", corpus="caso", N1="Página sem data; ano atribuído [2025]."))
lei("Lei n. 15.352/2026", "Lei n. 15.352, de 25 de fevereiro de 2026. Transforma cargos no âmbito do Poder Executivo federal; altera a Lei n. 13.709, de 14 de agosto de 2018, para dispor sobre a Agência Nacional de Proteção de Dados (ANPD)", "2026", "2026/02/25", P+"_ato2023-2026/2026/lei/l15352.htm", corpus="LGPD")
lei("Lei n. 15.504/2026", "Lei n. 15.504, de 15 de setembro de 2026. Altera a Lei n. 11.196, de 21 de novembro de 2005, para instituir o Regime Especial de Tributação para Serviços de Datacenter (Redata), e a Lei n. 15.211, de 17 de setembro de 2025", "2026", "2026/09/15", P+"_ato2023-2026/2026/lei/l15504.htm", corpus="15504")
lei("Resolução BCB n. 1/2020", "Resolução BCB n. 1, de 12 de agosto de 2020. Institui o arranjo de pagamentos Pix e aprova o seu Regulamento", "2020", "2020/08/12", "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolução%20BCB&numero=1", corpus="BCB", au="Banco Central do Brasil", note="DOU, seção 1, n. 155, p. 44, 13 ago. 2020.")
lei("Resolução CNDI/MDIC n. 1/2023", "Resolução CNDI/MDIC n. 1, de 6 de julho de 2023. Propõe a nova política industrial, com a finalidade de nortear as ações do Estado Brasileiro em favor do desenvolvimento industrial", "2023", "2023/07/06", "https://www.gov.br/mdic/pt-br/composicao/se/cndi/resolucoes/cndi", corpus="CNDI", au="Conselho Nacional de Desenvolvimento Industrial", note="DOU, seção 1, 19 jul. 2023; republicada em 20 jul. 2023.")

# --- Codificação (Quadro 3) ---
DIM = ["G governança", "K capacidades", "I infraestrutura-nuvem-dados", "T base tecnológica", "P proteção de dados e direitos", "E IA e tecnologias emergentes", "C infraestruturas críticas", "X cooperação internacional"]
LV = {"●": "explícita", "◐": "genérica"}
Q = {  # G K I T P E C X S, trilha, dispositivos
 "LGPD": ("●●◐–●◐–◐", "–", "governo digital e dados", "Arts. 20, 33, 46, 55-A (LGPD); Lei 15.352/2026 cria a Agência e a carreira."),
 "9573": ("●–––––●●", "–", "segurança", "Arts. 1º, 3º, 4º V, 5º, 14."),
 "IN1": ("●●––◐–––", "–", "segurança", "Arts. 9-12, 15 III, 18-22."),
 "BCB": ("●–●–●–◐–", "I", "governo digital e dados", "Art. 3º (participação obrigatória, redação original); art. 46 (SPI operado pelo BCB); art. 89 (segurança e antifraude). Soberania instrumentada sem uso do termo."),
 "10569": ("◐●––––●–", "–", "segurança", "Soberania apenas na contextualização do anexo (seções 1 e 2.4); não codificada. Eixo conscientização e capacitação (obj. 2.2)."),
 "14129": ("◐●●◐●–––", "–", "governo digital e dados", "Arts. 3º XXIII, 7º, 21 IX, 38 I, 39 III, 48."),
 "10748": ("●◐––––◐●", "–", "segurança", "Arts. 11 IV-V, 12 VII."),
 "IN5": ("◐–●–◐–––", "I", "segurança", "IN 8/2025: informação classificada (reservado e secreto) em nuvem privada/comunitária com data centers exclusivamente em território nacional; vedação ao ultrassecreto."),
 "CNDI": ("–––●–◐––", "D", "industrial e tecnológica", "Art. 9º, I (Missão 4: 'soberania digital e tecnológica')."),
 "11856": ("●●–●●–●●", "D", "segurança", "Art. 2º I (soberania nacional), II, III, V, VII; art. 3º; arts. 5º-7º."),
 "14968": ("–––●––––", "D/I", "industrial e tecnológica", "Art. 2º IX (diretriz: soberania tecnológica); art. 3º (Brasil Semicon)."),
 "12198": ("●●●–●–––", "–", "governo digital e dados", "Arts. 3º IX, 5º, 6º I d, 7º."),
 "12308": ("●––◐––––", "D", "governo digital e dados", "Art. 3º IV (objetivo da E-Digital: desenvolvimento socioeconômico soberano)."),
 "PBIA": ("◐●●●–●––", "D/I", "industrial e tecnológica", "Nuvem soberana R$ 1,4 bi; governança R$ 103,25 mi (0,45%)."),
 "12572": ("●●––●–●●", "D", "segurança", "Art. 3º I (soberania nacional); arts. 4º, 5º-6º, 8º VI, 10 V."),
 "12573": ("●●–●◐◐●●", "D", "segurança", "Art. 1º (eixo IV soberania nacional e governança); arts. 5º-6º, 8º, 9º, 10 III, IV e X, 11."),
 "15504": ("––●●–◐––", "–", "industrial e tecnológica", "Arts. 11-A §1º, 11-B §1º; sem requisito de localização de dados."),
}
SL = {"–": None, "D": ["soberania: declarada"], "I": ["soberania: instrumentada"], "D/I": ["soberania: declarada", "soberania: instrumentada"]}

def tags_for(c):
    if c is None: return []
    if c == "revogado": return ["corpus: trajetória (revogado)"]
    if c == "PL": return ["corpus: discutido (em tramitação)"]
    if c == "caso": return ["corpus: caso ilustrativo"]
    codes, s, tr, disp = Q[c]
    t = ["corpus: codificado", "trilha: " + tr]
    for d, v in zip(DIM, codes):
        if v in LV: t.append(f"{d}: {LV[v]}")
    t += SL[s] or ["soberania: ausente"]
    return t

KEEP = ("Castro","Lanzara","Goldoni","Rodrigues","Medeiros","Junqueira","Oliveira","Muara","Klein","Matos","Borba","Gonçalves","Brinkhues","Santos Júnior","Magalhães Santos")
def ini(a):
    if "," not in a or a.split(",")[0] in KEEP: return a
    sur, fn = a.split(",", 1)
    parts = [p for p in fn.replace(".", " ").split() if p]
    return sur + ", " + " ".join(p[0] + "." for p in parts)
def ris(e):
    L = [f"TY  - {e['TY']}"]
    for a in e.get('AU') or []: L.append(f"AU  - {ini(a)}")
    for a in e.get('A2') or []: L.append(f"A2  - {a}")
    L.append(f"TI  - {e['TI']}")
    m = {'T2': 'T2', 'PY': 'PY', 'DA': 'DA', 'VL': 'VL', 'IS': 'IS', 'SP': 'SP', 'ET': 'ET', 'PB': 'PB', 'CY': 'CY', 'M1': 'M1', 'M3': 'M3'}
    for k, tag in m.items():
        v = e.get(k) or (e.get(k.lower()) if k in ('SP',) else None)
        if k == 'SP': v = e.get('SP') or e.get('sp')
        if v: L.append(f"{tag}  - {v}")
    if e.get('DO') or e.get('doi'): L.append(f"DO  - {e.get('DO') or e.get('doi')}")
    if e.get('UR') or e.get('ur'): L.append(f"UR  - {e.get('UR') or e.get('ur')}")
    L.append("LA  - " + ("es" if e.get('LA') == 'es' else "pt" if (re.search(r"[ãçõéáíóúâêô]", e['TI']) or re.search(r"Brasil|Banco Central|Conselho", str(e.get('AU')))) else "en"))
    c = e.get('corpus')
    for t in tags_for(c) + ["artigo: Cibersegurança e soberania digital (RIPPMar)"]:
        L.append(f"KW  - {t}")
    notes = []
    if e.get('N1'): notes.append(e['N1'])
    if c in Q: notes.append("Codificação (Quadro 3) - dispositivos: " + Q[c][3] + " Dupla codificação independente; concordância de 87%; divergências resolvidas por consenso.")
    for n in notes: L.append(f"N1  - {n}")
    L.append("ER  - ")
    return "\n".join(L)

out = "\n\n".join(ris(e) for e in R) + "\n"
open(__import__("pathlib").Path(__file__).parents[1] / "data" / "referencias_codificadas.ris", "w", encoding="utf-8").write(out)
print(len(R), "itens;", sum(1 for e in R if e.get('corpus') in Q), "codificados")
