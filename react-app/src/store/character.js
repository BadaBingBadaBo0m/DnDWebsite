const SET_CHARACTER = "character/SET_CHARACTER";

const setCharacter = (character) => ({
  type: SET_CHARACTER,
  payload: character,
});

const initialState = { character: null };

export default function reducer(state = initialState, action) {
  switch (action.type) {
    default:
      return state;
  }
}