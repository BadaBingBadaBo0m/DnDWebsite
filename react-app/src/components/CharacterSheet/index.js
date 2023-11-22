import React from 'react';
import './characterSheet.css';

import CharacterAbilityScores from './CharacterAbilityScores';

const CharacterSheet = () => {

  return (
    <div id='character-sheet-container'>
      <ul id='character-sheet-character-info'>
        <li className='character-info-li'>
          <h2>Class</h2>
          <p>Class Name</p>
        </li>

        <li className='character-info-li'>
          <h2>Level</h2>
          <p>Level number</p>
        </li>

        <li className='character-info-li'>
          <h2>Name</h2>
          <h1>Character name</h1>
        </li>

        <li className='character-info-li'>
          <h2>Background</h2>
          <p>Background type</p>
        </li>

        <li className='character-info-li'>
          <h2>Alignment</h2>
          <p>Alignment type</p>
        </li>
      </ul>

      <CharacterAbilityScores />

    </div>
  )
};

export default CharacterSheet;
