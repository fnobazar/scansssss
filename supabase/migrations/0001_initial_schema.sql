create extension if not exists "pgcrypto";

create table if not exists public.profiles (
    id uuid primary key references auth.users(id) on delete cascade,
    display_name text,
    avatar_url text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create table if not exists public.discoveries (
    id uuid primary key default gen_random_uuid(),
    user_id uuid not null references auth.users(id) on delete cascade,
    type text not null,
    title text not null,
    description text,
    result jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now()
);

create table if not exists public.saved_items (
    id uuid primary key default gen_random_uuid(),
    user_id uuid not null references auth.users(id) on delete cascade,
    discovery_id uuid not null references public.discoveries(id) on delete cascade,
    created_at timestamptz not null default now(),
    unique(user_id, discovery_id)
);

create table if not exists public.searches (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references auth.users(id) on delete cascade,
    query text not null,
    created_at timestamptz not null default now()
);

create table if not exists public.scans (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references auth.users(id) on delete cascade,
    image_url text,
    result jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now()
);

create index if not exists discoveries_user_id_idx
on public.discoveries(user_id);

create index if not exists saved_items_user_id_idx
on public.saved_items(user_id);

create index if not exists searches_user_id_idx
on public.searches(user_id);

create index if not exists scans_user_id_idx
on public.scans(user_id);

alter table public.profiles enable row level security;
alter table public.discoveries enable row level security;
alter table public.saved_items enable row level security;
alter table public.searches enable row level security;
alter table public.scans enable row level security;

create policy "Users can view own profile"
on public.profiles
for select
using (auth.uid() = id);

create policy "Users can update own profile"
on public.profiles
for update
using (auth.uid() = id);

create policy "Users can view own discoveries"
on public.discoveries
for select
using (auth.uid() = user_id);

create policy "Users can create own discoveries"
on public.discoveries
for insert
with check (auth.uid() = user_id);

create policy "Users can delete own discoveries"
on public.discoveries
for delete
using (auth.uid() = user_id);

create policy "Users can view own saved items"
on public.saved_items
for select
using (auth.uid() = user_id);

create policy "Users can create own saved items"
on public.saved_items
for insert
with check (auth.uid() = user_id);

create policy "Users can delete own saved items"
on public.saved_items
for delete
using (auth.uid() = user_id);

create policy "Users can view own searches"
on public.searches
for select
using (auth.uid() = user_id);

create policy "Users can create own searches"
on public.searches
for insert
with check (auth.uid() = user_id);

create policy "Users can view own scans"
on public.scans
for select
using (auth.uid() = user_id);

create policy "Users can create own scans"
on public.scans
for insert
with check (auth.uid() = user_id);

create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
    insert into public.profiles (id, display_name, avatar_url)
    values (
        new.id,
        new.raw_user_meta_data ->> 'full_name',
        new.raw_user_meta_data ->> 'avatar_url'
    )
    on conflict (id) do nothing;

    return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;

create trigger on_auth_user_created
after insert on auth.users
for each row
execute procedure public.handle_new_user();
