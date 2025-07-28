[Visão Geral](/README.md) | [Diagrama Entidade Relacionamento](/docs/diagram_er.md) | [Diagrama De Classes](/docs/diagrama_classes.md) | [Fluxo de Requisições](/docs/fluxo_requisicao.md)

---

### URLs (Endpoints Planejados)

##### Convenções Utilizadas

- `{id}`: Representa um identificador único (ex: ID de uma empresa, cliente, etc.).
- `{empresaId}`: Identificador específico de uma empresa.

##### Autorização

Todas as requisições autenticadas devem conter o **Bearer Token (JWT)** no cabeçalho `Authorization`.

---

#### 1. Autenticação e Gestão de Contas de Cliente

Endpoints para que os clientes possam se registrar, fazer login e gerenciar suas contas.

##### `POST /auth/login`

**Descrição**: Autentica um usuário (cliente, funcionário ou administrador) e retorna um token de acesso (JWT).
**Autorização**: Pública.

###### Corpo da Requisição

```json
{
  "email": "usuario@exemplo.com",
  "senha": "senha_do_usuario"
}
```

###### Resposta de Sucesso (200 OK)

```json
{
  "token": "seu_token_jwt_aqui",
  "usuario": {
    "id": 1,
    "nome": "Nome do Usuário",
    "email": "usuario@exemplo.com",
    "tipo": "cliente"
  }
}
```

###### Respostas de Erro:

- `400 Bad Request`: Dados inválidos
- `401 Unauthorized`: Credenciais incorretas

---

##### `POST /clientes/cadastro`

**Descrição**: Cadastra um novo cliente na plataforma.
**Autorização**: Pública.

###### Corpo da Requisição

```json
{
  "nome": "Novo Cliente",
  "cpf": "123.456.789-00",
  "email": "novo.cliente@exemplo.com",
  "telefone": "38999998888",
  "senha": "senha_forte_123"
}
```

###### Resposta de Sucesso (201 Created)

```json
{
  "id": 1,
  "nome": "Novo Cliente",
  "email": "novo.cliente@exemplo.com",
  "pontos": 0
}
```

###### Respostas de Erro:

- `400 Bad Request`: Dados faltando ou inválidos
- `409 Conflict`: Email ou CPF já cadastrado

---

##### `GET /clientes/meu-perfil`

**Descrição**: Retorna os dados do cliente autenticado.
**Autorização**: Cliente Autenticado.

###### Resposta de Sucesso (200 OK)

```json
{
  "id": 1,
  "nome": "Nome do Cliente",
  "cpf": "123.456.789-00",
  "email": "cliente@exemplo.com",
  "telefone": "38999998888",
  "pontos": 1500
}
```

###### Respostas de Erro:

- `401 Unauthorized`

---

##### `PUT /clientes/meu-perfil`

**Descrição**: Atualiza os dados do cliente autenticado.
**Autorização**: Cliente Autenticado.

###### Corpo da Requisição

```json
{
  "nome": "Nome do Cliente Atualizado",
  "telefone": "38988887777",
  "senha_antiga": "senha_atual_123",
  "nova_senha": "nova_senha_forte_456"
}
```

**Resposta de Sucesso (200 OK):** Retorna o perfil atualizado.

###### Respostas de Erro:

- `400 Bad Request`
- `401 Unauthorized` (senha antiga incorreta)

---

##### `DELETE /clientes/meu-perfil`

**Descrição**: Exclui a conta do cliente autenticado.
**Autorização**: Cliente Autenticado.

###### Resposta de Sucesso:

- `204 No Content`

###### Respostas de Erro:

- `401 Unauthorized`

---

#### 2. Administrador da Plataforma

Endpoints exclusivos para o administrador geral do sistema Janu Prime.

##### `POST /admin/empresas`

**Descrição**: Cadastra uma nova empresa e seu superusuário associado. A empresa inicia como "desativada".
**Autorização**: Admin da Plataforma.

###### Corpo da Requisição

```json
{
  "empresa": {
    "nome": "Nova Empresa Parceira",
    "cnpj": "12.345.678/0001-99"
  },
  "super_usuario": {
    "nome": "Admin da Empresa",
    "email": "admin@novaempresa.com",
    "cpf": "987.654.321-00"
  }
}
```

###### Resposta de Sucesso (201 Created):

- Retorna os dados da empresa e do superusuário criado com uma senha temporária.

###### Respostas de Erro:

- `400 Bad Request`
- `403 Forbidden`
- `409 Conflict`: CNPJ, email ou CPF já existem

---

##### `GET /admin/empresas`

**Descrição**: Lista todas as empresas cadastradas na plataforma.
**Autorização**: Admin da Plataforma.

**Query String (opcional)**:

- `?status=ativo`
- `?status=inativo`
- `?page=1&limit=20`

###### Resposta de Sucesso (200 OK)

```json
{
  "metadata": { "total": 50, "page": 1, "limit": 20 },
  "empresas": [
    {
      "id": 1,
      "nome": "Empresa A",
      "cnpj": "11.111.111/0001-11",
      "ativo": true
    }
  ]
}
```

###### Respostas de Erro:

- `403 Forbidden`

---

##### `PATCH /admin/empresas/{id}/status`

**Descrição**: Ativa ou desativa uma empresa e seus superusuários.
**Autorização**: Admin da Plataforma.

###### Corpo da Requisição

```json
{
  "ativo": true
}
```

###### Resposta de Sucesso (200 OK):

- Retorna o objeto da empresa com o novo status.

###### Respostas de Erro:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

---

##### `GET /admin/metricas`

**Descrição**: Retorna métricas gerais da plataforma.
**Autorização**: Admin da Plataforma.

###### Resposta de Sucesso (200 OK)

```json
{
  "total_usuarios": 5230,
  "total_empresas_ativas": 48,
  "total_transacoes_mes": 12450,
  "total_pontos_acumulados": 1500000
}
```

###### Respostas de Erro:

- `403 Forbidden`

---

##### `GET /admin/logs`

**Descrição**: Retorna logs de auditoria da plataforma.
**Autorização**: Admin da Plataforma.

**Query String (opcional)**:

- `?tipo=operacional`
- `?data_inicio=AAAA-MM-DD`

###### Resposta de Sucesso (200 OK):

- Lista de logs.

###### Respostas de Erro:

- `403 Forbidden`

---

Claro! Aqui está a continuação da documentação técnica formatada em **Markdown**, seguindo o mesmo padrão:

---

#### 3. Estabelecimentos (Empresas)

Endpoints para consulta de informações públicas e gerenciamento do perfil pela própria empresa.

##### `GET /estabelecimentos`

**Descrição**: Lista todos os estabelecimentos parceiros ativos para os clientes.
**Autorização**: Pública.

**Query String (opcional)**:

- `?busca=pizzaria`
- `?ordenar_por=nome_asc`
- `?page=1&limit=10`

###### Resposta de Sucesso (200 OK):

- Lista paginada de estabelecimentos.

---

##### `GET /estabelecimentos/{id}`

**Descrição**: Busca os detalhes de um estabelecimento específico.
**Autorização**: Pública.

###### Resposta de Sucesso (200 OK)

```json
{
  "id": 1,
  "nome": "Pizzaria Sabor Local",
  "endereco": "Rua Principal, 123",
  "telefone": "3833334444",
  "descricao": "A melhor pizza da cidade!",
  "logotipo": "url_do_logo.jpg",
  "horario_funcionamento": "Ter-Dom: 18h-23h"
}
```

###### Respostas de Erro:

- `404 Not Found`

---

##### `GET /empresas/meu-perfil`

**Descrição**: Retorna os dados completos do estabelecimento do administrador ou funcionário autenticado.
**Autorização**: Admin da Empresa / Funcionário.

###### Resposta de Sucesso (200 OK):

- Similar ao `GET /estabelecimentos/{id}`, mas com mais campos (CNPJ, etc.).

###### Respostas de Erro:

- `401 Unauthorized`
- `403 Forbidden`

---

##### `PUT /empresas/meu-perfil`

**Descrição**: Atualiza o perfil do estabelecimento.
**Autorização**: Admin da Empresa.

###### Corpo da Requisição

```json
{
  "nome": "Novo Nome da Empresa",
  "endereco": "Novo Endereço",
  "descricao": "Nova descrição",
  "logotipo": "nova_url_logo.jpg"
}
```

###### Resposta de Sucesso (200 OK):

- Retorna o perfil atualizado.

###### Respostas de Erro:

- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`

---

#### 4. Gestão Interna da Empresa (Admins e Funcionários)

Endpoints para o gerenciamento de funcionários, produtos, anúncios e transações.

##### `POST /empresas/funcionarios`

**Descrição**: Cadastra um novo funcionário vinculado ao estabelecimento.
**Autorização**: Admin da Empresa.

###### Corpo da Requisição

```json
{
  "nome": "Novo Funcionário",
  "email": "funcionario@empresa.com",
  "cpf": "111.222.333-44"
}
```

###### Resposta de Sucesso (201 Created):

- Retorna os dados do funcionário criado com uma senha temporária.

###### Respostas de Erro:

- `400 Bad Request`
- `403 Forbidden`
- `409 Conflict`

---

##### `POST /empresas/catalogo`

**Descrição**: Cadastra um novo produto/recompensa no catálogo da empresa.
**Autorização**: Funcionário / Admin da Empresa.

###### Corpo da Requisição

```json
{
  "nome": "Pizza Grande",
  "descricao": "Qualquer sabor do cardápio",
  "imagem": "url_da_imagem.jpg",
  "pontos": 2000
}
```

###### Resposta de Sucesso (201 Created):

- Retorna o produto criado.

###### Respostas de Erro:

- `400 Bad Request`
- `403 Forbidden`

---

##### `PUT /empresas/catalogo/{produtoId}`

**Descrição**: Atualiza um produto do catálogo.
**Autorização**: Funcionário / Admin da Empresa.

###### Corpo da Requisição

```json
{
  "nome": "Pizza Grande Atualizada",
  "descricao": "Novo sabor",
  "pontos": 2500
}
```

###### Resposta de Sucesso (200 OK):

- Retorna o produto atualizado.

###### Respostas de Erro:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

---

##### `DELETE /empresas/catalogo/{produtoId}`

**Descrição**: Remove um produto do catálogo.
**Autorização**: Funcionário / Admin da Empresa.

###### Resposta de Sucesso:

- `204 No Content`

###### Respostas de Erro:

- `403 Forbidden`
- `404 Not Found`

---

##### `PATCH /tickets/credito/{ticketId}/validar`

**Descrição**: Aprova ou recusa um ticket de crédito (envio de nota fiscal).
**Autorização**: Funcionário / Admin da Empresa.

###### Corpo da Requisição

```json
{
  "status": "aprovado",
  "observacao": "Nota fiscal ilegível."
}
```

###### Resposta de Sucesso (200 OK):

- Retorna o ticket atualizado.

###### Respostas de Erro:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

---

##### `PATCH /tickets/debito/{ticketId}/validar`

**Descrição**: Confirma um resgate de pontos (débito) apresentado pelo cliente.
**Autorização**: Funcionário / Admin da Empresa.

###### Corpo da Requisição

```json
{
  "status": "concluido"
}
```

###### Resposta de Sucesso (200 OK):

- Retorna o ticket atualizado.

###### Respostas de Erro:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

---

Aqui está a continuação da sua documentação de **endpoints** em **Markdown** com formatação consistente com as seções anteriores:

---

#### 5. Transações e Pontos

Endpoints para o cliente acumular, resgatar e consultar seus pontos.

##### `POST /tickets/credito`

**Descrição**: Cliente envia dados de consumo para gerar pontos (anexando nota fiscal).
**Autorização**: Cliente Autenticado.

###### Corpo da Requisição (`multipart/form-data`)

- `estabelecimento_id`: ID do estabelecimento
- `numero_nota`: Número da nota fiscal
- `valor_nota`: Valor da nota
- `data_emissao`: Data da nota
- `imagem_nota`: Arquivo da nota fiscal (imagem)

###### Resposta de Sucesso (202 Accepted):

- O ticket foi aceito para processamento e está com status `"pendente"`.

###### Respostas de Erro:

- `400 Bad Request`
- `401 Unauthorized`

---

##### `POST /tickets/debito`

**Descrição**: Cliente solicita o resgate de pontos por um produto.
**Autorização**: Cliente Autenticado.

###### Corpo da Requisição

```json
{
  "produto_id": 123
}
```

###### Resposta de Sucesso (201 Created)

```json
{
  "id": 987,
  "status": "pendente",
  "produto": { "nome": "Pizza Grande" },
  "pontos": 2000,
  "codigo_resgate": "ABC-123"
}
```

###### Respostas de Erro:

- `400 Bad Request`: Pontos insuficientes
- `401 Unauthorized`
- `404 Not Found`: Produto não existe

---

##### `GET /clientes/extrato`

**Descrição**: Consulta o extrato completo de transações de pontos do cliente.
**Autorização**: Cliente Autenticado.

**Query String (opcional)**

- `?tipo=credito`
- `?periodo=ultimos_30_dias`
- `?estabelecimento_id=1`

###### Resposta de Sucesso (200 OK):

- Lista de transações com data, tipo, valor, status, etc.

###### Respostas de Erro:

- `401 Unauthorized`

---

##### `GET /clientes/saldo`

**Descrição**: Retorna o saldo atual de pontos do cliente e avisos de expiração.
**Autorização**: Cliente Autenticado.

###### Resposta de Sucesso (200 OK)

```json
{
  "saldo_total": 1500,
  "pontos_a_expirar": [
    {
      "pontos": 100,
      "data_expiracao": "2025-08-27"
    }
  ]
}
```

###### Respostas de Erro:

- `401 Unauthorized`

---

#### 6. Catálogo e Avaliações

Endpoints para consulta do catálogo de recompensas e para os clientes avaliarem os serviços.

##### `GET /estabelecimentos/{id}/catalogo`

**Descrição**: Lista os produtos/recompensas de um estabelecimento específico.
**Autorização**: Pública.

**Query String (opcional)**

- `?filtro_pontos_max=2000`
- `?busca=pizza`

###### Resposta de Sucesso (200 OK):

- Lista de produtos com nome, imagem, pontos, etc.

###### Respostas de Erro:

- `404 Not Found`

---

##### `POST /estabelecimentos/{id}/avaliacoes`

**Descrição**: Cliente avalia um estabelecimento parceiro.
**Autorização**: Cliente Autenticado.

###### Corpo da Requisição

```json
{
  "estrelas": 5,
  "comentario": "Atendimento excelente!"
}
```

###### Resposta de Sucesso (201 Created):

- Retorna a avaliação criada.

###### Respostas de Erro:

- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`: Cliente não pode avaliar sem ter consumido

---

##### `POST /plataforma/avaliacoes`

**Descrição**: Cliente avalia a plataforma Janu Prime.
**Autorização**: Cliente Autenticado.

###### Corpo da Requisição

```json
{
  "estrelas": 5,
  "comentario": "O aplicativo é muito fácil de usar."
}
```

###### Resposta de Sucesso (201 Created)

###### Respostas de Erro:

- `400 Bad Request`
- `401 Unauthorized`
