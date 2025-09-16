import { useState } from 'react'
import reactLogo from './assets/react.svg'
import techLogo from '/logo.svg'
import Header from './components/Header'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from './components/Home'
import Login from './components/Login/Login'
import Article from './components/Article/Article'
import './App.css'
import { UserStorage } from './UserContext'
import NotFound from './components/NotFound'
import ProtectedRoutes from './components/Helper/ProtectedRoutes'

function App() {

  return (
    <div className='App h-full'>
      <BrowserRouter>
        <UserStorage>
          <Header />
          <main className='h-full font-newsreader'>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/login/*" element={<Login />} />
              <Route path="/articles/*" element={<ProtectedRoutes><Article /></ProtectedRoutes>} />
              <Route path="*" element={<NotFound />} />
            </Routes>
          </main>
        </UserStorage>
      </BrowserRouter>
    </div>
  )
}

export default App
