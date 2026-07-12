import { NavLink } from 'react-router-dom';
import { motion } from 'framer-motion';
import { LayoutDashboard, Leaf, Users, ShieldCheck, Trophy, FileText, Settings as SettingsIcon } from 'lucide-react';

const links = [
  { to: '/app/dashboard', label: 'Dashboard', icon: LayoutDashboard },
  { to: '/app/environmental', label: 'Environmental', icon: Leaf },
  { to: '/app/social', label: 'Social', icon: Users },
  { to: '/app/governance', label: 'Governance', icon: ShieldCheck },
  { to: '/app/gamification', label: 'Gamification', icon: Trophy },
  { to: '/app/reports', label: 'Reports', icon: FileText },
  { to: '/app/settings', label: 'Settings', icon: SettingsIcon },
];

export default function Sidebar() {
  return (
    <aside className="w-60 bg-bgSurface border-r border-border h-screen p-4 flex flex-col gap-1">
      <div className="font-display font-extrabold text-xl text-primaryGreenDark mb-6 px-2">
        EcoSphere
      </div>
      {links.map((link) => (
        <NavLink key={link.to} to={link.to}>
          {({ isActive }) => (
            <motion.div
              whileHover={{ x: 3 }}
              className={`relative flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors ${
                isActive ? 'text-primaryGreenDark bg-bgSurfaceAlt' : 'text-textMuted hover:text-textPrimary'
              }`}
            >
              <link.icon size={18} />
              {link.label}
              {isActive && (
                <motion.div
                  layoutId="sidebar-active"
                  className="absolute left-0 top-0 bottom-0 w-1 bg-primaryGreen rounded-r"
                  transition={{ type: 'spring', stiffness: 400, damping: 30 }}
                />
              )}
            </motion.div>
          )}
        </NavLink>
      ))}
    </aside>
  );
}