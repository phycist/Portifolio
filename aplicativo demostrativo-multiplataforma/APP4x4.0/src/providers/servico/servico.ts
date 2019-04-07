//#################Biblioteca###################
import { Injectable } from '@angular/core';
import { Http, Headers, Response } from '@angular/http';
import 'rxjs/add/operator/map'; 
//#######################################


@Injectable()
export class ServicoProvider {

 //api local
 api: string = 'http://localhost/api/';

 //api hospedada
//  api: string = 'http://appmysql-cc.umbler.net/';

 
 
 
  constructor(public http: Http) {



  }

  listarDados(){
    return this.http.get(this.api + 'listar.php').map(res=>res.json())
  }






  
}
