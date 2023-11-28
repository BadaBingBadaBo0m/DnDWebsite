import React from 'react';
import { useSelector, useDispatch } from "react-redux"
import './CharacterItem.css';

const CharacterItem = ({character}) => {
    const curentUser = useSelector(state => state.session.user)

    return (
        <div>
          <h1>{character.name}</h1>
        </div>
      )

}

export default CharacterItem ;