import { useQuery } from '@tanstack/react-query';
import mockReports from '../mocks/reports.json';

export function useReportMeta() {
  return useQuery({
    queryKey: ['reports-meta'],
    queryFn: async () => {
      if (import.meta.env.VITE_USE_MOCKS === 'true') {
        await new Promise((r) => setTimeout(r, 300));
        return mockReports;
      }
      // real: fetch filter options from backend once available
      return mockReports;
    },
  });
}
