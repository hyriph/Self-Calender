// Write All of Your Data JavaScript File's Name.
let array = ['2021-01','2021-02']

// Don't Touch Here.
// This Code Will Automatically Imports Written JavaScript Files In Html.
for (item = 0; item < array.length; item++){
    let body = document.getElementById('body')
    let script = document.createElement('script')
    script.setAttribute('src','./CustomData/'+array[item]+'.js')
    body.appendChild(script)
}
Boot()
