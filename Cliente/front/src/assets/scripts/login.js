export default{
    
    setUserLogged(userLogged) {
        Cookies.set("userLogged", userLogged);
      },
      getUserLogged() {
        return Cookies.get("userLogged");
      },
}