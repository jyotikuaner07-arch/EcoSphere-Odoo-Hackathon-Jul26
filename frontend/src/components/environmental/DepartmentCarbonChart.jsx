import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';

export default function DepartmentCarbonChart({ data }) {
  return (
    <ResponsiveContainer width="100%" height={260}>
      <BarChart data={data}>
        <CartesianGrid strokeDasharray="3 3" stroke="#DCE5DE" vertical={false} />
        <XAxis dataKey="department" tick={{ fill: '#5C6B62', fontSize: 12 }} axisLine={{ stroke: '#DCE5DE' }} />
        <YAxis tick={{ fill: '#5C6B62', fontSize: 12 }} axisLine={{ stroke: '#DCE5DE' }} />
        <Tooltip
          contentStyle={{ background: '#FFFFFF', border: '1px solid #DCE5DE', borderRadius: 8 }}
          labelStyle={{ color: '#16241C', fontWeight: 600 }}
        />
        <Bar dataKey="co2e" fill="#2F7D4F" radius={[6, 6, 0, 0]} />
      </BarChart>
    </ResponsiveContainer>
  );
}