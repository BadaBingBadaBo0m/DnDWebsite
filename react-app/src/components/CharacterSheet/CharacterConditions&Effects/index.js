import React from 'react';
import './characterConditions&Effects.css';

const CharacterConditionsAndEffects = () => {

  return (
    <div id='character-conditions-and-effects-container'>
      <div id='character-hitDice-armorClass-deathSave-container'>
        <div id='character-hit-dice-container'>

          <div id='hit-die-container'>
            <div className='hit-die max'>
              <h2 className='character-sheet-h2'>MAX</h2>
              <p>1d8</p>
            </div>

            <div className='hit-die current'>
              <h2 className='character-sheet-h2'>CURRENT</h2>
              <p>1d8</p>
            </div>
          </div>

          <h2 className='character-sheet-h2'>HIT DICE</h2>
        </div>

        <div id='character-armor-class'>
          <p>16</p>
          <h2 className='character-sheet-h2'>ARMOR</h2>
          <h2 className='character-sheet-h2'>CLASS</h2>
        </div>

        <div id='character-death-saves'>
          <div id='death-save-failure'>
            <h2 className='character-sheet-h2'>FAILURE</h2>
          </div>

          <div id='death-save-success'>
            <h2 className='character-sheet-h2'>SUCCESS</h2>
          </div>

          <h2 className='character-sheet-h2'>DEATH SAVES</h2>
        </div>
      </div>

    </div>

  );
}

export default CharacterConditionsAndEffects;