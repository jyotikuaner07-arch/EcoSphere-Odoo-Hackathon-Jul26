import { motion } from 'framer-motion';
import { Leaf, Users, ShieldAlert } from 'lucide-react';
import { useDashboard } from '../hooks/useDashboard';
import ESGRing from '../components/shared/ESGRing';
import KpiCard from '../components/shared/KpiCard';
import Skeleton from '../components/shared/Skeleton';
import XPBar from '../components/gamification/XPBar';

export default function Dashboard() {
  const { data, isLoading, isError } = useDashboard();

  if (isError) {
    return <p className="text-danger">Couldn't load dashboard data. Try refreshing.</p>;
  }

  return (
    <div className="space-y-6">
      <h1 className="font-display font-bold text-2xl text-textPrimary">Dashboard</h1>

      {/* Hero row: ESG Ring + KPI cards */}
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-5">
        <div className="bg-bgSurface border border-border rounded-xl p-6 shadow-card flex items-center justify-center lg:col-span-1">
          {isLoading ? (
            <Skeleton className="h-44 w-44 rounded-full" />
          ) : (
            <ESGRing scores={data.organizationScore} />
          )}
        </div>

        <div className="lg:col-span-3 grid grid-cols-1 sm:grid-cols-3 gap-5">
          {isLoading ? (
            <>
              <Skeleton className="h-28" />
              <Skeleton className="h-28" />
              <Skeleton className="h-28" />
            </>
          ) : (
            <>
              <KpiCard label="Carbon Emitted (mo)" value={data.kpis.total_carbon_emitted} suffix=" kg" icon={Leaf} />
              <KpiCard label="CSR Participation" value={data.kpis.csr_participation_rate} suffix="%" icon={Users} />
              <KpiCard label="Open Compliance Issues" value={data.kpis.open_compliance_issues} icon={ShieldAlert} />
            </>
          )}
        </div>
      </div>

      {/* Second row: leaderboard + activity + XP */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="bg-bgSurface border border-border rounded-xl p-5 shadow-card"
        >
          <h2 className="font-display font-semibold text-textPrimary mb-3">Department Leaderboard</h2>
          {isLoading ? (
            <Skeleton className="h-40 w-full" />
          ) : (
            <ul className="space-y-2">
              {data.departmentLeaderboard.map((dept, i) => (
                <li key={dept.department_id} className="flex items-center justify-between text-sm py-1.5 border-b border-border last:border-0">
                  <span className="text-textMuted">{i + 1}. {dept.name}</span>
                  <span className="font-tabular font-semibold text-primaryGreenDark">{dept.total_score}</span>
                </li>
              ))}
            </ul>
          )}
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="bg-bgSurface border border-border rounded-xl p-5 shadow-card"
        >
          <h2 className="font-display font-semibold text-textPrimary mb-3">Recent Activity</h2>
          {isLoading ? (
            <Skeleton className="h-40 w-full" />
          ) : (
            <ul className="space-y-3">
              {data.recentActivity.map((item) => (
                <li key={item.id} className="text-sm text-textMuted">
                  <span className="text-textPrimary">{item.message}</span>
                </li>
              ))}
            </ul>
          )}
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="bg-bgSurface border border-border rounded-xl p-5 shadow-card"
        >
          <h2 className="font-display font-semibold text-textPrimary mb-3">Your Progress</h2>
          {isLoading ? (
            <Skeleton className="h-16 w-full" />
          ) : (
            <XPBar
              current={data.employeeXp.current_xp}
              floor={data.employeeXp.current_level_floor}
              nextFloor={data.employeeXp.next_level_floor}
            />
          )}
        </motion.div>
      </div>
    </div>
  );
}