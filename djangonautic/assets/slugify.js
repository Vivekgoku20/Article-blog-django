const titleinput=document.querySelector('input[name=title]')
const sluginput=document.querySelector('input[name=slug]')

const slugify = [val] => {
    return val.toString().toLowerCase().trim()
    .replace(/&/g,'-and-')
    .replace(/[\s\W-]+/g,'-')
};
titleInput.addEventListener('keyup',(e)=>{
    slugInput.setAttribute('value',slugify[titleInput.value]);
});