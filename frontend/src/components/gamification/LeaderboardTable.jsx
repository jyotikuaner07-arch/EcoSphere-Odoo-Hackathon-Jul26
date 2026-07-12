import { motion } from 'framer-motion';

export default function LeaderboardTable({ leaderboard, currentEmployeeId = 3 }) {
  const sorted = [...leaderboard].sort((a, b) => b.xp - a.xp);
  return (
    <div className="space-y-2">
      {sorted.map((row, i) => (
        <motion.div
          key={row.employee_id}
          initial={{ opacity: 0, x: -8 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: i * 0.05 }}
          className={`flex items-center justify-between px-3 py-2 rounded-lg ${
            row.employee_id === currentEmployeeId ? 'bg-bgSurfaceAlt' : ''
          }`}
        >
          <div className="flex items-center gap-3">
            <span className="text-sm font-tabular font-semibold text-textMuted w-5">{i + 1}</span>
            <div>
              <p className="text-sm font-medium text-textPrimary">{row.name}</p>
              <p className="text-xs text-textMuted">{row.department}</p>
            </div>
          </div>
          <span className="font-tabular font-semibold text-accentViolet">{row.xp} XP</span>
        </motion.div>
      ))}
    </div>
  );
}