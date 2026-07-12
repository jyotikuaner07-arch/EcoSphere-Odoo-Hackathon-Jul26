import { useQuery } from '@tanstack/react-query';
import client from '../api/axiosClient';
import { ENDPOINTS } from '../api/endpoints';
import mockSocial from '../mocks/social.json';

export function useSocial() {
  return useQuery({
    queryKey: ['social-summary'],
    queryFn: async () => {
      if (import.meta.env.VITE_USE_MOCKS === 'true') {
        await new Promise((r) => setTimeout(r, 500));
        return mockSocial;
      }
      const { data } = await client.get(ENDPOINTS.csrActivities);
      return data;
    },
  });
}