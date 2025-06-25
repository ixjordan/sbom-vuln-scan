import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import UploadForm from "./UploadForm";

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-4xl font-bold text-blue-700 mb-2">SBOM Vulnerability Dashboard</h1>
      <p className="text-gray-600 text-lg mb-6">Scan SBOM files or GitHub URLs for known vulnerabilities</p>

      <UploadForm />
    </div>
  );
}

export default App;

