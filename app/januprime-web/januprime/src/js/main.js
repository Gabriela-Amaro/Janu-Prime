import "bootstrap/dist/css/bootstrap.min.css";

import * as bootstrap from "bootstrap";

document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("tickets-home-container");
  const apiUrl = "https://jsonplaceholder.typicode.com/users"; // Usando a API de teste

  // Função para buscar e exibir os produtos
  function carregarProdutos() {
    fetch(apiUrl)
      .then((response) => {
        // Se a resposta não for OK (ex: erro 404, 500), lança um erro
        if (!response.ok) {
          throw new Error(`Erro na rede: ${response.statusText}`);
        }
        return response.json();
      })
      .then((produtos) => {
        // Limpa a mensagem "Carregando..."
        container.innerHTML = "";

        // Se não vier produtos, exibe uma mensagem
        if (produtos.length === 0) {
          container.innerHTML = "<p>Nenhum produto encontrado.</p>";
          return;
        }

        // Para cada produto na lista, cria um card do Bootstrap
        produtos.forEach((produto) => {
          const cardHtml = `
            <div class="col-6" style="margin-top: 2rem; margin-bottom: 2rem;">
              <div class="card" style="width: 100%;">
                <div class="card-body">
                  <h5 class="card-title">Ticket Débito</h5>
                  <h6 class="card-subtitle mb-2 text-body-secondary">${produto.name}</h6>
                  <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card’s content.</p>
                  <div class="d-grid mx-auto">
                    <button class="btn btn-primary" type="button">Visualizar</button>
                  </div>
                </div>
              </div>
            </div>
          `;
          // Adiciona o HTML do card ao container
          container.innerHTML += cardHtml;
        });
      })
      .catch((error) => {
        console.error("Falha ao buscar produtos:", error);
        // Exibe uma mensagem de erro para o usuário
        container.innerHTML =
          '<p class="text-danger">Não foi possível carregar os produtos. Tente novamente mais tarde.</p>';
      });
  }

  // Chama a função para iniciar o processo
  carregarProdutos();
});
