'use client';
import KeywriteWeb from '@keywrite/web';
import { Amharic } from '@keywrite/ethiopic-input-methods';
import { useEffect, useRef, useState } from 'react';
import { Textarea } from '@/components/ui/textarea';
import { Button } from '@/components/ui/button';

import { useDetector } from '@/hooks/useDetector';
import Header from '@/components/header';
import Analysis from '@/components/analysis';

export default function Home() {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [keywrite, setKeywrite] = useState<KeywriteWeb>();
  const [value, setValue] = useState<string>('');

  useEffect(() => {
    if (textareaRef.current && !keywrite) {
      setKeywrite(
        new KeywriteWeb(textareaRef.current, {
          Amharic: Amharic.inputMethod,
        })
      );
    }
  }, [setKeywrite, keywrite]);

  const { detect, loading, result } = useDetector();

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-slate-100">
      <div className="px-4 py-8">
        <Header />

        <div className="grid lg:grid-cols-2 gap-8">
          <div className="w-full h-full flex flex-col bg-white rounded-xl shadow-sm border border-slate-200 p-6">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-xl font-semibold text-slate-800">
                News Article
              </h2>
            </div>

            <Textarea
              ref={textareaRef}
              placeholder="Paste your news article here..."
              className="w-full h-48 rounded-b-none focus:ring-0 focus-visible:ring-0 focus-visible:border-ring"
              onChange={(e) => setValue(e.target.value)}
              value={value}
            />

            <div className="flex w-full">
              <Button
                className="w-full rounded-t-none"
                disabled={loading || value === ''}
                onClick={() =>
                  textareaRef?.current?.value &&
                  detect(textareaRef?.current?.value)
                }
              >
                Verify
              </Button>
            </div>
          </div>

          <Analysis result={result} loading={loading} />
        </div>
      </div>
    </div>
  );
}
