//------------Bibliotecas------------------------------------------
import { Component } from '@angular/core';
import { IonicPage, NavController, Platform, ToastController } from 'ionic-angular';

//==================================================================
//fazer o typescript reconhecer como objeto
declare var google: any;

//=================================================================
// obtendo a posição
var lat;
var long;
var options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
   };
  
  function success(pos) {
     var crd = pos.coords;
      lat = crd.latitude;
      long = crd.longitude
   };
  
   function error(err) {
     alert('ERROR(' + err.code + '): ' + err.message);
   };
  
   navigator.geolocation.getCurrentPosition(success, error, options);
  //===================================================================

// chamando a pagina======================================


 @IonicPage()
@Component({
  selector: 'page-rota',
  templateUrl: 'encontre-sua-rota.html',
})
//=============== clase do mapa============================================
export class Encotre_sua_rotaPage {
  //métodos 
  directionsService = new google.maps.DirectionsService();
  directionsDisplay = new google.maps.DirectionsRenderer();
  map: any;
  startPosition: any;
  originPosition: string;
  destinationPosition: string;
  //========================================================================
  constructor() { }

//===========================================================================
  // rodando o mapa
  ionViewDidLoad() {
    this.iniciarmapa();
  }
  
  //=========================================================================
  // contruindo o mapa
  iniciarmapa() {
        
    this.startPosition = new google.maps.LatLng( long, lat );
    
    const mapOptions = {
      zoom: 18,
      center: this.startPosition,
      disableDefaultUI: true
    }
    
    this.map = new google.maps.Map(document.getElementById('map'), mapOptions);
    this.directionsDisplay.setMap(this.map);
    
    const marker = new google.maps.Marker({
      position: this.startPosition,
      map: this.map,
    });
  }
  
  


//===========================================================================
// vamos traçar uma rota



}