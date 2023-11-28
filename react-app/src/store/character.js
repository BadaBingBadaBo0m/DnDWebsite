const SET_CHARACTER = "character/SET_CHARACTER";

const setCharacter = (character) => ({
  type: SET_CHARACTER,
  character
});

export const getCharacterById = (id) => async (dispatch) => {
  const response = await fetch(`/api/characters/${id}`);

  if (response.ok) {
    const data = await response.json();
    return dispatch(setCharacter(data));
  }

  return await response.json();
};

const initialState = {};

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_CHARACTER:
      return { ...state, ...action.character };
    default:
      return state;
  }
}