'use strict'

const header_section = document.getElementById("header_section")
const  menu_icon = document.getElementById('menu_icon')
const menu_back = document.getElementById('menu_back')

header_section.style.display = "none"
menu_back.style.display = "none"

function menu(){
    menu_icon.style.display = "none"
    header_section.style.display = "flex"
    menu_back.style.display = "block"
}


function menu_back_blur(){
    menu_icon.style.display = "block"
    header_section.style.display = "none"
    menu_back.style.display = "none"
}