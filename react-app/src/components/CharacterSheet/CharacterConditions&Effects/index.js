import React from 'react';
import './characterConditions&Effects.css';

const CharacterConditionsAndEffects = () => {

  return (
    <div id='character-conditions-and-effects-container'>
      <div id='character-hitDice-armorClass-deathSave-container'>
        <div id='character-hit-dice-container'>
          <div className='hit-die max'>
            <h2 className='character-sheet-h2'>MAX</h2>
            <p>1d8</p>
          </div>

          <div className='hit-die current'>
            <h2 className='character-sheet-h2'>CURRENT</h2>
            <p>1d8</p>
          </div>
        </div>

        <h2>HIT DICE</h2>
      </div>

    </div>
  );
}

export default CharacterConditionsAndEffects;