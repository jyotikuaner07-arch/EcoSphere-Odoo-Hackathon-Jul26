import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Droplets, RotateCcw, Trophy, CheckCircle2 } from 'lucide-react';

const initialLeaks = [
  { id: 1, x: 15, y: 20, found: false },
  { id: 2, x: 45, y: 35, found: false },
  { id: 3, x: 75, y: 25, found: false },
  { id: 4, x: 25, y: 65, found: false },
  { id: 5, x: 60, y: 70, found: false },
  { id: 6, x: 85, y: 55, found: false },
  { id: 7, x: 35, y: 45, found: false },
];

export default function WaterLeakHuntGame() {
  const [leaks, setLeaks] = useState(initialLeaks);
  const [timeLeft, setTimeLeft] = useState(60);
  const [gameOver, setGameOver] = useState(false);
  const [gameWon, setGameWon] = useState(false);
  const [gameStarted, setGameStarted] = useState(false);

  const foundCount = leaks.filter(l => l.found).length;

  useEffect(() => {
    let timer;
    if (gameStarted && !gameOver && !gameWon) {
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
  }, [gameStarted, gameOver, gameWon]);

  useEffect(() => {
    if (gameStarted && foundCount === initialLeaks.length) {
      setGameWon(true);
    }
  }, [foundCount, gameStarted]);

  const findLeak = (id) => {
    setLeaks(prev => prev.map(leak => {
      if (leak.id === id && !leak.found) {
        return { ...leak, found: true };
      }
      return leak;
    }));
  };

  const resetGame = () => {
    setLeaks(initialLeaks);
    setTimeLeft(60);
    setGameOver(false);
    setGameWon(false);
    setGameStarted(false);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <div className="text-center space-y-2">
        <h1 className="text-3xl font-display font-bold text-primaryGreenDark">
          Water Leak Hunt
        </h1>
        <p className="text-textMuted">Find all {initialLeaks.length} water leaks!</p>
      </div>

      <div className="flex justify-between items-center px-6">
        <div className="flex items-center gap-2">
          <CheckCircle2 className="text-green-500" size={24} />
          <p className="text-xl font-bold text-primaryGreenDark">
            Found: {foundCount}/{initialLeaks.length}
          </p>
        </div>
        <div className="flex items-center gap-2">
          <Droplets className="text-blue-500" size={24} />
          <p className="text-xl font-bold text-primaryGreenDark">Time: {timeLeft}s</p>
        </div>
      </div>

      {!gameStarted && !gameOver && !gameWon && (
        <div className="text-center py-12">
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="bg-white rounded-2xl p-8 shadow-lg"
          >
            <Droplets size={64} className="mx-auto text-blue-500 mb-6" />
            <h2 className="text-3xl font-bold mb-4">Ready to Hunt Leaks?</h2>
            <p className="text-textMuted mb-6">
              Find all {initialLeaks.length} water leaks before the timer runs out!
            </p>
            <button
              onClick={() => setGameStarted(true)}
              className="bg-primaryGreen hover:bg-primaryGreen/90 text-white px-8 py-3 rounded-xl font-semibold"
            >
              Start Game
            </button>
          </motion.div>
        </div>
      )}

      {gameStarted && !gameOver && !gameWon && (
        <div className="relative bg-gradient-to-br from-green-100 to-blue-100 rounded-2xl h-96 overflow-hidden shadow-lg">
          <AnimatePresence>
            {leaks.map(leak => (
              <motion.button
                key={leak.id}
                initial={leak.found ? { scale: 0, opacity: 0 } : { scale: 1, opacity: 1 }}
                animate={leak.found ? { scale: 0, opacity: 0 } : { scale: [1, 1.1, 1], opacity: 1 }}
                transition={{ repeat: Infinity, duration: 1.5 }}
                whileHover={{ scale: 1.3 }}
                onClick={() => findLeak(leak.id)}
                className={`absolute cursor-pointer ${leak.found ? 'hidden' : 'block'}`}
                style={{ left: `${leak.x}%`, top: `${leak.y}%` }}
              >
                <span className="text-4xl drop-shadow-lg">💧</span>
              </motion.button>
            ))}
          </AnimatePresence>
        </div>
      )}

      {(gameOver || gameWon) && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-2xl p-8 shadow-lg text-center"
        >
          <Trophy size={64} className={`mx-auto mb-6 ${gameWon ? 'text-yellow-500' : 'text-gray-400'}`} />
          <h2 className="text-3xl font-bold mb-4">
            {gameWon ? 'Congratulations! You found all leaks!' : 'Game Over!'}
          </h2>
          <p className="text-xl text-textMuted mb-6">
            You found {foundCount} out of {initialLeaks.length} leaks!
          </p>
          {gameWon && (
            <p className="text-lg text-green-600 mb-6">
              You saved 50 gallons of water! 🌊
            </p>
          )}
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
