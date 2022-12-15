const fs = require('fs')

const dir = fs.opendirSync('.')
let dirent
while ((dirent = dir.readSync()) !== null) {
  console.log(dirent.name)
  arr = dirent.name.split('.')
  if (arr.length === 3){
      newname = arr[1] + '.jpg'
      console.log(newname)
      fs.renameSync(dirent.name, newname)
  }
}
dir.closeSync()