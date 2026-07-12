import { useQuery } from '@tanstack/react-query';
import client from '../api/axiosClient';
import { ENDPOINTS } from '../api/endpoints';
import mockGovernance from '../mocks/governance.json';

export function useGovernance() {
  return useQuery({
    queryKey: ['governance-summary'],
    queryFn: async () => {
      if (import.meta.env.VITE_USE_MOCKS === 'true') {
        await new Promise((r) => setTimeout(r, 500));
        return mockGovernance;
      }
      const { data } = await client.get(ENDPOINTS.complianceIssues());
      return data;
    },
  });
}