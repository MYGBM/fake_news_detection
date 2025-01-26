import { Shield } from 'lucide-react';
import React from 'react';

export default function Header() {
  return (
    <header className="mb-12 text-center">
      <div className="flex items-center justify-center gap-2 mb-4">
        <Shield className="w-8 h-8 text-blue-600" />
        <h1 className="text-3xl font-bold text-slate-800">Fake News Checker</h1>
      </div>
      <p className="text-slate-600 max-w-3xl mx-auto">
        Verify the authenticity of news articles. Our tool helps you identify
        potential misinformation.
      </p>
    </header>
  );
}
