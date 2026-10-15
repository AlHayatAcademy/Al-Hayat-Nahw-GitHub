/* Apply the saved/system appearance before the first stylesheet is painted. */
(()=>{let theme='light';try{const saved=localStorage.getItem('al-hayat-nahw-theme');theme=saved==='dark'||saved==='light'?saved:window.matchMedia?.('(prefers-color-scheme: dark)').matches?'dark':'light'}catch{}document.documentElement.setAttribute('data-theme',theme)})();
