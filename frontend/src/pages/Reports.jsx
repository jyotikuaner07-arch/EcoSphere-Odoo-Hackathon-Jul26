import { useState } from 'react';
import { motion } from 'framer-motion';
import { Download } from 'lucide-react';
import { useReportMeta } from '../hooks/useReports';
import Skeleton from '../components/shared/Skeleton';
import ReportFilterPanel from '../components/reports/ReportFilterPanel';
import ReportPreview from '../components/reports/ReportPreview';

const REPORT_LABELS = {
  environmental: 'Environmental Report',
  social: 'Social Report',
  governance: 'Governance Report',
  'esg-summary': 'ESG Summary Report',
};

export default function Reports() {
  const { data, isLoading, isError } = useReportMeta();
  const [activeReport, setActiveReport] = useState('esg-summary');
  const [filters, setFilters] = useState({ department: '', module: '', dateFrom: '' });

  const handleExport = (format) => {
    // NOTE: wire to ENDPOINTS.exportReport(reportId, format) once backend returns a real report id + blob
    alert(`Export as ${format.toUpperCase()} — connect to backend export endpoint here.`);
  };

  if (isError) return <p className="text-danger">Couldn't load reports. Try refreshing.</p>;

  return (
    <div className="space-y-6">
      <h1 className="font-display font-bold text-2xl text-textPrimary">Reports</h1>

      <div className="flex flex-wrap gap-2">
        {isLoading ? <Skeleton className="h-9 w-64" /> : data.reportTypes.map((type) => (
          <button
            key={type}
            onClick={() => setActiveReport(type)}
            className={`px-4 py-2 rounded-full text-sm font-medium transition-colors ${
              activeReport === type ? 'bg-primaryGreen text-white' : 'bg-bgSurface border border-border text-textMuted'
            }`}
          >
            {REPORT_LABELS[type]}
          </button>
        ))}
      </div>

      <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bg-bgSurface border border-border rounded-xl p-5 shadow-card space-y-4">
        <h2 className="font-display font-semibold text-textPrimary">Filters — {REPORT_LABELS[activeReport]}</h2>
        {isLoading ? <Skeleton className="h-10 w-full" /> : <ReportFilterPanel filters={data.filters} values={filters} onChange={setFilters} />}

        <div className="pt-2">
          {isLoading ? <Skeleton className="h-32 w-full" /> : <ReportPreview rows={data.previewRows} />}
        </div>

        <div className="flex gap-2 pt-2">
          {['pdf', 'excel', 'csv'].map((format) => (
            <button
              key={format}
              onClick={() => handleExport(format)}
              className="flex items-center gap-1.5 text-xs font-medium px-3 py-1.5 rounded-full border border-border text-textPrimary hover:bg-bgSurfaceAlt transition-colors"
            >
              <Download size={13} /> {format.toUpperCase()}
            </button>
          ))}
        </div>
      </motion.div>
    </div>
  );
}
