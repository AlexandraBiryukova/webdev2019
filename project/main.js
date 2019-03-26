var mainList=document.getElementById("first");
var buttons=mainList.getElementsByTagName("button");
for(var i=0;i<buttons.length;i++){
    buttons[i].onclick=function(){
        var other=document.getElementsByClassName("list");
        for(var i=0;i<other.length;i++){
            other[i].style.setProperty("visibility","hidden");
        }
        other=document.getElementsByClassName("content");
        for(var i=0;i<other.length;i++){
            other[i].style.setProperty("visibility","hidden");
        }
        var l=this.getAttribute("id")+"L";
        var elem=document.getElementById(l);
        console.log(elem);
        elem.style.setProperty("visibility","visible");
    };
   
}

var lists=document.getElementsByClassName("list");

for(var i=0;i<lists.length;i++){
    var contents=lists[i].getElementsByTagName("button");
    for(var j=0;j<contents.length;j++){
        contents[j].onclick=function(){
            var other=document.getElementsByClassName("content");
        for(var i=0;i<other.length;i++){
            other[i].style.setProperty("visibility","hidden");
        }
        console.log(this.getAttribute("id")+"C");
            var cont=document.getElementById(this.getAttribute("id")+"C");
            console.log(cont);
            cont.style.visibility="visible";
        };  
        
}
}