const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      objectArr: [],
	  roomArr: [],
    },
    actions: {
      // Use getActions to call a function within a fuction

      getRooms: async () => {
        try {
          // fetching data from the backend
          const res = await fetch(process.env.BACKEND_URL + "/api/rooms");
          const data = await res.json();
          setStore({ roomArr: data });
		  console.log("//printing getRooms", data);
          // don't forget to return something, that is how the async resolves
          return data;
        } catch (error) {
          console.log("Error loading message from backend", error);
        }
      },

      getObjects: async () => {
        try {
          const res = await fetch(process.env.BACKEND_URL + "/api/objects");
          const data = await res.json();
          setStore({ objectArr: data });
		  return data;
        } catch (error) {
          console.error(error);
        }
      },
    },
  };
};
export default getState;