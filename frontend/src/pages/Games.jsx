import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { Trash2, Zap, Droplets } from 'lucide-react';

const games = [
  {
    id: 'waste-sorting',
    title: '🌱 Waste Sorting Challenge',
    description: 'Test your recycling skills by dragging and dropping items into the correct bins!',
    icon: Trash2,
    color: 'bg-green-100',
    textColor: 'text-green-700'
  },
  {
    id: 'energy-saver',
    title: '⚡ Energy Saver',
    description: 'Click to turn off appliances and save energy in this fast-paced game!',
    icon: Zap,
    color: 'bg-yellow-100',
    textColor: 'text-yellow-700'
  },
  {
    id: 'water-leak',
    title: '💧 Water Leak Hunt',
    description: 'Find all the hidden water leaks before the timer runs out!',
    icon: Droplets,
    color: 'bg-blue-100',
    textColor: 'text-blue-700'
  }
];

export default function Games() {
  return (
    <div className="max-w-6xl mx-auto space-y-8">
      <div className="text-center space-y-2 mb-12">
        <h1 className="text-4xl font-display font-bold text-primaryGreenDark">
          Eco Games
        </h1>
        <p className="text-textMuted text-lg">
          Have fun while learning about sustainability!
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {games.map((game, index) => (
          <motion.div
            key={game.id}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ y: -5, scale: 1.02 }}
            className="bg-white rounded-2xl p-8 shadow-lg border border-gray-100"
          >
            <div className={`${game.color} w-16 h-16 rounded-2xl flex items-center justify-center mb-6`}>
              <game.icon size={32} className={game.textColor} />
            </div>
            <h3 className="text-xl font-semibold text-textPrimary mb-3">
              {game.title}
            </h3>
            <p className="text-textMuted mb-6">
              {game.description}
            </p>
            <Link
              to={`/app/games/${game.id}`}
              className="inline-block bg-primaryGreen hover:bg-primaryGreen/90 text-white px-6 py-3 rounded-xl font-medium transition-colors"
            >
              Play Now
            </Link>
          </motion.div>
        ))}
      </div>
    </div>
  );
}
