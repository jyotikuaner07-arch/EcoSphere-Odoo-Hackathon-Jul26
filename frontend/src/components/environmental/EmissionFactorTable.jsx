import StatusBadge from '../shared/StatusBadge';

export default function EmissionFactorTable({ factors }) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-textMuted border-b border-border">
            <th className="py-2 pr-4 font-medium">Name</th>
            <th className="py-2 pr-4 font-medium">Source Type</th>
            <th className="py-2 pr-4 font-medium">CO2e Value</th>
            <th className="py-2 pr-4 font-medium">Unit</th>
            <th className="py-2 font-medium">Status</th>
          </tr>
        </thead>
        <tbody>
          {factors.map((f) => (
            <tr key={f.id} className="border-b border-border last:border-0 hover:bg-bgSurfaceAlt transition-colors">
              <td className="py-2.5 pr-4 text-textPrimary">{f.name}</td>
              <td className="py-2.5 pr-4 text-textMuted">{f.source_type}</td>
              <td className="py-2.5 pr-4 font-tabular text-textPrimary">{f.co2e_value}</td>
              <td className="py-2.5 pr-4 text-textMuted">{f.unit}</td>
              <td className="py-2.5"><StatusBadge status={f.status} /></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}