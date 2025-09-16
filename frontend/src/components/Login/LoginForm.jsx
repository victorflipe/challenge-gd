import React from 'react'
import Button from '../Forms/Button'
import useForm from '../../hooks/useForm'
import Input from '../Forms/Input'
import { UserContext } from '../../UserContext'
import Modal from '../Modal/Modal'

const LoginForm = () => {

    const email = useForm()
    const password = useForm()
    const { userLogin, error, loading, data, login } = React.useContext(UserContext)
    const [message, setMessage] = React.useState('')
    const [isOpen, setIsOpen] = React.useState(false);

    const handleLogin = async (event) => {
        event.preventDefault()

        try{

            if (email.validate() && password.validate()) {
                console.log(email.value)
                console.log(password.value)
                await userLogin(email.value, password.value)
                console.log(error)
                if(error){
                    setMessage(error)
                    setIsOpen(true)
                }
            }
        }catch(error){
            console.log(error)
            setMessage('Erro ao efetuar login')
            setIsOpen(true)
        }

    }

    React.useEffect(() => {
        // console.log(data)
    }, [])


    return (
        <section className='w-full lg:py-10'>
            <h1 className='text-4xl text-center font-semibold pb-5'>Bem vindo de volta</h1>
            <div className='mainContainer'>
                <form onSubmit={handleLogin} className='w-[40rem]'>
                    <Input label={"Email"} name="email" {...email} placeholder="Email" h={"h-[2rem]"}/>
                    <Input label={"Senha"} name="senha" {...password} placeholder="Senha" h={"h-[2rem]"}/>
                    <Button classButton={"w-full"}>Entrar</Button>

                    {/* <Error error={error && "Usuário ou senha inválidos"} /> */}
                </form>
            </div>

            {isOpen && <Modal onClose={() => setIsOpen(false)} >
                <div className='w-70 h-50 p-2 flex flex-col justify-center font-newsreader'>
                    <h1 className={`text-lg text-center font-semibold pb-2 text-red-600`}>{message}</h1>
                </div>
            </Modal>}
        </section>
    )
}

export default LoginForm