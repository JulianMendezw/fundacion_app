import React, { useState } from 'react'
import './style.css'
import axios from 'axios'

export const Logging = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [logging, setLogging] = useState(false)
  const [formError, setFormError] = useState(false)

  const handleSubmit = (event) => {
    event.preventDefault();

    const payload_api = {
      "email": email,
      "password": password,
    }
    axios.post("http://127.0.0.1:8000" + '/user/logging', payload_api)
      .then(function (response) {
        if (response.data.message.includes('Authenticated')) {
          console.log('logging success!')
          setFormError(false)
          setLogging(true)

        } else {
          setFormError(true)
          console.log("User authentication failed")
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  return (
    <div className='logging-container'>
      <h1>Bienvenido</h1>
      <p>Por favor ingrese correo y contraseña</p>
      <form onSubmit={(event) => handleSubmit(event)} className='logging-input'>
        <input type="email"
          onChange={(e) => setEmail(e.target.value)}
          value={email} 
          placeholder='Correo'
          />
        <input type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)} 
          placeholder='Contraseña'
          />

        {formError && <p>verifica tu email o contraseña</p>}
        <button type='submit'>Ingresar</button>
      </form>
      {
        logging && <div className='logging-success'>
          <img src="https://cdn.worldvectorlogo.com/logos/check-solid.svg" alt="" />
          <p>El usuario ha ingresado</p></div>
      }
    </div>
  )
}
