export default function ReportFilterPanel({ filters, values, onChange }) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
      <select
        value={values.department}
        onChange={(e) => onChange({ ...values, department: e.target.value })}
        className="border border-border rounded-lg px-3 py-2 text-sm text-textPrimary bg-bgSurface"
      >
        <option value="">All Departments</option>
        {filters.departments.map((d) => <option key={d} value={d}>{d}</option>)}
      </select>
      <select
        value={values.module}
        onChange={(e) => onChange({ ...values, module: e.target.value })}
        className="border border-border rounded-lg px-3 py-2 text-sm text-textPrimary bg-bgSurface"
      >
        <option value="">All Modules</option>
        {filters.modules.map((m) => <option key={m} value={m}>{m}</option>)}
      </select>
      <input
        type="date"
        value={values.dateFrom}
        onChange={(e) => onChange({ ...values, dateFrom: e.target.value })}
        className="border border-border rounded-lg px-3 py-2 text-sm text-textPrimary bg-bgSurface"
      />
    </div>
  );
}