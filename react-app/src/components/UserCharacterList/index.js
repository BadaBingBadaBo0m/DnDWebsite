import React from 'react';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import CharacterItem from './CharacterItem';
import { useSelector } from 'react-redux';

const UserCharacterList = () => {
    const sessionUser = useSelector(state => state.session.user);
    return (
        <div>
            {sessionUser ? (
                <div>
                    <ul className='character-list'>
                        {Object?.values(sessionUser.characters)?.sort((a, b) => new Date(b?.createdAt) - new Date(a?.createdAt))?.map(character =>
                        (
                            <li key={character?.id} className="character-item">
                                <CharacterItem character={character} />
                            </li>
                        )
                        )
                        }
                    </ul>
                </div>
            ) : (
                <h1>Hello</h1>
            )}
        </div>
    )
}

export default UserCharacterList;