import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

const PAGE_TITLES = {
  '/': 'Dashboard',
  '/upload': 'Data Upload',
  '/causal-analysis': 'Causal Analysis',
  '/customers': 'Customer Analysis',
  '/prescription': 'Prescription',
  '/optimization': 'Optimization',
  '/reports': 'Reports',
  '/monitoring': 'System Monitoring',
  '/settings': 'Settings',
};

const API_BASE = 'http://localhost:8000';

export default function Header({ apiConnected = true }) {
  const { pathname } = useLocation();
  const title = PAGE_TITLES[pathname] ?? 'Pricewise';

  const [datasetRows, setDatasetRows] = useState(0);

  useEffect(() => {
    const fetchDatasetInfo = async () => {
      try {
        const response = await fetch(`${API_BASE}/dataset-info`);

        if (!response.ok) {
          throw new Error('Failed to fetch dataset information');
        }

        const data = await response.json();

        setDatasetRows(data.rows ?? 0);
      } catch (error) {
        console.error('Dataset info error:', error);
        setDatasetRows(0);
      }
    };

    fetchDatasetInfo();

    // Refresh when navigating between pages
    const interval = setInterval(fetchDatasetInfo, 3000);

    return () => clearInterval(interval);
  }, [pathname]);

  return (
    <header className="top-header">

      {/* Left: Search */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
        <div className="header-search">
          <span
            className="material-symbols-outlined text-muted"
            style={{ fontSize: 18, opacity: 0.6 }}
          >
            search
          </span>

          <input
            type="text"
            placeholder="Search insights..."
          />
        </div>

        <span
          style={{
            fontFamily: 'var(--font-display)',
            fontSize: 18,
            fontWeight: 600,
            color: 'var(--on-surface)',
          }}
        >
          {title}
        </span>
      </div>

      {/* Right: Actions */}
      <div className="header-actions">

        {/* Dataset status */}
        <div
          style={{
            fontFamily: 'var(--font-mono)',
            fontSize: 11,
            color: 'var(--on-surface-var)',
            padding: '4px 12px',
            border: '1px solid var(--border)',
            borderRadius: 100,
            display: 'flex',
            alignItems: 'center',
            gap: 6,
          }}
        >
          <span
            className="material-symbols-outlined"
            style={{ fontSize: 14 }}
          >
            dataset
          </span>

          {datasetRows.toLocaleString()} rows
        </div>

        {/* API status */}
        <div className="header-status-badge">
          <span
            className="status-dot"
            style={{
              background: apiConnected
                ? 'var(--success)'
                : 'var(--danger)',
            }}
          />

          {apiConnected ? 'API LIVE' : 'API OFFLINE'}
        </div>

        {/* Notifications */}
        <button className="header-icon-btn">
          <span
            className="material-symbols-outlined"
            style={{ fontSize: 20 }}
          >
            notifications
          </span>
        </button>

        {/* Wi-fi / connection */}
        <button className="header-icon-btn">
          <span
            className="material-symbols-outlined"
            style={{ fontSize: 20 }}
          >
            wifi_tethering
          </span>
        </button>

        {/* Avatar */}
        <div
          className="header-avatar"
          title="Marketing Director"
        >
          MD
        </div>

      </div>
    </header>
  );
}