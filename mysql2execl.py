import pymysql  
import xlsxwriter      #excel write  
  
 
#连接数据库  
try:  
    connect=pymysql.connect(host='localhost',port=3306,  
                            user='root',password='',  
                            db='mining_books',  
                            charset='utf8')  
except pymysql.Error as err:  
    print("报错信息：",err)  
  
#获取游标  
cursor=connect.cursor()  
  
def createTable():  
    wb=xlsxwriter.Workbook('TestExcle.xls') #创建一个Excel文件  
    sheet=wb.add_worksheet('Test_sheet')   #创建一个工作表对象  
    bold = wb.add_format({'bold': True})    #定义一个加粗的格式对象  
    sheet.set_column(0,1, 30)   #设置第一列列宽度  
    sheet.set_column(0,2, 30)   #设置第二列列宽度  
   
    L=['章节名称','章节内容']       #将列名称定义  
    for ifs in range(len(L)):  
        sheet.write(1,ifs,L[ifs],bold) #将列名称插入表格  
  
    #查询语句  
    sql='select user,password from admin'  
  
    cursor.execute(sql)  
    numrows=int(cursor.rowcount)  
    for i in range(numrows):  
        g=cursor.fetchone()  
        sheet.write(i+2,0,g[0]) #第一行，第一列，数据  
        sheet.write(i+2,1,g[1]) #第一行，第二列，数据  
    wb.close()    #关闭Excel文件  
  
createTable()  
  
cursor.close()  
connect.close()