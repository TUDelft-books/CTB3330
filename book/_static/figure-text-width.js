(function () {
  var FIGURE_SELECTOR = [
    ".sd-container-fluid.center-grid figure.align-center"
  ].join(", ");

  function getDirectChild(figure, tagName) {
    for (var index = 0; index < figure.children.length; index += 1) {
      var child = figure.children[index];
      if (child.tagName === tagName) {
        return child;
      }
    }

    return null;
  }

  function getDirectTextBlocks(figure) {
    var blocks = [];

    for (var index = 0; index < figure.children.length; index += 1) {
      var child = figure.children[index];
      if (child.tagName === "P" || child.tagName === "UL" || child.tagName === "OL") {
        blocks.push(child);
      }
    }

    return blocks;
  }

  function updateFigureTextWidth(figure) {
    var image = getDirectChild(figure, "IMG");
    var textBlocks = getDirectTextBlocks(figure);

    if (!image || textBlocks.length === 0) {
      return;
    }

    var width = image.getBoundingClientRect().width;
    if (width > 0) {
      textBlocks.forEach(function (block) {
        block.style.width = width + "px";
        block.style.maxWidth = "100%";
      });
    }
  }

  function updateAll() {
    var figures = document.querySelectorAll(FIGURE_SELECTOR);

    figures.forEach(updateFigureTextWidth);
  }

  function initObservers() {
    var figures = document.querySelectorAll(FIGURE_SELECTOR);

    if ("ResizeObserver" in window) {
      var ro = new ResizeObserver(function (entries) {
        entries.forEach(function (entry) {
          var figure = entry.target.closest("figure.align-center");
          if (figure) {
            updateFigureTextWidth(figure);
          }
        });
      });

      figures.forEach(function (figure) {
        var image = getDirectChild(figure, "IMG");
        if (image) {
          ro.observe(image);
          if (!image.complete) {
            image.addEventListener("load", function () {
              updateFigureTextWidth(figure);
            });
          }
        }
      });
    } else {
      window.addEventListener("resize", updateAll);
    }

    window.addEventListener("load", updateAll);
    updateAll();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initObservers);
  } else {
    initObservers();
  }
})();
