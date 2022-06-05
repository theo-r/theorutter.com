import React from 'react'
import { Link } from 'gatsby'
import styled from 'styled-components'
import Navbar from './navbar'

const Header = () => {
  return (

    <div
      style={{
        textAlign: `center`,
        color: `white`,
      }}
    >
      <h1
        style={{
          paddingTop: `3rem`,
          paddingBottom: `1rem`,
          marginBottom: 0,
          marginTop: 0,
          fontStyle: `bold`,
          fontSize: `42px`
        }}
      >
        <Link
          style={{
            boxShadow: `none`,
            textDecoration: `none`,
            color: `inherit`,
          }}
          to={`/`}
        >
          {`Theo Rutter`}
        </Link>
      </h1>
      <Navbar />
    </div >
  )
}


const StyledHeader = styled(Header)`
  width: 100%;
  background-position: center center;
  background-repeat: repeat-y;
  background-size: cover;
`

export default StyledHeader