import React from 'react'
import { Route, Routes } from 'react-router-dom'
import LoginForm from './LoginForm'
import NotFound from '../NotFound'

const Login = () => {
    return (
        <section className='mainContainer'>
            <Routes>
                <Route path="/" element={<LoginForm />} />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </section>
    )
}

export default Login