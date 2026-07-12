import { motion } from 'framer-motion';
import { Users, GraduationCap, Activity } from 'lucide-react';
import { useSocial } from '../hooks/useSocial';
import KpiCard from '../components/shared/KpiCard';
import Skeleton from '../components/shared/Skeleton';
import CSRActivityCard from '../components/social/CSRActivityCard';
import ParticipationApprovalQueue from '../components/social/ParticipationApprovalQueue';
import DiversityChart from '../components/social/DiversityChart';

export default function Social() {
  const { data, isLoading, isError } = useSocial();

  if (isError) return <p className="text-danger">Couldn't load social data. Try refreshing.</p>;

  return (
    <div className="space-y-6">
      <h1 className="font-display font-bold text-2xl text-textPrimary">Social</h1>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
        {isLoading ? (
          <><Skeleton className="h-28" /><Skeleton className="h-28" /><Skeleton className="h-28" /></>
        ) : (
          <>
            <KpiCard label="Participation Rate" value={data.kpis.participation_rate} suffix="%" icon={Users} />
            <KpiCard label="Training Completion" value={data.kpis.training_completion} suffix="%" icon={GraduationCap} />
            <KpiCard label="Active Activities" value={data.kpis.active_activities} icon={Activity} />
          </>
        )}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="space-y-3">
          <h2 className="font-display font-semibold text-textPrimary">CSR Activities</h2>
          {isLoading ? <Skeleton className="h-48 w-full" /> : (
            <div className="space-y-3">
              {data.csrActivities.map((a) => <CSRActivityCard key={a.id} activity={a} />)}
            </div>
          )}
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="lg:col-span-2 bg-bgSurface border border-border rounded-xl p-5 shadow-card">
          <h2 className="font-display font-semibold text-textPrimary mb-3">Participation Approval Queue</h2>
          {isLoading ? <Skeleton className="h-48 w-full" /> : <ParticipationApprovalQueue items={data.participationQueue} />}
        </motion.div>
      </div>

      <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
        <h2 className="font-display font-semibold text-textPrimary mb-3">Diversity Metrics</h2>
        {isLoading ? <Skeleton className="h-64 w-full" /> : <DiversityChart data={data.diversityMetrics} />}
      </motion.div>
    </div>
  );
}