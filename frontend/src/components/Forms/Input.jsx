import React from 'react'
import styles from './Input.module.css'

const Input = ({ label, placeholder, type, name, value, error, onChange, onBlur}) => {
    return (
        <div className={styles.wrapper}>
            {label && <label htmlFor={name} className={styles.label}>{label}</label>}
            <input id={name} name={name} className={styles.input} type={type} value={value} onChange={onChange} onBlur={onBlur} placeholder={placeholder}/>
            {error && <p className={styles.error}>{error}</p>}
        </div>
    )
}

export default Input