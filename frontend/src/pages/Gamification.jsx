import { motion } from 'framer-motion';
import { useGamification } from '../hooks/useGamification';
import Skeleton from '../components/shared/Skeleton';
import ChallengeBoard from '../components/gamification/ChallengeBoard';
import BadgeCard from '../components/gamification/BadgeCard';
import LeaderboardTable from '../components/gamification/LeaderboardTable';
import RewardCard from '../components/gamification/RewardCard';

export default function Gamification() {
  const { data, isLoading, isError } = useGamification();

  if (isError) return <p className="text-danger">Couldn't load gamification data. Try refreshing.</p>;

  return (
    <div className="space-y-6">
      <h1 className="font-display font-bold text-2xl text-textPrimary">Gamification</h1>

      <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
        <h2 className="font-display font-semibold text-textPrimary mb-3">Challenges</h2>
        {isLoading ? <Skeleton className="h-64 w-full" /> : <ChallengeBoard challenges={data.challenges} />}
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="lg:col-span-2 bg-bgSurface border border-border rounded-xl p-5 shadow-card">
          <h2 className="font-display font-semibold text-textPrimary mb-3">Badges</h2>
          {isLoading ? <Skeleton className="h-32 w-full" /> : (
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
              {data.badges.map((b) => <BadgeCard key={b.id} badge={b} employeeStats={data.employeeStats} />)}
            </div>
          )}
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
          <h2 className="font-display font-semibold text-textPrimary mb-3">Leaderboard</h2>
          {isLoading ? <Skeleton className="h-40 w-full" /> : <LeaderboardTable leaderboard={data.leaderboard} />}
        </motion.div>
      </div>

      <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
        <h2 className="font-display font-semibold text-textPrimary mb-3">Rewards</h2>
        {isLoading ? <Skeleton className="h-32 w-full" /> : (
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            {data.rewards.map((r) => <RewardCard key={r.id} reward={r} />)}
          </div>
        )}
      </motion.div>
    </div>
  );
}