import React, { useState } from 'react';

export default function ROICalculator() {
  const [arr, setArr] = useState(250); // in millions USD
  const [facilities, setFacilities] = useState(15);

  // Value calculations based on platform benchmarks
  const estimatedOpexSavings = (arr * 0.0035).toFixed(2); // ~12% utility OPEX reduction impact
  const estimatedAuditSavings = (facilities * 45000 * 0.65).toLocaleString(); // 65% savings on $45k/facility audit costs
  const totalAnnualValue = (parseFloat(estimatedOpexSavings) * 1000000 + parseFloat(estimatedAuditSavings.replace(/,/g, ''))).toLocaleString();

  return (
    <div className="max-w-3xl mx-auto p-8 bg-slate-900 text-white rounded-2xl shadow-2xl border border-slate-800">
      <div className="text-center mb-8">
        <span className="px-3 py-1 text-xs font-semibold bg-emerald-500/15 text-emerald-400 rounded-full border border-emerald-500/30">
          ESG Profit Engine
        </span>
        <h2 className="text-3xl font-bold mt-3">Enterprise ROI & Value Calculator</h2>
        <p className="text-slate-400 mt-2">See how regulatory compliance transforms into a direct bottom-line financial asset.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <div className="bg-slate-800/50 p-5 rounded-xl border border-slate-700/50">
          <label className="block text-sm font-medium text-slate-300 mb-2">Company ARR: ${arr}M</label>
          <input 
            type="range" min="50" max="1000" step="25" value={arr} 
            onChange={(e) => setArr(Number(e.target.value))}
            className="w-full accent-emerald-500 cursor-pointer"
          />
        </div>
        <div className="bg-slate-800/50 p-5 rounded-xl border border-slate-700/50">
          <label className="block text-sm font-medium text-slate-300 mb-2">Global Facilities: {facilities}</label>
          <input 
            type="range" min="5" max="100" step="5" value={facilities} 
            onChange={(e) => setFacilities(Number(e.target.value))}
            className="w-full accent-emerald-500 cursor-pointer"
          />
        </div>
      </div>

      <div className="bg-emerald-950/30 border border-emerald-500/30 rounded-xl p-6 text-center">
        <p className="text-sm text-emerald-400 uppercase tracking-wider font-semibold">Total Estimated Annual Value Generated</p>
        <p className="text-4xl font-extrabold text-emerald-300 mt-2">${totalAnnualValue}</p>
        <div className="grid grid-cols-2 gap-4 mt-6 pt-6 border-t border-emerald-500/20 text-left">
          <div>
            <p className="text-xs text-slate-400">OPEX Reduction (Utility Spikes)</p>
            <p className="text-lg font-bold text-white mt-1">${estimatedOpexSavings}M / yr</p>
          </div>
          <div>
            <p className="text-xs text-slate-400">Audit Cost Savings (65% reduction)</p>
            <p className="text-lg font-bold text-white mt-1">${estimatedAuditSavings} / yr</p>
          </div>
        </div>
      </div>
    </div>
  );
}
