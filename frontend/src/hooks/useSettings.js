import { useQuery } from '@tanstack/react-query';
import mockSettings from '../mocks/settings.json';

export function useSettings() {
  return useQuery({
    queryKey: ['settings'],
    queryFn: async () => {
      if (import.meta.env.VITE_USE_MOCKS === 'true') {
        await new Promise((r) => setTimeout(r, 300));
        return mockSettings;
      }
      return mockSettings; // real: fetch ENDPOINTS.esgSettings + ENDPOINTS.notificationSettings
    },
  });
}