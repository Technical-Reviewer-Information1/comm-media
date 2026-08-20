(function () {
  'use strict';
  const $ = id => document.getElementById(id);

  /* ===== 共通クイズ ===== */
  function quiz(boxId, noteId, items, tail) {
    let ans = {};
    const box = $(boxId);
    box.innerHTML = items.map((b, i) => {
      const long = b.ch.some(c => c.length > 14);
      return '<div' + (i ? ' style="margin-top:16px;padding-top:14px;border-top:1px solid var(--line)"' : '') + '>' +
        '<p class="qhead" style="margin:0 0 8px">【' + b.k + '】　' + b.q + '</p>' +
        '<div class="choice4' + (long ? ' v' : '') + '" data-i="' + i + '">' + b.ch.map((c, j) =>
          '<button class="btn" data-i="' + i + '" data-c="' + c + '" style="text-align:' + (long ? 'left' : 'center') + '">' +
          '⓪①②③'[j] + '　' + c + '</button>').join('') +
        '</div><div class="note" id="' + boxId + 'fb' + i + '" hidden></div></div>';
    }).join('');
    box.querySelectorAll('button[data-c]').forEach(btn => btn.addEventListener('click', () => {
      const i = +btn.dataset.i, b = items[i], ok = btn.dataset.c === b.a;
      const row = box.querySelector('.choice4[data-i="' + i + '"]');
      row.classList.add('locked');
      [...row.children].forEach(x => { if (x.dataset.c === b.a) x.classList.add('correct'); else if (x === btn) x.classList.add('wrong'); });
      const fb = $(boxId + 'fb' + i);
      fb.hidden = false; fb.className = 'note ' + (ok ? 'ok' : 'ng');
      fb.innerHTML = (ok ? '正解。' : '正解は <strong>' + b.a + '</strong>。') + b.why;
      ans[i] = ok;
      const done = Object.keys(ans).length, right = Object.values(ans).filter(Boolean).length;
      const n = $(noteId);
      n.className = 'note ' + (done === items.length ? (right === done ? 'ok' : 'warn') : 'info');
      n.innerHTML = done + ' / ' + items.length + ' 問（正解 ' + right + ' 問）' + (done === items.length ? '<br>' + tail : '');
    }));
    $(noteId).className = 'note info'; $(noteId).textContent = '0 / ' + items.length + ' 問';
  }

  /* ===== STEP 1 ===== */
  const TL = [
    { y: '大昔', t: '口頭・身ぶり', d: '声や身ぶりで直接伝える。<strong>その場にいる人</strong>にしか伝わらず、記録も残らない。' },
    { y: '紀元前', t: '文字・粘土板', d: '文字の発明で、<strong>時間を超えて</strong>情報を残せるようになった。' },
    { y: '15世紀', t: '活版印刷', d: '同じ内容を大量に複製できるようになり、<strong>多くの人に同じ情報</strong>が届くようになった。' },
    { y: '19〜20世紀', t: '電話・ラジオ・テレビ', d: '電気を使って<strong>遠くへ速く</strong>伝えられるように。ラジオ・テレビは1対多の伝達。' },
    { y: '20世紀末〜', t: 'インターネット', d: '<strong>個人が世界に向けて発信</strong>できるようになり、多対多のやりとりが生まれた。' },
    { y: '現在', t: 'SNS・生成AI', d: '情報量が爆発的に増え、<strong>ビッグデータと人工知能</strong>の活用が進む。一方で信憑性の見極めが重要に。' }
  ];
  let tlCur = -1;
  function drawTL() {
    $('tlBox').innerHTML = TL.map((e, i) =>
      '<div class="e' + (i === tlCur ? ' on' : '') + '" data-i="' + i + '"><div class="y">' + e.y + '</div><div class="t">' + e.t + '</div></div>').join('');
    $('tlBox').querySelectorAll('.e').forEach(el => el.addEventListener('click', () => {
      tlCur = +el.dataset.i; drawTL();
      const n = $('tlNote'); n.className = 'note ok';
      n.innerHTML = '<strong>' + TL[tlCur].t + '</strong>　' + TL[tlCur].d;
    }));
  }

  /* ===== STEP 2 ===== */
  const MEDIA = [
    { t: '文字・音声・静止画・動画', a: '表現のメディア', why: '情報を表すための形式です。' },
    { t: '紙・USBメモリ・SDカード・DVD', a: '記録のメディア', why: '情報を保存しておくためのものです。' },
    { t: 'テレビ・ラジオ・インターネット・電話', a: '伝達のメディア', why: '情報を運ぶための手段です。' },
    { t: '新聞・書籍', a: '伝達のメディア', why: '情報を多くの人に届ける手段です（紙そのものは記録のメディア）。' }
  ];
  const MCH = ['表現のメディア', '伝達のメディア', '記録のメディア'];
  let mAns = {};
  function drawMedia() {
    $('mediaTable').innerHTML = '<thead><tr><th>種類</th><th>意味</th><th>例</th></tr></thead><tbody>' +
      '<tr><td><strong>表現のメディア</strong></td><td>情報を表す形式</td><td>文字・音声・静止画・動画</td></tr>' +
      '<tr><td><strong>伝達のメディア</strong></td><td>情報を伝える手段</td><td>テレビ・ラジオ・電話・インターネット・新聞</td></tr>' +
      '<tr><td><strong>記録のメディア</strong></td><td>情報を保存するもの</td><td>紙・USBメモリ・SDカード・DVD</td></tr></tbody>';
    $('mediaBox').innerHTML = MEDIA.map((m, i) =>
      '<div style="border:1px solid var(--line);border-radius:3px;padding:10px 12px;margin-bottom:8px">' +
      '<div style="font-weight:700;margin-bottom:8px">' + m.t + '</div>' +
      '<div class="choice4" data-i="' + i + '">' + MCH.map(c =>
        '<button class="btn" data-i="' + i + '" data-c="' + c + '" style="text-align:center">' + c + '</button>').join('') + '</div>' +
      '<div class="note" id="mdfb' + i + '" hidden style="margin-top:8px"></div></div>').join('');
    $('mediaBox').querySelectorAll('button[data-c]').forEach(b => b.addEventListener('click', () => {
      const i = +b.dataset.i, m = MEDIA[i], ok = b.dataset.c === m.a;
      const row = $('mediaBox').querySelector('.choice4[data-i="' + i + '"]');
      row.classList.add('locked');
      [...row.children].forEach(x => { if (x.dataset.c === m.a) x.classList.add('correct'); else if (x === b) x.classList.add('wrong'); });
      const fb = $('mdfb' + i); fb.hidden = false; fb.className = 'note ' + (ok ? 'ok' : 'ng');
      fb.innerHTML = '<strong>' + m.a + '</strong>　' + m.why;
      mAns[i] = ok;
      const done = Object.keys(mAns).length, right = Object.values(mAns).filter(Boolean).length;
      const n = $('mediaNote');
      n.className = 'note ' + (done === MEDIA.length ? (right === done ? 'ok' : 'warn') : 'info');
      n.innerHTML = done + ' / ' + MEDIA.length + ' 問（正解 ' + right + ' 問）';
    }));
    $('mediaNote').className = 'note info'; $('mediaNote').textContent = '0 / ' + MEDIA.length + ' 問';
  }

  /* ===== STEP 3 マトリックス ===== */
  const COLS = ['1対1', '1対多', '多対多'];
  const ROWS = ['同期（同時にやりとり）', '非同期（時間をずらして）'];
  const ITEMS = [
    { t: '電話', r: 0, c: 0 }, { t: 'テレビ放送', r: 0, c: 1 }, { t: 'ラジオ', r: 0, c: 1 },
    { t: 'ビデオ会議', r: 0, c: 2 }, { t: '手紙', r: 1, c: 0 }, { t: '電子メール', r: 1, c: 0 },
    { t: 'ブログ・Webページ', r: 1, c: 1 }, { t: '電子掲示板・SNS', r: 1, c: 2 }
  ];
  let sel = null, place = {};
  function drawMat() {
    $('poolBox').innerHTML = ITEMS.map((it, i) =>
      '<button class="m' + (place[i] ? ' used' : (sel === i ? ' on' : '')) + '" data-i="' + i + '">' + it.t + '</button>').join('');
    $('poolBox').querySelectorAll('.m').forEach(b => b.addEventListener('click', () => { sel = +b.dataset.i; drawMat(); }));
    let h = '<thead><tr><th></th>' + COLS.map(c => '<th>' + c + '</th>').join('') + '</tr></thead><tbody>';
    ROWS.forEach((r, ri) => {
      h += '<tr><th>' + r + '</th>';
      COLS.forEach((c, ci) => {
        const inCell = Object.keys(place).filter(k => place[k].r === ri && place[k].c === ci);
        h += '<td data-r="' + ri + '" data-c="' + ci + '">' + inCell.map(k =>
          '<span class="chip' + (place[k].ok ? '' : ' ng') + '">' + ITEMS[k].t + (place[k].ok ? '' : ' ×') + '</span>').join('') + '</td>';
      });
      h += '</tr>';
    });
    $('matBox').innerHTML = h + '</tbody>';
    $('matBox').querySelectorAll('td').forEach(td => td.addEventListener('click', () => {
      if (sel === null || place[sel]) return;
      const r = +td.dataset.r, c = +td.dataset.c, it = ITEMS[sel];
      place[sel] = { r: r, c: c, ok: it.r === r && it.c === c };
      const done = Object.keys(place).length, right = Object.values(place).filter(x => x.ok).length;
      sel = null; drawMat();
      const n = $('matNote');
      n.className = 'note ' + (done === ITEMS.length ? (right === done ? 'ok' : 'warn') : 'info');
      n.innerHTML = done + ' / ' + ITEMS.length + ' 個（正解 ' + right + ' 個）' +
        (done === ITEMS.length
          ? '<br>正解は　同期・1対1＝電話／同期・1対多＝テレビ放送・ラジオ／同期・多対多＝ビデオ会議／' +
            '非同期・1対1＝手紙・電子メール／非同期・1対多＝ブログ・Webページ／非同期・多対多＝電子掲示板・SNS。' +
            '<br><strong>同期</strong>は相手と時間を共有する必要があり、<strong>非同期</strong>は都合のよい時間にやりとりできます。'
          : '');
    }));
  }

  /* ===== STEP 4 ===== */
  const MSGS = [
    { box: '<div class="msg"><div class="who">友だちから</div>そんなこと言ってないけど。</div>',
      note: ['warn', '文字だけだと、<strong>怒っているのか、ただ事実を言っているのか</strong>が分かりません。表情や声のトーンといった<strong>非言語情報</strong>が伝わらないためです。'] },
    { box: '<div class="msg"><div class="who">友だちから</div>そんなこと言ってないけど😅</div>',
      note: ['ok', '絵文字が1つ加わるだけで、<strong>「軽く否定しているだけ」</strong>という気持ちが伝わります。絵文字やスタンプは、<strong>足りない非言語情報を補う工夫</strong>です。'] },
    { box: '<div class="msg"><div class="who">直接会って</div>「そんなこと言ってないけど」<br><span class="small" style="color:var(--muted)">（笑いながら、軽い調子で）</span></div>',
      note: ['ok', '対面では、表情・声のトーン・身ぶりなど多くの情報が同時に伝わるので、誤解が起きにくくなります。'] }
  ];
  function drawMsg(i) {
    $('msgBox').innerHTML = MSGS[i].box;
    const n = $('msgNote'); n.className = 'note ' + MSGS[i].note[0]; n.innerHTML = MSGS[i].note[1];
  }

  /* ===== STEP 5 ===== */
  const CHECKS = [
    { t: '発信者がだれか（個人か、公的機関か、企業か）を確かめた', w: '匿名の情報は、責任の所在が分かりません。' },
    { t: '情報の発信日・更新日を確かめた', w: '古い情報が今も正しいとは限りません。' },
    { t: '根拠となるデータや出典が示されているかを確かめた', w: '出典のない数字は確かめようがありません。' },
    { t: '別の信頼できる情報源と照らし合わせた', w: 'いちばん確実な方法です。1つの情報源だけで判断しないこと。' },
    { t: '自分にとって都合のよい情報ばかり集めていないか見直した', w: '見たい情報だけを見てしまう傾向（確証バイアス）に注意します。' }
  ];
  function drawCheck() {
    $('sampleNews').innerHTML = '<strong>例：SNSでこんな投稿を見つけました</strong><br>' +
      '「【拡散希望】○○を食べると成績が上がることが判明！　みんなに教えてあげて」<br>' +
      '<span class="small">フォロワー12万人のアカウント／いいね 8,400件</span>';
    $('checkBox').innerHTML = CHECKS.map((c, i) =>
      '<label><input type="checkbox" data-i="' + i + '"><span>' + c.t + '<br><span class="small" style="color:var(--muted)">' + c.w + '</span></span></label>').join('');
    $('checkBox').querySelectorAll('input').forEach(x => x.addEventListener('change', () => {
      const n = $('checkBox').querySelectorAll('input:checked').length;
      const nt = $('checkNote');
      nt.className = 'note ' + (n === CHECKS.length ? 'ok' : 'info');
      nt.innerHTML = n + ' / ' + CHECKS.length + ' 項目' +
        (n === CHECKS.length
          ? '<br>すべて確かめました。<strong>フォロワー数やいいねの数は、正しさの証明にはなりません。</strong>拡散する前に、まず確かめる習慣をつけましょう。'
          : '<br>フォロワー数が多いから正しい、とは限りません。');
    }));
    $('checkNote').className = 'note info';
    $('checkNote').textContent = '0 / ' + CHECKS.length + ' 項目';
  }

  function init() {
    drawTL(); drawMedia(); drawMat(); drawMsg(0); drawCheck();
    document.querySelectorAll('button[data-v]').forEach(b => b.addEventListener('click', () => drawMsg(+b.dataset.v)));
    $('matReset').addEventListener('click', () => { place = {}; sel = null; drawMat(); $('matNote').className = 'note info'; $('matNote').textContent = '0 / ' + ITEMS.length + ' 個'; });
    $('matNote').className = 'note info'; $('matNote').textContent = '0 / ' + ITEMS.length + ' 個';
    quiz('q1Box', 'q1Note', [
      { k: 'ア', q: 'メディアの変遷について説明したものとして<strong>適当でない</strong>ものは',
        ch: ['メディアの発展により、時間や距離に関係なくより多くの人が情報を受け取れるようになった', '個人による情報発信や動画投稿サイトの普及により情報量が増大し、ビッグデータと人工知能による社会や経済への影響が期待されている', 'メディアは時代とともに発展し、情報伝達の手段は音声から文字、映像、インターネットへと広がってきた', 'メディアは口頭での伝達から発展せず、現代でも情報のほとんどは会話によって伝えられている'],
        a: 'メディアは口頭での伝達から発展せず、現代でも情報のほとんどは会話によって伝えられている',
        why: 'STEP 1 のとおり、メディアは文字・印刷・電波・インターネットへと発展してきました。口頭のまま止まってはいません。' }
    ], '本文の答えは【ア】③ です。');
    quiz('q2Box', 'q2Note', [
      { k: 'イ', q: 'インターネット上のコミュニケーションの特性として最も適当なものは',
        ch: ['匿名性があるため、インターネットでは常に正確な情報のみが共有される', 'テキスト中心のコミュニケーションでは、相手の感情や意図が正確に伝わりにくいため、誤解を避けるためにスタンプや絵文字が使われることがある', 'インターネットでは通信内容が自動的に暗号化されるため、すべての情報が常に安全にやりとりされ、第三者に漏れることはない', 'インターネット上で発信される情報の正確性や信頼性は、その発信者の肩書きやフォロワー数から判断すればよい'],
        a: 'テキスト中心のコミュニケーションでは、相手の感情や意図が正確に伝わりにくいため、誤解を避けるためにスタンプや絵文字が使われることがある',
        why: 'STEP 4 で体験したとおりです。⓪は匿名性はむしろ無責任な情報を生みやすく、②はSSL/TLSで暗号化されても人的ミスによる漏洩はあり、③は肩書きやフォロワー数だけでは判断できません。' }
    ], '本文の答えは【イ】① です。');
    window.Terms.glossary($('glossBox'), ['メディア', 'マスメディア', 'ソーシャルメディア', '非言語情報', '情報の信憑性', 'ファクトチェック', 'ハルシネーション', '情報格差']);
    window.Terms.attach();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
