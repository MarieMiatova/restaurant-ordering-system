import React, { useState } from 'react' 
import { useNavigate } from 'react-router-dom' import { useCart } from '../components/CartContext' 
import { createOrder } from '../api'

export default function Checkout() { 
  const { items, totalPrice, clear } = useCart() const [name, setName] = useState('') 
  const [phone, setPhone] = useState('') const [loading, setLoading] = useState(false) 
  const navigate = useNavigate()

  const submit = async () => { 
    if (!name || !phone) { alert('Введите имя и телефон') 
      return } setLoading(true) 
      const order = { 
        customer: { name, phone }, 
        items: items.map(i => ({ id: i.id, name: i.name, qty: i.qty, price: i.price })),
        total: totalPrice 
      } 
     const res = await createOrder(order), 
     setLoading(false)
    
    if (res && res.id) { clear() alert('Заказ создан. ID: ' + res.id) navigate('/orders') } 
    else { alert('Не удалось создать заказ (mock used)') clear() navigate('/') } }

return (

<div>
<h1>Оформление заказа</h1>
<div className="card" style={{maxWidth:540}}>
<label>Имя</label>
<input value={name} onChange={e=>setName.target.value} style={{width:'100%',padding:8,marginTop:6,marginBottom:12}} />
<label>Телефон</label>
<input value={phone} onChange={e=>setPhone.target.value} style={{width:'100%',padding:8,marginTop:6,marginBottom:12}} />
<div className="small">Итого: {totalPrice.toFixed2} $</div>
<div style={{marginTop:12}}>
<button className="btn" onClick={submit} disabled={loading}>{loading ? 'Отправка...' : 'Отправить заказ'}</button>
</div>
</div>
</div>)}