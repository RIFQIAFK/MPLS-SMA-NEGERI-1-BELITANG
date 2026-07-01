import os

html_old = '<div class="hero-bg"></div>'
html_new = '''<div class="hero-bg-slider">
    <div class="hero-bg-slide active" style="background-image: url('FOTO/BEKRON/DSC00062.JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00164.JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00186.JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00187.JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00307 (1).JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00753.JPG')"></div>
    <div class="hero-bg-slide" style="background-image: url('FOTO/BEKRON/DSC00763.JPG')"></div>
    <div class="hero-bg-overlay"></div>
  </div>'''

css_old = '''    .hero-bg {
      position: absolute;
      inset: 0;
      background: var(--grad-hero);
      z-index: 0;
    }'''

css_new = '''    .hero-bg-slider {
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
      background: var(--grad-hero);
    }'''

js_append = '''
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
'''

files = ['modul1.html', 'modul2.html', 'modul3.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if html_old in content:
        content = content.replace(html_old, html_new)
        content = content.replace(css_old, css_new)
        
        # Append JS before closing script tag
        if "Auto-swap Hero Background" not in content:
            content = content.replace('</script>\n</body>', js_append + '</script>\n</body>')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
    else:
        print(f"Already updated {f}")

