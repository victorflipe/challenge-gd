import React from 'react'
import ArticleList from './ArticleList'
import ArticleNew from './ArticleNew'
import { Route, Routes } from 'react-router-dom'
import ArticleRead from './ArticleRead'
import { UserContext } from '../../UserContext'
import ArticleEdit from './ArticleEdit'

const Article = () => {

    // const {article} = React.useContext(UserContext)
    
    return (
        <section className='lg:px-[10rem]'>
            <Routes>
                <Route path="/" element={<ArticleList />} />
                <Route path="/new" element={<ArticleNew />} />
                <Route path="/read" element={<ArticleRead/>} />
                <Route path="/edit" element={<ArticleEdit/>} />
            </Routes>
        </section>
    )
}

export default Article