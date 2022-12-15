const fs = require('fs')

const dir = fs.opendirSync('.')
let dirent
let counter = 1
while ((dirent = dir.readSync()) !== null) {
  console.log(dirent.name)
  arr = dirent.name.split('.')
  if (arr.length === 4){
      if (counter < 10){
        newname = '0' + counter.toString() + '.jpg'
      } else {
        newname = counter.toString() + '.jpg'
      }
      console.log(newname)
      fs.renameSync(dirent.name, newname)
      counter++
  }
}
dir.closeSync()