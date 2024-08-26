import { supabase } from '$lib/supabaseClient';

export async function getEntity(entityId) {
  const res = await supabase.from('Entities').select('*').eq('id', entityId).single();
  if (res.error) {
    throw new Error(res.error.message);
  }
  return res.data;
}


export async function updateEntity(entityId, data) {
  const res = await supabase.from('Entities').update(data).eq('id', +entityId);
  if (res.error) {
    throw new Error(res.error.message);
  }
  return res.data;
}

export async function uploadLogo(path, file) {
  const { data, error } = await supabase.storage.from('logos').upload(path, file)
  if (error) {
    // Handle error
  } else {
    // Handle success
  }
}


export async function getEntities() {
  const res = await supabase.from('Entities').select('*');
  if (res.error) {
    throw new Error(res.error.message);
  }
  return res.data;
}

export async function fixNamesInDB() {
  // select all entities
  const res = await supabase.from('Entities').select('*');
  if (res.error) {
    throw new Error(res.error.message);
  }
  // if there is no name then use farsi name (name_fa) and if there is no farsi name then use english name (name_en)
  const changes = [];
  res.data.forEach(entity => {
    if (!entity.name) {
      if (entity.name_fa) {
        changes.push({ id: entity.id, name: entity.name_fa });
      } else if (entity.name_en) {
        changes.push({ id: entity.id, name: entity.name_en });
      }
    }
  });

  // update all entities
  changes.forEach(async change => {
    const res = await supabase.from('Entities').update(change).eq('id', change.id);
    if (res.error) {
      throw new Error(res.error.message);
    }
  });

}


export async function createEntity(data) {
  const res = await supabase.from('Entities').insert(data);
  if (res.error) {
    throw new Error(res.error.message);
  }
  return res.data;
}