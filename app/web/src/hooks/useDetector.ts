import { useState } from 'react';

export interface DetectorResult {
  prediction: {
    logistic_regression: string;
    gradient_boosting: string;
    random_forest: string;
    decision_tree: string;
  };

  probabilities: {
    logistic_regression: number;
    gradient_boosting: number;
    random_forest: number;
    decision_tree: number;
  };
}

export const useDetector = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<DetectorResult | null>(null);

  async function detect(text: string) {
    try {
      setLoading(true);
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/detect-news`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text }),
        }
      );

      const res = await response.json();
      setResult(res);
    } finally {
      setLoading(false);
    }
  }

  const reset = () => {
    setResult(null);
  };

  return {
    detect,
    loading,
    result,
    reset,
  };
};
