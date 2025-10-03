import Link from 'next/link'
export default function Home(){
  return (
    <div style={{padding:40,fontFamily:'Inter,system-ui',maxWidth:900,margin:'0 auto'}}>
      <h1>VisionBharatSphere — Frontend Demo</h1>
      <p>Quick links</p>
      <ul>
        <li><Link href="/ishihara">Ishihara Color Test</Link></li>
      </ul>
    </div>
  )
}
