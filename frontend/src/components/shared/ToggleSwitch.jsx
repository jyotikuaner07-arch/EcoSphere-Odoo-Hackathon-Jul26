export default function ToggleSwitch({ checked, onChange, label }) {
  return (
    <label className="flex items-center justify-between py-2 cursor-pointer">
      <span className="text-sm text-textPrimary">{label}</span>
      <button
        role="switch"
        aria-checked={checked}
        onClick={() => onChange(!checked)}
        className={`w-10 h-5.5 rounded-full transition-colors relative ${checked ? 'bg-primaryGreen' : 'bg-gray-300'}`}
      >
        <span
          className={`absolute top-0.5 w-4.5 h-4.5 bg-white rounded-full transition-transform ${checked ? 'translate-x-5' : 'translate-x-0.5'}`}
        />
      </button>
    </label>
  );
}