import { motion } from 'framer-motion';
import AnimatedCounter from './AnimatedCounter';

export default function KpiCard({ label, value, suffix = '', icon: Icon }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 14 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ y: -4, scale: 1.01 }}
      transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }}
      className="glass-card p-6"
    >
      <div className="flex items-center justify-between mb-3">
        <span className="text-textMuted text-sm font-medium">{label}</span>
        {Icon && (
          <div className="w-8 h-8 rounded-lg bg-primaryGreen/10 flex items-center justify-center">
            <Icon size={16} className="text-primaryGreen" />
          </div>
        )}
      </div>
      <div className="text-3xl text-textPrimary">
        <AnimatedCounter value={value} />{suffix}
      </div>
    </motion.div>
  );
}