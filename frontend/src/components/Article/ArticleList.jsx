import React from 'react'
import ArticleHeader from './ArticleHeader'
import Button from '../Forms/Button'
import { useNavigate } from 'react-router-dom'
import TagsList from '../Tags/TagsList'
import Input from '../Forms/Input'
import ArticleListItems from './ArticleListItems'
import useFetch from '../../hooks/useFetch'
import { GET_ARTICLES } from '../../api'
import useForm from '../../hooks/useForm'

const ArticleList = () => {

  const navigate = useNavigate()
  const { request } = useFetch()
  const filter = useForm('')

  const [articles, setArticles] = React.useState([])
  const [tagsFiltered, setTagsFiltered] = React.useState([])
  const [allArticles, setAllArticles] = React.useState([])

  const [pagination, setPagination] = React.useState(null)
  const [page, setPage] = React.useState(1)


  async function fetchArticles(fetchAll = false) {
    const limit = fetchAll ? 100 : 10 // ou número máximo de artigos
    const skip = fetchAll ? 0 : Math.max((page - 1) * limit, 0)
    const { url, options } = GET_ARTICLES(skip, limit)
    const { json } = await request(url, options)

    if (fetchAll) {
      setAllArticles(json.data)
    } else {
      setArticles(json.data)
      setPagination(json.pagination)
    }

  }

  React.useEffect(() => {
    if (filter.value.length >= 4 || tagsFiltered.length > 0) {
      if (allArticles.length === 0) fetchArticles(true)
    } else {
      fetchArticles()
    }
  }, [page, filter.value, tagsFiltered])


  React.useEffect(() => {
    let filtered = allArticles

    if (filter.value.length >= 4) {
      filtered = filtered.filter(item =>
        item.title.toLowerCase().includes(filter.value.toLowerCase())
      )
    }

    if (tagsFiltered.length > 0) {
      const tagsList = tagsFiltered.map(t => t.tag)
      filtered = filtered.filter(item =>
        item.tags.some(tag => tagsList.includes(tag.tag))
      )
    }

    const limit = 10
    const skip = Math.max((page - 1) * limit, 0)
    const paginated = filtered.slice(skip, skip + limit)

    setArticles(paginated)
    setPagination({
      total: filtered.length,
      skip,
      limit,
      pages: Math.ceil(filtered.length / limit)
    })
  }, [allArticles, filter.value, tagsFiltered, page])


  return (
    <section className='mb-10 md:px-[5rem]'>
      <ArticleHeader>
        <div className="flex justify-between items-center py-2">
          <h1 className='text-3xl font-semibold'>{"Todos os Artigos"}</h1>
          <Button onClick={() => navigate('/articles/new')}>Criar artigo</Button>
        </div>
      </ArticleHeader>



      <div className='mt-5'>

        <Input placeholder={"Pesquisar"} name="Pesquisar" onChange={() => filterArticles()} {...filter} error={false} />
      
        <TagsList setTagsFiltered={setTagsFiltered} />

        <ArticleListItems articles={articles} />

      </div>


      {pagination && (
        <div className="flex gap-2 mt-10 pb-10 justify-center">
          {Array.from({ length: pagination.pages }, (_, idx) => (
            <button
              key={idx}
              onClick={() => setPage(idx + 1)}
              className={`px-3 py-1 rounded-full cursor-pointer ${page === idx + 1 ? "bg-[#EDF2E8]" : ""
                }`}
            >
              {idx + 1}
            </button>
          ))}
        </div>
      )}

    </section>
  )
}

export default ArticleList