import StatusBadge from '../shared/StatusBadge';

export default function AcknowledgementTracker({ acknowledgements }) {
  return (
    <table className="w-full text-sm">
      <thead>
        <tr className="text-left text-textMuted border-b border-border">
          <th className="py-2 pr-4 font-medium">Employee</th>
          <th className="py-2 pr-4 font-medium">Policy</th>
          <th className="py-2 font-medium">Status</th>
        </tr>
      </thead>
      <tbody>
        {acknowledgements.map((a) => (
          <tr key={a.id} className="border-b border-border last:border-0">
            <td className="py-2.5 pr-4 text-textPrimary">{a.employee_name}</td>
            <td className="py-2.5 pr-4 text-textMuted">{a.policy_title}</td>
            <td className="py-2.5"><StatusBadge status={a.status === 'Acknowledged' ? 'Approved' : 'Pending'} /></td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}