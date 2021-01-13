const { Exec } = require("./dbs/mysql/exec")

const fetchData = async (author, keyword)=>{

  let sql = 'select * from goods'

  const execIns = new Exec()

  return await execIns.execSelect(sql)
}


let a = fetchData().then(res=>{
  let str = JSON.stringify(res)
  let data= JSON.parse(str)

  console.log(data)
})