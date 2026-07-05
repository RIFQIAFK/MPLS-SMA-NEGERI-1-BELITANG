/* ══════════════════════════════════════════════
   js/auth.js  –  Sistem Autentikasi Siswa SAPA Smansabel
   ══════════════════════════════════════════════ */

// ── Database Siswa ──
// Tambahkan data siswa di sini. Format: { username, password, nama, peleton }
const SISWA_DB = [
  { username: "MPLS26P101", password: "PLETON1", nama: "Siswa Uji Coba", peleton: "Peleton 1" },
  // Tambahkan siswa lain di bawah ini:
  // { username: "MPLS26P102", password: "PLETON1", nama: "Nama Siswa", peleton: "Peleton 1" },
];

const AUTH_SESSION_KEY = "sapa_siswa_session";

// ── Fungsi Login ──
function loginSiswa(username, password) {
  const siswa = SISWA_DB.find(
    s => s.username.toUpperCase() === username.toUpperCase() && s.password === password
  );
  if (siswa) {
    sessionStorage.setItem(AUTH_SESSION_KEY, JSON.stringify({
      username: siswa.username,
      nama: siswa.nama,
      peleton: siswa.peleton,
      loggedInAt: new Date().toISOString()
    }));
    return { success: true, nama: siswa.nama };
  }
  return { success: false };
}

// ── Cek apakah sudah login ──
function isLoggedIn() {
  return sessionStorage.getItem(AUTH_SESSION_KEY) !== null;
}

// ── Ambil data siswa yang sedang login ──
function getSiswaSession() {
  const data = sessionStorage.getItem(AUTH_SESSION_KEY);
  return data ? JSON.parse(data) : null;
}

// ── Logout ──
function logoutSiswa() {
  sessionStorage.removeItem(AUTH_SESSION_KEY);
}

// ── Guard: redirect ke login jika belum masuk ──
function requireLogin() {
  if (!isLoggedIn()) {
    window.location.href = "login_siswa.html";
  }
}
