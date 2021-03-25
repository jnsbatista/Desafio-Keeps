import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CoursesComponent } from './courses.component';
import { CourseListingComponent } from './course-listing/course-listing.component';
import { CourseRegistrationComponent } from './course-registration/course-registration.component';

@NgModule({
  imports: [
    CommonModule,
  ],
  declarations: [
    CoursesComponent, 
    CourseListingComponent,
    CourseRegistrationComponent
  ]

})
export class CoursesModule { }