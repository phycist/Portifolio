//###############Bibliotecas#####################################3
import { Component } from '@angular/core';
import { IonicPage, NavController,AlertController } from 'ionic-angular';
import { FormBuilder, Validators } from '@angular/forms';
import { ServicoProvider } from '../../providers/servico/servico';

//####################################################################

@IonicPage()
@Component({
  selector: 'page-encontre-seu-guia',
  templateUrl: 'encontre-seu-guia.html',
})
export class EncontreSeuGuiaPage {
  
  guias: any[];//data
  guia: any = [];
  nomes: boolean = true;
//-----------------------------------------------------------------------------------
  constructor(
    public navCtrl: NavController,
    public servicos: ServicoProvider,
    public alertCtrl: AlertController,
    public formBuilder: FormBuilder
  ){
    this.buscarDados();
    this.guia = this.formBuilder.group({
      nome:['', Validators.required],
      celular:['', Validators.required],
      
    });



  }

  buscarDados(){
    //retornar dados do banco mysql
    this.servicos.listarDados()
    .subscribe(
      data => this.guias = data,
      err => console.log(err)
    );
  }

//-----------------------------------------------------------------------------------
     
  


}
