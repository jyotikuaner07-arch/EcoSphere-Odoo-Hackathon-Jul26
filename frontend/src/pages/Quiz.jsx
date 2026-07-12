import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Play,
  RotateCcw,
  CheckCircle2,
  XCircle,
  Trophy,
  Clock,
  HelpCircle,
} from 'lucide-react';

// Sample quiz data
const SAMPLE_QUIZ = {
  id: 1,
  title: 'Sustainability Basics Quiz',
  description: 'Test your knowledge on environmental sustainability!',
  xp: 100,
  difficulty: 'Easy',
  questions: [
    {
      id: 1,
      question_text: 'What is the primary greenhouse gas emitted by human activities?',
      option_a: 'Oxygen',
      option_b: 'Carbon Dioxide (CO2)',
      option_c: 'Nitrogen',
      option_d: 'Hydrogen',
      correct_option: 'B',
    },
    {
      id: 2,
      question_text: 'Which of the following is a renewable energy source?',
      option_a: 'Coal',
      option_b: 'Natural Gas',
      option_c: 'Solar Power',
      option_d: 'Petroleum',
      correct_option: 'C',
    },
    {
      id: 3,
      question_text: 'What does "reduce, reuse, recycle" help to minimize?',
      option_a: 'Water usage',
      option_b: 'Waste generation',
      option_c: 'Energy consumption',
      option_d: 'All of the above',
      correct_option: 'D',
    },
  ],
};

export default function Quiz() {
  const [currentStep, setCurrentStep] = useState('intro'); // intro, playing, results
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [quizData] = useState(SAMPLE_QUIZ);

  const handleStartQuiz = () => {
    setCurrentStep('playing');
    setCurrentQuestionIndex(0);
    setSelectedAnswers({});
  };

  const handleSelectAnswer = (questionId, option) => {
    setSelectedAnswers((prev) => ({ ...prev, [questionId]: option }));
  };

  const handleNext = () => {
    if (currentQuestionIndex < quizData.questions.length - 1) {
      setCurrentQuestionIndex((prev) => prev + 1);
    } else {
      setCurrentStep('results');
    }
  };

  const handleRestart = () => {
    setCurrentStep('intro');
    setCurrentQuestionIndex(0);
    setSelectedAnswers({});
  };

  const calculateScore = () => {
    let score = 0;
    quizData.questions.forEach((q) => {
      if (selectedAnswers[q.id] === q.correct_option) {
        score++;
      }
    });
    return score;
  };

  const score = calculateScore();
  const totalQuestions = quizData.questions.length;
  const percentage = totalQuestions > 0 ? Math.round((score / totalQuestions) * 100) : 0;

  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-display font-bold text-primaryGreenDark mb-2">
          Sustainability Quiz
        </h1>
        <p className="text-textMuted">Test your knowledge and earn XP!</p>
      </div>

      <AnimatePresence mode="wait">
        {currentStep === 'intro' && (
          <motion.div
            key="intro"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="bg-white rounded-2xl p-8 shadow-lg text-center"
          >
            <div className="w-24 h-24 mx-auto mb-6 bg-primaryGreen/10 rounded-full flex items-center justify-center">
              <HelpCircle size={48} className="text-primaryGreen" />
            </div>
            <h2 className="text-2xl font-bold mb-4">{quizData.title}</h2>
            <p className="text-textMuted mb-8">{quizData.description}</p>
            <div className="flex flex-wrap justify-center gap-6 mb-8 text-sm">
              <div className="flex items-center gap-2">
                <Trophy className="text-primaryGreen" size={18} />
                <span>{quizData.xp} XP</span>
              </div>
              <div className="flex items-center gap-2">
                <HelpCircle className="text-primaryGreen" size={18} />
                <span>{quizData.questions.length} Questions</span>
              </div>
              <div className="flex items-center gap-2">
                <Clock className="text-primaryGreen" size={18} />
                <span>{quizData.difficulty}</span>
              </div>
            </div>
            <button
              onClick={handleStartQuiz}
              className="bg-primaryGreen hover:bg-primaryGreen/90 text-white px-8 py-3 rounded-xl font-semibold flex items-center gap-2 mx-auto transition-all"
            >
              <Play size={20} /> Start Quiz
            </button>
          </motion.div>
        )}

        {currentStep === 'playing' && (
          <motion.div
            key="playing"
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            className="bg-white rounded-2xl p-8 shadow-lg"
          >
            <div className="mb-6">
              <div className="flex justify-between items-center mb-2">
                <span className="text-sm font-medium text-textMuted">
                  Question {currentQuestionIndex + 1} of {totalQuestions}
                </span>
                <span className="text-sm font-medium text-textMuted">
                  {Math.round(((currentQuestionIndex + 1) / totalQuestions) * 100)}% Complete
                </span>
              </div>
              <div className="w-full bg-gray-100 h-2 rounded-full overflow-hidden">
                <motion.div
                  className="bg-primaryGreen h-full rounded-full"
                  initial={{ width: 0 }}
                  animate={{ width: `${((currentQuestionIndex + 1) / totalQuestions) * 100}%` }}
                  transition={{ duration: 0.5 }}
                />
              </div>
            </div>

            <h3 className="text-xl font-semibold mb-6">
              {quizData.questions[currentQuestionIndex].question_text}
            </h3>
            <div className="grid gap-3">
              {['A', 'B', 'C', 'D'].map((option) => {
                const optionKey = `option_${option.toLowerCase()}`;
                const label = quizData.questions[currentQuestionIndex][optionKey];
                const isSelected = selectedAnswers[quizData.questions[currentQuestionIndex].id] === option;
                return (
                  <button
                    key={option}
                    onClick={() => handleSelectAnswer(quizData.questions[currentQuestionIndex].id, option)}
                    className={`p-4 rounded-xl text-left transition-all border-2 ${
                      isSelected
                        ? 'border-primaryGreen bg-primaryGreen/10 text-primaryGreenDark font-semibold'
                        : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
                    }`}
                  >
                    <div className="flex items-center gap-3">
                      <span className="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center font-bold text-sm mr-3">
                        {option}
                      </span>
                      {label}
                    </div>
                  </button>
                );
              })}
            </div>
            <div className="flex justify-end mt-8">
              <button
                onClick={handleNext}
                disabled={!selectedAnswers[quizData.questions[currentQuestionIndex].id]}
                className="bg-primaryGreen hover:bg-primaryGreen/90 disabled:opacity-50 disabled:cursor-not-allowed text-white px-8 py-3 rounded-xl font-semibold flex items-center gap-2 transition-all"
              >
                {currentQuestionIndex === totalQuestions - 1 ? 'Finish' : 'Next'}
              </button>
            </div>
          </motion.div>
        )}

        {currentStep === 'results' && (
          <motion.div
            key="results"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-white rounded-2xl p-8 shadow-lg text-center"
          >
            <div className="w-32 h-32 mx-auto mb-6 bg-gradient-to-br from-primaryGreen to-primaryGreenDark rounded-full flex items-center justify-center text-white">
              <Trophy size={64} />
            </div>
            <h2 className="text-3xl font-bold mb-4">Quiz Complete!</h2>
            <p className="text-xl font-semibold text-primaryGreenDark mb-2">
              You scored {score} out of {totalQuestions} ({percentage}%)
            </p>
            <p className="text-textMuted mb-8">
              {percentage >= 80 ? 'Excellent job! You are a sustainability expert!' :
               percentage >= 60 ? 'Great effort! Keep learning!' :
               'Good try! Learn more about sustainability!'}
            </p>
            <div className="flex flex-wrap justify-center gap-8 mb-8">
              {quizData.questions.map((q, i) => {
                const isCorrect = selectedAnswers[q.id] === q.correct_option;
                return (
                  <div key={q.id} className="flex items-center gap-2">
                    {isCorrect ? (
                      <CheckCircle2 size={18} className="text-green-600" />
                    ) : (
                      <XCircle size={18} className="text-red-500" />
                    )}
                    <span className="text-sm">{i + 1}</span>
                  </div>
                );
              })}
            </div>
            <button
              onClick={handleRestart}
              className="bg-primaryGreen hover:bg-primaryGreen/90 text-white px-8 py-3 rounded-xl font-semibold flex items-center gap-2 mx-auto transition-all"
            >
              <RotateCcw size={20} /> Play Again
            </button>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
