/* Facebook Ads Agency Chicago — menus, forms, tools, tracking */
(function () {
  "use strict";
  var dl = (window.dataLayer = window.dataLayer || []);
  function track(event, data) {
    var o = { event: event };
    for (var k in data || {}) o[k] = data[k];
    dl.push(o);
  }

  /* ---------- Desktop dropdowns ---------- */
  var dds = Array.prototype.slice.call(document.querySelectorAll(".has-dd"));
  var finePointer = window.matchMedia && window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  function setOpen(li, open) {
    li.classList.toggle("open", open);
    li.querySelector(".dd-btn").setAttribute("aria-expanded", open ? "true" : "false");
  }
  function closeAll(except) {
    dds.forEach(function (li) { if (li !== except) setOpen(li, false); });
  }
  dds.forEach(function (li) {
    var btn = li.querySelector(".dd-btn");
    btn.addEventListener("click", function () {
      var open = !li.classList.contains("open");
      closeAll(li);
      setOpen(li, open);
    });
    if (finePointer) {
      var t;
      li.addEventListener("mouseenter", function () { clearTimeout(t); closeAll(li); setOpen(li, true); });
      li.addEventListener("mouseleave", function () { t = setTimeout(function () { setOpen(li, false); }, 150); });
    }
    li.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && li.classList.contains("open")) {
        setOpen(li, false);
        btn.focus();
      } else if (ev.key === "ArrowDown") {
        var links = li.querySelectorAll(".dd a");
        if (!links.length) return;
        ev.preventDefault();
        if (!li.classList.contains("open")) setOpen(li, true);
        var i = Array.prototype.indexOf.call(links, document.activeElement);
        links[Math.min(i + 1, links.length - 1)].focus();
      } else if (ev.key === "ArrowUp") {
        var ls = li.querySelectorAll(".dd a");
        var j = Array.prototype.indexOf.call(ls, document.activeElement);
        if (j > 0) { ev.preventDefault(); ls[j - 1].focus(); }
        else if (j === 0) { ev.preventDefault(); btn.focus(); }
      }
    });
    li.addEventListener("focusout", function (ev) {
      if (!li.contains(ev.relatedTarget)) setOpen(li, false);
    });
  });
  document.addEventListener("click", function (ev) {
    if (!ev.target.closest(".has-dd")) closeAll();
  });

  /* ---------- Mobile menu ---------- */
  var toggle = document.querySelector(".menu-toggle");
  var menu = document.getElementById("mobile-menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") !== "true";
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Close" : "Menu";
      menu.hidden = !open;
      document.body.classList.toggle("menu-open", open);
    });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && !menu.hidden) {
        menu.hidden = true;
        document.body.classList.remove("menu-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.textContent = "Menu";
        toggle.focus();
      }
    });
  }

  /* ---------- Contact click tracking ---------- */
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("a[href]");
    if (!a) return;
    var href = a.getAttribute("href");
    var method = href.indexOf("tel:") === 0 ? "phone" : href.indexOf("sms:") === 0 ? "sms" : href.indexOf("mailto:") === 0 ? "email" : null;
    if (method) {
      track("contact_click", { contact_method: method, link_location: a.closest(".float-contact") ? "floating_button" : a.closest("footer") ? "footer" : "page" });
    }
  });

  /* ---------- Free tools ---------- */
  var RESULTS_KEY = "faac_tool_results";
  function num(root, id) {
    var el = root.querySelector("#" + id);
    var v = el ? parseFloat(el.value) : NaN;
    return isFinite(v) ? v : NaN;
  }
  function money(v, dec) {
    if (!isFinite(v)) return "-";
    return "$" + v.toLocaleString("en-US", { minimumFractionDigits: dec || 0, maximumFractionDigits: dec || 0 });
  }
  function count(v, dec) {
    if (!isFinite(v)) return "-";
    return v.toLocaleString("en-US", { maximumFractionDigits: dec == null ? 0 : dec });
  }
  var calculators = {
    "ad-budget-calculator": function (root) {
      var budget = num(root, "budget"), cpl = num(root, "cpl"), close = num(root, "close"), value = num(root, "value"), goal = num(root, "goal");
      var leads = cpl > 0 ? budget / cpl : NaN;
      var customers = leads * (close / 100);
      var cpa = customers > 0 ? budget / customers : NaN;
      var revenue = customers * value;
      var roas = budget > 0 ? revenue / budget : NaN;
      var goalBudget = goal > 0 && cpl > 0 ? goal * cpl : NaN;
      var out = {
        leads: count(leads, 1), customers: count(customers, 1), cpa: money(cpa),
        revenue: money(revenue), roas: isFinite(roas) ? money(roas, 2) : "-", goalBudget: money(goalBudget)
      };
      var lines = [
        "Inputs: budget " + money(budget) + "/mo, cost per lead " + money(cpl) + ", close rate " + count(close, 1) + "%, customer value " + money(value),
        "Leads per month: " + out.leads,
        "New customers per month: " + out.customers,
        "Cost per customer: " + out.cpa,
        "Revenue: " + out.revenue,
        "Return per $1: " + out.roas
      ];
      if (isFinite(goalBudget)) lines.push("Budget for " + count(goal) + " leads: " + out.goalBudget);
      var row = root.querySelector("[data-goal-row]");
      if (row) row.hidden = !isFinite(goalBudget);
      return { out: out, summary: lines.join("\n") };
    },
    "break-even-calculator": function (root) {
      var value = num(root, "value"), margin = num(root, "margin"), close = num(root, "close");
      var roas = margin > 0 ? 100 / margin : NaN;
      var cpa = value * (margin / 100);
      var cpl = cpa * (close / 100);
      var out = { roas: isFinite(roas) ? count(roas, 2) + "x" : "-", cpa: money(cpa), cpl: money(cpl) };
      var lines = [
        "Inputs: sale value " + money(value) + ", gross margin " + count(margin, 1) + "%, close rate " + count(close, 1) + "%",
        "Break-even ROAS: " + out.roas,
        "Max cost per customer: " + out.cpa,
        "Max cost per lead: " + out.cpl
      ];
      return { out: out, summary: lines.join("\n") };
    }
  };

  Array.prototype.forEach.call(document.querySelectorAll(".tool[data-tool]"), function (root) {
    var slug = root.getAttribute("data-tool");
    var name = root.getAttribute("data-tool-name");
    var calc = calculators[slug];
    if (!calc) return;
    var used = false, last = null;
    function run(fromUser) {
      last = calc(root);
      for (var k in last.out) {
        var el = root.querySelector('[data-out="' + k + '"]');
        if (el) el.textContent = last.out[k];
      }
      if (fromUser && !used) {
        used = true;
        track("tool_used", { tool_name: slug });
      }
    }
    root.addEventListener("input", function () { run(true); });
    run(false);
    var cta = root.querySelector(".tool-to-offer");
    if (cta) {
      cta.addEventListener("click", function () {
        run(false);
        try {
          sessionStorage.setItem(RESULTS_KEY, JSON.stringify({ tool: slug, name: name, summary: last.summary }));
        } catch (err) { /* storage blocked: results just won't carry over */ }
        track("tool_to_offer_click", { tool_name: slug });
      });
    }
  });

  /* ---------- Forms → HubSpot ---------- */
  var CFG = window.SITE_CONFIG || {};
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  function getCookie(name) {
    var m = document.cookie.match(new RegExp("(?:^|; )" + name + "=([^;]*)"));
    return m ? decodeURIComponent(m[1]) : null;
  }

  function showError(field, msg) {
    var wrap = field.closest(".field");
    if (!wrap) return;
    wrap.classList.add("has-error");
    field.setAttribute("aria-invalid", "true");
    var p = wrap.querySelector(".field-error");
    if (!p) {
      p = document.createElement("p");
      p.className = "field-error";
      p.id = field.id + "-error";
      wrap.appendChild(p);
      field.setAttribute("aria-describedby", p.id);
    }
    p.textContent = msg;
  }
  function clearError(field) {
    var wrap = field.closest(".field");
    if (!wrap) return;
    wrap.classList.remove("has-error");
    field.removeAttribute("aria-invalid");
    var p = wrap.querySelector(".field-error");
    if (p) p.remove();
    field.removeAttribute("aria-describedby");
  }

  function validate(form) {
    var firstBad = null;
    Array.prototype.forEach.call(form.querySelectorAll("input, select, textarea"), function (f) {
      if (f.name === "hp_field") return;
      clearError(f);
      var v = (f.value || "").trim();
      var bad = null;
      if (f.required && !v) bad = "Please fill this in.";
      else if (f.type === "email" && v && !EMAIL_RE.test(v)) bad = "Please enter a valid email address.";
      if (bad) { showError(f, bad); if (!firstBad) firstBad = f; }
    });
    if (firstBad) firstBad.focus();
    return !firstBad;
  }

  function splitName(full) {
    var parts = full.trim().split(/\s+/);
    return { first: parts.shift() || "", last: parts.join(" ") };
  }

  function postTo(host, payload) {
    return fetch(host + "/submissions/v3/integration/submit/" + CFG.portal + "/" + CFG.form, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
  }

  function fieldsMissingFromForm(body) {
    var names = [];
    (body && body.errors || []).forEach(function (er) {
      if (er.errorType === "FIELD_NOT_IN_FORM_DEFINITION" || /form definition/i.test(er.message || "")) {
        var m = (er.message || "").match(/fields\.([\w-]+)/);
        if (m) names.push(m[1]);
      }
    });
    return names;
  }

  async function submitToHubSpot(fields, extraLines) {
    var context = { pageUri: location.href, pageName: document.title };
    var hutk = getCookie("hubspotutk");
    if (hutk) context.hutk = hutk;

    function payloadFrom(map) {
      var arr = [];
      for (var k in map) if (map[k]) arr.push({ objectTypeId: "0-1", name: k, value: map[k] });
      return { fields: arr, context: context };
    }

    var hosts = ["https://api.hsforms.com", "https://api-" + (CFG.region || "na1") + ".hsforms.com"];
    var res, host = hosts[0];
    res = await postTo(host, payloadFrom(fields));
    if (res.status === 404) {
      host = hosts[1];
      res = await postTo(host, payloadFrom(fields));
    }
    if (res.status === 400) {
      // A field isn't on the HubSpot form: move its value into the message and try once more.
      var body = null;
      try { body = await res.clone().json(); } catch (err) { /* ignore */ }
      var missing = fieldsMissingFromForm(body);
      if (missing.length && missing.indexOf("message") === -1) {
        var folded = [];
        missing.forEach(function (n) {
          if (fields[n]) folded.push(n.charAt(0).toUpperCase() + n.slice(1) + ": " + fields[n]);
          delete fields[n];
        });
        fields.message = (folded.join("\n") + (fields.message ? "\n\n" + fields.message : "")).trim();
        res = await postTo(host, payloadFrom(fields));
      }
    }
    return res.ok;
  }

  Array.prototype.forEach.call(document.querySelectorAll("form.lead-form"), function (form) {
    var formName = form.getAttribute("data-form");
    var status = form.querySelector(".form-status");

    // Calculator results carried over from a free tool
    var resultsBox = form.querySelector(".tool-results");
    var toolResults = null;
    if (resultsBox) {
      try { toolResults = JSON.parse(sessionStorage.getItem(RESULTS_KEY) || "null"); } catch (err) { toolResults = null; }
      if (toolResults && toolResults.summary) {
        resultsBox.hidden = false;
        resultsBox.querySelector(".tool-results-body").textContent = toolResults.name + "\n" + toolResults.summary;
        resultsBox.querySelector(".tool-results-remove").addEventListener("click", function () {
          toolResults = null;
          try { sessionStorage.removeItem(RESULTS_KEY); } catch (err) { /* ignore */ }
          resultsBox.hidden = true;
        });
      }
    }

    form.addEventListener("input", function (ev) {
      if (ev.target.closest(".field.has-error")) clearError(ev.target);
      if (!form.querySelector(".has-error")) { status.textContent = ""; status.classList.remove("error"); }
    });

    form.addEventListener("submit", async function (ev) {
      ev.preventDefault();
      status.textContent = "";
      status.classList.remove("error");
      if (form.hp_field && form.hp_field.value) return; // bot
      if (!validate(form)) {
        status.textContent = "Please check the highlighted fields.";
        status.classList.add("error");
        return;
      }
      var get = function (n) { var el = form.elements[n]; return el ? (el.value || "").trim() : ""; };
      var name = splitName(get("name"));
      var lines = ["Form: " + (formName === "free_audit" ? "Free account audit" : "Contact")];
      Array.prototype.forEach.call(form.querySelectorAll("[data-label]"), function (el) {
        var v = (el.value || "").trim();
        if (v) lines.push(el.getAttribute("data-label") + ": " + v);
      });
      if (toolResults && toolResults.summary) {
        lines.push("", "Calculator results (" + toolResults.name + "):", toolResults.summary);
      }
      var fields = {
        firstname: name.first,
        lastname: name.last,
        email: get("email"),
        phone: get("phone"),
        company: get("company"),
        website: get("website"),
        message: lines.join("\n")
      };

      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      var label = btn.textContent;
      btn.textContent = "Sending...";
      var ok = false;
      try { ok = await submitToHubSpot(fields); } catch (err) { ok = false; }
      btn.disabled = false;
      btn.textContent = label;

      if (ok) {
        track("generate_lead", { form_name: formName, tool_name: toolResults ? toolResults.tool : undefined });
        try { sessionStorage.removeItem(RESULTS_KEY); } catch (err) { /* ignore */ }
        var done = document.createElement("div");
        done.className = "form-success";
        done.setAttribute("tabindex", "-1");
        done.innerHTML = "<h3>Thanks, we got it.</h3><p>" +
          (formName === "free_audit"
            ? "We'll review your details and reach out to schedule your audit."
            : "We'll get back to you soon.") +
          " Need us sooner? Call or text <a href=\"tel:+17083931976\">(708) 393-1976</a>.</p>";
        form.replaceWith(done);
        done.focus();
      } else {
        status.innerHTML = "Something went wrong sending your message. Please try again, or email <a href=\"mailto:support@facebookadsagencychicago.com\">support@facebookadsagencychicago.com</a>.";
        status.classList.add("error");
      }
    });
  });
})();
