import glob

css_old = '''    .hero {
      position: relative;
      min-height: 100vh;
      display: flex;
      align-items: center;
      background: linear-gradient(
        135deg,
        rgba(3, 8, 26, 0.92) 0%,
        rgba(6, 14, 43, 0.88) 30%,
        rgba(10, 42, 110, 0.80) 70%,
        rgba(20, 103, 184, 0.75) 100%
      ), url('DSC07214.JPG') center/cover no-repeat;
      overflow: hidden;
      padding-top: 68px;
    }'''

css_new = '''    .hero {
      position: relative;
      min-height: 100vh;
      display: flex;
      align-items: center;
      overflow: hidden;
      padding-top: 68px;
    }
    .hero-bg-slider {
      position: absolute;
      inset: 0;
      z-index: 0;
    }
    .hero-bg-slide {
      position: absolute;
      inset: 0;
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      opacity: 0;
      transition: opacity 1.5s ease-in-out, transform 4s ease-in-out;
      transform: scale(1.05);
    }
    .hero-bg-slide.active {
      opacity: 1;
      transform: scale(1);
    }
    .hero-bg-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(
        135deg,
        rgba(3, 8, 26, 0.92) 0%,
        rgba(6, 14, 43, 0.88) 30%,
        rgba(10, 42, 110, 0.80) 70%,
        rgba(20, 103, 184, 0.75) 100%
      );
    }'''

html_old = '''<header class="hero" role="banner">
  <div class="hero-orb hero-orb-1"></div>'''

html_new = '''<header class="hero" role="banner">
  <div class="hero-bg-slider">
    <div class="hero-bg-slide active" style="background-image: url('FOTO/BEKRON/DSC00062.JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00164.JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00186.JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00187.JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00307 (1).JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00753.JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00763.JPG')"></div>
    <div class="hero-bg-overlay"></div>
  </div>

  <div class="hero-orb hero-orb-1"></div>'''

js_old = '''  /* -- Scroll-reveal -- */'''

js_new = '''  /* -- Auto-swap Hero Background -- */
  const heroSlides = document.querySelectorAll('.hero-bg-slide');
  if (heroSlides.length > 0) {
    let currentHero = 0;
    setInterval(() => {
      heroSlides[currentHero].classList.remove('active');
      currentHero = (currentHero + 1) % heroSlides.length;
      heroSlides[currentHero].classList.add('active');
    }, 5000); // Change background every 5 seconds
  }

  /* -- Scroll-reveal -- */'''

files = ['fasilitas.html', 'ketentuan.html', 'pelaksanaan.html', 'modul1.html', 'modul2.html', 'modul3.html']

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if css_old in content:
            content = content.replace(css_old, css_new)
            content = content.replace(html_old, html_new)
            if "Auto-swap Hero Background" not in content:
                content = content.replace(js_old, js_new)
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated {f}")
        else:
            print(f"css_old not found in {f}")
    except Exception as e:
        print(f"Error on {f}: {e}")
