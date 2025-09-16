import React from 'react'
import Button from '../Forms/Button'
import ArticleHeader from './ArticleHeader'
import Input from '../Forms/Input'
import ArticleForm from './ArticleForm'
import { useLocation } from 'react-router-dom';

const ArticleEdit = () => {

  const location = useLocation();
  const { article } = location.state || {};

  return (
    <section>
      {/* <ArticleForm onSubmit={handleSubmit} /> */}
      <ArticleForm article={article} />
    </section>
  )
}

export default ArticleEdit