(function() {
  // Create cursor elements
  var cursorDot = document.createElement('div');
  cursorDot.className = 'custom-cursor-dot';

  var cursorOutline = document.createElement('div');
  cursorOutline.className = 'custom-cursor-outline';

  document.body.appendChild(cursorDot);
  document.body.appendChild(cursorOutline);

  // Inject CSS
  var style = document.createElement('style');
  style.textContent = [
    'body:not(.touch-device), body:not(.touch-device) * { cursor: none !important; }',
    '.custom-cursor-dot {',
    '  width: 8px; height: 8px;',
    '  background-color: #38bdf8;',
    '  border-radius: 50%;',
    '  position: fixed; top: 0; left: 0;',
    '  transform: translate(-50%, -50%);',
    '  pointer-events: none;',
    '  z-index: 999999;',
    '  transition: width 0.15s ease, height 0.15s ease, background-color 0.15s ease;',
    '}',
    '.custom-cursor-outline {',
    '  width: 40px; height: 40px;',
    '  border: 2px solid rgba(56, 189, 248, 0.5);',
    '  border-radius: 50%;',
    '  position: fixed; top: 0; left: 0;',
    '  transform: translate(-50%, -50%);',
    '  pointer-events: none;',
    '  z-index: 999998;',
    '  transition: width 0.15s ease, height 0.15s ease, border-color 0.15s ease, background-color 0.15s ease;',
    '}',
    '.custom-cursor-dot.hover {',
    '  background-color: #fff; width: 12px; height: 12px;',
    '}',
    '.custom-cursor-outline.hover {',
    '  width: 60px; height: 60px;',
    '  border-color: #fff;',
    '  background-color: rgba(255,255,255,0.08);',
    '}'
  ].join('\n');
  document.head.appendChild(style);

  // State
  var mouseX = -100, mouseY = -100;
  var outlineX = -100, outlineY = -100;
  var isMoving = false;
  var isTouch = false;

  // Hide initially
  cursorDot.style.opacity = '0';
  cursorOutline.style.opacity = '0';

  // Touch detection — hide cursor on touch devices
  window.addEventListener('touchstart', function() {
    isTouch = true;
    document.body.classList.add('touch-device');
    cursorDot.style.display = 'none';
    cursorOutline.style.display = 'none';
  }, { once: true });

  // Mouse move
  window.addEventListener('mousemove', function(e) {
    if (isTouch) return;
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursorDot.style.left = mouseX + 'px';
    cursorDot.style.top = mouseY + 'px';
    if (!isMoving) {
      isMoving = true;
      cursorDot.style.opacity = '1';
      cursorOutline.style.opacity = '1';
    }
  });

  // Smooth trailing ring animation
  function animate() {
    outlineX += (mouseX - outlineX) * 0.18;
    outlineY += (mouseY - outlineY) * 0.18;
    cursorOutline.style.left = outlineX + 'px';
    cursorOutline.style.top = outlineY + 'px';
    requestAnimationFrame(animate);
  }
  animate();

  // Hover effects on interactive elements
  function bindHover() {
    var els = document.querySelectorAll('a, button, input, textarea, select, label, .nav-toggle, .nav-brand, .clickable, .wizard-step, .recap-slide, .btn, [role="button"]');
    for (var i = 0; i < els.length; i++) {
      if (!els[i].dataset.cursorBound) {
        els[i].dataset.cursorBound = '1';
        els[i].addEventListener('mouseenter', function() {
          cursorDot.classList.add('hover');
          cursorOutline.classList.add('hover');
        });
        els[i].addEventListener('mouseleave', function() {
          cursorDot.classList.remove('hover');
          cursorOutline.classList.remove('hover');
        });
      }
    }
  }
  bindHover();

  // Re-bind on DOM changes
  if (typeof MutationObserver !== 'undefined') {
    new MutationObserver(bindHover).observe(document.body, { childList: true, subtree: true });
  }

  // Hide/show on window leave/enter
  document.addEventListener('mouseleave', function() {
    cursorDot.style.opacity = '0';
    cursorOutline.style.opacity = '0';
  });
  document.addEventListener('mouseenter', function() {
    if (!isTouch) {
      cursorDot.style.opacity = '1';
      cursorOutline.style.opacity = '1';
    }
  });
})();
