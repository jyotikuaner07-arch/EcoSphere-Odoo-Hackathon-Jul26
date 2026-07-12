import { motion } from 'framer-motion';
import { Award } from 'lucide-react';
import { formatBadgeProgress } from '../../utils/badgeProgress';

export default function BadgeCard({ badge, employeeStats }) {
  const progress = formatBadgeProgress(badge.unlock_rule, employeeStats);
  const earned = badge.earned || progress.met;

  return (
    <motion.div
      whileHover={{ y: -3 }}
      className={`bg-bgSurface border border-border rounded-xl p-4 shadow-card text-center ${!earned ? 'opacity-50 grayscale' : ''}`}
    >
      <div className="w-12 h-12 mx-auto mb-2 rounded-full bg-bgSurfaceAlt flex items-center justify-center">
        <Award size={22} className={earned ? 'text-accentViolet' : 'text-textMuted'} />
      </div>
      <p className="text-sm font-medium text-textPrimary">{badge.name}</p>
      <p className="text-xs text-textMuted mb-1">{badge.description}</p>
      {!earned && <p className="text-xs text-accentViolet font-tabular">{progress.label}</p>}
    </motion.div>
  );
}