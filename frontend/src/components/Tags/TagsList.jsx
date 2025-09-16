import React from 'react'
import useFetch from '../../hooks/useFetch'
import { GET_TAGS } from '../../api'

const TagsList = ({tagsArticle, tagsSelectedArticle=[], setTagsFiltered}) => {
    // console.log('No começo: ', tagsSelectedArticle)
    const { request } = useFetch()
    const [tags, setTags] = React.useState([])
    const [tagsSelected, setTagsSelected] = React.useState([...tagsSelectedArticle])
    
    React.useEffect(() => {

        if(tagsArticle){
            setTags(tagsArticle)
            return
        }

        async function fetchTags() {
            const { url, options } = GET_TAGS('')
            const { json } = await request(url, options)
            setTags(json.data)
        }

        fetchTags()
    }, [tagsArticle])

    

    React.useEffect(() => {
        console.log('Tags filtradas: ', tagsSelected)
        setTagsFiltered([...tagsSelected])
    }, [tagsSelected])

    React.useEffect(()=>{
        console.log('filtradas 1: ', tagsSelectedArticle)

        setTagsFiltered([...tagsSelectedArticle])
        console.log('filtradas: ', tagsSelected)
    }, [])

    const handleClick = (tag) => {

        const tagExists = tagsSelected.some((item) => item.id == tag.id)

        if (tagExists){
            const tagsFiltered = tagsSelected.filter((tag_item) => tag_item.id != tag.id)
            setTagsSelected(tagsFiltered)
            return
        }

        setTagsSelected([...tagsSelected, tag])
        
        // let filtered = []
        // filtered = tagsSelected.filter((item) =>item !== tag.id)
        // console.log('dsdsds',filtered)
        // setTagsSelected(filtered)
    }


    return (
        <section className=''>
            <div className='w-auto overflow-x-auto h-20 flex items-center'>
                {tags.map((tag, idx) => (
                    <span key={idx} className={`tags ${tagsSelected.map(item => item.id).includes(tag.id) ? 'tag-ativa' : ''}`} onClick={() => handleClick(tag)}>{tag.tag}</span>
                ))}

            </div>
        </section>
    )
}

export default TagsList