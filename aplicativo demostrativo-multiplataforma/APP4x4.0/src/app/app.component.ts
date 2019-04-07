//============Bibliotecas==============================
import { Component, ViewChild } from '@angular/core';
import { Nav, Platform } from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';

import { HomePage } from '../pages/home/home';
import { SobrePage } from '../pages/sobre/sobre';
import { QuemSomosPage } from '../pages/quem-somos/quem-somos';
import { NoticiasPage } from '../pages/noticias/noticias';
import { ContacteNosPage  } from '../pages/contacte-nos/contacte-nos';
import { Encotre_sua_rotaPage }  from '../pages/encontre-sua-rota/encontre-sua-rota';
import { EncontreSeuGuiaPage } from '../pages/encontre-seu-guia/encontre-seu-guia'

import { Exemplo4Page } from '../pages/exemplo4/exemplo4';


//=========================================================

@Component({
  templateUrl: 'app.html'
})
//====================Essencial===================================
export class MyApp {
  @ViewChild(Nav) nav: Nav;

  rootPage: any = HomePage;

  pages: Array<{title: string, component: any}>;

  constructor(public platform: Platform, public statusBar: StatusBar, public splashScreen: SplashScreen) {
    this.initializeApp();


    // used for an example of ngFor and navigation
    this.pages = [
      { title: 'Home', component: HomePage },
      { title: 'Quem somos', component: QuemSomosPage },
      { title: 'Notícias sobre 4x4 ', component: NoticiasPage },
      { title: 'Encontre sua rota ', component: Encotre_sua_rotaPage },
      { title: 'Encontre seu guia ', component: EncontreSeuGuiaPage },
      { title: 'Contacte - nos ', component:ContacteNosPage },
      { title: 'Sobre o APP', component: SobrePage  },
      { title: 'exemplo4', component: Exemplo4Page}
            
    ];
  }
//=========================================================================
  initializeApp() {
    this.platform.ready().then(() => {
      // Okay, so the platform is ready and our plugins are available.
      // Here you can do any higher level native things you might need.
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });
  }

  openPage(page) {
    // Reset the content nav to have just this page
    // we wouldn't want the back button to show in this scenario
    this.nav.setRoot(page.component);
  }
}
//==========================================================================
