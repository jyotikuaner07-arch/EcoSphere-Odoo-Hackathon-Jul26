import { useAuth } from '../../context/AuthContext';
import { Bell } from 'lucide-react';

export default function Topbar() {
  const { user } = useAuth();
  return (
    <header className="glass-panel h-16 flex items-center justify-end px-8 gap-5 sticky top-0 z-10 border-b-0">
      <button className="text-textMuted hover:text-primaryGreenDark transition-colors">
        <Bell size={20} />
      </button>
      <span className="text-textMuted text-sm">
        {user?.name} · <span className="text-textPrimary font-medium">{user?.role}</span>
      </span>
    </header>
  );
}