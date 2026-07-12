import { NavLink } from 'react-router-dom';

const links = [
  { to: '/app/dashboard', label: 'Dashboard' },
  { to: '/app/environmental', label: 'Environmental' },
  { to: '/app/social', label: 'Social' },
  { to: '/app/governance', label: 'Governance' },
  { to: '/app/gamification', label: 'Gamification' },
  { to: '/app/reports', label: 'Reports' },
  { to: '/app/settings', label: 'Settings' },
];

export default function Sidebar() {
  return (
    <aside className="w-56 bg-bgSurface h-screen p-4 flex flex-col gap-2">
      <div className="text-accentGrowth font-bold text-lg mb-4">EcoSphere</div>
      {links.map((link) => (
        <NavLink
          key={link.to}
          to={link.to}
          className={({ isActive }) =>
            `px-3 py-2 rounded text-textMuted hover:text-textPrimary ${isActive ? 'bg-bgBase text-accentGrowth' : ''}`
          }
        >
          {link.label}
        </NavLink>
      ))}
    </aside>
  );
}