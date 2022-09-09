
console.log('hello world')

const copyBtns = [...document.getElementsByClassName('copy-btn')]
console.log(copyBtns)

let previous = null

copyBtns.forEach(btn=> btn.addEventListener('click', ()=>{
    console.log('click')
    const color = btn.getAttribute('data-hex')
    console.log(color) 
    navigator.clipboard.writeText(color)
    btn.textContent = 'copied'

    // navigator.clipboard.readText().then(clipText=>{
    //     console.log(clipText)
    //     btn.textContent = `copied ${clipText}`
    // })

    if (previous){
        previous.textContent = 'click'
    }
    previous = btn
}))


function googleTranslateElementInit() { 
    new google.translate.TranslateElement(
        {pageLanguage: 'en'}, 
        'google_translate_element'
    ); 
} 