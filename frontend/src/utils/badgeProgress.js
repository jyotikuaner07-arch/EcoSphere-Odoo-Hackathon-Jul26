export function formatBadgeProgress(unlockRule, employeeStats) {
  const { metric, operator, value } = unlockRule;
  const current = employeeStats[metric] ?? 0;
  const met = operator === '>=' ? current >= value : current === value;
  return { current, target: value, label: `${current} of ${value}`, met };
}