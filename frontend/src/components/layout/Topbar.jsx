import { useAuth } from '../../context/AuthContext';
import { Bell } from 'lucide-react';

export default function Topbar() {
  const { user } = useAuth();
  return (
    <header className="h-16 bg-bgSurface border-b border-border flex items-center justify-end px-6 gap-4">
      <button className="text-textMuted hover:text-primaryGreenDark transition-colors">
        <Bell size={20} />
      </button>
      <span className="text-textMuted text-sm">
        {user?.name} · <span className="text-textPrimary font-medium">{user?.role}</span>
      </span>
    </header>
  );
}