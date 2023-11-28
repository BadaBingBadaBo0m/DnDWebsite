import React from 'react';
import { useSelector, useDispatch } from "react-redux"
import './CharacterItem.css';

const CharacterItem = ({character}) => {

    return (
        <div className='character-item'>
          <h1>{character.name}</h1>
          <p>{character.level} | {character.race.name}</p>
        </div>
      )

}

export default CharacterItem ;