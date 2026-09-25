# EconoCausal Implementation Plan

## Audit Summary

### A. Existing project

- The frontend is a Vite React app with React Router, Axios, Plotly.js, and `react-plotly.js` already installed.
- Routes are declared for Dashboard, Data Upload, Causal Analysis, Customer Analysis, Prescription, Optimization, Reports, Monitoring, and Settings.
- Dashboard, upload, causal analysis, customer analysis, prescription, optimization, and reports pages already exist and use a centralized mock service layer.
- Existing reusable surfaces include the sidebar, header, customer table concepts, budget input concepts, drag-and-drop upload concepts, and Plotly chart wrappers for ITE, uplift, Qini, propensity, revenue, and ROI.
- Backend currently contains DML feature extraction, LightGBM estimators, EconML `LinearDML` training, ITE/ATE evaluation, and ITE CSV export. There is no REST application yet.
- The raw retail dataset and an ITE output exist. The notebook flow is the main executable backend integration today.

### B. Stitch provides

- A coherent dark enterprise causal-AI visual system: deep navy/obsidian surfaces, thin slate borders, violet causal emphasis, emerald/rose/amber semantic states, Geist/Inter/JetBrains Mono typography, compact 8px-or-less geometry, and tonal elevation.
- Screen references for dashboard overview, causal analysis, customer segments, data upload preview, prescription optimization, and system monitoring/reports.
- Reusable interaction patterns: fixed sidebar, sticky header, status badges, dense tables, right-side customer detail drawer, KPI grids, causal chart panels, refutation cards, robustness score, drift warning, and export actions.

### C. Needs modification

- Preserve the current route/page structure, but align its spacing, card geometry, typography, responsive behavior, and interaction states more closely with Stitch.
- Replace fabricated upload metadata with parsed CSV metadata and route upload/validation/analysis through the service layer.
- Consolidate the duplicate legacy mock data and obsolete component styles into the central data contract.
- Make budget validation and discount-tier selection controlled and enforceable.
- Replace report alerts with downloadable/generated artifacts where the backend is available, with clear mock fallback states.
- Add loading, empty, error, success, disabled, and mobile navigation states consistently.

### D. Missing

- `Monitoring.jsx` and `Settings.jsx`, which currently prevent the frontend production build.
- FastAPI app, request/response schemas, health/upload/validation/analysis/ITE/propensity/customer/optimization/report/monitoring routes.
- SciPy optimization, revenue/ROI calculations, random-targeting comparison, causal refutation execution, data validation, drift detection, model result persistence, and propensity/allocation exports.
- Cleaned data output and automated data, ML, optimization, API, frontend-contract, and end-to-end tests.
- Architecture, methodology, and results documentation updates.

### E. Preserve

- The existing Stitch-inspired CSS token vocabulary and Plotly dependency choices.
- Existing page layouts and reusable chart components where their behavior is sound.
- Mock data as a deterministic development fallback while backend integration is incomplete.
- Existing DML service boundaries and notebook outputs, extending their contracts rather than rewriting the causal engine unnecessarily.

## Architecture Map

| Stitch screen/pattern | React surface | Shared logic/data |
|---|---|---|
| Dashboard overview | `pages/Dashboard.jsx` | KPI summary, category breakdown, ITE/uplift/Qini charts, model status |
| Data upload preview | `pages/DataUploadPage.jsx`, `components/DataUpload.jsx` | upload service, CSV metadata parser, validation service, preview table |
| Causal deep dive | `pages/CausalAnalysis.jsx` | causal metrics, DAG view, refutation results, ITE and propensity charts |
| Customer segment analysis | `pages/CustomerAnalysis.jsx`, `components/CustomerTable.jsx` | customer query/filter model, detail drawer, recommendation data |
| Prescription optimization | `pages/Prescription.jsx`, `components/BudgetInput.jsx` | optimization request, budget constraints, allocation table/chart |
| Optimization results | `pages/Optimization.jsx` | optimized/random comparison, revenue/ROI charts |
| Reports and monitoring | `pages/Reports.jsx`, new `pages/Monitoring.jsx` | report/export service, health/quality/drift service |
| Application preferences | new `pages/Settings.jsx` | local preferences only; no secrets |

## Execution Order

1. **Frontend build repair and shared shell**
   - Add Monitoring and Settings pages.
   - Keep all existing routes live and add mobile navigation behavior.
   - Normalize shared status, button, table, tooltip, and empty-state patterns.

2. **Central data/service contract**
   - Make mock data deterministic and expose one customer/result schema.
   - Update `api.js` to support a real REST base URL with mock fallback and explicit error handling.
   - Keep pages thin: data loading and mutations belong in services/hooks, not duplicated in each page.

3. **Planner-complete frontend workflows**
   - Connect upload, validation, analysis, customer filters/detail, budget constraints, optimization, reports, monitoring, and settings.
   - Reuse current chart components, adding missing treatment-category and discount-allocation Plotly charts where required.
   - Ensure charts accept data props and remain responsive and interactive.

4. **Backend/API implementation**
   - Add FastAPI entrypoint, Pydantic schemas, route modules, and CORS configuration for the Vite dev server.
   - Add validation and drift services, refutation service, optimization service, and model/result store.
   - Extend causal outputs with treatment, outcome, propensity, category, discount, expected gain, and ROI.
   - Provide `/health`, `/upload`, `/validate`, `/causal-analysis`, `/ite`, `/propensity`, `/customers`, `/optimization`, `/reports`, and `/monitoring` without duplicate equivalent routes.

5. **Artifacts and tests**
   - Generate or document cleaned data, propensity scores, and optimized allocation outputs.
   - Add tests for data quality, propensity and ITE ranges, refutation status, optimization edge cases, API validation, and frontend response compatibility.
   - Fix the data-generation notebook's absent-file assumption so all documented notebook entry points use the repository dataset.

6. **Validation and polish**
   - Run `npm install`, `npm run lint`, `npm run build`, backend tests, and a dev-server smoke check.
   - Verify every route, upload/validation flow, budget constraints, chart render, table filtering/detail, exports, and responsive layouts.
   - Compare against Stitch screenshots and retain causal explanations so metrics are never presented as ordinary prediction scores.

## Key Decisions

- Use the existing React/Vite/Plotly stack and FastAPI/Pydantic for the REST boundary; no new frontend state library or cloud infrastructure.
- Use a mock-first service adapter so the demo remains usable without a running backend, while real API calls can be enabled through configuration.
- Treat `Persuadable`, `Sure Thing`, `Lost Cause`, and `Do Not Disturb` as the canonical UI categories; retain causal terminology for ATE, ITE, propensity, uplift, Qini, DML, and DoWhy.
- Preserve user worktree changes and edit only the modules needed for the planner and build requirements.

## Validation Gates

- Frontend production build passes with no unresolved imports.
- All nine navigation destinations render without dead links.
- Mock mode supports the full demonstration flow from upload through report.
- Backend endpoints validate inputs and return a stable schema.
- Causal and optimization tests cover the explicit planner edge cases.
- Desktop, tablet, and mobile layouts have no clipped controls or overlapping content.
