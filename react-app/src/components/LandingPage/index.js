import React from 'react';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';

const LandingPage = () => {

  return (
    <div>
      <h1>Our crappy dnd website</h1>
      <NavLink to="/charactersheet">Character Sheet</NavLink>
    </div>
  )
}

export default LandingPage;