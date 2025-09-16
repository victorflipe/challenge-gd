import React from 'react'
// import styles from './Button.module.css'

const Button = ({children, classButton, h, ...props}) => {
  return (
    <button {...props} className={`button ${classButton} ${h}`}>{children}</button>
  )
}

export default Button