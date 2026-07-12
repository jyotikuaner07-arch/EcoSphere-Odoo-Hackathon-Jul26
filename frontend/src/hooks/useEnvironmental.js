import { useQuery } from '@tanstack/react-query';
import client from '../api/axiosClient';
import { ENDPOINTS } from '../api/endpoints';
import mockEnvironmental from '../mocks/environmental.json';

export function useEnvironmental() {
  return useQuery({
    queryKey: ['environmental-summary'],
    queryFn: async () => {
      if (import.meta.env.VITE_USE_MOCKS === 'true') {
        await new Promise((r) => setTimeout(r, 500));
        return mockEnvironmental;
      }
      // Real integration: combine these once backend endpoints are live
      const [factors, transactions, goals] = await Promise.all([
        client.get(ENDPOINTS.emissionFactors),
        client.get(ENDPOINTS.carbonTransactions()),
        client.get(ENDPOINTS.goals()),
      ]);
      return {
        emissionFactors: factors.data,
        carbonTransactions: transactions.data,
        goals: goals.data,
      };
    },
  });
}