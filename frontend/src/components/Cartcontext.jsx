import React, { createContext, useContext, useState } from 'react'

const CartContext = createContext()

export function CartProvider({ children }) { const [items, setItems] = useState([])

const addToCart = (product) => { setItems(prev => { 
  const found = prev.find(p => p.id === product.id) 
  if (found) return prev.map(p => p.id === product.id ? {...p, qty: p.qty + 1} : p) 
    return [...prev, {...product, qty: 1}] 
  })
}

const removeFromCart = (id) => { setItems(prev => prev.filter(p => p.id !== id)) }
const updateQty = (id, qty) => { setItems(prev => prev.map(p => p.id === id ? {...p, qty: Math.max(1, qty)} : p)) }
const clear = () => setItems([])

const totalItems = items.reduce((s, i) => s + i.qty, 0) 
const totalPrice = items.reduce((s, i) => s + i.qty * (i.price || 0), 0)

return ( {children} ) }

export const useCart = () => useContext(CartContext)