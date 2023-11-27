import React from 'react';
import './characterProficiencies.css';

const CharacterProficiencies = () => {

  return (
    <div id='character-proficiency-container'>

      <div className='proficiency-container'>
        <h2 className='character-sheet-h2'>Armor & Weapons</h2>
      </div>

      <div className='proficiency-container'>
        <h2 className='character-sheet-h2'>Tools</h2>
      </div>

      <div className='proficiency-container'>
        <h2 className='character-sheet-h2'>Languages</h2>
      </div>

    </div>
  );
};

export default CharacterProficiencies;