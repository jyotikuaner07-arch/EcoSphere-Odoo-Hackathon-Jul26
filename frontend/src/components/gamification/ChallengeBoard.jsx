import { motion } from 'framer-motion';
import { CHALLENGE_STATUS } from '../../constants/enums';
import StatusBadge from '../shared/StatusBadge';

const DIFFICULTY_COLOR = { Easy: 'text-primaryGreenDark', Medium: 'text-accentAmber', Hard: 'text-danger' };

export default function ChallengeBoard({ challenges }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
      {CHALLENGE_STATUS.map((status) => {
        const col = challenges.filter((c) => c.status === status);
        return (
          <div key={status} className="bg-bgBase rounded-lg p-3 min-w-0">
            <h3 className="text-xs font-semibold text-textPrimary mb-2">{status} ({col.length})</h3>
            <div className="space-y-2">
              {col.map((c) => (
                <motion.div key={c.id} whileHover={{ y: -2 }} className="bg-bgSurface rounded-lg p-3 shadow-card">
                  <p className="text-sm font-medium text-textPrimary mb-1">{c.title}</p>
                  <p className="text-xs text-textMuted mb-2 line-clamp-2">{c.description}</p>
                  <div className="flex items-center justify-between text-xs">
                    <span className="font-tabular font-semibold text-accentViolet">{c.xp} XP</span>
                    <span className={DIFFICULTY_COLOR[c.difficulty]}>{c.difficulty}</span>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}