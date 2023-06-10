// stores/counter.js
import { defineStore } from 'pinia'

export const LoginStore = defineStore('counter', {
  state: () => ({
    Token:""
  }),

  
  actions: {
    Login(Token){
        this.Token = Token
    },
    LogOut(){
        this.Token=""
    }
    
  },
})