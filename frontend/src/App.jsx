import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Menu from './pages/Menu'
import Cart from './pages/Cart'
import Checkout from './pages/Checkout'
import Orders from './pages/Orders'
import Header from './components/Header'

export default function App {
return (
<div className="app">
<Header />
<main className="container">
<Routes>
<Route path="/" element={<Menu />} />
<Route path="/cart" element={<Cart />} />
<Route path="/checkout" element={<Checkout />} />
<Route path="/orders" element={<Orders />} />
</Routes>
</main>
</div>
)}