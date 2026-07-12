import { motion } from 'framer-motion';
import AnimatedCounter from './AnimatedCounter';

export default function KpiCard({ label, value, suffix = '', icon: Icon }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ y: -3 }}
      transition={{ duration: 0.3 }}
      className="bg-bgSurface border border-border rounded-xl p-5 shadow-card hover:shadow-cardHover transition-shadow"
    >
      <div className="flex items-center justify-between mb-2">
        <span className="text-textMuted text-sm font-medium">{label}</span>
        {Icon && <Icon size={18} className="text-primaryGreen" />}
      </div>
      <div className="text-2xl text-textPrimary">
        <AnimatedCounter value={value} />{suffix}
      </div>
    </motion.div>
  );
}