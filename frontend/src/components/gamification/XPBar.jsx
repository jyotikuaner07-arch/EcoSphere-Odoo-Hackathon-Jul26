import { motion } from 'framer-motion';

export default function XPBar({ current, floor, nextFloor }) {
  const pct = Math.min(100, Math.max(0, ((current - floor) / (nextFloor - floor)) * 100));
  return (
    <div>
      <div className="flex justify-between text-xs text-textMuted mb-1">
        <span>{current} XP</span>
        <span>{nextFloor} XP</span>
      </div>
      <div className="h-2 bg-bgSurfaceAlt rounded-full overflow-hidden">
        <motion.div
          className="h-full bg-accentViolet rounded-full"
          initial={{ width: 0 }}
          animate={{ width: `${pct}%` }}
          transition={{ duration: 1, ease: 'easeOut', delay: 0.3 }}
        />
      </div>
    </div>
  );
}