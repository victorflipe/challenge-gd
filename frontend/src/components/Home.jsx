import React from 'react'
import { Link } from 'react-router-dom'


const Home = () => {
    return (
        <div className='mainContainer'>
            <h1 className='text-6xl font-semibold pb-5'>Insights & Learning</h1>
            <p className='text-xl pb-5'>Explorando as tendências Tech, um post por vez</p>
            <Link to="/login" className='button'>
                Começar a ler
            </Link>
        </div>
    )
}

export default Home