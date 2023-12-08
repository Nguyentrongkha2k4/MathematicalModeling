from gamspy import Container, Set, Parameter, Variable, Equation, Model, Sum, Sense, Problem
import numpy as np
m=Container()
A=np.random.randint(0,5,size=(8,5)) # Ma trận số lượng nguyên liệu A
print(A)
i_values = [str(v) for v in range(1, 9)]  # Chỉ số sản phẩm
j_values = [str(v) for v in range(1, 6)]  # Chỉ số nguyên liệu
k_values = ["1", "2"]  # Chỉ số sự kiện

# Tạo các tập i, j, k trong mô hình
i = Set(m, "i", records=i_values)
j = Set(m, "j", records=j_values)
k = Set(m, "k", records=k_values)
print(i.records)
print(j.records)
print(k.records)
d=np.random.binomial(10,1/2,size=(2,8)) # Vector nhu cầu sản phẩm
print(d)
p=np.array([0.5, 0.5]) # Vector xác suất sự kiện
print(p)
b=np.random.randint(5,20,size=(5,1)) # Vector giá tiển mua nguyên liệu lúc đầu
print(b)
s=np.random.randint(1,b,size=(5,1)) # Vector giá tiền bán lại nguyên liệu sau khi sản xuất
print(s)
q=np.random.randint(100,200,size=(8,1)) # Vector số tiền bán sản phẩm i
print(q)
l=np.random.randint(50,q-25,size=(8,1)) # Vector số tiền sản xuất sảm phẩm i
print(l)
x=Variable(m,"x",domain=[j],type="integer") # Biến quyết định x: Số lượng nguyên liệu mua trước khi biết nhu cầu
y=Variable(m,"y",domain=[k,j],type="integer") # Biến quyết định y: Số nguyên liệu còn dư sau khi sản xuất
z=Variable(m,"z",domain=[k,i],type="integer") # Biến quyết định z: Số sản phẩm sản xuất
va=Parameter(m,"va",domain=[i,j],records=A) # Tham chiếu giá trị ma trận A
vq=Parameter(m,"vq",domain=[i],records=q)   # Tham chiếu giá trị vector q
vl=Parameter(m,"vl",domain=[i],records=l)   # Tham chiếu giá trị vector l
vb=Parameter(m,"vb",domain=[j],records=b)   # Tham chiếu giá trị vector b
vs=Parameter(m,"vs",domain=[j],records=s)   # Tham chiếu giá trị vector s
vd=Parameter(m,"vd",domain=[k,i],records=d) # Tham chiếu giá trị vector d
vp=Parameter(m,"vp",domain=[k],records=p)   # Tham chiếu giá trị vector p

print("va: ")
print( va.records )
print("--------------------------")
print("vq: ")
print( vq.records )
print("--------------------------")
print("vl: ")
print( vl.records )
print("--------------------------")
print("vb: ")
print( vb.records )
print("--------------------------")
print("vs: " )
print( vs.records )
print("--------------------------")
print("vd: ")
print( vd.records )
print("--------------------------")
print("vp: ")
print( vp.records )
stage1=Equation(m,"stage1",domain=[k,j])
stage2=Equation(m,"stage2",domain=[k,i])
stage1[k,j]=y[k,j]==x[j]-Sum(i,va[i,j]*z[k,i])
stage2[k,i]=z[k,i]<=vd[k,i]
Modelobject=Sum(j,vb[j]*x[j])+Sum(k,vp[k]*(Sum(i,(vl[i]-vq[i])*z[k,i])-Sum(j,vs[j]*y[k,j])))
Assign1=Model( container=m, name="Assign1", equations=[stage1,stage2], problem=Problem.MIP, sense=Sense.MIN, objective=Modelobject)
Assign1.solve()

print("The result of optimization is: {}".format(Assign1.objective_value) )
print("--------------------------")
print("Variable x : ")
print( x.records )
print("--------------------------")
print("Variable y : ")
print( y.records )
print("--------------------------")
print("Variable z : ")
print( z.records )