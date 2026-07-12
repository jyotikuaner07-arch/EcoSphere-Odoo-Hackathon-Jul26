import StatusBadge from '../shared/StatusBadge';

export default function CarbonTransactionTable({ transactions }) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-textMuted border-b border-border">
            <th className="py-2 pr-4 font-medium">Department</th>
            <th className="py-2 pr-4 font-medium">Source</th>
            <th className="py-2 pr-4 font-medium">Quantity</th>
            <th className="py-2 pr-4 font-medium">CO2e (kg)</th>
            <th className="py-2 pr-4 font-medium">Mode</th>
            <th className="py-2 font-medium">Date</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((t) => (
            <tr key={t.id} className="border-b border-border last:border-0 hover:bg-bgSurfaceAlt transition-colors">
              <td className="py-2.5 pr-4 text-textPrimary">{t.department_name}</td>
              <td className="py-2.5 pr-4 text-textMuted">{t.source_type}</td>
              <td className="py-2.5 pr-4 font-tabular text-textPrimary">{t.quantity}</td>
              <td className="py-2.5 pr-4 font-tabular text-textPrimary">{t.co2e_calculated}</td>
              <td className="py-2.5 pr-4"><StatusBadge status={t.calculation_mode} /></td>
              <td className="py-2.5 text-textMuted">{new Date(t.created_at).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}