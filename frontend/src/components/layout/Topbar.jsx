import { useAuth } from '../../context/AuthContext';

export default function Topbar() {
  const { user } = useAuth();
  return (
    <header className="h-14 bg-bgSurface flex items-center justify-end px-6 gap-4">
      <span className="text-textMuted text-sm">{user?.name} · {user?.role}</span>
    </header>
  );
}