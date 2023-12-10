import CharacterAbilityScores from './CharacterAbilityScores';
import CharacterSavingThrows from './CharacterSavingThrows';
import CharacterVitals from './CharacterVitals';
import CharacterConditionsAndEffects from './CharacterConditions&Effects';
import CharacterBonuses from './CharacterBonuses';
import CharacterSkills from './CharacterSkills';
import CharacterProficiencies from './CharacterProficiencies';
import QuickReference from './CharacterQuickReference';

import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getCharacterById } from '../../store/character';
import './characterSheet.css';

const CharacterSheet = () => {
  const dispatch = useDispatch();
  const character = useSelector(state => state.currentCharacter)
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    (async () => {
      const res = await dispatch(getCharacterById(3));

      if (res.errors) {
        setErrors(res);
      }
    })();
  }, []);

  if (!Object.keys(character).length) {
    return (
      <h1>Bruh it loading</h1>
    );
  };


  return (
    <div id='character-sheet-container'>
      <ul id='character-sheet-character-info'>
        <li className='character-info-li'>
          <h2>Class</h2>
          <p>{character.classes[0].name}</p>
        </li>

        <li className='character-info-li'>
          <h2>Level</h2>
          <p>{character.level}</p>
        </li>

        <li className='character-info-li'>
          <h2>Name</h2>
          <h1>{character.name}</h1>
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

      <CharacterAbilityScores character={character} />

      <div id='character-sheet-character-stats'>
        <CharacterSavingThrows />

        <CharacterVitals character={character} />

        <CharacterConditionsAndEffects character={character} />

        <CharacterBonuses />
      </div>

      <div id='character-proficiency-skills-quick-reference'>
        <CharacterSkills />

        <CharacterProficiencies />

        <QuickReference />
      </div>

    </div>
  )
};

export default CharacterSheet;
