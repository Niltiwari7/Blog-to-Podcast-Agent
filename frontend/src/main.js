import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { vuetify } from './plugin/vuetify'


const app = createApp(App)
            .use(vuetify)
            
app.mount('#app')
