var b=document.getElementById("btn1");
b.onclick=function(){
    var input=document.getElementById("inp");
    var text=input.value;
    var ul=document.getElementById("list");
    var li=document.createElement("li");
    var s=document.createElement("label");
    if (!text.replace(/\s/g, '').length) {
        alert("Event can't be empty!");
        input.value="";
        return false;
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
            }else{
                a.style.setProperty("text-decoration","none");
            }
        }
    };
    var d=document.createElement("div");
    var i=document.createElement("img");
    i.src="/images/bin.png";
    i.style.width="20px";
    d.className="image";
    i.onclick=function (e){
        var a=e.target;
        var aa=a.parentElement.parentElement;
        console.log(aa);
        aa.remove();
    }
    d.appendChild(i);
    li.appendChild(ch);
    li.appendChild(s);
    li.appendChild(d);
    ul.appendChild(li);
    input.value="";
    return false;
};

