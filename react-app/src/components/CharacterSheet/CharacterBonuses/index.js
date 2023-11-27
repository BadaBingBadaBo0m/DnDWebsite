import React from 'react';
import './characterBonuses.css';

const CharacterBonuses = () => {

  return (
    <ul id='character-bonuses-container'>
      <li className='character-bonus'>
        <h2 className='character-sheet-h2'>SPELL ATTACK BONUS</h2>
        <p>+0</p>
      </li>

      <li className='character-bonus'>
        <h2 className='character-sheet-h2'>SPELL SAVE DC</h2>
        <p>8</p>
      </li>

      <li className='character-bonus'>
        <h2 className='character-sheet-h2'>CONCENTRATION SAVE</h2>
        <p>+0</p>
      </li>

      <li className='character-bonus'>
        <h2 className='character-sheet-h2'>PASSIVE PERCEPTION</h2>
        <p>+0</p>
      </li>
    </ul>
  )
}

export default CharacterBonuses;