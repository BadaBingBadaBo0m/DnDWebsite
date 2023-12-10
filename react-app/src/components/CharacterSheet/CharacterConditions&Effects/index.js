import React from 'react';
import './characterConditions&Effects.css';

const CharacterConditionsAndEffects = ({ character }) => {

  return (
    <div id='character-conditions-and-effects-container'>
      <div id='character-hitDice-armorClass-deathSave-container'>
        <div id='character-hit-dice-container'>

          <div id='hit-die-container'>
            <div className='hit-die max'>
              <h2 className='character-sheet-h2'>MAX</h2>
              <p>{character.level}</p>
            </div>

            <div className='hit-die current'>
              <h2 className='character-sheet-h2'>CURRENT</h2>
              <p>{character.classes[0].hit_dice}</p>
            </div>
          </div>

          <h2 className='character-sheet-h2'>HIT DICE</h2>
        </div>

        <div id='character-armor-class'>
          {/* armor class is calculated later 10 + dex modifier + armor*/}
          <p>16</p>
          <h2 className='character-sheet-h2'>ARMOR</h2>
          <h2 className='character-sheet-h2'>CLASS</h2>
        </div>

        <div id='character-death-saves'>
          <div className='death-save failure'>
            <h2 className='character-sheet-h2'>FAILURE</h2>
            <i className="fa-regular fa-circle"></i>
            <i className="fa-regular fa-circle"></i>
            <i className="fa-regular fa-circle"></i>
          </div>

          <div className='death-save success'>
            <h2 className='character-sheet-h2'>SUCCESS</h2>
            <i className="fa-regular fa-circle"></i>
            <i className="fa-regular fa-circle"></i>
            <i className="fa-regular fa-circle"></i>
          </div>

          <h2 className='character-sheet-h2'>DEATH SAVES</h2>
        </div>
      </div>

      <div id='conditions-effects'>
        <p>CONDITIONS</p>
        <h2 className='character-sheet-h2'>CONDITIONS</h2>
      </div>
    </div>

  );
}

export default CharacterConditionsAndEffects;