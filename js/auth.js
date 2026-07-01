// ============================================================
// SAPA Smansabel – Auth JavaScript
// Admin Login & Session Guard
// ============================================================

const ADMIN_CREDENTIALS = {
  username: 'admin',
  password: 'mpls2026'
};

const SESSION_KEY = 'sapa_admin_session';

// ── Check if already logged in (on login page) ──────────────
function checkAlreadyLoggedIn() {
  const session = sessionStorage.getItem(SESSION_KEY);
  if (session) {
    window.location.href = 'dashboard.html';
  }
}

// ── Guard Dashboard page ────────────────────────────────────
function guardDashboard() {
  const session = sessionStorage.getItem(SESSION_KEY);
  if (!session) {
    window.location.href = 'admin.html';
    return false;
  }
  return true;
}

// ── Get current session user ────────────────────────────────
function getSessionUser() {
  return sessionStorage.getItem(SESSION_KEY) || 'Admin';
}

// ── Logout ──────────────────────────────────────────────────
function logout() {
  sessionStorage.removeItem(SESSION_KEY);
  window.location.href = 'admin.html';
}

// ── Login Page Logic ────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function () {
  const loginForm  = document.getElementById('loginForm');
  const loginAlert = document.getElementById('loginAlert');
  const loginBtn   = document.getElementById('loginBtn');
  const togglePwd  = document.getElementById('togglePassword');
  const pwdInput   = document.getElementById('loginPassword');

  // Password toggle
  if (togglePwd && pwdInput) {
    togglePwd.addEventListener('click', () => {
      const isText = pwdInput.type === 'text';
      pwdInput.type = isText ? 'password' : 'text';
      togglePwd.textContent = isText ? '👁' : '🙈';
    });
  }

  // If on login page, check if already logged in
  if (loginForm) {
    checkAlreadyLoggedIn();

    loginForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const user = document.getElementById('loginUsername').value.trim();
      const pass = document.getElementById('loginPassword').value;

      // Show loading
      loginBtn.disabled = true;
      loginBtn.innerHTML = '<span style="display:inline-block;width:18px;height:18px;border:3px solid rgba(255,255,255,0.4);border-top-color:#fff;border-radius:50%;animation:spin 0.7s linear infinite;vertical-align:middle;margin-right:8px;"></span>Masuk...';

      setTimeout(() => {
        if (user === ADMIN_CREDENTIALS.username && pass === ADMIN_CREDENTIALS.password) {
          sessionStorage.setItem(SESSION_KEY, user);
          window.location.href = 'dashboard.html';
        } else {
          loginBtn.disabled = false;
          loginBtn.innerHTML = '🔐 Masuk ke Dashboard';
          if (loginAlert) {
            loginAlert.classList.remove('hidden');
            setTimeout(() => loginAlert.classList.add('hidden'), 5000);
          }
          // Shake animation
          loginForm.classList.add('shake');
          setTimeout(() => loginForm.classList.remove('shake'), 500);
        }
      }, 1200);
    });
  }

  // Logout buttons
  const logoutBtns = document.querySelectorAll('[data-logout]');
  logoutBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      logout();
    });
  });
});
