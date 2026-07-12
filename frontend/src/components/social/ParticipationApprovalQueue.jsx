import { useState } from 'react';
import { CheckCircle2, XCircle, FileWarning } from 'lucide-react';
import StatusBadge from '../shared/StatusBadge';

export default function ParticipationApprovalQueue({ items, evidenceRequired = true }) {
  const [rows, setRows] = useState(items);

  const decide = (id, decision) => {
    // NOTE: wire to ENDPOINTS.approveParticipation(id) / rejectParticipation(id) once backend is live
    setRows((prev) => prev.map((r) => (r.id === id ? { ...r, approval_status: decision } : r)));
  };

  return (
    <div className="space-y-3">
      {rows.map((row) => {
        const blocked = evidenceRequired && !row.proof_url && row.approval_status === 'Pending';
        return (
          <div key={row.id} className="flex items-center justify-between border border-border rounded-lg p-3">
            <div>
              <p className="text-sm font-medium text-textPrimary">{row.employee_name}</p>
              <p className="text-xs text-textMuted">{row.activity_title} · {row.points_earned} pts</p>
              {blocked && (
                <p className="text-xs text-danger flex items-center gap-1 mt-1">
                  <FileWarning size={12} /> Proof required before approval
                </p>
              )}
            </div>
            <div className="flex items-center gap-2">
              <StatusBadge status={row.approval_status} />
              {row.approval_status === 'Pending' && (
                <>
                  <button
                    disabled={blocked}
                    onClick={() => decide(row.id, 'Approved')}
                    className="text-primaryGreen disabled:text-gray-300 disabled:cursor-not-allowed"
                    aria-label="Approve"
                  >
                    <CheckCircle2 size={20} />
                  </button>
                  <button
                    onClick={() => decide(row.id, 'Rejected')}
                    className="text-danger"
                    aria-label="Reject"
                  >
                    <XCircle size={20} />
                  </button>
                </>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
}