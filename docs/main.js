(() => {
  // Hero mute toggle
  const heroVid = document.getElementById('hero-vid');
  const heroMute = document.getElementById('hero-mute');
  if (heroVid && heroMute) {
    heroMute.addEventListener('click', () => {
      const wasMuted = heroVid.muted;
      heroVid.muted = !wasMuted;
      heroMute.setAttribute('aria-pressed', wasMuted ? 'false' : 'true');
      heroMute.setAttribute('aria-label', wasMuted ? 'mute brag video' : 'unmute brag video');
      // When unmuting, ensure it actually plays with sound (some browsers require gesture)
      if (!heroVid.muted) {
        const p = heroVid.play();
        if (p && p.catch) p.catch(() => {});
      }
    });
  }

  // Gallery videos use the native <video controls> player. No custom JS.

  // Copy buttons
  document.querySelectorAll('.copy[data-copy]').forEach((btn) => {
    btn.addEventListener('click', async () => {
      const text = btn.dataset.copy || '';
      try {
        await navigator.clipboard.writeText(text);
        btn.dataset.state = 'copied';
        const orig = btn.textContent;
        btn.textContent = 'copied';
        setTimeout(() => {
          btn.dataset.state = '';
          btn.textContent = orig;
        }, 1600);
      } catch {
        // fallback: select inside the <pre>
        const pre = btn.closest('.install');
        if (pre) {
          const range = document.createRange();
          range.selectNodeContents(pre.querySelector('code'));
          const sel = window.getSelection();
          sel.removeAllRanges();
          sel.addRange(range);
        }
      }
    });
  });
})();
