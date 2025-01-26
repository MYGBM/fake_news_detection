import { useEffect, useState } from 'react';

export const useDevice = () => {
  const [device, setDevice] = useState('mobile');

  useEffect(() => {
    const userAgent = navigator.userAgent.toLowerCase();
    const mobile =
      /android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(
        userAgent
      );
    if (mobile) {
      setDevice('mobile');
    } else {
      setDevice('desktop');
    }
  }, []);

  return device;
};
