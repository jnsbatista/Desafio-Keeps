import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { EnrollmentsComponent } from './enrollments/enrollments.component';
import { StudentsComponent } from './students/students.component';
import { CoursesComponent } from './courses/courses.component';
import { CourseListingComponent } from './courses/course-listing/course-listing.component';
import { CourseRegistrationComponent } from './courses/course-registration/course-registration.component';

const routes: Routes = [

  { path: 'enrollments', 
    component: EnrollmentsComponent},
  { path: 'students', 
    component: StudentsComponent},
  { path: 'courses', 
    component: CoursesComponent
  },
  { path: 'course/new',
  component: CourseRegistrationComponent
  },
  { path: 'course/list',
  component: CourseListingComponent
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [
  StudentsComponent, 
  EnrollmentsComponent, 
  CoursesComponent,
  CourseRegistrationComponent,
  CourseListingComponent
]