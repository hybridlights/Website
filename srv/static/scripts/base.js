


document.body.addEventListener('scroll', () => {
    // Needed to add the scrolling behavior to the body because of some css in 
    // the html and body tags that prevent a empty space outside the page when scrolling fast
    // thats also why i use "document.documentElement.scrollTop || document.body.scrollTop"
    // instead of window.scrollY
    const header = document.querySelector('header');
    if ((document.documentElement.scrollTop || document.body.scrollTop ) > 50) {
        header.style.height = '10vh'
    } else {
        header.style.height = '20vh'
    }
})