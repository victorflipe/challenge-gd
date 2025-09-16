import React from 'react'
import styles from './TextArea.module.css'

const TextArea = ({ label, placeholder, name, value, error, onChange, onBlur, rows, cols}) => {
    return (
        <div className={styles.wrapper}>
            {label && <label htmlFor={name} className={styles.label}>{label}</label>}
            <textarea id={name} name={name} className={styles.textarea} value={value} onChange={onChange} onBlur={onBlur} placeholder={placeholder} rows={rows} cols={cols}/>
            {error && <p className={styles.error}>{error}</p>}
        </div>
    )
}

export default TextArea