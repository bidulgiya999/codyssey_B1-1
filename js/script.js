"use strict";

/* ================================================================
   1. 애플리케이션 설정과 상태
   화면에 영향을 주는 값을 한 객체에서 관리해
   "이벤트 → 상태 변경 → 렌더링" 흐름을 명확히 합니다.
   ================================================================ */
const GITHUB_USERNAME = "bidulgiya999";
const GITHUB_API_URL = `https://api.github.com/users/${GITHUB_USERNAME}/repos?sort=updated&per_page=100`;
const FORM_ENDPOINT = "https://formsubmit.co/ajax/jae94bro@gmail.com";
const SCROLL_TOP_THRESHOLD = 300;
const HEADER_SCROLL_THRESHOLD = 60;
const OBSERVER_THRESHOLD = 0.2;

// 학습 문서의 링크가 가리킬 수 있는 홈페이지 요소를 허용 목록으로 제한합니다.
// 예: index.html?focus=hero-visual#hero → Hero 오른쪽 이미지 강조
const GUIDE_TARGETS = {
  header: { selector: "#site-header", label: "상단 헤더와 내비게이션" },
  hero: { selector: "#hero", label: "첫 화면(Hero) 전체" },
  "hero-copy": { selector: ".hero-copy", label: "첫 화면 왼쪽 소개 문구" },
  "hero-visual": { selector: ".hero-visual", label: "첫 화면 오른쪽 MRI 히트맵 이미지" },
  about: { selector: "#about", label: "About 전체 영역" },
  profile: { selector: ".profile-frame", label: "About의 프로필 사진" },
  skills: { selector: "#skills", label: "Skills 전체 영역" },
  "skill-cards": { selector: ".skills-grid", label: "기술 스택 카드 모음" },
  projects: { selector: "#projects", label: "GitHub Projects 전체 영역" },
  "project-filters": { selector: "#project-filters", label: "프로젝트 언어 필터" },
  "project-cards": { selector: "#projects-grid", label: "GitHub 프로젝트 카드 목록" },
  contact: { selector: "#contact", label: "Contact 전체 영역" },
  "contact-form": { selector: "#contact-form", label: "이름·이메일·메시지 입력 폼" },
  footer: { selector: ".site-footer", label: "페이지 하단 Footer" },
  "scroll-top": { selector: "#scroll-top", label: "맨 위로 이동 버튼" },
};

// 브라우저가 저장소 접근을 막더라도 사이트가 중단되지 않도록 안전하게 값을 읽습니다.
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
    status: "idle",
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
const formUrlField = document.querySelector("#form-url");
const formFields = document.querySelectorAll("#contact-form [data-validate]");
const submitButton = document.querySelector(".submit-button");
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

// 상태 객체의 테마 값을 실제 화면과 스크린 리더용 설명에 함께 반영합니다.
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
// 메뉴의 열림 상태를 class와 ARIA 속성에 동시에 반영합니다.
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

// 스크롤 위치에 따라 헤더 강조와 TOP 버튼 노출 여부만 갱신합니다.
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

// 학습 문서에서 넘어온 링크라면 정확한 대상까지 이동한 뒤 잠시 강조합니다.
const highlightGuideTarget = () => {
  const targetKey = new URLSearchParams(window.location.search).get("focus");
  const targetInfo = GUIDE_TARGETS[targetKey];

  if (!targetInfo) return;

  const target = document.querySelector(targetInfo.selector);
  if (!target) return;

  const wasVisible = target.classList.contains("visible");
  const needsPositioning = window.getComputedStyle(target).position === "static";

  if (needsPositioning) target.classList.add("guide-highlight-positioned");
  if (targetKey === "scroll-top") target.classList.add("visible");
  target.classList.add("guide-highlight");
  target.dataset.guideHighlight = `학습 가이드 위치 · ${targetInfo.label}`;
  target.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "center" });

  window.setTimeout(() => {
    target.classList.remove("guide-highlight");
    target.classList.remove("guide-highlight-positioned");
    if (targetKey === "scroll-top" && !wasVisible) target.classList.remove("visible");
    delete target.dataset.guideHighlight;
  }, 5000);
};

/* ================================================================
   7. GitHub API 상태 → Projects UI 렌더링
   외부 문자열은 innerHTML에 넣기 전에 escapeHtml로 이스케이프합니다.
   ================================================================ */
// GitHub에서 받은 문자열이 HTML로 해석되지 않도록 특수문자를 치환합니다.
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

// 저장소의 대표 언어를 중복 없이 모아 동적 필터 버튼을 만듭니다.
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

// API 응답 한 건을 화면에 표시할 프로젝트 카드 HTML로 변환합니다.
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

// loading/error/empty/success 상태마다 서로 다른 화면을 그립니다.
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

// 요청이 10초를 넘으면 중단하고, 필요한 값만 화면용 객체로 정리합니다.
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

// 부모 요소에서 클릭을 한 번만 감지하는 이벤트 위임 방식입니다.
projectFilters.addEventListener("click", (event) => {
  const button = event.target.closest("[data-language]");
  if (!button) return;

  state.projects.activeLanguage = button.dataset.language;
  renderProjects();
});

/* ================================================================
   8. 폼 입력 상태 → 필드별 오류와 성공 메시지 렌더링
   ================================================================ */
// 필드별 검증 규칙을 한 객체에 모아 입력 및 제출 시 동일하게 재사용합니다.
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

// 검증 결과를 상태에 저장해 화면 렌더링과 데이터 처리를 분리합니다.
const validateField = (fieldName) => {
  const error = validators[fieldName](state.form.values[fieldName]);
  state.form.errors[fieldName] = error;
  return error;
};

// 사용자가 한 번이라도 입력한 필드에만 오류를 표시합니다.
const renderFieldValidation = (fieldName) => {
  const field = document.querySelector(`#${fieldName}`);
  const errorElement = document.querySelector(`#${fieldName}-error`);
  const shouldShow = state.form.touched.has(fieldName);
  const error = shouldShow ? state.form.errors[fieldName] : "";

  field.setAttribute("aria-invalid", String(Boolean(error)));
  errorElement.textContent = error;
};

// 전송 중에는 중복 제출을 막고 버튼 문구로 진행 상태를 안내합니다.
const renderSubmitState = () => {
  const isSubmitting = state.form.status === "submitting";
  submitButton.disabled = isSubmitting;
  submitButton.textContent = isSubmitting ? "전송 중..." : "메시지 보내기";
};

// FormSubmit이 로컬 파일로 오인하지 않도록 현재 HTTP 페이지 주소를 명시합니다.
const getCurrentFormUrl = () => new URL(window.location.pathname, window.location.origin).href;

formFields.forEach((field) => {
  field.addEventListener("input", (event) => {
    const { name, value } = event.target;
    state.form.values[name] = value;
    state.form.touched.add(name);
    validateField(name);
    renderFieldValidation(name);
    formStatus.textContent = "";
    formStatus.dataset.status = "";
  });
});

contactForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (state.form.status === "submitting") return;

  const fieldNames = Object.keys(state.form.values);

  fieldNames.forEach((fieldName) => {
    // 브라우저 자동 완성으로 input 이벤트가 생략된 경우에도 현재 값을 다시 읽습니다.
    state.form.values[fieldName] = contactForm.elements[fieldName].value;
    state.form.touched.add(fieldName);
    validateField(fieldName);
    renderFieldValidation(fieldName);
  });

  const firstInvalidField = fieldNames.find((fieldName) => state.form.errors[fieldName]);
  if (firstInvalidField) {
    formStatus.textContent = "입력 내용을 다시 확인해주세요.";
    formStatus.dataset.status = "error";
    document.querySelector(`#${firstInvalidField}`).focus();
    return;
  }

  state.form.status = "submitting";
  formStatus.textContent = "";
  formStatus.dataset.status = "";
  renderSubmitState();

  const controller = new AbortController();
  const timeoutId = window.setTimeout(() => controller.abort(), 10000);
  const payload = Object.fromEntries(new FormData(contactForm).entries());
  payload._url = getCurrentFormUrl();

  try {
    const response = await fetch(FORM_ENDPOINT, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
      signal: controller.signal,
    });

    const result = await response.json().catch(() => ({}));
    const serviceRejected = result.success === false || result.success === "false";
    const serviceMessage = typeof result.message === "string" ? result.message : "";
    const needsActivation = serviceRejected && /activat/i.test(serviceMessage);

    // 첫 요청은 전송 실패가 아니라 수신 이메일 소유권 확인 단계입니다.
    if (needsActivation) {
      formStatus.textContent = "FormSubmit 활성화 메일을 보냈습니다. Gmail에서 Activate Form을 누른 뒤 다시 전송해주세요.";
      formStatus.dataset.status = "pending";
      return;
    }

    if (!response.ok || serviceRejected) {
      throw new Error(serviceMessage || `메일 전송 서비스 응답 오류가 발생했습니다. (${response.status})`);
    }

    formStatus.textContent = "메시지를 전송했습니다. 첫 사용이라면 수신함의 FormSubmit 인증 메일을 승인해주세요.";
    formStatus.dataset.status = "success";
    contactForm.reset();
    state.form.values = { name: "", email: "", message: "" };
    state.form.errors = {};
    state.form.touched.clear();
    fieldNames.forEach(renderFieldValidation);
  } catch (error) {
    const isLocalFileError = /web server|HTML files/i.test(error.message);
    const message = error.name === "AbortError"
      ? "전송 시간이 초과되었습니다. 네트워크 연결을 확인한 뒤 다시 시도해주세요."
      : isLocalFileError
        ? "HTML 파일을 직접 열지 말고 VS Code Live Server 주소에서 실행해주세요."
        : "메시지를 전송하지 못했습니다. 잠시 후 다시 시도하거나 이메일 주소로 직접 연락해주세요.";
    console.error("문의 폼 전송 오류:", error);
    formStatus.textContent = message;
    formStatus.dataset.status = "error";
  } finally {
    window.clearTimeout(timeoutId);
    state.form.status = "idle";
    renderSubmitState();
  }
});

/* ================================================================
   9. 초기 렌더링
   ================================================================ */
currentYear.textContent = new Date().getFullYear();
renderTheme();
renderMenu();
renderScrollState();
renderSubmitState();
formUrlField.value = getCurrentFormUrl();
loadProjects();
highlightGuideTarget();
