import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';

export default function DiversityChart({ data }) {
  return (
    <ResponsiveContainer width="100%" height={260}>
      <BarChart data={data} layout="vertical">
        <CartesianGrid strokeDasharray="3 3" stroke="#DCE5DE" horizontal={false} />
        <XAxis type="number" tick={{ fill: '#5C6B62', fontSize: 12 }} axisLine={{ stroke: '#DCE5DE' }} />
        <YAxis type="category" dataKey="category" tick={{ fill: '#5C6B62', fontSize: 12 }} width={100} axisLine={{ stroke: '#DCE5DE' }} />
        <Tooltip contentStyle={{ background: '#FFFFFF', border: '1px solid #DCE5DE', borderRadius: 8 }} />
        <Bar dataKey="value" fill="#D9A441" radius={[0, 6, 6, 0]} />
      </BarChart>
    </ResponsiveContainer>
  );
}