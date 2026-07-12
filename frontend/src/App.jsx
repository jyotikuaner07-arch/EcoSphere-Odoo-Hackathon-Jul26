import { Routes, Route, Navigate, useParams } from 'react-router-dom';
import AppShell from './components/layout/AppShell';
import Dashboard from './pages/Dashboard';
import Environmental from './pages/Environmental';
import Social from './pages/Social';
import Governance from './pages/Governance';
import Gamification from './pages/Gamification';
import Reports from './pages/Reports';
import Settings from './pages/Settings';
import Quiz from './pages/Quiz';
import Games from './pages/Games';
import WasteSortingGame from './components/games/WasteSortingGame';
import EnergySaverGame from './components/games/EnergySaverGame';
import WaterLeakHuntGame from './components/games/WaterLeakHuntGame';

const GameRouter = () => {
  const { gameId } = useParams();
  switch (gameId) {
    case 'waste-sorting':
      return <WasteSortingGame />;
    case 'energy-saver':
      return <EnergySaverGame />;
    case 'water-leak':
      return <WaterLeakHuntGame />;
    default:
      return <Navigate to="/app/games" replace />;
  }
};

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/app/dashboard" replace />} />
      <Route path="/app" element={<AppShell />}>
        <Route path="dashboard" element={<Dashboard />} />
        <Route path="environmental" element={<Environmental />} />
        <Route path="social" element={<Social />} />
        <Route path="governance" element={<Governance />} />
        <Route path="gamification" element={<Gamification />} />
        <Route path="games" element={<Games />} />
        <Route path="games/:gameId" element={<GameRouter />} />
        <Route path="quiz" element={<Quiz />} />
        <Route path="reports" element={<Reports />} />
        <Route path="settings" element={<Settings />} />
      </Route>
    </Routes>
  );
}