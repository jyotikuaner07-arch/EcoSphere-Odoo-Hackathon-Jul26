import { motion } from 'framer-motion';

const STATUS_COLOR = {
  'On Track': 'text-primaryGreenDark bg-bgSurfaceAlt',
  'At Risk': 'text-danger bg-red-50',
};

export default function GoalProgressCard({ goal }) {
  const pct = Math.min(100, Math.round((goal.current_value / goal.target_value) * 100));
  return (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-bgSurface border border-border rounded-xl p-4 shadow-card"
    >
      <div className="flex justify-between items-start mb-2">
        <div>
          <p className="text-sm font-medium text-textPrimary">{goal.department_name}</p>
          <p className="text-xs text-textMuted">{goal.metric_type}</p>
        </div>
        <span className={`text-xs font-medium px-2 py-1 rounded-full ${STATUS_COLOR[goal.status] || 'text-textMuted bg-bgSurfaceAlt'}`}>
          {goal.status}
        </span>
      </div>
      <div className="h-2 bg-bgSurfaceAlt rounded-full overflow-hidden mb-1">
        <motion.div
          className={`h-full rounded-full ${goal.status === 'At Risk' ? 'bg-danger' : 'bg-primaryGreen'}`}
          initial={{ width: 0 }}
          animate={{ width: `${pct}%` }}
          transition={{ duration: 1, ease: 'easeOut' }}
        />
      </div>
      <p className="text-xs text-textMuted font-tabular">
        {goal.current_value} / {goal.target_value} · due {new Date(goal.deadline).toLocaleDateString()}
      </p>
    </motion.div>
  );
}