import StatusBadge from '../shared/StatusBadge';
import { FileText } from 'lucide-react';

export default function PolicyList({ policies }) {
  return (
    <div className="space-y-2">
      {policies.map((p) => (
        <div key={p.id} className="flex items-center justify-between border border-border rounded-lg p-3">
          <div className="flex items-center gap-2">
            <FileText size={16} className="text-accentBlue" />
            <div>
              <p className="text-sm font-medium text-textPrimary">{p.title}</p>
              <p className="text-xs text-textMuted">{p.version} · effective {new Date(p.effective_date).toLocaleDateString()}</p>
            </div>
          </div>
          <StatusBadge status={p.status} />
        </div>
      ))}
    </div>
  );
}