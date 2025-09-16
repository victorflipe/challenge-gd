import React from 'react'
import Button from '../Forms/Button'
import ArticleHeader from './ArticleHeader'
import Input from '../Forms/Input'
import ArticleForm from './ArticleForm'

const ArticleNew = () => {


  return (
    <section>
      <ArticleForm onSubmit={handleSubmit}/>
    </section>
  )
}

export default ArticleNew