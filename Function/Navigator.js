function Boot(){
    document.getElementById('Title').innerText = array[0].replace('-',' / ')
    var select = document.getElementById('select')

    for (b=0;b<array.length;b++){
        var option = document.createElement('option')
        option.value = array[b]
        option.innerText = array[b]
        select.add(option, null)
    }
}

function Condition(){
    if (select.value == array[0]){
        var left = document.getElementById('left')
        left.style.backgroundColor = '#4d5257'
        left.setAttribute('onpointerdown','')
        left.style.pointerEvents = 'none'
    } else {
        var left = document.getElementById('left')
        left.style.backgroundColor = '#0D1E32'
        left.setAttribute('onpointerdown',"ripplet(arguments[0], {opacity:'0.25'})")
        left.style.pointerEvents = 'auto'
    }
    if (select.value == array[array.length-1]){
        var right = document.getElementById('right')
        right.style.backgroundColor = '#4d5257'
        right.setAttribute('onpointerdown','')
        right.style.pointerEvents = 'none'
    } else {
        var right = document.getElementById('right')
        right.style.backgroundColor = '#0D1E32'
        right.setAttribute('onpointerdown',"ripplet(arguments[0], {opacity:'0.25'})")
        right.style.pointerEvents = 'auto'
    }
}

function HideAllCalender(){
    for (h=0;h<array.length;h++){
        document.getElementById(array[h]).style.display = 'none'
    }
}

function ChangeTo(){
    var Index = select.selectedIndex
    document.getElementById('Title').innerText = array[Index].replace('-',' - ')
    document.getElementById(select.value).style.display = 'block'
}

function SelectChange(){
    HideAllCalender()
    Condition()
    ChangeTo()
}

function LeftClick(){
    document.getElementById(select.value).style.display = 'none'
    select.selectedIndex = select.selectedIndex - 1
    Condition()
    ChangeTo()
}

function RightClick(){
    document.getElementById(select.value).style.display = 'none'
    select.selectedIndex = select.selectedIndex + 1
    Condition()
    ChangeTo()
}