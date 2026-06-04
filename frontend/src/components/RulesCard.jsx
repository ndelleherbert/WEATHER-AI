export default function RulesCard({ rules }) {
  if (!rules) return null;

  return (
    <div className="bg-green-900 p-4 rounded-xl">
      <h2 className="text-xl font-bold mb-3">📊 Rules Engine</h2>

      <p><b>Risk:</b> {rules.risk}</p>
      <p><b>Advice:</b> {rules.advice}</p>
      <p><b>Summary:</b> {rules.summary}</p>
    </div>
  );
}