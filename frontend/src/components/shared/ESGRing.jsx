import { motion } from 'framer-motion';

const RINGS = [
  { key: 'environmental_score', color: '#2F7D4F', radius: 70 },
  { key: 'social_score', color: '#D9A441', radius: 55 },
  { key: 'governance_score', color: '#4C7EA8', radius: 40 },
];

export default function ESGRing({ scores }) {
  const size = 180;
  const center = size / 2;

  return (
    <div className="relative flex items-center justify-center" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="-rotate-90">
        {RINGS.map((ring) => {
          const circumference = 2 * Math.PI * ring.radius;
          const value = scores[ring.key] ?? 0;
          const offset = circumference - (value / 100) * circumference;
          return (
            <g key={ring.key}>
              <circle
                cx={center}
                cy={center}
                r={ring.radius}
                stroke="#EEF5EE"
                strokeWidth={10}
                fill="none"
              />
              <motion.circle
                cx={center}
                cy={center}
                r={ring.radius}
                stroke={ring.color}
                strokeWidth={10}
                fill="none"
                strokeLinecap="round"
                strokeDasharray={circumference}
                initial={{ strokeDashoffset: circumference }}
                animate={{ strokeDashoffset: offset }}
                transition={{ duration: 1.2, ease: 'easeOut', delay: 0.2 }}
              />
            </g>
          );
        })}
      </svg>
      <div className="absolute flex flex-col items-center">
        <span className="font-display font-extrabold text-3xl text-textPrimary font-tabular">
          {scores.total_score ?? 0}
        </span>
        <span className="text-textMuted text-xs">ESG Score</span>
      </div>
    </div>
  );
}