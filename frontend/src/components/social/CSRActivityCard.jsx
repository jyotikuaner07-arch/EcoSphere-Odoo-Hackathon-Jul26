import { motion } from 'framer-motion';
import { Calendar } from 'lucide-react';
import StatusBadge from '../shared/StatusBadge';

export default function CSRActivityCard({ activity }) {
  return (
    <motion.div
      whileHover={{ y: -3 }}
      className="bg-bgSurface border border-border rounded-xl p-4 shadow-card hover:shadow-cardHover transition-shadow"
    >
      <div className="flex justify-between items-start mb-2">
        <p className="font-medium text-textPrimary">{activity.title}</p>
        <StatusBadge status={activity.status} />
      </div>
      <p className="text-xs text-textMuted mb-2">{activity.department_name}</p>
      <div className="flex items-center gap-1 text-xs text-textMuted">
        <Calendar size={13} />
        {new Date(activity.date).toLocaleDateString()}
      </div>
    </motion.div>
  );
}