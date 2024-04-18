import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from "@angular/common/http";
import { RouterModule, Routes} from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
// import {CompanyService} from "../data.service";
import { CompanyComponent } from './company/company.component';
import { VacancyComponent } from './vacancy/vacancy.component';


@NgModule({
  declarations: [
    AppComponent,
    CompanyComponent,
    VacancyComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }