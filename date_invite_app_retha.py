import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="A Quick Question", page_icon="💚", layout="centered")

st.markdown("""
<style>
.stApp {
  background: linear-gradient(135deg, #8B0000 0%, #C1121F 52%, #E63946 100%);
}
.block-container {max-width: 850px; padding-top: 2rem;}
.hero {
  background: rgba(255,255,255,.88);
  border: 1px solid #eadff0;
  border-radius: 24px;
  padding: 28px;
  box-shadow: 0 18px 50px rgba(65,35,75,.10);
  text-align:center;
  margin-bottom:18px;
}
.hero h1 {font-size:2.15rem; margin-bottom:8px; color:#2c2430;}
.hero p {color:#6c5b70; font-size:1.05rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>Hi Retha ❤️</h1>
  <p>I made you something small...</p>
</div>
""", unsafe_allow_html=True)

components.html(r'''
<!doctype html>
<html>
<head>
<style>
*{box-sizing:border-box;font-family:Arial,sans-serif}
body{margin:0;background:transparent;color:#2c2430}
.card{background:white;border:1px solid #eadff0;border-radius:24px;padding:34px 24px;text-align:center;min-height:410px;box-shadow:0 14px 35px rgba(65,35,75,.08)}
h2{font-size:30px;margin:8px 0}.sub{color:#756878;margin:8px 0 28px}
.stage{position:relative;height:150px;max-width:560px;margin:0 auto}
button{border:0;border-radius:999px;padding:14px 30px;font-size:18px;font-weight:700;cursor:pointer;box-shadow:0 8px 18px rgba(0,0,0,.10)}
#yes{background:#2ab673;color:white;position:absolute;left:22%;top:45px;transform:translateX(-50%)}
#no{background:#2c2430;color:white;position:absolute;left:70%;top:45px;transform:translateX(-50%);transition:left .13s ease,top .13s ease}
#message{min-height:28px;color:#8a5f78;font-weight:700;margin-top:4px}
#result{display:none;padding-top:24px}.choices{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:20px}.choice{background:#f3e9f3;color:#3d3040;border:1px solid #dfcfe1;box-shadow:none;font-size:15px}.decline{display:none;margin-top:12px;color:#6f626f;font-size:14px}.decline button{font-size:13px;padding:8px 14px;background:#eee7ef;color:#544b56;box-shadow:none}
</style>
</head>
<body>
<div class="card">
  <div id="question">
    <div style="font-size:38px">🌷</div>
    <h2>Hi Retha, would you like to go out with me?</h2>
    <div class="sub">Nothing complicated. Just the two of us having a good time.</div>
    <div class="stage" id="stage">
      <button id="yes">YES 😊</button>
      <button id="no">NO 🙈</button>
    </div>
    <div id="message"></div>
    <div class="decline" id="decline">Okay okay 😂 genuine option: <button id="realNo">No, thank you</button></div>
  </div>
  <div id="result">
    <div style="font-size:48px">🎉</div>
    <h2>Okay, it's a date 😅</h2>
    <div class="sub">Pick the vibe:</div>
    <div class="choices">
      <button class="choice">☕ Coffee</button>
      <button class="choice">🍽️ Dinner</button>
      <button class="choice">🎳 Activity</button>
      <button class="choice">🎁 Surprise me</button>
    </div>
    <p id="picked" style="margin-top:24px;font-weight:700;color:#2ab673"></p>
  </div>
</div>
<script>
const noBtn=document.getElementById('no');
const yesBtn=document.getElementById('yes');
const stage=document.getElementById('stage');
const msg=document.getElementById('message');
const decline=document.getElementById('decline');
let dodges=0;
const texts=['Are you sure? 😭','Think about it 😂','One more chance 👀'];
function dodge(){
  if(dodges>=3){ decline.style.display='block'; return; }
  const maxX=Math.max(40,stage.clientWidth-noBtn.offsetWidth-20);
  const maxY=Math.max(25,stage.clientHeight-noBtn.offsetHeight-12);
  noBtn.style.left=(20+Math.random()*(maxX-20))+'px';
  noBtn.style.top=(8+Math.random()*(maxY-8))+'px';
  noBtn.style.transform='none';
  msg.textContent=texts[dodges];
  dodges++;
  if(dodges>=3) decline.style.display='block';
}
noBtn.addEventListener('mouseenter',dodge);
noBtn.addEventListener('click',dodge);
yesBtn.addEventListener('click',()=>{document.getElementById('question').style.display='none';document.getElementById('result').style.display='block';});
document.getElementById('realNo').addEventListener('click',()=>{msg.textContent='All good 🤝 Thanks for being honest.';noBtn.style.display='none';yesBtn.style.display='none';decline.style.display='none';});
document.querySelectorAll('.choice').forEach(b=>b.addEventListener('click',()=>{document.getElementById('picked').textContent='Good choice 😌 — '+b.textContent.replace(/^[^ ]+ /,'');}));
</script>
</body>
</html>
''', height=470)

st.caption("Built for one simple question ❤️")
