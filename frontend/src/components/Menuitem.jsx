import React from 'react'

export default function MenuItem, onAdd {

return (
<div className="card menu-item">
{item.image ? <img src={item.image} alt={item.name} /> : <div style={{height:140, background:'#eee', borderRadius:6}} />}
<h3>{item.name}</h3>
<p className="small">{item.description}</p>
<div className="row" style={{marginTop:8, justifyContent:'space-between'}}>
<strong>{item.price}$</strong>
<button className="btn" onClick={onAdditem}>Добавить</button>
</div>
</div>
)}