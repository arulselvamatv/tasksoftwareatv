// Shared interactivity for navbar, sidebar, and profile menu
(function(){
  function qs(sel){ return document.querySelector(sel); }
  function qsa(sel){ return document.querySelectorAll(sel); }

  const hamburgerBtn = qs('#hamburgerBtn');
  const sidebar = qs('#sidebar');
  const sidebarOverlay = qs('#sidebarOverlay');
  const profileBtn = qs('#profileBtn');
  const profileMenu = qs('#profileMenu');

  function toggleSidebar() {
    if(!sidebar) return;
    const isOpen = !sidebar.classList.contains('-translate-x-full');
    if (isOpen) {
      closeSidebar();
    } else {
      sidebar.classList.remove('-translate-x-full');
      sidebar.classList.add('translate-x-0');
      if (sidebarOverlay) sidebarOverlay.classList.remove('hidden');
    }
  }

  function closeSidebar() {
    if(!sidebar) return;
    sidebar.classList.add('-translate-x-full');
    sidebar.classList.remove('translate-x-0');
    if (sidebarOverlay) sidebarOverlay.classList.add('hidden');
  }

  // Use delegated click handling for the hamburger button to avoid double-listeners
  // (some pages previously attached their own handlers which could toggle twice)
  document.addEventListener('click', function(e){
    try {
      if (e.target.closest && e.target.closest('#hamburgerBtn')) {
        // debug
        console.log('[shared.js] hamburger clicked');
        toggleSidebar();
        return;
      }
    } catch (err) {
      // ignore
    }
  });

  if (sidebarOverlay) sidebarOverlay.addEventListener('click', closeSidebar);

  if (profileBtn && profileMenu) {
    profileBtn.addEventListener('click', function(e){
      e.stopPropagation();
      profileMenu.classList.toggle('hidden');
    });

    document.addEventListener('click', function(e){
      if (!profileBtn.contains(e.target) && !profileMenu.contains(e.target)) {
        profileMenu.classList.add('hidden');
      }
    });
  }

  // Small helper to safely attach listener if element exists
  window.safeOn = function(selector, event, handler){
    const el = qs(selector);
    if(el) el.addEventListener(event, handler);
  };

  // Back button: used on detail pages to go back to task list
  document.addEventListener('DOMContentLoaded', function(){
    const backBtn = qs('#backBtn');
    if (backBtn) {
      // show floating button on todo.html
      try {
        const path = location.pathname.split('/').pop();
        if (path === 'todo.html' || path === 'task-detail.html') {
          backBtn.classList.add('visible');
        }
      } catch (e) {}

      backBtn.addEventListener('click', function(){
        try {
          if (location.pathname.endsWith('todo.html') || location.pathname.endsWith('tasks.html')) {
            window.location.href = 'tasks.html';
          } else {
            history.back();
          }
        } catch (err) {
          history.back();
        }
      });
    }
  });
})();
