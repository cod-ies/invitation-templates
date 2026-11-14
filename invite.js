(function () {
  var stage = document.querySelector(".stage");
  var seal = document.querySelector(".seal");
  if (!stage || !seal) return;

  function openInvite() {
    if (stage.classList.contains("is-open")) return;
    stage.classList.add("is-open");
    seal.setAttribute("aria-expanded", "true");
  }

  seal.addEventListener("click", openInvite);
})();
