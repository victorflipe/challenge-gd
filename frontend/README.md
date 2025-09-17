# Concepção do Projeto

Após a criação do backend minimamente funcional, partimos para a criação do frontend.

## Decisões Técnicas

- **Vite + React**: Proporciona uma ambiente de desenvolvimento rápido com builds otimizados utilizando pouca configuração
- **Tailwind CSS**: Acelerar e facilitar a estilização dos itens
- **CSS Modules**: Facilita a manutenção e garante estilos únicos para cada componente
- **Context API**: Gerenciar o estado global de modo mais simples
- **Arquitetura Modular**: A aplicação foi dividida em pastas como assets, components, hooks, styles e uitls

## Organização do Código
```bash
src/
├─ assets/ # Imagens e ícones
├─ components/ # Componentes reutilizáveis 
├─ hooks/ # Custom Hooks
├─ styles/ # Estilos globais
├─ utils/ # Funções utilitárias
├─ api.js # Integração com APIs
├─ App.jsx # Raiz da aplicação
├─ main.jsx 
└─ UserContext.jsx #Gerenciamento de estado global
```

## Passos para construção

### Passo 1. Estruturação mínima e teste de funcionamento

Foi criado o seguinte:
 - hooks: Funções customizadas
 - api.js: Centraliza e formata o modelo das requisições
 - utils: Formatação das datas
 - Criação dos componentes **Header** e **Home** para configurar os estilos como cores, fontes e alinhamento

Na pasta components, foi criado uma pasta por Entidade da aplicação.

### Passo 2. Tela para Cadastro de Artigo:

- Criação dos Componentes:
    - Input e TextArea
    - Criação de CustomHooks

- Criação de Form para ser usado tanto na Edição quanto na Criação de Artigo (componentes ArticleEdit e ArticleNew)

- Criação do ArticleHeader para ser chamado nos componentes do Article

### Passo 3. Listagem de Artigos

- Criação dos Componentes:
 - ArticlList: Listando todos os artigos
 - ArticleRead: Para leitura do artigo
 - Estruturação do componente ListTags

### Passo 4. Comentários

- Criação do componente de Comentário e inclusão no ArticleRead
- Ajuste nas consultas à API


### Passo 5. Filtros 
- Ajuste das funções para filtro ao inserir o Title do Artigo e ao selecionar Tags
- Inclusão de Paginação

### Passo 6. Modal 
- Inclusão do Modal para exibir mensagem de sucesso ou erro

### Passo 7. Proteção de rotas e Login

Nesse passo, foi feito a validação do login, armazenando o token e implementando proteção nas rotas.

### Passo 8. Ajustes para mobile

Realização de ajustes nas classes, alterando tamanho de fontes, renderização de itens, etc

### Passo 9. Criação do Container

Como último passo, foi criado o container do frotend para ser executado diretamente no Docker, assim como o backend e banco de dados.