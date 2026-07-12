import { motion } from 'framer-motion';
import StatusBadge from '../shared/StatusBadge';

const COLUMNS = ['Open', 'Overdue', 'Resolved'];

const SEVERITY_COLOR = {
  High: 'border-l-4 border-l-danger',
  Medium: 'border-l-4 border-l-accentAmber',
  Low: 'border-l-4 border-l-primaryGreen',
};

export default function ComplianceKanban({ issues }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {COLUMNS.map((col) => {
        const colIssues = issues.filter((i) => i.status === col);
        return (
          <div key={col} className="bg-bgBase rounded-lg p-3">
            <h3 className="text-sm font-semibold text-textPrimary mb-2">{col} ({colIssues.length})</h3>
            <div className="space-y-2">
              {colIssues.map((issue) => (
                <motion.div
                  key={issue.id}
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  className={`bg-bgSurface rounded-lg p-3 shadow-card ${SEVERITY_COLOR[issue.severity] || ''}`}
                >
                  <p className="text-sm text-textPrimary mb-1">{issue.description}</p>
                  <p className="text-xs text-textMuted mb-2">Owner: {issue.owner_name} · Due {new Date(issue.due_date).toLocaleDateString()}</p>
                  <StatusBadge status={issue.severity === 'High' ? 'Overdue' : issue.status} />
                </motion.div>
              ))}
              {colIssues.length === 0 && <p className="text-xs text-textMuted">No issues</p>}
            </div>
          </div>
        );
      })}
    </div>
  );
}