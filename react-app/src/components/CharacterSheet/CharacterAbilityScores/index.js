import React from 'react';
import './character-ability-score.css';

const CharacterAbilityScores = ({ character }) => {

  return (
    <div id='character-ability-scores'>
      <div className='ability-score'>
        <h3>STRENGTH</h3>
        <p>{character.strength}</p>
      </div>

      <div className='ability-score'>
        <h3>DEXTERITY</h3>
        <p>{character.dexterity}</p>
      </div>

      <div className='ability-score'>
        <h3>CONSTITUTION</h3>
        <p>{character.constitution}</p>
      </div>

      <div className='ability-score'>
        <h3>INTELLIGENCE</h3>
        <p>{character.intelligence}</p>
      </div>

      <div className='ability-score'>
        <h3>WISDOM</h3>
        <p>{character.wisdom}</p>
      </div>

      <div className='ability-score'>
        <h3>CHARISMA</h3>
        <p>{character.charisma}</p>
      </div>

      <div className='ability-score'>
        <h3>PROFICIENCY</h3>
        <p>+2</p>
        <h4>BONUS</h4>
      </div>

      <div className='ability-score'>
        <h3>WALKING</h3>
        <p>30</p>
        <h4>SPEED</h4>
      </div>

      <div className='ability-score'>
        <h3>INITIATIVE</h3>
        <p>+0</p>
      </div>
    </div>
  )
}

export default CharacterAbilityScores;