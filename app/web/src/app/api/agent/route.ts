import { NextResponse, userAgent } from 'next/server';

export function GET({ headers }: { headers: Headers }) {
  const agent = userAgent({ headers });

  return NextResponse.json({
    device: agent?.device?.type === 'mobile' ? 'mobile' : 'desktop',
  });
}
