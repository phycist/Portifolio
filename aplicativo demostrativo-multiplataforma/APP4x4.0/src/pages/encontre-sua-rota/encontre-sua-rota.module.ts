import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { Encotre_sua_rotaPage } from './encontre-sua-rota';

@NgModule({
  declarations: [
    Encotre_sua_rotaPage,
  ],
  imports: [
    IonicPageModule.forChild(Encotre_sua_rotaPage),
  ],
  exports: [
    Encotre_sua_rotaPage
  ]
})
export class Encotre_sua_rota_PageModule {}
