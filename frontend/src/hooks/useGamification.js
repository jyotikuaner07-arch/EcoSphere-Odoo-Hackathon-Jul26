import { useQuery } from '@tanstack/react-query';
import client from '../api/axiosClient';
import { ENDPOINTS } from '../api/endpoints';
import mockGamification from '../mocks/gamification.json';

export function useGamification() {
  return useQuery({
    queryKey: ['gamification-summary'],
    queryFn: async () => {
      if (import.meta.env.VITE_USE_MOCKS === 'true') {
        await new Promise((r) => setTimeout(r, 500));
        return mockGamification;
      }
      const { data } = await client.get(ENDPOINTS.challenges());
      return data;
    },
  });
}