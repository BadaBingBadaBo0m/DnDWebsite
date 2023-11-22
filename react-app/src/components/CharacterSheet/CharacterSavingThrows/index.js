import React from 'react';
import './characterSavingThrows.css';

const CharacterSavingThrows = () => {

  return (
    <div id='character-saving-throws-container'>
      <div id='character-saving-throws'>
        <div>
          <ul>
            <li className='saving-throw'>
              <p>+3</p>
              <h3>STRENGTH</h3>
            </li>

            <li className='saving-throw'>
              <p>+3</p>
              <h3>DEXTERITY</h3>
            </li>

            <li className='saving-throw'>
              <p>+3</p>
              <h3>CONSTITUTION</h3>
            </li>
          </ul>
        </div>

        <div>
          <ul>
            <li className='saving-throw'>
              <p>+3</p>
              <h3>INTELLIGENCE</h3>
            </li>

            <li className='saving-throw'>
              <p>+3</p>
              <h3>WISDOM</h3>
            </li>

            <li className='saving-throw'>
              <p>+3</p>
              <h3>CHARISMA</h3>
            </li>
          </ul>
        </div>
      </div>

      <h2>SAVING THROWS</h2>
    </div>
  );
}

export default CharacterSavingThrows;