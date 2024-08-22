
import { createClient } from "@supabase/supabase-js";

// THESE ARE PUBLIC KEYS, NO NEED TO HIDE THEM
const SUPABASE_URL = "https://nfqygicyznsmfftnobxo.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5mcXlnaWN5em5zbWZmdG5vYnhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjQxMDE5MzgsImV4cCI6MjAzOTY3NzkzOH0.9Swj4OZI9K-Xzg6Cm9zmkFy9CXWQq5E6aAQnDoYGRLE";

const supabaseUrl = SUPABASE_URL;
const supabaseKey = SUPABASE_ANON_KEY;

export const supabase = createClient(supabaseUrl, supabaseKey);
