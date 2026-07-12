import { useQuery } from '@tanstack/react-query';
import client from '../api/axiosClient';
import { ENDPOINTS } from '../api/endpoints';
import mockDashboard from '../mocks/dashboard.json';

export function useDashboard() {
  return useQuery({
    queryKey: ['dashboard-summary'],
    queryFn: async () => {
      if (import.meta.env.VITE_USE_MOCKS === 'true') {
        // simulate network delay so the skeleton loading state is visible while you build
        await new Promise((r) => setTimeout(r, 500));
        return mockDashboard;
      }
      const { data } = await client.get(ENDPOINTS.dashboardSummary);
      return data;
    },
  });
}