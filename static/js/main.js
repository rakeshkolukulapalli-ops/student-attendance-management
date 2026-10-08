* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background: #f4f7fb;
    color: #1f2937;
}

.container {
    width: min(1100px, 90%);
    margin: 0 auto;
}

.topbar {
    background: linear-gradient(135deg, #1d4ed8, #2563eb);
    color: white;
    padding: 18px 0;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.topbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.brand {
    font-size: 1.5rem;
    font-weight: 700;
}

.nav {
    display: flex;
    gap: 20px;
}

.nav a {
    color: white;
    text-decoration: none;
    font-weight: 600;
}

.main-content {
    padding: 30px 0 50px;
}

.page-header {
    margin-bottom: 25px;
}

.page-header h1 {
    font-size: 2rem;
    margin-bottom: 8px;
}

.page-header p {
    color: #4b5563;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 20px;
    margin-bottom: 28px;
}

.stat-card {
    border-radius: 12px;
    padding: 22px 18px;
    color: white;
    box-shadow: 0 10px 20px rgba(15, 23, 42, 0.08);
}

.stat-card span {
    display: block;
    font-size: 0.9rem;
    margin-bottom: 8px;
    opacity: 0.95;
}

.stat-card strong {
    font-size: 2rem;
}

.stat-card.primary { background: #2563eb; }
.stat-card.success { background: #16a34a; }
.stat-card.warning { background: #f59e0b; }
.stat-card.danger { background: #dc2626; }

.panel {
    background: #fff;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.05);
    margin-bottom: 25px;
}

.panel-header {
    margin-bottom: 18px;
}

.panel-header h2 {
    font-size: 1.3rem;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
}

th, td {
    border-bottom: 1px solid #e5e7eb;
    padding: 12px 10px;
    text-align: left;
}

th {
    background: #f8fafc;
    color: #374151;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(200px, 1fr));
    gap: 18px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 7px;
}

.full-width {
    grid-column: 1 / -1;
}

label {
    font-weight: 600;
}

input, select, button {
    font: inherit;
}

input, select {
    width: 100%;
    padding: 10px 12px;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    background: #fff;
}

.primary-btn {
    border: none;
    background: #2563eb;
    color: white;
    padding: 10px 18px;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 700;
}

.date-form {
    display: flex;
    align-items: end;
    gap: 12px;
    max-width: 400px;
}

.form-actions {
    margin-top: 18px;
}

.two-column {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 24px;
}

.flash-container {
    margin-bottom: 20px;
}

.flash {
    padding: 12px 14px;
    border-radius: 8px;
    margin-bottom: 10px;
    font-weight: 600;
}

.flash-success { background: #dcfce7; color: #166534; }
.flash-danger { background: #fee2e2; color: #991b1b; }

.badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 700;
}

.badge-present { background: #dcfce7; color: #166534; }
.badge-absent { background: #fee2e2; color: #991b1b; }
.badge-late { background: #fef3c7; color: #92400e; }

@media (max-width: 768px) {
    .topbar .container,
    .nav,
    .two-column,
    .form-grid,
    .date-form {
        flex-direction: column;
        display: flex;
    }

    .nav {
        gap: 10px;
    }

    .topbar .container {
        align-items: flex-start;
    }
}
