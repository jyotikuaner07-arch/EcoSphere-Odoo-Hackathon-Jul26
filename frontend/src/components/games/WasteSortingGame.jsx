import { useState, useRef } from 'react';
import { motion } from 'framer-motion';
import { Trash2, RotateCcw, Trophy } from 'lucide-react';

const wasteItems = [
  { id: 1, name: 'Plastic Bottle', type: 'plastic', emoji: '🍾' },
  { id: 2, name: 'Banana Peel', type: 'organic', emoji: '🍌' },
  { id: 3, name: 'Glass Jar', type: 'glass', emoji: '🏺' },
  { id: 4, name: 'Newspaper', type: 'paper', emoji: '📰' },
  { id: 5, name: 'Aluminum Can', type: 'metal', emoji: '🥫' },
  { id: 6, name: 'Food Scraps', type: 'organic', emoji: '🥕' },
];

const bins = [
  { id: 'plastic', name: 'Plastic', color: 'bg-blue-500', emoji: '♻️' },
  { id: 'organic', name: 'Organic', color: 'bg-green-600', emoji: '🌱' },
  { id: 'glass', name: 'Glass', color: 'bg-green-700', emoji: '🍾' },
  { id: 'paper', name: 'Paper', color: 'bg-blue-700', emoji: '📰' },
  { id: 'metal', name: 'Metal', color: 'bg-gray-700', emoji: '⚡' },
];

export default function WasteSortingGame() {
  const [items, setItems] = useState(wasteItems);
  const [score, setScore] = useState(0);
  const [draggedItem, setDraggedItem] = useState(null);
  const [gameComplete, setGameComplete] = useState(false);

  const handleDragStart = (item) => {
    setDraggedItem(item);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (binId) => {
    if (draggedItem) {
      if (draggedItem.type === binId) {
        setScore(prev => prev + 10);
        setItems(prev => prev.filter(item => item.id !== draggedItem.id));
      }
      setDraggedItem(null);

      if (items.length === 1) {
        setGameComplete(true);
      }
    }
  };

  const resetGame = () => {
    setItems(wasteItems);
    setScore(0);
    setGameComplete(false);
    setDraggedItem(null);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <div className="text-center space-y-2">
        <h1 className="text-3xl font-display font-bold text-primaryGreenDark">
          Waste Sorting Challenge
        </h1>
        <p className="text-textMuted">Drag and drop items into the correct bins!</p>
      </div>

      <div className="flex items-center justify-center gap-3">
        <Trophy className="text-yellow-500" size={24} />
        <p className="text-2xl font-bold text-primaryGreenDark">Score: {score}</p>
      </div>

      {gameComplete ? (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-2xl p-8 shadow-lg text-center"
        >
          <Trophy size={64} className="mx-auto text-yellow-500 mb-6" />
          <h2 className="text-3xl font-bold mb-4">Congratulations!</h2>
          <p className="text-xl text-textMuted mb-6">
            You scored {score} points!
          </p>
          <button
            onClick={resetGame}
            className="bg-primaryGreen hover:bg-primaryGreen/90 text-white px-8 py-3 rounded-xl font-semibold flex items-center gap-2 mx-auto"
          >
            <RotateCcw size={20} /> Play Again
          </button>
        </motion.div>
      ) : (
        <>
          <div className="flex flex-wrap justify-center gap-4 p-6 bg-white rounded-2xl shadow-lg">
            {items.map((item) => (
              <motion.div
                key={item.id}
                whileHover={{ scale: 1.1 }}
                whileDrag={{ scale: 1.2, zIndex: 50 }}
                drag
                dragSnapToOrigin
                onDragStart={() => handleDragStart(item)}
                className="bg-gray-100 p-4 rounded-xl cursor-grab active:cursor-grabbing shadow-md"
              >
                <span className="text-5xl">{item.emoji}</span>
                <p className="text-sm text-textMuted mt-2">{item.name}</p>
              </motion.div>
            ))}
          </div>

          <div className="grid grid-cols-5 gap-4">
            {bins.map((bin) => (
              <div
                key={bin.id}
                onDragOver={handleDragOver}
                onDrop={() => handleDrop(bin.id)}
                className={`${bin.color} p-6 rounded-2xl shadow-lg text-white text-center`}
              >
                <span className="text-4xl block mb-2">{bin.emoji}</span>
                <h3 className="font-bold">{bin.name}</h3>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
