n,k,l,c,d,p,nl,np=map(int,input().split())
t_dr=k*l
t_sl=c*d
dr_t=nl*n
sl_t=n
s_t=np*n

o=[t_dr/dr_t,t_sl/sl_t,p/s_t]
print(min(list(map(int,o))))















