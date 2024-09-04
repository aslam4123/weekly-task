mwr=[['shirt',101,'XL',2000,'Levis',10],['Jeans',102,'L',2500,'Zara',15],['Tshirt',103,'M',1000,'Adidas',20]]
import datetime
while True:
    print('''
           1.product Details
           2.view the product Details
           3.update the product Details
           4.Delete the product Details
           5.Add deatails
           6.Search the product Details
           7.Exit''')
    
    choice=int(input('enter the choice:'))
    if choice==1:
        product=str(input('enter the product:'))
        id=int(input('enter the id:'))
        size=str(input('enter the size:'))
        price=int(input('enter the price:'))
        brand=str(input('enter the brand:'))
        stock=int(input('enter the stock:'))
        mwr.append([product,id,size,price,brand,stock])
    elif choice==2:
        for i in mwr:
            print(i)
    elif choice==3:
        id=int(input('enter the id:'))
        f=0
        for i in mwr:
            if id in i:
                while True:
                    print('''
                          1.Update product
                          2.Update size
                          3.Update price
                          4.Update brand
                          5.Update stock
                          6.exit''')
                    choice=int(input('enter the choice:'))

                    if choice==1:
                        product=str(input('enter the product:'))
                        i[0]=product
                    elif choice==2:
                        size=str(input('enter the size:'))
                        i[2]=size
                    elif choice==3:
                        price=int(input('enter the price:'))
                        i[3]=price
                    elif choice==4:
                        brand=str(input('enter the brand:'))
                        i[4]=brand
                    elif choice==5:
                        stock=int(input('enter the stock:'))
                        i[5]=stock
                    elif choice==6:
                        break
                    else:
                        print('invalid name')
                        f=1
        if f==0:
            print('invalid id')
    elif choice==4:
        id=int(input('enter the id:'))
        f=0
        for i in mwr:
            if id in i:
                mwr.remove(i)
                f=1
        if f==0:
            print('invalid id')
    elif choice==5:
        id=int(input('enter the id:'))
        for i in mwr:
            if id in i:
                task=input('enter the task:')
                date=datetime.datetime.now().strftime('%x')
                i.append([task,date])
                              
    elif choice==6:
        id=int(input('enter the id:'))
        f=0
        for i in mwr:
            if id in i:
                print(i)
                f=1
        if f==0:
            print('invalid id')
    elif choice==7:
        break
    else:
        print('invalid choice')