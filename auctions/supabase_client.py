from supabase import create_client, Client

url: str = "https://antowpgqpbqtojkbdbzx.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFudG93cGdxcGJxdG9qa2JkYnp4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMjE4NTQ5OCwiZXhwIjoyMDE3NzYxNDk4fQ.Bksils0hKlA179BtUBkDY8ucACiQXVPxHPp1sdxkJ-s"
supabase: Client = create_client(url, key)
