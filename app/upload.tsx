// frontend/pages/upload.tsx
import React, { useState } from 'react'

export default function Upload() {
  const [file, setFile] = useState(null)

  const handleUpload = async () => {
    const formData = new FormData()
    formData.append("file", file)
    await fetch("/upload/", {
      method: "POST",
      body: formData,
    })
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Upload Academic Document</h1>
      <input type="file" onChange={(e) => setFile(e.target.files?.[0])} />
      <button className="bg-blue-500 text-white px-4 py-2 mt-2" onClick={handleUpload}>Upload</button>
    </div>
  )
}
