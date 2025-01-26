import { NextResponse, userAgent } from 'next/server';

export function GET({ headers }: Request) {
  const agent = userAgent({ headers });

  return NextResponse.json({
    device: agent?.device?.type === 'mobile' ? 'mobile' : 'desktop',
  });
}
