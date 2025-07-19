"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { supabase } from "@/lib/supabaseClient";

export default function ProtocolDetail() {
  const { id } = useParams();
  const [protocol, setProtocol] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchProtocol() {
      setLoading(true);
      const { data, error } = await supabase
        .from("protocol")
        .select("*")
        .eq("id", id)
        .single();
      if (error) {
        setError(error.message);
        setProtocol(null);
      } else {
        setProtocol(data);
        setError(null);
      }
      setLoading(false);
    }
    if (id) fetchProtocol();
  }, [id]);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-8">
      {loading && <p>Loading protocol...</p>}
      {error && <p className="text-red-500">Error: {error}</p>}
      {!loading && !error && protocol && (
        <div className="w-full max-w-2xl bg-white rounded shadow p-6">
          <h1 className="text-2xl font-bold mb-4">{protocol.title}</h1>
          <section className="mb-4">
            <h2 className="font-semibold">Op Note Template</h2>
            <p className="whitespace-pre-line bg-gray-50 p-2 rounded">{protocol.op_note}</p>
          </section>
          <section className="mb-4">
            <h2 className="font-semibold">Post-op Drops</h2>
            <p className="whitespace-pre-line bg-gray-50 p-2 rounded">{protocol.post_op_drops}</p>
          </section>
          <section className="mb-4">
            <h2 className="font-semibold">Follow-up Plan</h2>
            <p className="whitespace-pre-line bg-gray-50 p-2 rounded">{protocol.follow_up}</p>
          </section>
          <section className="mb-4">
            <h2 className="font-semibold">Warnings & Pearls</h2>
            <p className="whitespace-pre-line bg-gray-50 p-2 rounded">{protocol.pearls}</p>
          </section>
          <section className="mb-4">
            <h2 className="font-semibold">Tags</h2>
            <div className="flex flex-wrap gap-2">
              {protocol.tags && protocol.tags.length > 0 ? (
                protocol.tags.map((tag: string, idx: number) => (
                  <span key={idx} className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs">{tag}</span>
                ))
              ) : (
                <span className="text-gray-400">No tags</span>
              )}
            </div>
          </section>
        </div>
      )}
    </main>
  );
} 