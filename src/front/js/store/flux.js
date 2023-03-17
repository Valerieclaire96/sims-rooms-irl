const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      token: null,
      objectArr: [],
      roomArr: [],
      cf_url: "https://3000-valerieclai-simsroomsir-iz3s95rq8c0.ws-us90.gitpod.io",
      cb_url: process.env.BACKEND_URL,
      userArr: [],
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
      createUser: async (name, email, password) => {
        const cb_url = getStore().cb_url;
        const cf_url = getStore().cf_url;
        const opts = {
          method: "POST",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
          },
          body: JSON.stringify({
            name: name,
            email: email,
            password: password,
          }),
        };
        try {
          const res = await fetch(process.env.BACKEND_URL + "/api/singup", opts);
          if (res.status !== 200) {
            alert("there has been an error");
            return false;
          }
          const data = await res.json();
          setStore({ userArr: data });
          // console.log(data);
          if (data.status == "true") {
            //redirect to login
            window.location.href = cf_url + "/login";
          }

          
          return true;
        } catch (error) {
          console.error(error, "here is the error");
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


