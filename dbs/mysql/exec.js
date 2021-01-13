const mysql = require("mysql2")
const { config } = require("./conf")

class Exec{

  constructor(){
    // 静态属性与静态方法(ES6明确规定，Class内部只有静态方法，没有静态属性 )
    this.conn = null;
    this.initConnect();
  }
  // 创建 数据库连接
  initConnect(){

    if(!this.conn){
      this.conn = mysql.createConnection({
        ...config.MYSQL
      })
    }
  }
  // 执行 sql 语句
  execSelect(sqlStr_){

    return new Promise( (resolve, reject)=>{
      // fields 数据库字段
      this.conn.query(sqlStr_, (err, result)=>{
        if(err){
          reject(err)

          this.conn.end()
          return
        }
        //
        resolve(result)

        this.conn.end()
      })
    })
  }
}

module.exports = {
  Exec
}