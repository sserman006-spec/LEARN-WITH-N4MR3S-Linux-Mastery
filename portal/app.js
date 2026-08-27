const KEY="learn_with_n4mr3s_linux_v1";
const C=window.CHALLENGES||[];
const fresh=()=>({name:"",completed:[],attempts:0,correct:0,points:0,xp:0,streak:0,bestStreak:0});
let s=load();
function load(){try{return {...fresh(),...JSON.parse(localStorage.getItem(KEY))}}catch(e){return fresh()}}
function save(){localStorage.setItem(KEY,JSON.stringify(s));render()}
function esc(x){return String(x).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[c]))}
async function hash(v){let b=await crypto.subtle.digest("SHA-256",new TextEncoder().encode(v.trim()));return [...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,"0")).join("")}
function current(){return s.completed.length+1}
function render(){
 document.getElementById("name").value=s.name||"";
 let a=s.attempts?Math.round(s.correct/s.attempts*100):100;
 document.getElementById("stats").innerHTML=`<div class="statgrid">
 <div class="stat">Completed<b>${s.completed.length}/50</b></div><div class="stat">Points<b>${s.points}</b></div>
 <div class="stat">XP<b>${s.xp}</b></div><div class="stat">Accuracy<b>${a}%</b></div>
 <div class="stat">Streak<b>🔥 ${s.streak}</b></div><div class="stat">Best<b>${s.bestStreak}</b></div></div>`;
 document.getElementById("bar").style.width=(s.completed.length/50*100)+"%";
 document.getElementById("levels").innerHTML=C.map(c=>{let d=s.completed.includes(c.id),u=c.id===current();return `<div class="row ${d?"done":""} ${u?"current":""} ${!d&&!u?"locked":""}"><span>${d?"✅":u?"▶️":"🔒"}</span><button ${!d&&!u?"disabled":""} onclick="openLevel(${c.id})">${c.id}. ${esc(c.name)}</button></div>`}).join("");
}
function openLevel(id){
 if(id!==current()&&!s.completed.includes(id))return;
 const c=C[id-1], done=s.completed.includes(id);
 document.getElementById("main").innerHTML=`<div class="hero"><div><div class="level">LEVEL ${c.id}/50 · ${esc(c.category)}</div><h1>${esc(c.name)}</h1><div class="meta">Difficulty: ${"⭐".repeat(c.difficulty)}</div></div></div>
 <div class="section"><h2>📖 What you'll learn</h2><p>${esc(c.description)}</p><p>${esc(c.whatYouLearn)}</p></div>
 <div class="section"><h2>🎯 Objective</h2><div class="objective">${esc(c.objective)}</div></div>
 <div class="section"><h2>🧩 Tasks</h2>${c.tasks.map((x,i)=>`<div class="task"><b>Task ${i+1}:</b> ${esc(x)}</div>`).join("")}</div>
 <div class="section"><h2>💡 Hint</h2><div class="hint">${esc(c.hint)}</div></div>
 <div class="section"><h2>🚩 Submit Flag</h2><div class="submit"><input id="flag" placeholder="CTF{...}"><button onclick="submit(${c.id})">Submit</button></div><p id="result"></p></div>
 ${done?'<p class="success">✅ Completed.</p>':""}`;
}
async function submit(id){
 if(id!==current())return;
 let v=document.getElementById("flag").value.trim(),r=document.getElementById("result");
 if(!v){r.className="error";r.textContent="Enter the flag you found.";return}
 s.attempts++;
 if(await hash(v)==C[id-1].flagHash){
   s.correct++;s.completed.push(id);s.streak++;s.bestStreak=Math.max(s.bestStreak,s.streak);
   s.points+=100+s.streak*10;s.xp+=50+s.streak*5;save();
   r.className="success";r.textContent=`✅ Correct! Level ${id} completed.`;
   setTimeout(()=>id<50&&openLevel(id+1),500);
 }else{s.streak=0;r.className="error";r.textContent="❌ Incorrect flag. Keep investigating.";save()}
}
document.getElementById("saveName").onclick=()=>{s.name=document.getElementById("name").value.trim()||"Player";save()};
document.getElementById("export").onclick=()=>{let b=new Blob([JSON.stringify(s,null,2)],{type:"application/json"}),a=document.createElement("a");a.href=URL.createObjectURL(b);a.download=(s.name||"player")+"_progress.json";a.click();URL.revokeObjectURL(a.href)};
document.getElementById("import").onchange=async e=>{try{let x=JSON.parse(await e.target.files[0].text());if(!Array.isArray(x.completed)||x.completed.some(n=>n<1||n>50))throw 0;s={...fresh(),...x};save();alert("Progress imported.")}catch(_){alert("Invalid progress file.")}};
document.getElementById("reset").onclick=()=>{if(confirm("Reset local progress?")){s=fresh();localStorage.removeItem(KEY);location.reload()}};
render();openLevel(current());
