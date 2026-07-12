import { NavLink } from 'react-router-dom';
import { motion } from 'framer-motion';
import { LayoutDashboard, Leaf, Users, ShieldCheck, Trophy, FileText, Settings as SettingsIcon, Globe2, HelpCircle } from 'lucide-react';

const links = [
  { to: '/app/dashboard', label: 'Dashboard', icon: LayoutDashboard },
  { to: '/app/environmental', label: 'Environmental', icon: Leaf },
  { to: '/app/social', label: 'Social', icon: Users },
  { to: '/app/governance', label: 'Governance', icon: ShieldCheck },
  { to: '/app/gamification', label: 'Gamification', icon: Trophy },
  { to: '/app/quiz', label: 'Quiz', icon: HelpCircle },
  { to: '/app/reports', label: 'Reports', icon: FileText },
  { to: '/app/settings', label: 'Settings', icon: SettingsIcon },
];

export default function Sidebar() {
  return (
    <aside className="glass-panel w-64 h-screen sticky top-0 p-5 flex flex-col gap-1">
      <div className="flex items-center gap-2 mb-8 px-2">
        <motion.div
          animate={{ rotate: [0, 8, -8, 0] }}
          transition={{ duration: 6, repeat: Infinity, ease: 'easeInOut' }}
          className="w-9 h-9 rounded-full bg-primaryGreen/15 flex items-center justify-center"
        >
          <Globe2 size={20} className="text-primaryGreenDark" />
        </motion.div>
        <span className="font-display font-extrabold text-xl text-primaryGreenDark">
          EcoSphere
        </span>
      </div>
      {links.map((link) => (
        <NavLink key={link.to} to={link.to}>
          {({ isActive }) => (
            <motion.div
              whileHover={{ x: 4 }}
              transition={{ type: 'spring', stiffness: 400, damping: 25 }}
              className={`relative flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium mb-1 ${
                isActive
                  ? 'text-primaryGreenDark bg-white/70 shadow-sm'
                  : 'text-textMuted hover:text-textPrimary hover:bg-white/40'
              }`}
            >
              <link.icon size={18} />
              {link.label}
            </motion.div>
          )}
        </NavLink>
      ))}
    </aside>
  );
}