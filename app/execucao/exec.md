<!-- FAZER ARQUVO .ENV -->

#### **Backend**

```bash
docker compose build --no-cache
```

```bash
docker compose up -d
```

```bash
docker compose exec app python manage.py migrate
```

#### **Frontend Web**

```bash
npm install
```

```bash
npm run dev
```

Fazer a build da versão de produção:

```bash
npm run build
```

Rodar o preview da versão de produção

```bash
npm run preview
```
