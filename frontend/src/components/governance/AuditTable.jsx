export default function AuditTable({ audits }) {
  return (
    <table className="w-full text-sm">
      <thead>
        <tr className="text-left text-textMuted border-b border-border">
          <th className="py-2 pr-4 font-medium">Title</th>
          <th className="py-2 pr-4 font-medium">Department</th>
          <th className="py-2 pr-4 font-medium">Auditor</th>
          <th className="py-2 pr-4 font-medium">Status</th>
          <th className="py-2 font-medium">Date</th>
        </tr>
      </thead>
      <tbody>
        {audits.map((a) => (
          <tr key={a.id} className="border-b border-border last:border-0 hover:bg-bgSurfaceAlt transition-colors">
            <td className="py-2.5 pr-4 text-textPrimary">{a.title}</td>
            <td className="py-2.5 pr-4 text-textMuted">{a.department_name}</td>
            <td className="py-2.5 pr-4 text-textMuted">{a.auditor}</td>
            <td className="py-2.5 pr-4 text-textMuted">{a.status}</td>
            <td className="py-2.5 text-textMuted">{new Date(a.date).toLocaleDateString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}