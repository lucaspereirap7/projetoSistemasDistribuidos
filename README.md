# 🏋️‍♂️ Fitness Advisor - Sistema de Consultoria Fitness com IA

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Um sistema inteligente de consultoria fitness que utiliza inteligência artificial para criar planos personalizados de treino e nutrição. O projeto inclui uma **interface web intuitiva** com formulário para facilitar a interação do usuário, além de uma API robusta para integração com outros sistemas.

## 🎯 Funcionalidades

### 🖥️ Interface Web
- **Formulário Interativo**: Interface amigável em HTML/CSS/JavaScript para inserção de dados
- **Experiência do Usuário**: Design responsivo e intuitivo para todos os dispositivos
- **Validação em Tempo Real**: Feedback instantâneo durante o preenchimento
- **Resultados Formatados**: Exibição clara e organizada dos planos gerados

### 🤖 Sistema de IA
- **Análise de Perfil Fitness**: Avalia seu perfil completo considerando idade, peso, altura, gênero e nível de atividade
- **Planos de Treino Personalizados**: Cria rotinas de exercícios adaptadas aos seus objetivos e disponibilidade
- **Planos Alimentares Balanceados**: Gera dietas personalizadas com base nas suas necessidades nutricionais
- **Cálculo de Necessidades Calóricas**: Determina automaticamente sua demanda calórica diária
- **Frases Motivacionais**: Oferece motivação personalizada para manter você focado nos seus objetivos

## 🚀 Tecnologias Utilizadas

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e rápido para construção de APIs
- **[Pydantic AI](https://ai.pydantic.dev/)** - Framework para desenvolvimento de aplicações com IA
- **Python 3.8+** - Linguagem de programação principal

### Frontend
- **HTML5** - Estrutura da interface web
- **CSS3** - Estilização responsiva e moderna
- **JavaScript** - Interatividade e comunicação com a API
- **Design Responsivo** - Compatível com desktop, tablet e mobile



## 📋 Pré-requisitos

- **Python 3.8+** instalado
- **pip** (gerenciador de pacotes do Python)
- **Navegador web** moderno (Chrome, Firefox, Safari, Edge)

## 🛠️ Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/joaopaulodaree/trabalho-pratico-sd.git
cd trabalho-pratico-sd
git checkout fitness-advisor
```

### 2. Instale as dependências Python
```bash
pip install -r requirements.txt
```

### 3. Execute o servidor
```bash
uvicorn main:app --reload
```

### 4. Acesse a aplicação
- **Interface Web**: Disponível através do Live Server
- **Documentação da API**: [http://localhost:8000/docs](http://localhost:8000/docs)

## 📖 Como Usar

### 🖥️ Interface Web (Recomendado)

1. **Acesse o formulário**: Abra o Live Server em sua IDE
2. **Preencha seus dados**:
   - Idade
   - Peso em kg
   - Altura em cm
   - Gênero (Masculino/Feminino)
   - Nível de atividade física
   - Objetivo fitness
   - Dias de treino por semana
3. **Clique em "Gerar Plano"**
4. **Visualize seus resultados**: O sistema exibirá seu plano personalizado na mesma página

### 🔧 API REST (Para Desenvolvedores)

#### Endpoint Principal: `/analyze`

**POST** `/analyze`

```json
{
    "age": 21,
    "weight": 81,
    "height": 183,
    "gender": "male",
    "activity_level": "sedentary",
    "fitness_goal": "muscle_gain",
    "dietary_restrictions": [
        "lactose intolerant"
    ],
    "injuries": [],
    "preferred_workout_time": "morning",
    "available_equipment": [
        "all"
    ],
    "workout_days_per_week": 5
}
```

## 🎨 Funcionalidades da Interface

### Validação de Formulário
- **Validação em tempo real** dos campos
- **Mensagens de erro** claras e específicas
- **Indicadores visuais** para campos obrigatórios

### Design Responsivo
- **Layout adaptável** para desktop, tablet e mobile
- **Tipografia otimizada** para diferentes tamanhos de tela
- **Experiência consistente** em todos os dispositivos

### Interações Inteligentes
- **Loading states** durante o processamento
- **Animações suaves** para melhor UX
- **Feedback visual** em todas as ações

## 🚀 Funcionalidades Avançadas

### Customização de Planos
- **Preferências alimentares**: Vegetariano, vegano, sem glúten
- **Restrições físicas**: Lesões físicas
- **Equipamentos disponíveis**: Halteres, elasticos, etc.

### Exportação de Dados
- **PDF**: Planos formatados para impressão
- **JSON**: Dados estruturados para outras aplicações

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Veja como você pode ajudar:

### Para Desenvolvedores Frontend
1. Melhore o design da interface
2. Adicione novas funcionalidades JavaScript
3. Otimize a responsividade
4. Implemente novas animações

### Para Desenvolvedores Backend
1. Otimize os algoritmos de IA
2. Adicione novos endpoints
3. Melhore a performance
4. Implemente testes automatizados

### Processo de Contribuição
1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 🐛 Solução de Problemas

### Interface não carrega
- Verifique se o servidor está rodando corretamente pelo Live Server
- Confirme que todos os arquivos estáticos estão no lugar correto
- Verifique o console do navegador para erros JavaScript

### Erro na geração de planos
- Verifique os logs do servidor para mensagens de erro
- Teste a API diretamente em `/docs`

### Problemas de compatibilidade
- Use navegadores modernos (Chrome 80+, Firefox 75+, Safari 13+)
- Certifique-se de ter JavaScript habilitado
- Limpe o cache do navegador se necessário

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🌟 Reconhecimentos

- **Ollama** - Por tornar a IA acessível localmente
- **FastAPI** - Framework incrível para APIs Python
- **Pydantic AI** - Simplificando o desenvolvimento com IA
- **Comunidade Open Source** - Por inspiração e suporte

## 🎯 Roadmap

### Versão 2.0 (Próxima)
- [ ] 🔐 Sistema de autenticação de usuários
- [ ] 💾 Banco de dados para histórico de planos
- [ ] 📊 Dashboard com métricas de progresso
- [ ] 🔔 Sistema de notificações e lembretes

### Versão 2.1
- [ ] 📱 Aplicativo mobile (React Native)
- [ ] 🏃‍♂️ Integração com dispositivos wearables
- [ ] 👥 Sistema de comunidade e gamificação
- [ ] 🌍 Suporte a múltiplos idiomas

### Versão 3.0
- [ ] 🤖 IA ainda mais avançada com deep learning
- [ ] 🎥 Vídeos de exercícios integrados
- [ ] 🍽️ Calculadora de calorias com fotos
- [ ] 👨‍⚕️ Integração com profissionais de saúde

## 📊 Estatísticas

- **Linguagem principal**: Python (70%), JavaScript (20%), HTML/CSS (10%)
- **Linhas de código**: ~500 (estimativa)
- **Funcionalidades**: 15+ recursos implementados
- **Compatibilidade**: 95% dos navegadores modernos

# 5. Validação do Problema

## 5.1 Introdução

A busca por saúde, qualidade de vida e condicionamento físico é um fenômeno crescente em escala global. Apesar desse movimento, as taxas de sedentarismo permanecem elevadas, e mesmo indivíduos fisicamente ativos frequentemente relatam dificuldades em aderir a rotinas de treino e dietas de forma consistente e eficaz (World Health Organization [WHO], 2022).

O desenvolvimento de soluções digitais que combinem **Inteligência Artificial (IA)** com princípios da **prescrição personalizada de exercício físico e nutrição** representa uma inovação promissora para mitigar esse cenário. Entretanto, para justificar a relevância da proposta, é imprescindível compreender, de forma fundamentada, a **magnitude do problema**, suas **causas estruturais** e as **evidências científicas** que sustentam a abordagem adotada.

---

## 5.2 Evidências da Relevância do Problema

### 5.2.1 Prevalência do Sedentarismo

De acordo com o relatório **Global Status Report on Physical Activity 2022** da Organização Mundial da Saúde, aproximadamente **28% da população mundial adulta não atinge os níveis mínimos recomendados de atividade física** (WHO, 2022). No Brasil, estima-se que 47% da população seja insuficientemente ativa (Guthold et al., 2018).  

O sedentarismo está associado a doenças crônicas não transmissíveis, como diabetes tipo 2, obesidade, doenças cardiovasculares e depressão (Lee et al., 2012). A **carga econômica global do sedentarismo** ultrapassa US$ 54 bilhões em custos diretos de saúde e produtividade perdida (Ding et al., 2016).

---

### 5.2.2 Falhas na Adoção de Planos de Treino e Nutrição

Estudos longitudinais demonstram que **até 50% dos iniciantes em programas de exercícios abandonam suas rotinas nos primeiros seis meses**, principalmente por falta de suporte personalizado, monitoramento e motivação (Annesi, 2003; Dishman et al., 1981). No âmbito nutricional, a **adesão a planos alimentares personalizados** também é baixa, especialmente quando estes não consideram restrições culturais, preferências individuais e suporte comportamental (Teixeira et al., 2015).

Além disso, o conhecimento insuficiente sobre princípios de treinamento e nutrição faz com que muitas pessoas sigam **planos genéricos**, retirados de fontes não confiáveis, o que aumenta o risco de lesões, frustrações e dietas restritivas ineficazes (Schoenfeld, 2016; Slater & Phillips, 2011).

---

### 5.2.3 Limitações de Acesso a Profissionais Especializados

Segundo dados do **American Council on Exercise (ACE)**, o custo médio de um personal trainer nos EUA varia de US$ 50 a US$ 100 por hora. Na América Latina, apesar de valores mais baixos, a desigualdade socioeconômica limita o acesso para grande parte da população (Teixeira et al., 2015). Além disso, a procura por **nutricionistas** enfrenta barreiras culturais e econômicas semelhantes.

Esses fatores evidenciam uma **lacuna de mercado** para soluções que democratizem o acesso a informações confiáveis, **baseadas em evidências**, de forma **escalável e acessível**.

---

## 5.3 Natureza Multidimensional da Dor

A “dor” enfrentada pelo público-alvo é **multidimensional**, envolvendo fatores:

- **Fisiológicos:** planos inadequados podem causar overtraining, lesões e deficiências nutricionais (Kraemer & Ratamess, 2004).
- **Psicológicos:** falta de motivação, ausência de reforço positivo e suporte comportamental afetam a adesão (Ryan & Deci, 2000).
- **Logísticos e Financeiros:** indisponibilidade de tempo para deslocamentos, custos de academia, consultas e falta de infraestrutura adequada.
- **Educacionais:** dificuldade de interpretar recomendações técnicas, volume excessivo de informações contraditórias na internet (Nutbeam, 2000).

---

## 5.4 Fundamentação da Solução Proposta

A utilização de **IA** como estratégia de apoio personalizado é respaldada por evidências robustas. Revisões sistemáticas recentes demonstram que sistemas digitais de suporte à decisão podem melhorar significativamente a **adesão a programas de atividade física**, resultando em **melhores desfechos de saúde** (Wang et al., 2021).

A **prescrição automatizada** de exercícios, quando baseada em diretrizes consolidadas, como as do **American College of Sports Medicine (ACSM)**, pode alcançar níveis de segurança e eficácia comparáveis à orientação presencial, desde que seja adaptativa, personalizada e incorporada a princípios de mudança comportamental (Garber et al., 2011).

Além disso, há crescente evidência de que **elementos motivacionais**, como **mensagens de incentivo personalizadas**, podem aumentar a persistência em programas de exercício (Michie et al., 2009). A incorporação de um **coach virtual** que gera frases motivacionais adaptadas ao perfil do usuário alinha-se a modelos de autoconcordância e motivação intrínseca (Ryan & Deci, 2000).

---

## 5.5 Impacto Potencial

Combinando **personalização baseada em dados**, **baixo custo marginal**, **acesso instantâneo** e **motivação contínua**, a solução proposta tem potencial para:

1. **Reduzir barreiras de acesso** a recomendações de treino e dieta de qualidade.
2. **Minimizar o abandono precoce** de programas de atividade física e nutrição.
3. **Promover mudanças comportamentais sustentáveis**, impactando positivamente indicadores de saúde pública.
4. **Contribuir para redução de custos** do sistema de saúde, por meio da prevenção de doenças crônicas relacionadas ao sedentarismo e má alimentação.

---

## 📚 Referências

- Annesi, J. J. (2003). Effects of a cognitive behavioral treatment package on exercise attendance and drop out in fitness centers. *European Journal of Sport Science*, 3(2), 1–16.
- Dishman, R. K. (1981). The problem of exercise adherence: Fighting sloth in nations with market economies. *Quest*, 33(3), 279–294.
- Ding, D., Lawson, K. D., Kolbe-Alexander, T. L., Finkelstein, E. A., Katzmarzyk, P. T., van Mechelen, W., & Pratt, M. (2016). The economic burden of physical inactivity: a global analysis of major non-communicable diseases. *The Lancet*, 388(10051), 1311–1324.
- Garber, C. E., Blissmer, B., Deschenes, M. R., Franklin, B. A., Lamonte, M. J., Lee, I. M., ... & Swain, D. P. (2011). Quantity and Quality of Exercise for Developing and Maintaining Cardiorespiratory, Musculoskeletal, and Neuromotor Fitness in Apparently Healthy Adults: Guidance for Prescribing Exercise. *Medicine & Science in Sports & Exercise*, 43(7), 1334–1359.
- Guthold, R., Stevens, G. A., Riley, L. M., & Bull, F. C. (2018). Worldwide trends in insufficient physical activity from 2001 to 2016: a pooled analysis of 358 population-based surveys with 1·9 million participants. *The Lancet Global Health*, 6(10), e1077–e1086.
- Kraemer, W. J., & Ratamess, N. A. (2004). Fundamentals of resistance training: progression and exercise prescription. *Medicine & Science in Sports & Exercise*, 36(4), 674–688.
- Lee, I. M., Shiroma, E. J., Lobelo, F., Puska, P., Blair, S. N., & Katzmarzyk, P. T. (2012). Effect of physical inactivity on major non-communicable diseases worldwide: an analysis of burden of disease and life expectancy. *The Lancet*, 380(9838), 219–229.
- Michie, S., Abraham, C., Whittington, C., McAteer, J., & Gupta, S. (2009). Effective techniques in healthy eating and physical activity interventions: a meta-regression. *Health Psychology*, 28(6), 690–701.
- Nutbeam, D. (2000). Health literacy as a public health goal: a challenge for contemporary health education and communication strategies into the 21st century. *Health Promotion International*, 15(3), 259–267.
- Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist*, 55(1), 68–78.
- Schoenfeld, B. J. (2016). Science and Development of Muscle Hypertrophy. Human Kinetics.
- Slater, G., & Phillips, S. M. (2011). Nutrition guidelines for strength sports: sprinting, weightlifting, throwing events, and bodybuilding. *Journal of Sports Sciences*, 29(sup1), S67–S77.
- Teixeira, P. J., Carraca, E. V., Markland, D., Silva, M. N., & Ryan, R. M. (2012). Exercise, physical activity, and self-determination theory: A systematic review. *International Journal of Behavioral Nutrition and Physical Activity*, 9(1), 78.
- Wang, Y., Xue, H., Huang, Y., & Huang, L. (2021). A Systematic Review of Application and Effectiveness of mHealth Interventions for Obesity and Diabetes Treatment and Self-Management. *Advances in Nutrition*, 12(6), 2001–2017.
- World Health Organization (2022). *Global status report on physical activity 2022*. Geneva: WHO.


---

<div align="center">

**⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório! ⭐**

*Desenvolvido por Iago Carvalho Souto, João Augusto Dias Neto, João Paulo Daré, Lucas de Oliveira Pereira e Renan Augusto da Silva*

</div>
