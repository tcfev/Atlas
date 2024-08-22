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

export async function uploadLogo(path,file) {
    const { data, error } = await supabase.storage.from('logos').upload(path, file)
    if (error) {
      // Handle error
    } else {
      // Handle success
    }
  }