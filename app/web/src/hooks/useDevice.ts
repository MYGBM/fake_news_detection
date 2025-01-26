import { useEffect, useState } from 'react';

export const useDevice = () => {
  const [device, setDevice] = useState<string>('desktop');

  useEffect(() => {
    async function check() {
      try {
        const response = await fetch(`/api/agent`);

        const res = await response.json();
        setDevice(res.device);
      } finally {
      }
    }

    check();
  }, []);

  return device;
};
