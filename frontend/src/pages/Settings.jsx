import { useState } from 'react';
import { motion } from 'framer-motion';
import { useSettings } from '../hooks/useSettings';
import Skeleton from '../components/shared/Skeleton';
import ToggleSwitch from '../components/shared/ToggleSwitch';
import StatusBadge from '../components/shared/StatusBadge';

export default function Settings() {
  const { data, isLoading, isError } = useSettings();
  const [weights, setWeights] = useState(null);
  const [toggles, setToggles] = useState(null);
  const [notifs, setNotifs] = useState(null);

  if (isError) return <p className="text-danger">Couldn't load settings. Try refreshing.</p>;
  if (!isLoading && !weights) {
    // hydrate local editable state once on load
    setWeights(data.esgSettings.weights);
    setToggles({
      auto_emission_calculation: data.esgSettings.auto_emission_calculation,
      evidence_requirement: data.esgSettings.evidence_requirement,
      badge_auto_award: data.esgSettings.badge_auto_award,
    });
    setNotifs(data.notificationSettings);
  }

  return (
    <div className="space-y-6">
      <h1 className="font-display font-bold text-2xl text-textPrimary">Settings</h1>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-5">
        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
          <h2 className="font-display font-semibold text-textPrimary mb-3">Departments</h2>
          {isLoading ? <Skeleton className="h-32 w-full" /> : (
            <table className="w-full text-sm">
              <tbody>
                {data.departments.map((d) => (
                  <tr key={d.id} className="border-b border-border last:border-0">
                    <td className="py-2 text-textPrimary">{d.name}</td>
                    <td className="py-2 text-textMuted">{d.code}</td>
                    <td className="py-2 font-tabular text-textMuted">{d.employee_count} employees</td>
                    <td className="py-2"><StatusBadge status={d.status} /></td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
          <h2 className="font-display font-semibold text-textPrimary mb-3">Categories</h2>
          {isLoading ? <Skeleton className="h-32 w-full" /> : (
            <table className="w-full text-sm">
              <tbody>
                {data.categories.map((c) => (
                  <tr key={c.id} className="border-b border-border last:border-0">
                    <td className="py-2 text-textPrimary">{c.name}</td>
                    <td className="py-2 text-textMuted">{c.type}</td>
                    <td className="py-2"><StatusBadge status={c.status} /></td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </motion.div>
      </div>

      <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
        <h2 className="font-display font-semibold text-textPrimary mb-3">ESG Weighting</h2>
        {isLoading || !weights ? <Skeleton className="h-24 w-full" /> : (
          <div className="space-y-3">
            {Object.entries(weights).map(([key, val]) => (
              <div key={key}>
                <div className="flex justify-between text-sm mb-1">
                  <span className="capitalize text-textPrimary">{key}</span>
                  <span className="font-tabular text-textMuted">{val}%</span>
                </div>
                <input
                  type="range" min={0} max={100} value={val}
                  onChange={(e) => setWeights({ ...weights, [key]: Number(e.target.value) })}
                  className="w-full accent-primaryGreen"
                />
              </div>
            ))}
            <p className="text-xs text-textMuted">Total: {Object.values(weights).reduce((a, b) => a + b, 0)}% (should equal 100%)</p>
          </div>
        )}
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-5">
        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
          <h2 className="font-display font-semibold text-textPrimary mb-3">Configuration Toggles</h2>
          {isLoading || !toggles ? <Skeleton className="h-24 w-full" /> : (
            <>
              <ToggleSwitch label="Auto Emission Calculation" checked={toggles.auto_emission_calculation} onChange={(v) => setToggles({ ...toggles, auto_emission_calculation: v })} />
              <ToggleSwitch label="Evidence Requirement" checked={toggles.evidence_requirement} onChange={(v) => setToggles({ ...toggles, evidence_requirement: v })} />
              <ToggleSwitch label="Badge Auto-Award" checked={toggles.badge_auto_award} onChange={(v) => setToggles({ ...toggles, badge_auto_award: v })} />
            </>
          )}
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card">
          <h2 className="font-display font-semibold text-textPrimary mb-3">Notification Settings</h2>
          {isLoading || !notifs ? <Skeleton className="h-24 w-full" /> : (
            <>
              <ToggleSwitch label="Compliance Issue Raised" checked={notifs.compliance_issue_raised} onChange={(v) => setNotifs({ ...notifs, compliance_issue_raised: v })} />
              <ToggleSwitch label="Approval Decisions" checked={notifs.approval_decisions} onChange={(v) => setNotifs({ ...notifs, approval_decisions: v })} />
              <ToggleSwitch label="Policy Reminders" checked={notifs.policy_reminders} onChange={(v) => setNotifs({ ...notifs, policy_reminders: v })} />
              <ToggleSwitch label="Badge Unlocked" checked={notifs.badge_unlocked} onChange={(v) => setNotifs({ ...notifs, badge_unlocked: v })} />
              <ToggleSwitch label="Also Send Email" checked={notifs.email_enabled} onChange={(v) => setNotifs({ ...notifs, email_enabled: v })} />
            </>
          )}
        </motion.div>
      </div>
    </div>
  );
}