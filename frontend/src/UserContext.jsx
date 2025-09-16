import React from 'react'
import { GET_TAGS, GET_USER, LOGIN_USER } from './api'
import { useNavigate } from 'react-router-dom'

export const UserContext = React.createContext()


export const UserStorage = ({ children }) => {

    const [data, setData] = React.useState(null)
    const [login, setLogin] = React.useState(null)
    const [loading, setLoading] = React.useState(false)
    const [error, setError] = React.useState(null)
    const navigate = useNavigate()


    const userLogout = React.useCallback(async () => {
        setData(null)
        setError(null)
        setLoading(false)
        setLogin(false)
        window.localStorage.removeItem('token')
    }, [])

    React.useEffect(() => {
        async function autoLogin() {
            const token = window.localStorage.getItem('token')

            if (token) {
                try {
                    setError(null)
                    setLoading(true)

                    await getUser()

                } catch (error) {
                    setError(error.message)
                    userLogout()
                } finally {
                    setLoading(false)
                }
            } else {
                setLogin(false)
            }
        }
        autoLogin()
    }, [])



    const getUser = async () => {
        const { url, options } = GET_USER()
        const response = await fetch(url, options)
        const json = await response.json()
        setData(json)
        setLogin(true)
    }

    const userLogin = async (email, password) => {
        try {

            setError(null)
            setLoading(true)

            const { url, options } = LOGIN_USER({ email, password })
            const response = await fetch(url, options)
            // const response = await data.json()
            let { data } = await response.json()
            console.log(data)
            
            if (!response.ok) {
                const message = data.detail || "Credenciais inválidas. Tente novamente";
                // setError
                throw new Error(message)
            }

            console.log(data)
            window.localStorage.setItem('token', data.access_token)

            await getUser()

            navigate('/articles')

        } catch (error) {
            setError(error.message)
            setLogin(false)
        } finally {
            setLoading(false)
        }
    }



    return (
        <UserContext.Provider value={{ userLogin, userLogout, data, error, loading, login }}>
            {children}
        </UserContext.Provider>
    )
}