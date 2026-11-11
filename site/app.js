(function () {
  "use strict";

  var posts = window.POSTS || [];
  var graella = document.getElementById("graella");
  var contador = document.getElementById("num-posts");
  var visor = document.getElementById("visor");
  var visorImg = document.getElementById("visor-img");
  var visorCaption = document.getElementById("visor-caption");
  var visorEtiquetes = document.getElementById("visor-etiquetes");
  var visorMarca = document.getElementById("visor-marca");
  var btnTancar = visor.querySelector(".visor__tancar");
  var btnPrevi = visor.querySelector(".visor__nav--previ");
  var btnSeguent = visor.querySelector(".visor__nav--seguent");
  var avis = document.getElementById("avis");
  var idxActual = -1;
  var avisTimer = null;

  if (contador) contador.textContent = posts.length;

  function milers(n) {
    return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  }

  function mostrarAvis(text) {
    avis.textContent = text;
    avis.classList.add("is-visible");
    clearTimeout(avisTimer);
    avisTimer = setTimeout(function () {
      avis.classList.remove("is-visible");
    }, 2400);
  }

  /* ---------- graella ---------- */
  posts.forEach(function (post, i) {
    var boto = document.createElement("button");
    boto.type = "button";
    boto.className = "casella";
    boto.setAttribute("aria-label", "Obre la publicació: " + post.titol);

    var img = document.createElement("img");
    img.src = "assets/posts/" + post.fitxer;
    img.alt = post.alt || post.titol;
    img.loading = i < 9 ? "eager" : "lazy";
    img.decoding = "async";
    img.width = 1080;
    img.height = 1350;
    boto.appendChild(img);

    var vel = document.createElement("span");
    vel.className = "casella__vel";
    vel.innerHTML = "<span>♥ " + milers(post.magrada) + "</span><span>💬 " + post.comentaris + "</span>";
    boto.appendChild(vel);

    if (post.pendent) {
      var estat = document.createElement("span");
      estat.className = "casella__estat";
      estat.textContent = "PENDENT DE FOTO";
      boto.appendChild(estat);
    }

    boto.addEventListener("click", function () { obrir(i); });
    graella.appendChild(boto);
  });

  /* ---------- visor ---------- */
  function obrir(i) {
    idxActual = i;
    var post = posts[i];

    visorImg.src = "assets/posts/" + post.fitxer;
    visorImg.alt = post.alt || post.titol;
    visorCaption.textContent = post.caption;
    visorEtiquetes.textContent = post.hashtags;
    visorMarca.textContent = milers(post.magrada) + " m'agrada · " + post.comentaris + " comentaris";

    visor.hidden = false;
    document.body.style.overflow = "hidden";
    btnTancar.focus();

    btnPrevi.hidden = i === 0;
    btnSeguent.hidden = i === posts.length - 1;
  }

  function tancar() {
    visor.hidden = true;
    document.body.style.overflow = "";
    var casella = graella.children[idxActual];
    if (casella) casella.focus();
  }

  function moure(pas) {
    var nou = idxActual + pas;
    if (nou < 0 || nou >= posts.length) return;
    obrir(nou);
  }

  btnTancar.addEventListener("click", tancar);
  btnPrevi.addEventListener("click", function () { moure(-1); });
  btnSeguent.addEventListener("click", function () { moure(1); });

  visor.addEventListener("click", function (e) {
    if (e.target === visor) tancar();
  });

  document.addEventListener("keydown", function (e) {
    if (visor.hidden) return;
    if (e.key === "Escape") tancar();
    else if (e.key === "ArrowLeft") moure(-1);
    else if (e.key === "ArrowRight") moure(1);
  });

  /* ---------- botons de mostra ---------- */
  document.querySelectorAll("[data-avis]").forEach(function (b) {
    b.addEventListener("click", function () { mostrarAvis(b.getAttribute("data-avis")); });
  });
})();
