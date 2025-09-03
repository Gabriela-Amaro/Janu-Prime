[Visão Geral](/README.md) | [Diagrama Entidade Relacionamento](/docs/diagram_er.md) | [Diagrama De Classes](/docs/diagrama_classes.md) | [Fluxo de Requisições](/docs/fluxo_requisicao.md) | [Endpoints](/docs/endpoints.md)

---

# Definição detalhada das funcionalidades da plataforma

## Requisitos Funcionais (RF)

### RF1. Administrador do Sistema

#### RF1.1. Cadastrar novas empresas

* Cadastra empresas inicialmente **desativadas**, com um **superusuário** (administrador da empresa) associado.
* Conta do superusuário criada com login genérico que deve ser alterado no **primeiro acesso**.

#### RF1.2. Gerenciar empresas e superusuários

* Listar empresas e superusuários.
* Ativar/desativar contas de empresas e superusuários.

#### RF1.3. Visualizar métricas da plataforma

* Acessar dashboards contendo:

  * Número de usuários cadastrados.
  * Total de transações realizadas.
  * Pontos acumulados na plataforma.
  * Avaliações de estabelecimentos e da plataforma.

#### RF1.4. Auditoria e logs

* Acesso a registros de atividades **administrativas** e **operacionais** do sistema.

---

### RF2. Administrador (superusuário) de cada empresa

#### RF2.1. Cadastrar e gerenciar funcionários

* Cadastro de usuários vinculados ao estabelecimento com login genérico.
* Troca de senha obrigatória no primeiro acesso.

#### RF2.2. Gerenciar perfil do estabelecimento

* Atualizar dados do estabelecimento:

  * Nome, endereço, telefone, descrição.
  * Logotipo, CNPJ, imagens.
  * Horário de funcionamento.

#### RF2.3. Acompanhar métricas do estabelecimento

* Visualização de:

  * Volume de transações.
  * Produtos/serviços mais resgatados.
  * Avaliações dos clientes.

#### RF2.4. Auditoria e logs

* Acesso a registros de atividades **administrativas** e **operacionais** do estabelecimento.

#### Demais funcionalidades comum aos funcionários

---

### RF3. Funcionários das empresas parceiras

#### RF3.1. Gerenciar tickets de crédito

* Confirmar ou recusar pedidos de crédito de pontos mediante **análise de nota fiscal**.

#### RF3.2. Gerenciar tickets de débito (resgate)

* Validar ou recusar uso de pontos em resgates de clientes.

#### RF3.3. Gerenciar catálogo de produtos e serviços

* Cadastrar, editar e remover itens disponíveis para troca por pontos.

#### RF3.4. Gerenciar anúncios

* Cadastrar banners promocionais com data de expiração.

#### RF3.5. Visualizar feedbacks

* Acesso às avaliações feitas pelos clientes sobre produtos/serviços e atendimento.

#### RF3.5. Histórico de transações

* Consulta de todas as operações de crédito e débito de pontos realizadas por clientes.

---

### RF4. Cliente (Consumidor)

#### RF4.1. Cadastro e acesso

* Cadastro: nome, CPF, e-mail, telefone e senha.
* Login com e-mail e senha.
* Recuperação de senha (opcional).

#### RF4.2. Gerenciamento de conta

* Edição de dados pessoais.
* Exclusão de conta.

#### RF4.3. Consulta de estabelecimentos

* Lista de comércios participantes com **filtros** e **ordenadores** (nome, localização, avaliação).

#### RF4.4. Resgate de pontos (débito)

* Solicitar resgate de recompensa e acompanhar status (pendente, aprovado, recusado, cancelado).

#### RF4.5. Acúmulo de pontos (crédito)

* Envio de dados de consumo:

  * Anexar imagem da nota fiscal.
  * Informar número, valor e data de emissão.
* Acompanhamento de status de validação.

#### RF4.6. Extrato de pontos (histórico)

* Consulta de todas as transações de crédito e débito:

  * Data, tipo, valor em pontos, descrição, status e observações.
* Filtros por período, tipo de operação e estabelecimento.

#### RF4.7. Saldo atual de pontos

* Exibição do total disponível.
* Avisos de pontos que estão prestes a expirar.

#### RF4.8. Catálogo de recompensas

* Listagem de produtos/serviços por estabelecimento.
* Filtros por valor em pontos ou nome.

#### RF4.9. Avaliações

* Avaliar estabelecimentos e a plataforma com estrelas e comentário.
* Histórico de avaliações realizadas.

#### RF4.10. Notificações (MVP opcional)

* Alertas sobre mudanças no status de tickets, novidades no catálogo, promoções e expiração de pontos.

---

## Requisitos Não Funcionais (RNF)

### RNF1. Usabilidade

* Interface intuitiva e acessível para usuários com diferentes níveis de letramento digital.

### RNF2. Desempenho

* Tempo de resposta máximo de **2 segundos** para ações críticas (login, pontuação, resgate).

### RNF3. Segurança

* Comunicação via **HTTPS**.
* Armazenamento seguro de senhas (hash).
* Autenticação por tokens JWT.
* Proteção contra XSS, CSRF e SQL Injection.
* Política de senhas fortes.

### RNF4. Escalabilidade

* Arquitetura preparada para aumento de usuários e estabelecimentos, com possibilidade de migração para infraestrutura mais robusta.

### RNF5. Compatibilidade

* Aplicação responsiva para **Android**, **iOS** e navegadores modernos.

### RNF6. Confiabilidade e Disponibilidade

* Disponibilidade mínima de **99%**.
* Mecanismos de backup automático e recuperação de desastres.

### RNF7. Manutenibilidade

* Código e arquitetura seguindo padrões que facilitem manutenção e evolução futura.

