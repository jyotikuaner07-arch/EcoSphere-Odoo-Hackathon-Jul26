import { motion } from 'framer-motion';
import { ShieldCheck, ClipboardList, AlertTriangle } from 'lucide-react';
import { useGovernance } from '../hooks/useGovernance';
import KpiCard from '../components/shared/KpiCard';
import Skeleton from '../components/shared/Skeleton';
import PolicyList from '../components/governance/PolicyList';
import AcknowledgementTracker from '../components/governance/AcknowledgementTracker';
import AuditTable from '../components/governance/AuditTable';
import ComplianceKanban from '../components/governance/ComplianceKanban';

export default function Governance() {
  const { data, isLoading, isError } = useGovernance();

  if (isError) return <p className="text-danger">Couldn't load governance data. Try refreshing.</p>;

  return (
    <div className="space-y-6">
      <h1 className="font-display font-bold text-2xl text-textPrimary">Governance</h1>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
        {isLoading ? (
          <><Skeleton className="h-28" /><Skeleton className="h-28" /><Skeleton className="h-28" /></>
        ) : (
          <>
            <KpiCard label="Policy Ack. Rate" value={data.kpis.policy_ack_rate} suffix="%" icon={ShieldCheck} />
            <KpiCard label="Open Audits" value={data.kpis.open_audits} icon={ClipboardList} />
            <KpiCard label="Overdue Issues" value={data.kpis.overdue_issues} icon={AlertTriangle} />
          </>
        )}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-5">
        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
          <h2 className="font-display font-semibold text-textPrimary mb-3">ESG Policies</h2>
          {isLoading ? <Skeleton className="h-40 w-full" /> : <PolicyList policies={data.policies} />}
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
          <h2 className="font-display font-semibold text-textPrimary mb-3">Policy Acknowledgements</h2>
          {isLoading ? <Skeleton className="h-40 w-full" /> : <AcknowledgementTracker acknowledgements={data.acknowledgements} />}
        </motion.div>
      </div>

      <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
        <h2 className="font-display font-semibold text-textPrimary mb-3">Audits</h2>
        {isLoading ? <Skeleton className="h-40 w-full" /> : <AuditTable audits={data.audits} />}
      </motion.div>

      <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
        <h2 className="font-display font-semibold text-textPrimary mb-3">Compliance Issues</h2>
        {isLoading ? <Skeleton className="h-64 w-full" /> : <ComplianceKanban issues={data.complianceIssues} />}
      </motion.div>
    </div>
  );
}