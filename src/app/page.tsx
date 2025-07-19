"use client";

import { supabase } from "@/lib/supabaseClient";
import { useEffect, useState } from "react";
import Link from "next/link";

export default function Home() {
  const [protocols, setProtocols] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchProtocols() {
      setLoading(true);
      const { data, error } = await supabase.from("protocol").select("id, title").order("created_at", { ascending: false });
      if (error) {
        setError(error.message);
        setProtocols([]);
      } else {
        setProtocols(data || []);
        setError(null);
      }
      setLoading(false);
    }
    fetchProtocols();
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-2xl font-bold mb-4">OphthoGuide Protocols</h1>
      {loading && <p>Loading protocols...</p>}
      {error && <p className="text-red-500">Error: {error}</p>}
      {!loading && !error && (
        <ul className="w-full max-w-xl">
          {protocols.length === 0 ? (
            <li className="text-gray-500">No protocols found.</li>
          ) : (
            protocols.map((protocol) => (
              <li key={protocol.id} className="border-b py-2">
                <Link href={`/protocol/${protocol.id}`} className="text-blue-600 hover:underline">
                  {protocol.title}
                </Link>
              </li>
            ))
          )}
        </ul>
      )}
    </main>
  );
}
