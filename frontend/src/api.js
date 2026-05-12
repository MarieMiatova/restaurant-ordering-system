async function safeFetch(url, options) { 
  try { const res = await 
    fetch(url, options) 
    if (!res.ok) throw new Error('network') 
      return res.json() } 
    catch (e) { 
      return null 
    } }

export async function getMenu() { 
  const data = await safeFetch(${API_BASE}/menu) 
  if (data) return data 
  return [ { id: 1, name: 'Маргарита', description: 'Томатный соус, сыр', price: 8.5, image: '' }, 
    { id: 2, name: 'Пепперони', description: 'Острая колбаса, сыр', price: 10.0, image: '' }, 
    { id: 3, name: 'Салат Цезарь', description: 'Курица, пармезан', price: 7.0, image: '' } ] 
  }

export async function createOrder(order) { 
  const res = await safeFetch(${API_BASE}/orders, { method: 'POST', headers: { 'Content-Type': 'application/json' }, 
    body: JSON.stringify(order) }) 
    if (res) return res 
    return { id: Math.floor(Math.random()*10000), status: 'created', ...order } 
}

export async function getOrders() { 
  const data = await safeFetch(${API_BASE}/orders) 
  if (data) return data 
  return [ { id: 1234, total: 25.5, items: [{ name: 'Пепперони', qty: 1 }], createdAt: new Date().toISOString() } ]
}