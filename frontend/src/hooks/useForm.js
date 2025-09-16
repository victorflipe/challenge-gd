import React from 'react'

const types = {
    email: {
        regex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        message: "Preencha um email válido"
    },
    password: {
        regex: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/,
        message: "A senha deve ter pelo menos 8 caracteres, incluindo letras e números"
    },
    number: {
        regex: /^\d+$/,
        message: "Utilize apenas números"
    },
    string: {
        regex: /\S+/,
        message: "O campo não pode estar vazio"
    }
}

const useForm = (type) => {
    const [value, setValue] = React.useState('')
    const [error, setError] = React.useState(null)

    const validate = (value) => {
        if (type === false) return true
        if (value.length === 0) {
            setError("Preencha um valor.")
            return false
        }
        if (types[type] && !types[type].regex.test(value)) {
            setError(types[type].message)
            return false
        }
        setError(null)
        return true
    }

    const onChange = ({ target }) => {
        if (error) validate(target.value)
        setValue(target.value)
    }

    return {
        value,
        error,
        setValue,
        onChange,
        validate: () => validate(value),
        onBlur: () => validate(value)
    }
}

export default useForm