import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Zap, RotateCcw, Trophy } from 'lucide-react';

const appliances = ['💡', '📺', '❄️', '🖥️', '🎵', '🔌'];

export default function EnergySaverGame() {
  const [activeAppliances, setActiveAppliances] = useState([]);
  const [score, setScore] = useState(0);
  const [timeLeft, setTimeLeft] = useState(30);
  const [gameOver, setGameOver] = useState(false);
  const [gameStarted, setGameStarted] = useState(false);

  useEffect(() => {
    let timer;
    if (gameStarted && !gameOver) {
      timer = setInterval(() => {
        setTimeLeft(prev => {
          if (prev <= 1) {
            setGameOver(true);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }
    return () => clearInterval(timer);
  }, [gameStarted, gameOver]);

  useEffect(() => {
    let spawner;
    if (gameStarted && !gameOver) {
      spawner = setInterval(() => {
        setActiveAppliances(prev => {
          if (prev.length < 8) {
            const newAppliance = {
              id: Date.now(),
              emoji: appliances[Math.floor(Math.random() * appliances.length)],
              x: Math.random() * 80 + 10,
              y: Math.random() * 60 + 20
            };
            return [...prev, newAppliance];
          }
          return prev;
        });
      }, 1000);
    }
    return () => clearInterval(spawner);
  }, [gameStarted, gameOver]);

  const turnOffAppliance = (id) => {
    setActiveAppliances(prev => prev.filter(a => a.id !== id));
    setScore(prev => prev + 5);
  };

  const resetGame = () => {
    setScore(0);
    setTimeLeft(30);
    setGameOver(false);
    setGameStarted(false);
    setActiveAppliances([]);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <div className="text-center space-y-2">
        <h1 className="text-3xl font-display font-bold text-primaryGreenDark">
          Energy Saver
        </h1>
        <p className="text-textMuted">Click to turn off appliances and save energy!</p>
      </div>

      <div className="flex justify-between items-center px-6">
        <div className="flex items-center gap-2">
          <Trophy className="text-yellow-500" size={24} />
          <p className="text-xl font-bold text-primaryGreenDark">Score: {score}</p>
        </div>
        <div className="flex items-center gap-2">
          <Zap className="text-yellow-500" size={24} />
          <p className="text-xl font-bold text-primaryGreenDark">Time: {timeLeft}s</p>
        </div>
      </div>

      {!gameStarted && !gameOver && (
        <div className="text-center py-12">
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="bg-white rounded-2xl p-8 shadow-lg"
          >
            <Zap size={64} className="mx-auto text-yellow-500 mb-6" />
            <h2 className="text-3xl font-bold mb-4">Ready to Save Energy?</h2>
            <p className="text-textMuted mb-6">Turn off as many appliances as you can in 30 seconds!</p>
            <button
              onClick={() => setGameStarted(true)}
              className="bg-primaryGreen hover:bg-primaryGreen/90 text-white px-8 py-3 rounded-xl font-semibold"
            >
              Start Game
            </button>
          </motion.div>
        </div>
      )}

      {gameStarted && !gameOver && (
        <div className="relative bg-gradient-to-br from-green-50 to-blue-50 rounded-2xl h-96 overflow-hidden shadow-lg">
          <AnimatePresence>
            {activeAppliances.map(appliance => (
              <motion.button
                key={appliance.id}
                initial={{ scale: 0, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                exit={{ scale: 0, opacity: 0 }}
                whileHover={{ scale: 1.2 }}
                whileTap={{ scale: 0.9 }}
                onClick={() => turnOffAppliance(appliance.id)}
                className="absolute text-5xl cursor-pointer"
                style={{ left: `${appliance.x}%`, top: `${appliance.y}%` }}
              >
                {appliance.emoji}
              </motion.button>
            ))}
          </AnimatePresence>
        </div>
      )}

      {gameOver && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-2xl p-8 shadow-lg text-center"
        >
          <Trophy size={64} className="mx-auto text-yellow-500 mb-6" />
          <h2 className="text-3xl font-bold mb-4">Game Over!</h2>
          <p className="text-xl text-textMuted mb-2">
            You scored {score} points!
          </p>
          <p className="text-lg text-textMuted mb-6">
            You saved {score * 0.5} kWh of energy! 🌱
          </p>
          <button
            onClick={resetGame}
            className="bg-primaryGreen hover:bg-primaryGreen/90 text-white px-8 py-3 rounded-xl font-semibold flex items-center gap-2 mx-auto"
          >
            <RotateCcw size={20} /> Play Again
          </button>
        </motion.div>
      )}
    </div>
  );
}
