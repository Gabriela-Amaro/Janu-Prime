// Sistema de navegação
export function showPage(pageName) {
  const content = document.getElementById('page-content');
  
  // Remove classe ativa de todos os links
  document.querySelectorAll('.nav-link').forEach(link => {
    link.classList.remove('active');
  });
  
  // Remove classe ativa de todos os dropdown items
  document.querySelectorAll('.dropdown-item').forEach(item => {
    item.classList.remove('active');
  });
  
  // Adiciona classe ativa ao link atual
  const activeLink = document.querySelector(`[onclick="showPage('${pageName}')"]`);
  if (activeLink) {
    activeLink.classList.add('active');
  }
  
  // Adiciona classe ativa ao dropdown item correspondente
  const activeDropdownItem = document.querySelector(`[onclick="showPage('${pageName}')"].dropdown-item`);
  if (activeDropdownItem) {
    activeDropdownItem.classList.add('active');
  }
  
  // Carrega o conteúdo da página
  content.innerHTML = getPageContent(pageName);
  content.classList.add('fade-in-up');
  
  // Fecha o offcanvas se estiver aberto
  const offcanvas = bootstrap.Offcanvas.getInstance(document.getElementById('offcanvasNavbar'));
  if (offcanvas) {
    offcanvas.hide();
  }
}

// Gera o conteúdo das páginas
function getPageContent(pageName) {
  switch (pageName) {
    case 'dashboard':
      return getDashboardContent();
    case 'perfil':
      return getPerfilContent();
    case 'catalogo':
      return getCatalogoContent();
    case 'anuncios':
      return getAnunciosContent();
    case 'transacoes':
      return getTransacoesContent();
    case 'funcionarios':
      return getFuncionariosContent();
    case 'metricas':
      return getMetricasContent();
    case 'auditoria':
      return getAuditoriaContent();
    default:
      return getDashboardContent();
  }
}

// Importar funções de geração de conteúdo das páginas
import { getDashboardContent } from '../pages/dashboard.js';
import { getPerfilContent } from '../pages/perfil.js';
import { getCatalogoContent } from '../pages/catalogo.js';
import { getAnunciosContent } from '../pages/anuncios.js';
import { getTransacoesContent } from '../pages/transacoes.js';
import { getFuncionariosContent } from '../pages/funcionarios.js';
import { getMetricasContent } from '../pages/metricas.js';
import { getAuditoriaContent } from '../pages/auditoria.js';
