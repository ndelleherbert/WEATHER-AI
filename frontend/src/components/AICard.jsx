export default function AICard({ ai }) {
  if (!ai) return null;

  return (
    <div className="bg-purple-900 p-4 rounded-xl">
      <h2 className="text-xl font-bold mb-3">🧠 AI Analysis</h2>

      <p><b>Summary:</b> {ai.summary}</p>
      <p><b>Risk:</b> {ai.risk_level}</p>
      <p><b>Insight:</b> {ai.insight}</p>

      <div className="mt-2">
        <b>Recommendations:</b>
        <ul className="list-disc ml-5">
          {ai.recommendations?.map((r, i) => (
            <li key={i}>{r}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}