import React, { useEffect, useState } from 'react' 
import { getMenu } from '../api' 
import MenuItem from '../components/MenuItem' 
import { useCart } from '../components/CartContext'

export default function Menu() { const [menu, setMenu] = useState([]) const [loading, setLoading] = useState(true) 
  const { addToCart } = useCart()

useEffect(() => { 
  getMenu().then(data => { setMenu(data || []) setLoading(false) }) }, []
)

return (
  <div>
  <h1>Меню</h1>
  {loading ? <p>Загрузка...</p> : null}
  <div className="grid">
  {menu.map(item => (
  <MenuItem key={item.id} item={item} onAdd={addToCart} />
  ))}
  </div>
  <p className="footer-note">Данные берутся из {import.meta.env.VITE_API_BASE || '/api'}</p>
  </div>
)}