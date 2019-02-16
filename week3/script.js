document.open=time();
setInterval(time,1000);
function time(){
    var h=document.getElementById("h1");
    h.innerHTML=new Date().toLocaleTimeString().slice(0,5);
    var d=document.getElementById("date");
    d.innerHTML=new Date().toDateString();
}


var b=document.getElementById("btn1");
b.onclick=function(){
    var input=document.getElementById("inp");
    var text=input.value;
    var ul=document.getElementById("list");
    var li=document.createElement("li");
    var s=document.createElement("span");
    if (!text.replace(/\s/g, '').length) {
        alert("Event can't be empty!");
        input.value="";
        return false;
    }
    console.log(text.length)
    if(text.length>60){
        var t="";
        for(var i=0;i<text.length;i++){
            t+=text[i];
            if(i%59===0&&i!==0){
                // t+="\n";
                t+="...";
                break;
            }
        }
        
        text=t.replace(/\n/g, '<br>');
    }
    s.innerHTML=text;
    s.localName="l";
    
    var  ch=document.createElement("input");
    
    ch.type="checkbox";
    ch.name="check";
    ch.onchange=function(){
        var l=document.getElementsByName("check");
        for(var i=0;i<l.length;i++){
            var a=l[i].parentElement;
            if(l[i].checked){
                a.style.setProperty("text-decoration","line-through");
                a.style.background="linear-gradient(to right, rgba(15, 187, 86, 0.363),rgba(116, 118, 238, 0.356))";
            }else{
                a.style.setProperty("text-decoration","none");
                a.style.background="linear-gradient(to right,rgba(177, 14, 49, 0.329), rgba(116, 118, 238, 0.356))";
            }
        }
    };
    
    
    var d=document.createElement("div");
    var i=document.createElement("img");
    i.src="/images/delete.png";
    i.style.width="30px";
    d.className="image";
    i.onclick=function (e){
        var a=e.target;
        var aa=a.parentElement.parentElement;
        console.log(aa);
        aa.remove();
        btn1.style.visibility="visible";
        inp.style.visibility="visible";
    }
    btn1.style.setProperty("visibility","hidden");
    var inp=document.getElementById("inp");
    inp.style.setProperty("visibility","hidden");
    d.appendChild(i);
    li.appendChild(ch);
    li.appendChild(d);
    li.appendChild(s);
    
    ul.appendChild(li);
    
    input.value="";
    return false;
};
var i=document.getElementById("imgL");
i.onclick=function(){
    var l= document.getElementById("toDo");
    l.style.visibility="visible";
    i2.style.visibility="visible";
    i.style.visibility="hidden";
    btn1.style.visibility="visible";
    inp.style.visibility="visible";
};
var i2=document.getElementById("imgL2");
i2.onclick=function(){
    var l= document.getElementById("toDo");
    l.style.visibility="hidden";
    i.style.visibility="visible";
    i2.style.visibility="hidden";
    btn1.style.visibility="hidden";
    inp.style.visibility="hidden";
    var ul=document.getElementById("list");
    ul.innerHTML="";
};
     
var backStr=[
"https://images.unsplash.com/photo-1504333638930-c8787321eee0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80",
"https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80",
"https://images.unsplash.com/photo-1473806189829-9641421a59f1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80",
"https://images.unsplash.com/photo-1487715433499-93acdc0bd7c3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1414&q=80",
"https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1504&q=80",
"https://images.unsplash.com/photo-1473408655921-6e1310501bdc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80",
"https://images.unsplash.com/photo-1468276311594-df7cb65d8df6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80"];


var bod=document.getElementById("body");

bod.style.backgroundImage="url("+backStr[Math.floor(Math.random()*backStr.length)]+")";




