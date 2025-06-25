import { useState } from "react";
import axios from "axios";

function UploadForm() {
  const [file, setFile] = useState(null);
  const [url, setUrl] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const formData = {};

    if (file) {
      // For now we just send the file path placeholder
      // You'd need to handle actual file content with a real backend
      formData.file_path = "sample_data/sample_sbom.json"; // Placeholder for demo
    } else if (url) {
      formData.url = url;
    }

    try {
      const res = await axios.post("http://127.0.0.1:8000/api/scan", formData);
      setResponse(res.data);
    } catch (err) {
      alert("Something went wrong: " + err.message);
    }

    setLoading(false);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow mb-6">
      <h2 className="text-xl font-semibold mb-4">Scan SBOM</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block mb-1 font-medium">Upload SBOM File</label>
          <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        </div>
        <div>
          <label className="block mb-1 font-medium">Or Enter GitHub Manifest URL</label>
          <input
            type="text"
            placeholder="https://github.com/user/repo/blob/main/requirements.txt"
            className="border border-gray-300 p-2 w-full rounded"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
        </div>
        <button
          type="submit"
          disabled={loading}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          {loading ? "Scanning..." : "Scan Now"}
        </button>
      </form>

      {response && (
        <div className="mt-6 p-4 bg-gray-100 rounded">
          <h3 className="font-semibold mb-2">Scan Result:</h3>
          <pre className="text-sm">{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default UploadForm;
