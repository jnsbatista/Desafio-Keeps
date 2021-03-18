import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CoursesComponent } from './courses/courses.component';
import { EnrollmentsComponent } from './enrollments/enrollments.component';
import { StudentsComponent } from './students/students.component';

const routes: Routes = [
  {
    path: 'students',
    component: StudentsComponent
  },
  {
    path: 'courses',
    component: CoursesComponent
  },
  {
    path: 'enrollments',
    component: EnrollmentsComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [
  StudentsComponent,
  CoursesComponent,
  EnrollmentsComponent,
]
