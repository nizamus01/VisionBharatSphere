import {useEffect, useState} from 'react'

const plates = [
  // embed the same 24 plates array (urls + correct)
  {src:"https://i.ibb.co/gZBVZbt3/Screenshot-2025-09-27-195645.png",correct:"12"},
  {src:"https://i.ibb.co/gb6VbLFP/Screenshot-2025-09-27-222858.png",correct:"8"},
  {src:"https://i.ibb.co/hFL0Y2h8/Screenshot-2025-09-28-012612.png",correct:"29"},
  {src:"https://i.ibb.co/9mw8gVYc/Screenshot-2025-09-28-014304.png",correct:"5"},
  {src:"https://i.ibb.co/JRZcfNPM/Screenshot-2025-09-28-021814.png",correct:"3"},
  {src:"https://i.ibb.co/VYdYt5rB/Screenshot-2025-09-28-022034.png",correct:"15"},
  {src:"https://i.ibb.co/xKm8JCRb/Screenshot-2025-09-28-022316.png",correct:"74"},
  {src:"https://i.ibb.co/7JtxZPB0/Screenshot-2025-09-28-022511.png",correct:"6"},
  {src:"https://i.ibb.co/PzZWRkY4/Screenshot-2025-09-28-022721.png",correct:"45"},
  {src:"https://i.ibb.co/nFhgKt8/Screenshot-2025-09-28-022858.png",correct:"5"},
  {src:"https://i.ibb.co/1G93PJN5/Screenshot-2025-09-28-023156.png",correct:"7"},
  {src:"https://i.ibb.co/dsc4PJFX/Screenshot-2025-09-28-024011.png",correct:"16"},
  {src:"https://i.ibb.co/G3987H2c/Screenshot-2025-09-28-024327.png",correct:"73"},
  {src:"https://i.ibb.co/TMXxssHB/Screenshot-2025-09-28-024710.png",correct:""},
  {src:"https://i.ibb.co/pBs69vtJ/Screenshot-2025-09-28-024947.png",correct:""},
  {src:"https://i.ibb.co/mC2GDVKh/Screenshot-2025-09-28-025208.png",correct:"26"},
  {src:"https://i.ibb.co/TqR54D9j/Screenshot-2025-09-28-025403.png",correct:"42"},
  {src:"https://i.ibb.co/LDPsy1WX/Screenshot-2025-09-28-025555.png",correct:""},
  {src:"https://i.ibb.co/XfJKbgw8/Screenshot-2025-09-28-025745.png",correct:""},
  {src:"https://i.ibb.co/4nRHvfdH/Screenshot-2025-09-28-025937.png",correct:""},
  {src:"https://i.ibb.co/QjC2zPgr/Screenshot-2025-09-28-030118.png",correct:""},
  {src:"https://i.ibb.co/Pvgck9CX/Screenshot-2025-09-28-030243.png",correct:""},
  {src:"https://i.ibb.co/HT4prLpy/Screenshot-2025-09-28-030450.png",correct:""},
  {src:"https://i.ibb.co/fGDtSp9x/Screenshot-2025-09-28-030605.png",correct:""}
]

export default function IshiharaPage(){
  const [idx,setIdx] = useState(0)
  const [answers,setAnswers] = useState(Array(24).fill(null))
  const [loaded,setLoaded] = useState(0)

  useEffect(()=>{
    plates.forEach(p=>{ const img=new Image(); img.src=p.src; img.onload=()=>setLoaded(l=>l+1); img.onerror=()=>setLoaded(l=>l+1); })
  },[])

  function selectOption(val){
    const a = answers.slice(); a[idx]=val; setAnswers(a);
  }

  function next(){ if(idx<23) setIdx(i=>i+1); }
  function prev(){ if(idx>0) setIdx(i=>i-1); }

  function finish(){
    let correct=0; for(let i=0;i<24;i++){ const ca = plates[i].correct === '' ? 'Nothing' : plates[i].correct; if(answers[i]===ca) correct++; }
    const percent = Math.round((correct/24)*100);
    alert(`Score ${correct}/24 — ${percent}%`);
  }

  const options = (()=>{
    const p = plates[idx]; let opts = p.correct && p.correct!=='' ? [p.correct] : [];
    const distractors = ['1','2','3','4','5','6','7','8','9','12','13','15','16','17','26','29','42','45','70','71','73','74','78'];
    let i=0; while(opts.length<3 && i<distractors.length){ if(!opts.includes(distractors[i])) opts.push(distractors[i]); i++; }
    opts.push('Nothing'); for(let s=opts.length-1;s>0;s--){ const j=Math.floor(Math.random()*(s+1)); [opts[s],opts[j]]=[opts[j],opts[s]] }
    return opts.slice(0,4);
  })()

  return (
    <div style={{padding:20,fontFamily:'Inter,system-ui'}}>
      <h1>Ishihara Test</h1>
      <div>Loaded {loaded}/24</div>
      <div style={{display:'flex',gap:20,marginTop:20}}>
        <div style={{width:440}}>
          <div style={{width:420,height:420,borderRadius:999,overflow:'hidden',background:'#fff',display:'flex',alignItems:'center',justifyContent:'center'}}>
            <img src={plates[idx].src} alt={`Plate ${idx+1}`} style={{width:'100%',height:'100%',objectFit:'contain'}}/>
          </div>
          <div style={{display:'flex',gap:10,marginTop:10}}>
            {options.map((o,i)=> (
              <button key={i} onClick={()=>selectOption(o)} style={{padding:10,flex:1,background:answers[idx]===o? '#10b981':'#fff'}}>{o}</button>
            ))}
          </div>
          <div style={{display:'flex',gap:8,marginTop:12}}>
            <button onClick={prev}>◀ Prev</button>
            <button onClick={next}>Next ▶</button>
            <button onClick={finish}>Finish</button>
          </div>
        </div>
        <div style={{flex:1}}>
          <h3>Answers</h3>
          <div style={{background:'#fff',padding:12,borderRadius:8}}>
            {answers.map((a,i)=> <div key={i} style={{padding:6,borderBottom:'1px solid #eef'}}>{`Plate ${i+1}: ${a|| '—'}`}</div>)}
          </div>
        </div>
      </div>
    </div>
  )
}
