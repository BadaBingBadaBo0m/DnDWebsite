import React from 'react';
import './characterVitals.css';

const CharacterVitals = () => {

  return (
    <div id='character-vitals-container'>
      <div id='character-temp-max-hp'>
        <div className='character-vital'>
          <h2 className='character-sheet-h2'>MAX HP</h2>
          <p>HP</p>
        </div>

        <div className='character-vital'>
          <h2 className='character-sheet-h2'>TEMP HP</h2>
          <p>TEMP HP</p>
        </div>
      </div>

      <div id='character-current-hp'>
        <h2 className='character-sheet-h2'>HP</h2>
        <p>HP NUMBER</p>
      </div>
    </div>
  );
}

export default CharacterVitals;