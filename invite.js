(function () {
  var stage = document.querySelector(".stage");
  var seal = document.querySelector(".seal");
  var folio = document.querySelector(".folio");
  var reduce = document.documentElement.classList.contains("reduce");
  if (!stage || !seal) return;

  var months = {
    januar: 0, februar: 1, märz: 2, marz: 2, april: 3, mai: 4, juni: 5,
    juli: 6, august: 7, september: 8, oktober: 9, november: 10, dezember: 11
  };

  function berlinInstant(y, mo, d, hh, mm) {
    var fmt = new Intl.DateTimeFormat("en-US", {
      timeZone: "Europe/Berlin",
      hourCycle: "h23",
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit"
    });
    var guess = Date.UTC(y, mo, d, hh, mm);
    for (var i = 0; i < 4; i++) {
      var parts = {};
      fmt.formatToParts(new Date(guess)).forEach(function (p) { parts[p.type] = p.value; });
      var shown = Date.UTC(+parts.year, +parts.month - 1, +parts.day, +parts.hour % 24, +parts.minute);
      guess += Date.UTC(y, mo, d, hh, mm) - shown;
    }
    return guess;
  }

  function readWhen() {
    var raw = folio ? folio.getAttribute("data-when") : "";
    var m = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})$/.exec(raw || "");
    if (!m) return null;
    return berlinInstant(+m[1], +m[2] - 1, +m[3], +m[4], +m[5]);
  }

  function unit(n, one, many) {
    return n + " " + (n === 1 ? one : many);
  }

  function paintCount() {
    var target = readWhen();
    if (!target) return;
    var left = target - Date.now();
    var line = folio.querySelector("[data-until]");
    if (left <= 0) {
      folio.querySelectorAll("[data-unit] b").forEach(function (b) { b.textContent = "0"; });
      if (line) line.textContent = "Der Abend ist da.";
      return;
    }
    var days = Math.floor(left / 86400000);
    var hours = Math.floor((left % 86400000) / 3600000);
    var minutes = Math.floor((left % 3600000) / 60000);
    var values = { days: days, hours: hours, minutes: minutes };
    folio.querySelectorAll("[data-unit]").forEach(function (node) {
      var b = node.querySelector("b");
      var next = String(values[node.getAttribute("data-unit")]);
      if (b.textContent !== next) {
        b.textContent = next;
        b.classList.remove("tick");
        void b.offsetWidth;
        b.classList.add("tick");
      }
    });
    if (line) {
      line.textContent = "Noch " + unit(days, "Tag", "Tage") + ", " + unit(hours, "Stunde", "Stunden") + " und " + unit(minutes, "Minute", "Minuten") + ".";
    }
  }

  var scratchBox = document.querySelector(".scratch");
  var canvas = scratchBox ? scratchBox.querySelector("canvas") : null;
  var ctx = null;
  var scratching = false;
  var moves = 0;

  function drawFoil() {
    if (!canvas || !scratchBox || reduce || scratchBox.classList.contains("is-done")) return;
    var w = scratchBox.clientWidth;
    var h = scratchBox.clientHeight;
    if (!w || !h) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var coat = getComputedStyle(stage).getPropertyValue("--wax").trim() || "#8c6232";
    var inkOn = getComputedStyle(stage).getPropertyValue("--wax-ink").trim() || "#fff8ef";
    var display = getComputedStyle(stage).getPropertyValue("--display").trim() || "Georgia, serif";
    ctx.globalCompositeOperation = "source-over";
    ctx.fillStyle = coat;
    ctx.fillRect(0, 0, w, h);
    ctx.fillStyle = inkOn;
    ctx.font = "italic 22px " + display;
    ctx.textAlign = "left";
    ctx.textBaseline = "middle";
    ctx.fillText("Kratzt die Schicht weg", 22, h / 2);
  }

  function scratchAt(e) {
    if (!ctx || scratchBox.classList.contains("is-done")) return;
    var rect = canvas.getBoundingClientRect();
    ctx.globalCompositeOperation = "destination-out";
    ctx.beginPath();
    ctx.arc(e.clientX - rect.left, e.clientY - rect.top, 18, 0, Math.PI * 2);
    ctx.fill();
    moves += 1;
    if (moves % 6 === 0) measureFoil();
  }

  function measureFoil() {
    var data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
    var clear = 0;
    var seen = 0;
    var i;
    for (i = 3; i < data.length; i += 64) {
      seen += 1;
      if (data[i] < 40) clear += 1;
    }
    if (seen && clear / seen > 0.46) finishScratch();
  }

  function finishScratch() {
    scratchBox.classList.add("is-done");
    scratching = false;
  }

  function armScratch() {
    if (!scratchBox) return;
    if (reduce) {
      scratchBox.classList.add("is-done");
      return;
    }
    drawFoil();
    canvas.addEventListener("pointerdown", function (e) {
      if (scratchBox.classList.contains("is-done")) return;
      scratching = true;
      try { canvas.setPointerCapture(e.pointerId); } catch (err) { /* synthetic events */ }
      scratchAt(e);
    });
    canvas.addEventListener("pointermove", function (e) {
      if (scratching) scratchAt(e);
    });
    canvas.addEventListener("pointerup", function () { scratching = false; measureFoil(); });
    canvas.addEventListener("pointercancel", function () { scratching = false; });
    var reveal = folio.querySelector(".reveal-secret");
    if (reveal) reveal.addEventListener("click", finishScratch);
  }

  var storeKey = "feierlink-rsvp:" + location.pathname;
  var party = folio ? folio.querySelector(".party") : null;
  var amountNode = folio ? folio.querySelector("[data-amount]") : null;
  var namesBox = folio ? folio.querySelector(".names") : null;
  var yes = folio ? folio.querySelector('[data-answer="yes"]') : null;
  var no = folio ? folio.querySelector('[data-answer="no"]') : null;
  var countNode = folio ? folio.querySelector("[data-live-count]") : null;
  var labelNode = folio ? folio.querySelector("[data-live-label]") : null;
  var comingNode = folio ? folio.querySelector(".coming") : null;

  function readNames() {
    if (!namesBox) return [];
    return [].slice.call(namesBox.querySelectorAll("input")).map(function (input) {
      return input.value.trim();
    }).filter(Boolean);
  }

  function joinNames(list) {
    if (list.length < 2) return list[0] || "";
    return list.slice(0, -1).join(", ") + " und " + list[list.length - 1];
  }

  function peopleLine(list) {
    if (!list.length) return "Noch keine Namen.";
    if (list.length === 1) return "Es kommt 1 Person: " + list[0] + ".";
    return "Es kommen " + list.length + " Personen: " + joinNames(list) + ".";
  }

  function showTally(answer, list) {
    if (answer === "no") {
      countNode.textContent = "0";
      labelNode.textContent = "Personen kommen";
      comingNode.textContent = "Ihr habt abgesagt. Es kommen 0 Personen.";
      return;
    }
    if (answer === "yes" && !list.length) {
      countNode.textContent = "";
      labelNode.textContent = "Namen fehlen noch";
      comingNode.textContent = "Tippt die Namen. Gezählt wird, wer einen Namen hat.";
      return;
    }
    if (answer === "yes") {
      countNode.textContent = String(list.length);
      labelNode.textContent = list.length === 1 ? " Person kommt" : " Personen kommen";
      comingNode.textContent = peopleLine(list);
      return;
    }
    countNode.textContent = "";
    labelNode.textContent = "Noch keine Antwort";
    comingNode.textContent = "Noch keine Antwort auf diesem Gerät.";
  }

  function fields(n, saved) {
    var current = [].slice.call(namesBox.querySelectorAll("input")).map(function (input) {
      return input.value;
    });
    namesBox.innerHTML = "";
    var i;
    for (i = 0; i < n; i++) {
      var input = document.createElement("input");
      input.maxLength = 48;
      input.autocomplete = "name";
      input.placeholder = "Name";
      input.setAttribute("aria-label", "Person " + (i + 1));
      input.value = (saved && saved[i]) || current[i] || "";
      namesBox.appendChild(input);
    }
    amountNode.textContent = String(n);
  }

  function saveAnswer(answer) {
    var list = answer === "yes" ? readNames() : [];
    var payload = { answer: answer, names: list };
    try { localStorage.setItem(storeKey, JSON.stringify(payload)); } catch (err) { /* private mode */ }
    showTally(answer, list);
  }

  function armRsvp() {
    if (!party || !yes || !no) return;
    var saved = null;
    try { saved = JSON.parse(localStorage.getItem(storeKey) || "null"); } catch (err) { saved = null; }
    var start = saved && saved.names && saved.names.length ? saved.names.length : 1;
    fields(Math.min(8, start), saved && saved.names);
    if (saved && saved.answer === "yes") {
      yes.classList.add("is-on");
      party.hidden = false;
      showTally("yes", saved.names || []);
    } else if (saved && saved.answer === "no") {
      no.classList.add("is-on");
      showTally("no", []);
    } else {
      showTally("", []);
    }
    yes.addEventListener("click", function () {
      yes.classList.add("is-on");
      no.classList.remove("is-on");
      party.hidden = false;
      saveAnswer("yes");
    });
    no.addEventListener("click", function () {
      no.classList.add("is-on");
      yes.classList.remove("is-on");
      party.hidden = true;
      saveAnswer("no");
    });
    folio.querySelectorAll("[data-step]").forEach(function (button) {
      button.addEventListener("click", function () {
        var n = +amountNode.textContent + +button.getAttribute("data-step");
        if (n < 1 || n > 8) return;
        fields(n);
        saveAnswer("yes");
      });
    });
    namesBox.addEventListener("input", function () { saveAnswer("yes"); });
  }

  var sx = 0;
  var sy = 0;
  var tracking = false;
  function nearest(dir) {
    var panels = [].slice.call(document.querySelectorAll(".folio .panel"));
    var edge = stage.getBoundingClientRect().top + 64;
    var i;
    if (dir > 0) {
      for (i = 0; i < panels.length; i++) {
        if (panels[i].getBoundingClientRect().top > edge) return panels[i];
      }
    } else {
      for (i = panels.length - 1; i >= 0; i--) {
        if (panels[i].getBoundingClientRect().top < edge - 80) return panels[i];
      }
    }
    return null;
  }
  function scrollToPanel(panel) {
    if (!panel) return;
    var top = panel.getBoundingClientRect().top - stage.getBoundingClientRect().top + stage.scrollTop - 16;
    stage.scrollTo({ top: top, behavior: reduce ? "auto" : "smooth" });
  }
  stage.addEventListener("pointerdown", function (e) {
    if (e.target.closest(".scratch, button, input, a")) return;
    sx = e.clientX;
    sy = e.clientY;
    tracking = true;
  });
  stage.addEventListener("pointerup", function (e) {
    if (!tracking) return;
    tracking = false;
    var dy = sy - e.clientY;
    var dx = e.clientX - sx;
    if (Math.abs(dx) > 100 || Math.abs(dy) < 72) return;
    scrollToPanel(nearest(dy > 0 ? 1 : -1));
  });
  stage.addEventListener("pointercancel", function () { tracking = false; });

  function openInvite() {
    if (stage.classList.contains("is-open")) return;
    stage.classList.add("is-open");
    seal.setAttribute("aria-expanded", "true");
    window.requestAnimationFrame(function () {
      drawFoil();
    });
  }

  seal.addEventListener("click", openInvite);
  if (reduce) openInvite();
  if (folio) {
    paintCount();
    window.setInterval(paintCount, 15000);
    armScratch();
    armRsvp();
  }
})();
