"use strict";

/* ================================================================
   1. 애플리케이션 설정과 상태
   화면에 영향을 주는 값을 한 객체에서 관리해
   "이벤트 → 상태 변경 → 렌더링" 흐름을 명확히 합니다.
   ================================================================ */
const GITHUB_USERNAME = "bidulgiya999";
const GITHUB_API_URL = `https://api.github.com/users/${GITHUB_USERNAME}/repos?sort=updated&per_page=100`;
const SCROLL_TOP_THRESHOLD = 300;
const HEADER_SCROLL_THRESHOLD = 60;
const OBSERVER_THRESHOLD = 0.2;

const getStoredTheme = () => {
  try {
    return localStorage.getItem("portfolio-theme");
  } catch {
    return null;
  }
};

const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
const storedTheme = getStoredTheme();

const state = {
  theme: storedTheme === "dark" || storedTheme === "light"
    ? storedTheme
    : systemPrefersDark
      ? "dark"
      : "light",
  menuOpen: false,
  projects: {
    status: "idle",
    items: [],
    error: "",
    activeLanguage: "all",
  },
  form: {
    values: { name: "", email: "", message: "" },
    errors: {},
    touched: new Set(),
  },
};

/* ================================================================
   2. DOM 선택
   querySelector와 querySelectorAll로 필요한 요소를 한 번만 찾습니다.
   ================================================================ */
const siteHeader = document.querySelector("#site-header");
const themeToggle = document.querySelector("#theme-toggle");
const themeIcon = document.querySelector("#theme-icon");
const themeLabel = document.querySelector("#theme-label");
const menuToggle = document.querySelector("#menu-toggle");
const navMenu = document.querySelector("#nav-menu");
const navLinks = document.querySelectorAll('a[href^="#"]');
const scrollTopButton = document.querySelector("#scroll-top");
const revealElements = document.querySelectorAll(".reveal");
const projectsGrid = document.querySelector("#projects-grid");
const projectFilters = document.querySelector("#project-filters");
const contactForm = document.querySelector("#contact-form");
const formStatus = document.querySelector("#form-status");
const formFields = document.querySelectorAll("#contact-form input, #contact-form textarea");
const currentYear = document.querySelector("#current-year");

/* ================================================================
   3. 테마 상태 → 문서 렌더링
   localStorage에는 기기별 사용자 선택만 저장합니다.
   ================================================================ */
const saveTheme = (theme) => {
  try {
    localStorage.setItem("portfolio-theme", theme);
  } catch {
    // 저장소가 차단된 환경에서도 테마 전환 자체는 계속 동작합니다.
  }
};

const renderTheme = () => {
  const isDark = state.theme === "dark";
  document.documentElement.dataset.theme = state.theme;
  themeIcon.textContent = isDark ? "☀" : "◐";
  themeLabel.textContent = isDark ? "라이트 모드" : "다크 모드";
  themeToggle.setAttribute("aria-label", isDark ? "라이트 모드로 전환" : "다크 모드로 전환");
};

themeToggle.addEventListener("click", () => {
  state.theme = state.theme === "dark" ? "light" : "dark";
  saveTheme(state.theme);
  renderTheme();
});

/* ================================================================
   4. 모바일 메뉴와 부드러운 스크롤
   ================================================================ */
const renderMenu = () => {
  navMenu.classList.toggle("active", state.menuOpen);
  menuToggle.classList.toggle("active", state.menuOpen);
  document.body.classList.toggle("menu-open", state.menuOpen);
  menuToggle.setAttribute("aria-expanded", String(state.menuOpen));
  menuToggle.setAttribute("aria-label", state.menuOpen ? "메뉴 닫기" : "메뉴 열기");
};

const closeMenu = () => {
  state.menuOpen = false;
  navMenu.classList.remove("active");
  menuToggle.classList.remove("active");
  document.body.classList.remove("menu-open");
  menuToggle.setAttribute("aria-expanded", "false");
  menuToggle.setAttribute("aria-label", "메뉴 열기");
};

menuToggle.addEventListener("click", () => {
  state.menuOpen = !state.menuOpen;
  renderMenu();
});

navLinks.forEach((link) => {
  link.addEventListener("click", (event) => {
    const targetId = link.getAttribute("href");
    const target = document.querySelector(targetId);

    if (!target) return;
    event.preventDefault();
    closeMenu();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});

/* ================================================================
   5. 스크롤 이벤트 → 헤더와 스크롤 탑 버튼 렌더링
   requestAnimationFrame으로 과도한 화면 갱신을 줄입니다.
   ================================================================ */
let scrollTicking = false;

const renderScrollState = () => {
  const scrollPosition = window.scrollY;
  siteHeader.classList.toggle("scrolled", scrollPosition >= HEADER_SCROLL_THRESHOLD);
  scrollTopButton.classList.toggle("visible", scrollPosition >= SCROLL_TOP_THRESHOLD);
  scrollTicking = false;
};

window.addEventListener("scroll", () => {
  if (!scrollTicking) {
    window.requestAnimationFrame(renderScrollState);
    scrollTicking = true;
  }
});

// 새로고침할 때 URL에 섹션 주소(#projects 등)가 있어도 버튼 상태를 바로 맞춥니다.
renderScrollState();

scrollTopButton.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});

/* ================================================================
   6. Intersection Observer 스크롤 애니메이션
   ================================================================ */
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (reduceMotion || !("IntersectionObserver" in window)) {
  revealElements.forEach((element) => element.classList.add("visible"));
} else {
  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: OBSERVER_THRESHOLD },
  );

  revealElements.forEach((element) => revealObserver.observe(element));
}

/* ================================================================
   7. GitHub API 상태 → Projects UI 렌더링
   외부 문자열은 innerHTML에 넣기 전에 escapeHtml로 이스케이프합니다.
   ================================================================ */
const escapeHtml = (value) => String(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;")
  .replaceAll("'", "&#039;");

const formatDate = (dateString) => new Intl.DateTimeFormat("ko-KR", {
  year: "numeric",
  month: "short",
  day: "numeric",
}).format(new Date(dateString));

const renderProjectFilters = () => {
  const languages = [...new Set(
    state.projects.items
      .map(({ language }) => language)
      .filter(Boolean),
  )].sort((first, second) => first.localeCompare(second));

  projectFilters.hidden = languages.length === 0;
  if (languages.length === 0) {
    projectFilters.innerHTML = "";
    return;
  }

  const filterNames = ["all", ...languages];
  projectFilters.innerHTML = filterNames.map((language) => {
    const isActive = state.projects.activeLanguage === language;
    const label = language === "all" ? "전체" : escapeHtml(language);
    return `
      <button
        class="filter-button${isActive ? " active" : ""}"
        type="button"
        data-language="${escapeHtml(language)}"
        aria-pressed="${isActive}"
      >${label}</button>
    `;
  }).join("");
};

const createProjectCard = (project) => {
  const {
    name,
    description,
    htmlUrl,
    language,
    stars,
    forks,
    updatedAt,
  } = project;

  return `
    <article class="project-card">
      <div class="project-card-header">
        <h3>
          <a class="repo-link" href="${htmlUrl}" target="_blank" rel="noopener noreferrer">
            ${escapeHtml(name)}
          </a>
        </h3>
        <span aria-hidden="true">↗</span>
      </div>
      <p class="project-description">
        ${escapeHtml(description || "프로젝트 설명이 아직 없습니다.")}
      </p>
      <div class="project-meta" aria-label="저장소 정보">
        <span><i class="language-dot" aria-hidden="true"></i>${escapeHtml(language || "기타")}</span>
        <span>★ ${stars}</span>
        <span>⑂ ${forks}</span>
        <span>업데이트 ${escapeHtml(formatDate(updatedAt))}</span>
      </div>
    </article>
  `;
};

const renderProjects = () => {
  const { status, items, error, activeLanguage } = state.projects;
  projectsGrid.setAttribute("aria-busy", String(status === "loading"));

  if (status === "loading") {
    projectFilters.hidden = true;
    projectsGrid.innerHTML = `
      <div class="project-state">
        <span class="spinner" aria-hidden="true"></span>
        <p>프로젝트를 불러오는 중입니다.</p>
      </div>
    `;
    return;
  }

  if (status === "error") {
    projectFilters.hidden = true;
    projectsGrid.innerHTML = `
      <div class="project-state">
        <strong>프로젝트를 불러올 수 없습니다.</strong>
        <p>${escapeHtml(error)}</p>
        <button class="button button-primary" id="retry-projects" type="button">다시 시도</button>
      </div>
    `;
    document.querySelector("#retry-projects").addEventListener("click", loadProjects);
    return;
  }

  if (status === "success" && items.length === 0) {
    projectFilters.hidden = true;
    projectsGrid.innerHTML = `
      <div class="project-state">
        <strong>표시할 프로젝트가 없습니다.</strong>
        <p>공개 저장소가 생성되면 이곳에 자동으로 표시됩니다.</p>
      </div>
    `;
    return;
  }

  renderProjectFilters();
  const filteredProjects = activeLanguage === "all"
    ? items
    : items.filter(({ language }) => language === activeLanguage);

  if (filteredProjects.length === 0) {
    projectsGrid.innerHTML = `
      <div class="project-state">
        <strong>이 언어로 만든 프로젝트가 없습니다.</strong>
        <p>다른 필터를 선택해주세요.</p>
      </div>
    `;
    return;
  }

  projectsGrid.innerHTML = filteredProjects.map(createProjectCard).join("");
};

async function loadProjects() {
  state.projects.status = "loading";
  state.projects.error = "";
  renderProjects();

  const controller = new AbortController();
  const timeoutId = window.setTimeout(() => controller.abort(), 10000);

  try {
    const response = await fetch(GITHUB_API_URL, {
      headers: { Accept: "application/vnd.github+json" },
      signal: controller.signal,
    });

    if (!response.ok) {
      if (response.status === 403) {
        throw new Error("GitHub API 요청 한도에 도달했습니다. 잠시 후 다시 시도해주세요.");
      }
      if (response.status === 404) {
        throw new Error("GitHub 사용자를 찾을 수 없습니다.");
      }
      throw new Error(`GitHub API 응답 오류가 발생했습니다. (${response.status})`);
    }

    const repositories = await response.json();
    state.projects.items = repositories.slice(0, 6).map((repository) => {
      const {
        name,
        description,
        html_url: htmlUrl,
        language,
        stargazers_count: stars,
        forks_count: forks,
        updated_at: updatedAt,
      } = repository;

      const safeUrl = typeof htmlUrl === "string" && htmlUrl.startsWith("https://github.com/")
        ? htmlUrl
        : `https://github.com/${GITHUB_USERNAME}`;

      return {
        name,
        description,
        htmlUrl: safeUrl,
        language,
        stars,
        forks,
        updatedAt,
      };
    });
    state.projects.status = "success";
    state.projects.activeLanguage = "all";
  } catch (error) {
    state.projects.status = "error";
    state.projects.error = error.name === "AbortError"
      ? "요청 시간이 초과되었습니다. 네트워크 연결을 확인해주세요."
      : error.message;
  } finally {
    window.clearTimeout(timeoutId);
    renderProjects();
  }
}

projectFilters.addEventListener("click", (event) => {
  const button = event.target.closest("[data-language]");
  if (!button) return;

  state.projects.activeLanguage = button.dataset.language;
  renderProjects();
});

/* ================================================================
   8. 폼 입력 상태 → 필드별 오류와 성공 메시지 렌더링
   ================================================================ */
const validators = {
  name: (value) => {
    if (!value.trim()) return "이름을 입력해주세요.";
    if (value.trim().length < 2) return "이름은 두 글자 이상 입력해주세요.";
    return "";
  },
  email: (value) => {
    if (!value.trim()) return "이메일을 입력해주세요.";
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(value.trim()) ? "" : "올바른 이메일 형식을 입력해주세요.";
  },
  message: (value) => {
    if (!value.trim()) return "메시지를 입력해주세요.";
    if (value.trim().length < 10) return "메시지는 10자 이상 입력해주세요.";
    return "";
  },
};

const validateField = (fieldName) => {
  const error = validators[fieldName](state.form.values[fieldName]);
  state.form.errors[fieldName] = error;
  return error;
};

const renderFieldValidation = (fieldName) => {
  const field = document.querySelector(`#${fieldName}`);
  const errorElement = document.querySelector(`#${fieldName}-error`);
  const shouldShow = state.form.touched.has(fieldName);
  const error = shouldShow ? state.form.errors[fieldName] : "";

  field.setAttribute("aria-invalid", String(Boolean(error)));
  errorElement.textContent = error;
};

formFields.forEach((field) => {
  field.addEventListener("input", (event) => {
    const { name, value } = event.target;
    state.form.values[name] = value;
    state.form.touched.add(name);
    validateField(name);
    renderFieldValidation(name);
    formStatus.textContent = "";
  });
});

contactForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const fieldNames = Object.keys(state.form.values);

  fieldNames.forEach((fieldName) => {
    state.form.touched.add(fieldName);
    validateField(fieldName);
    renderFieldValidation(fieldName);
  });

  const firstInvalidField = fieldNames.find((fieldName) => state.form.errors[fieldName]);
  if (firstInvalidField) {
    formStatus.textContent = "입력 내용을 다시 확인해주세요.";
    document.querySelector(`#${firstInvalidField}`).focus();
    return;
  }

  formStatus.textContent = "입력 내용을 확인했습니다. 이메일 링크로 연락을 이어가주세요.";
  contactForm.reset();
  state.form.values = { name: "", email: "", message: "" };
  state.form.errors = {};
  state.form.touched.clear();

  fieldNames.forEach(renderFieldValidation);
});

/* ================================================================
   9. 초기 렌더링
   ================================================================ */
currentYear.textContent = new Date().getFullYear();
renderTheme();
renderMenu();
renderScrollState();
loadProjects();
