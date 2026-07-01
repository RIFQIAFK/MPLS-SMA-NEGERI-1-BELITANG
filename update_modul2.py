import sys

with open('modul2.html', 'r', encoding='utf-8') as f:
    content = f.read()

split_str = '<!-- MAIN CARD -->'
if split_str not in content:
    print("Cannot find MAIN CARD")
    sys.exit(1)

head_part = content.split(split_str)[0]

new_content = """<!-- MAIN CARD -->
<div class="container">
<div class="ckg-card" id="ckgMainCard">

  <!-- Progress Bar -->
  <div class="step-progress" id="stepProgress">
    <div class="step-dot active" id="dot0"></div>
    <div class="step-line" id="line0"></div>
    <div class="step-dot" id="dot1"></div>
    <div class="step-line" id="line1"></div>
    <div class="step-dot" id="dot2"></div>
    <div class="step-line" id="line2"></div>
    <div class="step-dot" id="dot3"></div>
    <span class="step-label">Tahap <span id="stepNum">1</span>/4</span>
  </div>

  <!-- Panel 0: Identitas & Ukuran Tubuh -->
  <div class="form-panel active" id="panel0">
    <div class="segment-header">
      <div class="segment-icon-wrap" style="background:#dbeafe;">??</div>
      <div>
        <h3>Identitas & Ukuran Tubuh</h3>
        <p>Isi data dirimu dan hasil pengukuran tubuh</p>
      </div>
    </div>
    <div class="id-form-grid">
      <div class="field-group">
        <label class="field-label" for="ckgNama">Nama Lengkap *</label>
        <input type="text" id="ckgNama" class="field-input" placeholder="Contoh: Budi Santoso" />
      </div>
      <div class="field-group">
        <label class="field-label" for="ckgKelas">Kelas *</label>
        <select id="ckgKelas" class="field-input">
          <option value="">-- Pilih Kelas --</option>
          <option>X-IPA 1</option><option>X-IPA 2</option>
          <option>X-IPS 1</option><option>X-IPS 2</option>
        </select>
      </div>
    </div>
    
    <div class="id-form-grid" style="margin-top: 1rem;">
      <div class="field-group">
        <label class="field-label" for="ckgTinggi">Tinggi Badan (cm) *</label>
        <input type="number" id="ckgTinggi" class="field-input" placeholder="Contoh: 165" />
      </div>
      <div class="field-group">
        <label class="field-label" for="ckgBerat">Berat Badan (kg) *</label>
        <input type="number" id="ckgBerat" class="field-input" placeholder="Contoh: 55" />
      </div>
      <div class="field-group">
        <label class="field-label" for="ckgPerut">Lingkar Perut (cm) *</label>
        <input type="number" id="ckgPerut" class="field-input" placeholder="Contoh: 75" />
      </div>
    </div>
  </div>

  <!-- Panel 1: Riwayat Penyakit -->
  <div class="form-panel" id="panel1">
    <div class="segment-header">
      <div class="segment-icon-wrap" style="background:#fee2e2;">??</div>
      <div>
        <h3>Riwayat Penyakit</h3>
        <p>Informasi medis keluarga dan pribadi</p>
      </div>
    </div>
    <div class="question-card">
      <div class="question-text"><span class="question-number">No 1</span>Apakah <b>keluarga inti</b> (orang tua/saudara) memiliki riwayat diabetes, darah tinggi, penyakit jantung, stroke, atau kanker?</div>
      <div class="option-row">
        <label class="option-btn yes"><input type="radio" name="rwytKeluarga" value="Ya" /><span class="option-emoji">??</span>Ya, Ada</label>
        <label class="option-btn no"><input type="radio" name="rwytKeluarga" value="Tidak" /><span class="option-emoji">?</span>Tidak Ada</label>
      </div>
    </div>
    <div class="question-card">
      <div class="question-text"><span class="question-number">No 2</span>Apakah <b>Anda sendiri</b> pernah didiagnosis memiliki diabetes, darah tinggi, penyakit jantung, asma, atau kolesterol tinggi?</div>
      <div class="option-row">
        <label class="option-btn yes"><input type="radio" name="rwytPribadi" value="Ya" /><span class="option-emoji">??</span>Ya, Pernah</label>
        <label class="option-btn no"><input type="radio" name="rwytPribadi" value="Tidak" /><span class="option-emoji">??</span>Tidak Pernah</label>
      </div>
    </div>
  </div>

  <!-- Panel 2: Gaya Hidup & Pola Makan -->
  <div class="form-panel" id="panel2">
    <div class="segment-header">
      <div class="segment-icon-wrap" style="background:#dcfce7;">??</div>
      <div>
        <h3>Gaya Hidup & Pola Makan</h3>
        <p>Kebiasaan sehari-harimu</p>
      </div>
    </div>
    
    <div class="question-card">
      <div class="question-text"><span class="question-number">No 1</span>Bagaimana status kebiasaan merokok Anda?</div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
        <label class="option-btn yes"><input type="radio" name="merokok" value="Aktif" />Perokok Aktif</label>
        <label class="option-btn yes"><input type="radio" name="merokok" value="Kadang" />Kadang-kadang</label>
        <label class="option-btn"><input type="radio" name="merokok" value="Mantan" />Mantan Perokok</label>
        <label class="option-btn no"><input type="radio" name="merokok" value="Tidak" />Tidak Pernah</label>
      </div>
    </div>

    <div class="question-card">
      <div class="question-text"><span class="question-number">No 2</span>Apakah Anda berolahraga fisik minimal 30 menit dalam sehari?</div>
      <div class="option-row">
        <label class="option-btn no"><input type="radio" name="olahraga" value="Ya" /><span class="option-emoji">??</span>Ya, Rutin</label>
        <label class="option-btn yes"><input type="radio" name="olahraga" value="Tidak" /><span class="option-emoji">???</span>Jarang / Tidak</label>
      </div>
    </div>

    <div class="question-card">
      <div class="question-text"><span class="question-number">No 3</span>Apakah Anda mengonsumsi sayur dan buah setiap hari?</div>
      <div class="option-row">
        <label class="option-btn no"><input type="radio" name="sayur" value="Ya" /><span class="option-emoji">??</span>Ya, Setiap Hari</label>
        <label class="option-btn yes"><input type="radio" name="sayur" value="Tidak" /><span class="option-emoji">??</span>Tidak Menentu</label>
      </div>
    </div>

    <div class="question-card">
      <div class="question-text"><span class="question-number">No 4</span>Seberapa sering Anda mengonsumsi makanan manis, asin, atau berminyak/berlemak tinggi?</div>
      <div class="option-row">
        <label class="option-btn yes"><input type="radio" name="junkfood" value="Sering" /><span class="option-emoji">??</span>Sering</label>
        <label class="option-btn"><input type="radio" name="junkfood" value="Jarang" /><span class="option-emoji">??</span>Kadang-kadang</label>
        <label class="option-btn no"><input type="radio" name="junkfood" value="Tidak" /><span class="option-emoji">??</span>Jarang Sekali</label>
      </div>
    </div>
  </div>

  <!-- Panel 3: Analisis AI & Hasil -->
  <div class="form-panel text-center" id="panel3">
    <!-- Loading State -->
    <div id="aiLoading" style="padding: 4rem 1rem;">
      <div class="ai-pulse-wrap">
        <div class="ai-pulse-ring"></div>
        <div class="ai-pulse-core">?</div>
      </div>
      <h3 style="margin-top:1.5rem; color:#1d4ed8;">AI Gemini Sedang Menganalisis...</h3>
      <p style="color:#64748b; font-size:0.9rem;">Memproses data kesehatan, genetik, dan gaya hidup Anda.</p>
    </div>

    <!-- Result State -->
    <div id="aiResult" style="display:none;">
      
      <!-- Safe Result -->
      <div id="resSafe" style="display:none; padding: 2rem 0;">
        <div style="font-size: 4rem; margin-bottom:1rem;">??</div>
        <h2 style="color:#059669; font-weight:800; margin-bottom:1rem;">Gaya Hidup Anda Sangat Sehat!</h2>
        <p style="color:#475569; font-size:1.05rem; max-width:500px; margin:0 auto 2rem; line-height:1.6;">Berdasarkan perhitungan BMI dan kebiasaan Anda, Anda berada di kategori <strong>Risiko Rendah</strong>. Pertahankan pola makan bergizi, olahraga rutin, dan gaya hidup sehat Anda!</p>
        <div style="background:#ecfdf5; border: 1px solid #a7f3d0; border-radius:16px; padding:1.5rem; max-width:400px; margin:0 auto;">
          <h4 style="color:#047857; margin-bottom:0.5rem;">Saran AI:</h4>
          <ul style="text-align:left; color:#065f46; font-size:0.9rem; padding-left:1.2rem;">
            <li>Jaga konsistensi olahraga 30 menit/hari.</li>
            <li>Tidur yang cukup (7-8 jam semalam).</li>
            <li>Tetap hindari rokok dan makanan ultra-proses.</li>
          </ul>
        </div>
      </div>

      <!-- Warning Result (Ticket) -->
      <div id="resWarning" style="display:none;">
        <h2 style="color:#dc2626; font-weight:800; margin-bottom:0.5rem; font-size: 1.6rem;">Pemeriksaan Lanjutan Diperlukan</h2>
        <p style="color:#64748b; font-size:0.95rem; margin-bottom: 2rem;">Berdasarkan skrining awal, Anda disarankan mengunjungi fasilitas kesehatan terdekat.</p>
        
        <div class="ticket-wrapper">
          <div class="ticket-header">
            <div class="ticket-title">TIKET PEMERIKSAAN PUSKESMAS</div>
            <div class="ticket-subtitle">Bawa tiket digital ini ke Puskesmas atau Klinik Jejaring SMAN 1 Belitang</div>
          </div>
          <div class="ticket-body">
            <div style="display:flex; justify-content:space-between; margin-bottom:1rem;">
              <div style="text-align:left;">
                <div style="font-size:0.75rem; color:#64748b; text-transform:uppercase;">Nama Pasien</div>
                <div style="font-weight:700; color:#1e293b;" id="ticketNama">Budi Santoso</div>
              </div>
              <div style="text-align:right;">
                <div style="font-size:0.75rem; color:#64748b; text-transform:uppercase;">Kelas</div>
                <div style="font-weight:700; color:#1e293b;" id="ticketKelas">X-IPA 1</div>
              </div>
            </div>
            
            <div class="ticket-divider"></div>
            
            <div style="text-align:left; margin-bottom:1.5rem;">
              <div style="font-size:0.8rem; font-weight:700; color:#b91c1c; margin-bottom:0.5rem;">Rekomendasi Pengecekan (Gratis):</div>
              <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
                <span class="badge-cek">Cek Darah (Gula & Asam Urat)</span>
                <span class="badge-cek">Cek Kolesterol</span>
                <span class="badge-cek">Tensi Darah</span>
                <span class="badge-cek">Konsultasi Gizi</span>
              </div>
            </div>

            <div class="barcode-area">
              <div class="barcode-lines"></div>
              <div class="barcode-number">UKS-2026-<span id="ticketRandom">89412</span></div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- Navigation -->
  <div class="panel-nav">
    <button class="btn-nav-prev" id="btnPrev" style="display: none;">Kembali</button>
    <button class="btn-nav-next" id="btnNext">Selanjutnya</button>
  </div>

</div>
</div>

<!-- ===== FOOTER ===== -->
<footer class="site-footer" role="contentinfo" style="margin-top:4rem;">
  <div class="container">
    <div class="footer-grid" style="grid-template-columns: 1fr; text-align: center;">
      <div>
        <div class="footer-brand-name">SMAN 1 <span>BELITANG</span></div>
        <p class="footer-desc" style="margin: 0 auto 1rem; max-width: 600px;">
          Modul Kesehatan - Skrining Dini UKS. Data Anda dijamin kerahasiaannya.
        </p>
        <span class="footer-copy">© 2026 SMAN 1 BELITANG. All rights reserved.</span>
      </div>
    </div>
  </div>
</footer>

<style>
  /* Extra CSS for the Ticket & AI animation */
  .ai-pulse-wrap {
    position: relative;
    width: 80px; height: 80px;
    margin: 0 auto;
    display: flex; align-items: center; justify-content: center;
  }
  .ai-pulse-core {
    font-size: 2rem;
    position: relative;
    z-index: 2;
  }
  .ai-pulse-ring {
    position: absolute;
    inset: 0;
    border-radius: 50%;
    background: #bfdbfe;
    animation: ping 1.5s cubic-bezier(0, 0, 0.2, 1) infinite;
  }
  @keyframes ping {
    75%, 100% {
      transform: scale(2);
      opacity: 0;
    }
  }

  .ticket-wrapper {
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    max-width: 450px;
    margin: 0 auto;
    overflow: hidden;
    position: relative;
    filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));
  }
  .ticket-wrapper::before, .ticket-wrapper::after {
    content:'';
    position:absolute;
    top: 90px;
    width: 30px; height: 30px;
    background: #f8faff;
    border-radius: 50%;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
  }
  .ticket-wrapper::before { left: -15px; }
  .ticket-wrapper::after { right: -15px; }
  
  .ticket-header {
    background: linear-gradient(135deg, #1e3a8a, #1d4ed8);
    padding: 1.5rem;
    color: white;
  }
  .ticket-title { font-weight: 900; font-size: 1.25rem; letter-spacing: 1px; }
  .ticket-subtitle { font-size: 0.8rem; color: #bfdbfe; margin-top: 0.25rem; }
  
  .ticket-body { padding: 2rem 1.5rem; background: #fff; }
  
  .ticket-divider {
    height: 0;
    border-top: 2px dashed #cbd5e1;
    margin: 1rem -1.5rem 1.5rem;
  }
  
  .badge-cek {
    background: #fee2e2;
    color: #b91c1c;
    padding: 0.35rem 0.75rem;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 700;
  }

  .barcode-area { margin-top: 2rem; text-align: center; }
  .barcode-lines {
    height: 50px;
    background: repeating-linear-gradient(
      90deg,
      #1e293b,
      #1e293b 3px,
      transparent 3px,
      transparent 6px,
      #1e293b 6px,
      #1e293b 10px,
      transparent 10px,
      transparent 13px,
      #1e293b 13px,
      #1e293b 14px,
      transparent 14px,
      transparent 18px
    );
    margin-bottom: 0.5rem;
  }
  .barcode-number { font-family: 'Courier New', monospace; font-weight: 800; font-size: 1.1rem; letter-spacing: 0.2rem; color: #334155; }
</style>

<script>
  // Mobile Nav Toggle
  const navToggle = document.getElementById('navToggle');
  const mobileNav = document.getElementById('mobileNav');
  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('open');
    mobileNav.classList.toggle('open');
  });

  /* -- Multi-step Form Logic -- */
  let currentStep = 0;
  const totalSteps = 4;
  const btnPrev = document.getElementById('btnPrev');
  const btnNext = document.getElementById('btnNext');
  const stepNum = document.getElementById('stepNum');

  function updateUI() {
    // Panels
    for (let i = 0; i < totalSteps; i++) {
      const panel = document.getElementById('panel' + i);
      if (panel) {
        if (i === currentStep) {
          panel.classList.add('active');
        } else {
          panel.classList.remove('active');
        }
      }
    }
    // Progress Dots/Lines
    for (let i = 0; i < totalSteps; i++) {
      const dot = document.getElementById('dot' + i);
      if (dot) {
        if (i <= currentStep) dot.classList.add('active');
        else dot.classList.remove('active');
      }
      if (i < totalSteps - 1) {
        const line = document.getElementById('line' + i);
        if (line) {
          if (i < currentStep) line.classList.add('active');
          else line.classList.remove('active');
        }
      }
    }

    stepNum.innerText = currentStep + 1;

    // Buttons
    btnPrev.style.display = (currentStep === 0) ? 'none' : 'block';
    
    if (currentStep === totalSteps - 1) {
      btnNext.style.display = 'none'; // Hide next button on result step
      btnPrev.style.display = 'none';
      runAIAnalysis();
    } else if (currentStep === totalSteps - 2) {
      btnNext.innerText = 'Kirim & Analisis';
      btnNext.style.background = 'linear-gradient(135deg, #10b981, #059669)';
      btnNext.style.borderColor = '#059669';
    } else {
      btnNext.innerText = 'Selanjutnya';
      btnNext.style.background = '';
      btnNext.style.borderColor = '';
      btnNext.style.display = 'block';
    }
  }

  function validateStep() {
    if(currentStep === 0) {
      if(!document.getElementById('ckgNama').value || !document.getElementById('ckgKelas').value ||
         !document.getElementById('ckgTinggi').value || !document.getElementById('ckgBerat').value || !document.getElementById('ckgPerut').value) {
        alert("Harap lengkapi semua data identitas dan ukuran tubuh!");
        return false;
      }
    }
    return true;
  }

  btnNext.addEventListener('click', () => {
    if (!validateStep()) return;
    if (currentStep < totalSteps - 1) {
      currentStep++;
      updateUI();
    }
  });

  btnPrev.addEventListener('click', () => {
    if (currentStep > 0) {
      currentStep--;
      updateUI();
    }
  });

  // Calculate Risk and Show Result
  function runAIAnalysis() {
    document.getElementById('aiLoading').style.display = 'block';
    document.getElementById('aiResult').style.display = 'none';

    setTimeout(() => {
      document.getElementById('aiLoading').style.display = 'none';
      document.getElementById('aiResult').style.display = 'block';
      
      let isHighRisk = false;

      // Check BMI
      const t = parseFloat(document.getElementById('ckgTinggi').value) / 100;
      const b = parseFloat(document.getElementById('ckgBerat').value);
      if(t > 0 && b > 0) {
        const bmi = b / (t * t);
        if(bmi > 25) isHighRisk = true; // Overweight or Obese
      }

      // Check Waist
      const p = parseFloat(document.getElementById('ckgPerut').value);
      if (p > 90) isHighRisk = true;

      // Check Questionnaires
      const rwKeluarga = document.querySelector('input[name="rwytKeluarga"]:checked');
      if (rwKeluarga && rwKeluarga.value === 'Ya') isHighRisk = true;
      
      const rwPribadi = document.querySelector('input[name="rwytPribadi"]:checked');
      if (rwPribadi && rwPribadi.value === 'Ya') isHighRisk = true;
      
      const merokok = document.querySelector('input[name="merokok"]:checked');
      if (merokok && (merokok.value === 'Aktif' || merokok.value === 'Kadang')) isHighRisk = true;
      
      const olahraga = document.querySelector('input[name="olahraga"]:checked');
      if (olahraga && olahraga.value === 'Tidak') isHighRisk = true; // wait, Tidak berarti tidak olahraga
      
      const junkfood = document.querySelector('input[name="junkfood"]:checked');
      if (junkfood && junkfood.value === 'Sering') isHighRisk = true;

      if (isHighRisk) {
        // Populate Ticket
        document.getElementById('ticketNama').innerText = document.getElementById('ckgNama').value || 'Siswa';
        document.getElementById('ticketKelas').innerText = document.getElementById('ckgKelas').value || '-';
        document.getElementById('ticketRandom').innerText = Math.floor(10000 + Math.random() * 90000);
        document.getElementById('resWarning').style.display = 'block';
        document.getElementById('resSafe').style.display = 'none';
      } else {
        document.getElementById('resSafe').style.display = 'block';
        document.getElementById('resWarning').style.display = 'none';
      }
    }, 2500); // 2.5 seconds loading simulation
  }

  // Init
  updateUI();

  /* -- Auto-swap Hero Background -- */
  const heroSlides = document.querySelectorAll('.hero-bg-slide');
  if (heroSlides.length > 0) {
    let currentHero = 0;
    setInterval(() => {
      heroSlides[currentHero].classList.remove('active');
      currentHero = (currentHero + 1) % heroSlides.length;
      heroSlides[currentHero].classList.add('active');
    }, 5000);
  }
</script>
</body>
</html>
"""

final_content = head_part + new_content

with open('modul2.html', 'w', encoding='utf-8') as f:
    f.write(final_content)
print("Updated modul2.html successfully.")
