import { Component, OnInit, OnDestroy } from '@angular/core';
import {MyServiceService} from './services/my-service.service';
import {ITask,ITaskList} from './models/todo';
import { loadInternal } from '@angular/core/src/render3/util';
import { checkAndUpdateBinding } from '@angular/core/src/view/util';



@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public taskLists:ITaskList[]=[];
  public curList:ITaskList;
  public tasks: ITask[]=[];
  public loading=true;
  public creating=false;
  public updated_name='';
  public name='';
  constructor(private provider: MyServiceService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res=>{
      this.taskLists=res;
    });
  }
  createOrNot(){
    this.creating=true;
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
      if (res.length>0){
        this.loading=true;
      }else{
        this.loading=false;
      }

    });
  }
  createList(){
    if(this.name!==''){
      this.provider.createList(this.name).then(res=>{
        this.name='';
        this.taskLists.push(res);
      });
    }
  }
  deleteList(li:ITaskList){
    this.provider.deleteList(li.id).then(res=>{
      console.log(li.name+"deleted");
      this.provider.getTaskLists().then(r=>{
        this.taskLists=r;
      });
    });
  }

  canUp(c:ITaskList){
    var l=document.getElementById(c.id+"");
    var i=document.getElementById(c.name).getElementsByTagName("img")[1];
   
    if(l.style.getPropertyValue("visibility")!="visible"){
      l.style.setProperty("visibility","visible");
      i.setAttribute("src","../../assets/update2.png");
    }else{
      l.style.setProperty("visibility","hidden");
      i.setAttribute("src","../../assets/update.png");

    }
    console.log(l);
  }
    
  updateList(c: ITaskList) {
      this.canUp(c);
      if(this.updated_name!=''){
        c.name=this.updated_name;
        this.updated_name='';
        this.provider.updateList(c).then(res => {
        console.log(c.name);
      });
      
    }
    }
    mouseOn(){
      var el=document.getElementById("yes");
        el.setAttribute("src","../../assets/add2.png");
        
      
    }
    mouseOff(){
      var el=document.getElementById("yes");
        el.setAttribute("src", "../../assets/add.png");
      
    }

  }

  


