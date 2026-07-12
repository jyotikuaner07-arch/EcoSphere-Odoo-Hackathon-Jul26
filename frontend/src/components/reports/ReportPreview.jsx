export default function ReportPreview({ rows }) {
  return (
    <table className="w-full text-sm">
      <thead>
        <tr className="text-left text-textMuted border-b border-border">
          <th className="py-2 pr-4 font-medium">Department</th>
          <th className="py-2 pr-4 font-medium">Metric</th>
          <th className="py-2 font-medium">Value</th>
        </tr>
      </thead>
      <tbody>
        {rows.map((r, i) => (
          <tr key={i} className="border-b border-border last:border-0">
            <td className="py-2.5 pr-4 text-textPrimary">{r.department}</td>
            <td className="py-2.5 pr-4 text-textMuted">{r.metric}</td>
            <td className="py-2.5 font-tabular text-textPrimary">{r.value}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}