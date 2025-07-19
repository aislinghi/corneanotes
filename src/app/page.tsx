"use client";

import Image from "next/image";
import { supabase } from "@/lib/supabaseClient";
import { useEffect, useState } from "react";

export default function Home() {
  const [status, setStatus] = useState("Testing Supabase connection...");

  useEffect(() => {
    async function testSupabase() {
      try {
        // Try to fetch from a table that may not exist yet
        const { data, error } = await supabase.from("protocol").select("*").limit(1);
        if (error) {
          setStatus(`Supabase connected, but error fetching: ${error.message}`);
        } else {
          setStatus("Supabase connection successful!");
        }
      } catch (err) {
        setStatus(`Supabase connection failed: ${err}`);
      }
    }
    testSupabase();
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-2xl font-bold mb-4">OphthoGuide</h1>
      <p>{status}</p>
    </main>
  );
}
