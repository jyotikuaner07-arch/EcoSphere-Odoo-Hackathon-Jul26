import { motion } from 'framer-motion';
import { Gift } from 'lucide-react';

export default function RewardCard({ reward, employeePoints = 340, onRedeem }) {
  const outOfStock = reward.stock <= 0;
  const insufficientPoints = employeePoints < reward.points_required;
  const disabled = outOfStock || insufficientPoints;

  return (
    <motion.div whileHover={{ y: -3 }} className="bg-bgSurface border border-border rounded-xl p-4 shadow-card">
      <Gift size={20} className="text-accentAmber mb-2" />
      <p className="text-sm font-medium text-textPrimary">{reward.name}</p>
      <p className="text-xs text-textMuted mb-3">{reward.description}</p>
      <div className="flex items-center justify-between">
        <span className="font-tabular font-semibold text-textPrimary">{reward.points_required} pts</span>
        <button
          disabled={disabled}
          onClick={() => onRedeem?.(reward.id)}
          className="text-xs font-medium px-3 py-1.5 rounded-full bg-primaryGreen text-white disabled:bg-gray-200 disabled:text-textMuted disabled:cursor-not-allowed transition-colors"
        >
          {outOfStock ? 'Out of stock' : insufficientPoints ? 'Not enough points' : 'Redeem'}
        </button>
      </div>
    </motion.div>
  );
}