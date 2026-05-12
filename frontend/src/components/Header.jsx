import React from 'react'
import { Link } from 'react-router-dom'
import { useCart } from './CartContext'

export default function Header {
const { totalItems } = useCart

return (
<header className="header">
<div className="brand">
<Link to="/">Restaurant</Link>
</div>
<nav>
<Link to="/">Меню</Link>
<Link to="/orders" style={{marginLeft:12}}>Заказы</Link>
<Link to="/cart" style={{marginLeft:12}}>Корзина</Link>
</nav>
</header>

)}