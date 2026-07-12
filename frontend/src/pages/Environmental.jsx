import { motion } from 'framer-motion';
import { Leaf, TrendingDown, Target } from 'lucide-react';
import { useEnvironmental } from '../hooks/useEnvironmental';
import KpiCard from '../components/shared/KpiCard';
import Skeleton from '../components/shared/Skeleton';
import DepartmentCarbonChart from '../components/environmental/DepartmentCarbonChart';
import GoalProgressCard from '../components/environmental/GoalProgressCard';
import EmissionFactorTable from '../components/environmental/EmissionFactorTable';
import CarbonTransactionTable from '../components/environmental/CarbonTransactionTable';

export default function Environmental() {
  const { data, isLoading, isError } = useEnvironmental();

  if (isError) {
    return <p className="text-danger">Couldn't load environmental data. Try refreshing.</p>;
  }

  return (
    <div className="space-y-6">
      <h1 className="font-display font-bold text-2xl text-textPrimary">Environmental</h1>

      {/* KPIs */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
        {isLoading ? (
          <>
            <Skeleton className="h-28" />
            <Skeleton className="h-28" />
            <Skeleton className="h-28" />
          </>
        ) : (
          <>
            <KpiCard label="Total Carbon Emitted" value={data.kpis.total_carbon_emitted} suffix=" kg" icon={Leaf} />
            <KpiCard label="Trend vs Last Month" value={data.kpis.carbon_trend_pct} suffix="%" icon={TrendingDown} />
            <KpiCard label="Goals On Track" value={data.kpis.goals_on_track} suffix={` / ${data.kpis.goals_total ?? ''}`} icon={Target} />
          </>
        )}
      </div>

      {/* Chart + Goals */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          className="lg:col-span-2 bg-bgSurface border border-border rounded-xl p-5 shadow-card"
        >
          <h2 className="font-display font-semibold text-textPrimary mb-3">Carbon by Department</h2>
          {isLoading ? <Skeleton className="h-64 w-full" /> : <DepartmentCarbonChart data={data.departmentCarbon} />}
        </motion.div>

        <div className="space-y-4">
          <h2 className="font-display font-semibold text-textPrimary">Sustainability Goals</h2>
          {isLoading ? (
            <>
              <Skeleton className="h-24 w-full" />
              <Skeleton className="h-24 w-full" />
            </>
          ) : (
            data.goals.map((goal) => <GoalProgressCard key={goal.id} goal={goal} />)
          )}
        </div>
      </div>

      {/* Emission Factors */}
      <motion.div
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-bgSurface border border-border rounded-xl p-5 shadow-card"
      >
        <h2 className="font-display font-semibold text-textPrimary mb-3">Emission Factors</h2>
        {isLoading ? <Skeleton className="h-40 w-full" /> : <EmissionFactorTable factors={data.emissionFactors} />}
      </motion.div>

      {/* Carbon Transactions */}
      <motion.div
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-bgSurface border border-border rounded-xl p-5 shadow-card"
      >
        <h2 className="font-display font-semibold text-textPrimary mb-3">Recent Carbon Transactions</h2>
        {isLoading ? <Skeleton className="h-40 w-full" /> : <CarbonTransactionTable transactions={data.carbonTransactions} />}
      </motion.div>
    </div>
  );
}