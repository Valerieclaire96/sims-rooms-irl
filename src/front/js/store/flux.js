const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      token: sessionStorage.getItem('token'),
      objectArr: [],
      roomArr: [],
      cf_url:
        "https://3000-valerieclai-simsroomsir-e3rn5q37h3v.ws-us92.gitpod.io",
      cb_url: process.env.BACKEND_URL,
      user: null,
      favorites: [],
      user_name: null
    },
    actions: {
      // Use getActions to call a function within a fuction
      syncTokenFromSessionStore: () => {
        const token = sessionStorage.getItem("token");
        if (token && token != "" && token != undefined)
          setStore({ token: token });
      },


      
      addFavorite: (item) => {
        const cb_url = getStore().cb_url
        let f = getStore().favorites;
        let t = getStore().token;
        if (sessionStorage.getItem("token")) {
          const opts = {
            headers: {
              Authorization: "Bearer " + t,
			        'Content-Type': 'application/json'
            },
            method: "POST",
            body: JSON.stringify({sims_card: item}),
          };
          fetch(cb_url + "/api/favorites", opts)
            .then((response) => response.json())
            .then((data) => {
              if(data.msg == "ok") {
                f.push(item);
                setStore({ favorites: f });
              }
            })
            .catch((error) => {console.log(error);});
        }
      },
      removeFavorite: (item) => {
        const cb_url = getStore().cb_url
        let f = getStore().favorites;
        let t = getStore().token;
        if (sessionStorage.getItem("token")) {
          const opts = {
            headers: {
              Authorization: "Bearer " + t,
			        'Content-Type': 'application/json'
            },
            method: "DELETE",
            body: JSON.stringify({sims_card: item}),
          };
          fetch(cb_url + "/api/deletefav", opts)
            .then((response) => response.json())
            .then((data) => {
              if(data.msg == "ok") {
                f.forEach((el, i) => {
                  if (el.id === item.id && el.sims_card === item.sims_card) {
                    f.splice(i, 1);
                  }
                });
                setStore({ favorites: f });
              }
            })
            .catch((error) => {console.log(error);});
        }
      },

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
      logout: () => {
        const cf_url = getStore().cf_url
        const token = sessionStorage.removeItem("token");
        setStore({ token: null });
        window.location.href = cf_url + "/";
      },

      login: async (email, password) => {
        console.log(email, password);
        const opts = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email,
            password: password,
          }),
        };
          const res = await fetch(process.env.BACKEND_URL + "/api/login", opts);
          if (res.status < 200 || res.status >= 300) {
            throw new Error("There was an error signing in");
          }
          const data = await res.json();
          
          sessionStorage.setItem("token", data.access_token);
          // data.favorites.forEach(f => {
          //   //was returning an error bc it didnt like the single quotes so the line below turns the single into double quotes 
          //   f.item = f.item.replace(/'/g, '"')
          //   f.item = JSON.parse(f.item)
          // })
           console.log("USER INFO HERE",data)
          setStore({ token: data.access_token, favorites: data.user.favorites, user: data.id, user_name: data.user.name});
          return true;
      },
      
      changePassword: async (token, password) => {
        console.log(token, password);
        const opts = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
          },
          body: JSON.stringify({
            password: password,
          }),
        };
          const res = await fetch(process.env.BACKEND_URL + "/api/recover-password", opts);
          if (res.status < 200 || res.status >= 300) {
            throw new Error("There was an error changing password");
          }
          const data = await res.json();
          
           console.log("USER INFO HERE",data)
          return true;
      },

      getUser: async () => {
        const token = sessionStorage.getItem("token");
        const opts = {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            'Authorization': "Bearer " + token,
          },
        };
          const res = await fetch(process.env.BACKEND_URL + "/api/user", opts);
          if (res.status < 200 || res.status >= 300) {
            throw new Error("There was an error signing in");
          }
          const data = await res.json();
          console.log("DATA", data)
          setStore({ user: data, favorites: data.favorites, user_name:data.name});
          return true;
      },

      createUser: async (name, email, password) => {
        const cb_url = getStore().cb_url;
        const cf_url = getStore().cf_url;
        const opts = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: name,
            email: email,
            password: password,
          }),
        };
          const res = await fetch(
            process.env.BACKEND_URL + "/api/signup",
            opts
          );
          if (res.status < 200 || res.status >= 300) {
            throw new Error("There was an error signing up the user");
          }
          const data = await res.json();
          setStore({ user: data });
          // console.log(data);
          return true;
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
