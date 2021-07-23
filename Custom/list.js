// Write All of Your Data JavaScript File's Name.
let array = ['2021-01','2021-02','2021-03','2021-04','2021-05','2021-06']

// Don't Touch Here.
// This Code Will Automatically Imports Written JavaScript Files In Html.
for (item = 0; item < array.length; item++){
    let body = document.getElementById('body')
    let script = document.createElement('script')
    script.setAttribute('src','./CustomData/'+array[item]+'.js')
    body.appendChild(script)
}
Boot()

document.getElementById('Calender').setAttribute('onpointerdown', 'ripplet(arguments[0], {opacity:\'0.3\', spreadingDuration:\'2s\', clearingDuration:\'0.5s\', clearingDelay:\'0s\'})')
