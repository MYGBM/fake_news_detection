import { DetectorResult } from '@/hooks/useDetector';
import React, { useState } from 'react';
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { Skeleton } from '@/components/ui/skeleton';
import { Cell, Pie, PieChart } from 'recharts';
import { AlertTriangle } from 'lucide-react';

export default function Analysis({
  result,
  loading,
}: {
  result?: DetectorResult | null;
  loading?: boolean;
}) {
  const [selectedModel, setSelectedModel] =
    useState<string>('gradient_boosting');

  const chartData = result
    ? [
        {
          name: result.prediction[
            selectedModel as keyof DetectorResult['prediction']
          ],
          value:
            result.probabilities[
              selectedModel as keyof DetectorResult['prediction']
            ] * 100,
        },
        {
          name:
            result.prediction[
              selectedModel as keyof DetectorResult['prediction']
            ] == 'Fake'
              ? 'Real'
              : 'Fake',
          value:
            (1 -
              result.probabilities[
                selectedModel as keyof DetectorResult['prediction']
              ]) *
            100,
        },
      ]
    : [];
  return (
    <div className="overflow-hidden bg-white rounded-xl shadow-sm border border-slate-200 p-6">
      <div className="flex justify-between">
        <h2 className="text-xl font-semibold text-slate-800 mb-6">
          Analysis Results
        </h2>

        {result && (
          <div className="flex gap-2">
            <Select
              defaultValue={selectedModel}
              onValueChange={setSelectedModel}
            >
              <SelectTrigger className="w-[180px]">
                <SelectValue placeholder="Select model" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectLabel>Models</SelectLabel>
                  <SelectItem value="logistic_regression">
                    Logistic Regression
                  </SelectItem>
                  <SelectItem value="decision_tree">Decision Tree</SelectItem>
                  <SelectItem value="random_forest">Random Forest</SelectItem>
                  <SelectItem value="gradient_boosting">
                    Gradient Boosting
                  </SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </div>
        )}
      </div>

      {loading && (
        <Skeleton className="w-full h-1/2 flex items-center justify-center">
          Analyzing...
        </Skeleton>
      )}

      {!loading && result && (
        <div
          key={`selectedModel-${selectedModel}`}
          className={`${
            result.prediction[
              selectedModel as keyof DetectorResult['prediction']
            ] === 'Fake'
              ? 'bg-red-50 border-red-100'
              : 'bg-green-50 border-green-100'
          } border rounded-lg p-4 mb-6`}
        >
          <div className="flex items-center gap-2 mb-2">
            <AlertTriangle
              className={`w-5 h-5 ${
                result.prediction[
                  selectedModel as keyof DetectorResult['prediction']
                ] === 'Fake'
                  ? 'text-red-500'
                  : 'text-green-500'
              }`}
            />
            <h3
              className={`font-semibold ${
                result.prediction[
                  selectedModel as keyof DetectorResult['prediction']
                ] === 'Fake'
                  ? 'text-red-700'
                  : 'text-green-700'
              }`}
            >
              Likely{' '}
              {
                result.prediction[
                  selectedModel as keyof DetectorResult['prediction']
                ]
              }{' '}
              News
            </h3>
          </div>
          <p
            className={`text-sm ${
              result.prediction[
                selectedModel as keyof DetectorResult['prediction']
              ] === 'Fake'
                ? 'text-red-600'
                : 'text-green-600'
            }`}
          >
            Our analysis indicates this article{' '}
            {result.prediction[
              selectedModel as keyof DetectorResult['prediction']
            ] === 'Fake'
              ? 'contains potential misinformation'
              : 'appears to be authentic'}
            .
          </p>
        </div>
      )}

      {!loading && result && (
        <div className="overflow-auto">
          <h3 className="font-medium text-slate-700 mb-4">
            Confidence Analysis
          </h3>
          <div className="flex justify-center overflow-auto">
            <PieChart
              width={350}
              margin={{ top: 10, right: 25, left: 25, bottom: 5 }}
              height={300}
              key={selectedModel}
            >
              <Pie
                data={chartData}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                outerRadius={80}
                label={(entry) => `${entry.name} (${entry.value.toFixed(2)}%)`}
                labelLine={false}
              >
                {chartData.map((entry, index) => (
                  <Cell
                    key={index}
                    fill={
                      entry.name === 'Fake'
                        ? 'rgb(239, 68, 68)'
                        : 'rgb(34, 197, 94)'
                    }
                  />
                ))}
              </Pie>
            </PieChart>
          </div>
        </div>
      )}
    </div>
  );
}
