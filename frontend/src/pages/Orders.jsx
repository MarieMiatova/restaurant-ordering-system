import React, { useEffect, useState } from 'react' 
import { getOrders } from '../api'

export default function Orders() { 
  const [orders, setOrders] = useState(null) 
  useEffect(() => { getOrders().then(d => setOrders(d || [])) }, []) 
  if (orders === null) 
    return  <p>Загрузка...</p>
return (

<div>

<h1>Заказы</h1>
{orders.length === 0 ? <p>Нет заказов</p> : (
<div className="grid">

{orders.map(o => (
<div key={o.id} className="card">
<div><strong>ID:</strong> {o.id}</div>

<div className="small">{o.createdAt ? new Dateo.createdAt.toLocaleString: ''}</div>
<div><strong>Итого:</strong> {o.total} $</div>

<div className="small">{o.items?.map(it => ${it.name} x${it.qty}).join(', ')}</div>
</div>))}
</div>)}
</div>)}