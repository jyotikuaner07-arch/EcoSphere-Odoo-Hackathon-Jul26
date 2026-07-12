const COLORS = {
  Active: 'text-primaryGreenDark bg-bgSurfaceAlt',
  Inactive: 'text-textMuted bg-gray-100',
  AUTO: 'text-accentBlue bg-blue-50',
  MANUAL: 'text-accentAmber bg-amber-50',
  Draft: 'text-textMuted bg-gray-100',
  Active_Challenge: 'text-primaryGreenDark bg-bgSurfaceAlt',
  'Under Review': 'text-accentAmber bg-amber-50',
  Completed: 'text-accentBlue bg-blue-50',
  Archived: 'text-textMuted bg-gray-100',
  Open: 'text-danger bg-red-50',
  Resolved: 'text-primaryGreenDark bg-bgSurfaceAlt',
  Overdue: 'text-white bg-danger',
  Pending: 'text-accentAmber bg-amber-50',
  Approved: 'text-primaryGreenDark bg-bgSurfaceAlt',
  Rejected: 'text-danger bg-red-50',
};

export default function StatusBadge({ status }) {
  return (
    <span className={`text-xs font-medium px-2.5 py-1 rounded-full ${COLORS[status] || 'text-textMuted bg-bgSurfaceAlt'}`}>
      {status}
    </span>
  );
}