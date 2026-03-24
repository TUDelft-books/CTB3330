document.addEventListener('DOMContentLoaded', function () {
  var handledFigures = new WeakSet();

  document.querySelectorAll('.sticky-margin').forEach(function (marker) {
    var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    var mainFigure = marker.tagName === 'FIGURE' ? marker : marker.closest('figure');

    if (!mainFigure || handledFigures.has(mainFigure)) return;
    handledFigures.add(mainFigure);

    var aside = document.createElement('aside');
    aside.className = 'margin sidebar sticky-margin sticky-margin-generated';
    aside.innerHTML = '<p class="sidebar-title"></p>';

    var figureClone = mainFigure.cloneNode(true);
    aside.appendChild(figureClone);
    mainFigure.insertAdjacentElement('afterend', aside);

    function ensureMathVisible() {
      // Clear any hidden styles on math elements and MathJax containers
      aside.querySelectorAll('.math').forEach(function(m) { m.style.display = ''; });
      aside.querySelectorAll('mjx-container').forEach(function(mjx) { 
        mjx.style.visibility = '';
        mjx.style.display = '';
      });
    }

    var sourceImage = mainFigure.querySelector('.sticky-margin') || mainFigure.querySelector('img');
    var targetImage = aside.querySelector('img');
    var lastSourceRect = null;
    var currentAnimation = null;
    var typesetRequestId = 0;

    function refreshAsideCloneFromMain() {
      var freshClone = mainFigure.cloneNode(true);
      var oldClone = aside.querySelector('figure');

      if (oldClone) {
        oldClone.replaceWith(freshClone);
      } else {
        aside.appendChild(freshClone);
      }

      targetImage = aside.querySelector('img');
    }

    function queueAsideTypeset(attempt) {
      var currentAttempt = typeof attempt === 'number' ? attempt : 0;

      if (!aside.classList.contains('is-visible')) {
        return;
      }

      ensureMathVisible();

      if (!window.MathJax || typeof window.MathJax.typesetPromise !== 'function') {
        if (currentAttempt < 60) {
          setTimeout(function () {
            queueAsideTypeset(currentAttempt + 1);
          }, 100);
        }
        return;
      }

      var requestId = ++typesetRequestId;

      function runTypeset() {
        if (requestId !== typesetRequestId || !aside.classList.contains('is-visible')) {
          return;
        }

        // First typeset the source figure, then clone that final state into the margin.
        // This avoids cloning a transient mid-render MathJax state on normal refresh.
        window.MathJax.typesetPromise([mainFigure]).then(function () {
          if (requestId !== typesetRequestId || !aside.classList.contains('is-visible')) {
            return;
          }

          refreshAsideCloneFromMain();
          ensureMathVisible();

          return window.MathJax.typesetPromise([aside]);
        }).then(function () {
          if (requestId !== typesetRequestId || !aside.classList.contains('is-visible')) {
            return;
          }
          ensureMathVisible();
        }).catch(function () {
          // Ignore transient MathJax failures during page load races.
        });
      }

      if (window.MathJax.startup && window.MathJax.startup.promise) {
        window.MathJax.startup.promise.then(runTypeset).catch(function () {
          // Ignore startup timing failures.
        });
      } else {
        runTypeset();
      }
    }

    function cancelCurrentAnimation() {
      if (currentAnimation) {
        currentAnimation.cancel();
        currentAnimation = null;
      }
    }

    function createFlightClone(image, rect) {
      var clone = image.cloneNode(true);
      clone.className = image.className;
      clone.classList.add('sticky-margin-flight');
      clone.style.left = rect.left + 'px';
      clone.style.top = rect.top + 'px';
      clone.style.width = rect.width + 'px';
      clone.style.height = rect.height + 'px';
      document.body.appendChild(clone);
      return clone;
    }

    function animateFlight(clone, fromRect, toRect, onComplete) {
      cancelCurrentAnimation();

      var animation = clone.animate([
        {
          left: fromRect.left + 'px',
          top: fromRect.top + 'px',
          width: fromRect.width + 'px',
          height: fromRect.height + 'px',
          opacity: 1
        },
        {
          left: toRect.left + 'px',
          top: toRect.top + 'px',
          width: toRect.width + 'px',
          height: toRect.height + 'px',
          opacity: 1
        }
      ], {
        duration: 750,
        easing: 'cubic-bezier(0.22, 1, 0.36, 1)',
        fill: 'forwards'
      });

      currentAnimation = animation;

      function finalize() {
        clone.remove();
        currentAnimation = null;
        onComplete();
      }

      animation.addEventListener('finish', finalize);
      animation.addEventListener('cancel', finalize);
    }

    function rememberSourceRect() {
      if (!sourceImage || window.innerWidth < 1200) return;

      var rect = sourceImage.getBoundingClientRect();
      if (rect.bottom > 0 && rect.top < window.innerHeight && rect.width > 0 && rect.height > 0) {
        lastSourceRect = rect;
      }
    }

    function showStickyMargin() {
      if (aside.classList.contains('is-visible')) {
        queueAsideTypeset();
        return;
      }

      cancelCurrentAnimation();

      if (
        prefersReducedMotion ||
        !sourceImage ||
        !targetImage ||
        !lastSourceRect ||
        window.innerWidth < 1200
      ) {
        ensureMathVisible();
        aside.classList.add('is-visible');
        queueAsideTypeset();
        return;
      }

      aside.classList.add('is-preparing');
      var targetRect = targetImage.getBoundingClientRect();
      aside.classList.remove('is-preparing');

      if (targetRect.width === 0 || targetRect.height === 0) {
        ensureMathVisible();
        aside.classList.add('is-visible');
        queueAsideTypeset();
        return;
      }

      var clone = createFlightClone(sourceImage, lastSourceRect);

      animateFlight(clone, lastSourceRect, targetRect, function () {
        ensureMathVisible();
        aside.classList.add('is-visible');
        queueAsideTypeset();
      });
    }

    function hideStickyMargin() {
      if (!aside.classList.contains('is-visible')) {
        return;
      }

      cancelCurrentAnimation();

      if (prefersReducedMotion || !sourceImage || !targetImage || window.innerWidth < 1200) {
        aside.classList.remove('is-visible');
        return;
      }

      var sourceRect = sourceImage.getBoundingClientRect();
      var targetRect = targetImage.getBoundingClientRect();

      if (
        sourceRect.width === 0 ||
        sourceRect.height === 0 ||
        targetRect.width === 0 ||
        targetRect.height === 0
      ) {
        aside.classList.remove('is-visible');
        return;
      }

      var clone = createFlightClone(targetImage, targetRect);
      aside.classList.remove('is-visible');

      animateFlight(clone, targetRect, sourceRect, function () {});
    }

    rememberSourceRect();
    window.addEventListener('scroll', rememberSourceRect, { passive: true });
    window.addEventListener('resize', rememberSourceRect);

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        rememberSourceRect();

        if (window.innerWidth < 1200) {
          hideStickyMargin();
          return;
        }

        if (entry.isIntersecting) {
          hideStickyMargin();
        } else if (entry.boundingClientRect.bottom < 0) {
          showStickyMargin();
        } else {
          hideStickyMargin();
        }
      });
    }, { threshold: 0 });

    observer.observe(mainFigure);

    // Manually trigger visibility check on page load for current scroll position
    requestAnimationFrame(function() {
      rememberSourceRect();
      var rect = mainFigure.getBoundingClientRect();
      
      if (window.innerWidth >= 1200 && rect.bottom < 0) {
        showStickyMargin();
      } else {
        hideStickyMargin();
      }
    });
  });
});
