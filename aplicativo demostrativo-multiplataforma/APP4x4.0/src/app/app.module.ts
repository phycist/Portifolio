//#################Bibliotecas de funcionamento#########################
import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule } from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { MyApp } from './app.component';
//#########################################################################

// As paginas adicionadas
import { HomePage } from '../pages/home/home';
import { SobrePage } from '../pages/sobre/sobre';
import { QuemSomosPage } from '../pages/quem-somos/quem-somos';
import { NoticiasPage } from '../pages/noticias/noticias';
import { ContacteNosPage  } from '../pages/contacte-nos/contacte-nos';
import { Encotre_sua_rotaPage } from '../pages/encontre-sua-rota/encontre-sua-rota';
//#######################################################################3#########
//exeriencia
import { EncontreSeuGuiaPage } from '../pages/encontre-seu-guia/encontre-seu-guia';
import { Exemplo4Page } from '../pages/exemplo4/exemplo4';
import { ServicoProvider } from '../providers/servico/servico';
import { HttpModule } from '@angular/http';

//#############################################################


@NgModule({
  declarations: [
   // Para adicionar as paginas alteramos aqui
    MyApp,
    HomePage,
    QuemSomosPage,
    NoticiasPage,
    Encotre_sua_rotaPage,
    EncontreSeuGuiaPage,
    ContacteNosPage,
    SobrePage,
    Exemplo4Page

  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    HttpModule    
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    // Para adicionar as paginas alteramos aqui
    MyApp,
    HomePage,
   QuemSomosPage,
   NoticiasPage,
   Encotre_sua_rotaPage,
   EncontreSeuGuiaPage,
   ContacteNosPage,
    SobrePage,
    Exemplo4Page
    
  ],
  providers: [
    StatusBar,
    SplashScreen,
 
   {provide: ErrorHandler, useClass: IonicErrorHandler},
    ServicoProvider,
      
 
  ]
})
export class AppModule {}
