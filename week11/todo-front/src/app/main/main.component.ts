import { Component, OnInit, OnDestroy } from '@angular/core';
import {MyServiceService} from './services/my-service.service';
import {ITask,ITaskList} from './models/todo';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public taskLists:ITaskList[]=[];
  public curList:ITaskList;
  public tasks: ITask[]=[];
  constructor(private provider: MyServiceService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res=>{
      this.taskLists=res;
    });
  }
  getExList(list: ITaskList) {
    this.provider.getExactList(list.id).then(res => {
      this.curList=res;
      console.log(this.curList);
    });
  }
  getTasks(l:ITaskList){
    this.provider.getTasks(l.id).then(res=>{
      this.tasks=res;
    });
  }

  

}
