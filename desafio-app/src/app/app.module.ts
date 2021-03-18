import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LayoutModule } from '@angular/cdk/layout';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule, routingComponents } from './app-routing.module';
import { MainNavModule } from './main-nav/main-nav.module';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    routingComponents
   ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    LayoutModule,
    MainNavModule,

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
