R=print
P='ExCircle'
O='CircumCircle'
N='ShiftedOrientation'
M='InCircle'
L=float
G=abs
F=round
E=range
B=len
import math as D,numpy as S
from scipy.spatial import Delaunay as T
import random as Q
A=[]
C=[]
def H(X,Y):
	A=X[0]-X[1];B=Y[0]-Y[1]
	if A==0 and B==0:return 1
	return A*A+B*B
def Y(A,B,C):
	E=H(B,C);F=H(A,C);G=H(A,B);J=D.sqrt(E);K=D.sqrt(F);L=D.sqrt(G)
	try:M=D.acos((F+G-E)/(2*K*L));N=D.acos((E+G-F)/(2*J*L));O=D.acos((E+F-G)/(2*J*K))
	except:R('Error point',A,B,C);R('Error',E,F,G)
	return[I(M),I(N),I(O)]
def J(p,c,orientation):A=orientation;B=c[0];C=c[1];E=p[0];G=p[1];H=(B-E)*D.cos(A)+(C-G)*D.sin(A);I=(B-E)*D.sin(A)+(C-G)*D.cos(A);return F(D.sqrt(H**2+I**2),2)
def Z(points):K=points;N=K[0];O=K[1];P=K[2];B=A[N];E=A[O];F=A[P];Q=C[N];R=C[O];S=C[P];T=B[0];U=E[0];V=F[0];W=B[1];X=E[1];Y=F[1];G=D.dist(B,E);H=D.dist(E,F);I=D.dist(F,B);L=(T*H+U*I+V*G)/(G+H+I);M=(W*H+X*I+Y*G)/(G+H+I);Z=J(B,[L,M],Q);a=J(E,[L,M],R);b=J(F,[L,M],S);return[Z,a,b]
def I(rad):return rad*180*7/22
def a(tringle,angels):H=angels;G=tringle;T=G[0];U=G[1];V=G[2];Q=A[T];R=A[U];S=A[V];I,J=Q[0],Q[1];K,L=R[0],R[1];M,N=S[0],S[1];B=H[0];C=H[1];E=H[2];O=(I*D.sin(2*B)+K*D.sin(2*C)+M*D.sin(2*E))/(D.sin(2*B)+D.sin(2*C)+D.sin(2*E));P=(J*D.sin(2*B)+L*D.sin(2*C)+N*D.sin(2*E))/(D.sin(2*B)+D.sin(2*C)+D.sin(2*E));W=D.dist([O,P],[(K+M)/2,(L+N)/2]);X=D.dist([O,P],[(I+M)/2,(J+N)/2]);Y=D.dist([O,P],[(K+I)/2,(L+J)/2]);Z=[F(W,2),F(X,2),F(Y,2)];return Z
def b(tringle,angels):C=angels;B=tringle;Q=B[0];R=B[1];S=B[2];H=A[Q];I=A[R];J=A[S];K,L=H[0],H[1];M,N=I[0],I[1];O,P=J[0],J[1];T=D.dist([M,N],[O,P]);U=D.dist([O,P],[K,L]);V=D.dist([K,L],[M,N]);E=(T+U+V)/2;W=C[0];X=C[1];Y=C[2];Z=G(F(E*D.tan(W/2),2));a=G(F(E*D.tan(X/2),2));b=G(F(E*D.tan(Y/2),2));return[Z,a,b]
def GetUserKey(size):return bin(Q.getrandbits(size))[2:],Q.randint(1,360)
def c(XYArray):return T(XYArray).simplices
def K(Orientation,key):return G(Orientation+key)%360
def d(Max_Length_of_InCentre_to_vertex,Max_Orientation,Max_Length_of_Circum_Centre_to_tringle_side,Max_Radius_Of_Ex_Circle):A=10;B=10;C=10;E=10;F=D.ceil(Max_Length_of_InCentre_to_vertex/A);G=D.ceil(Max_Orientation/B);H=D.ceil(Max_Length_of_Circum_Centre_to_tringle_side/C);I=D.ceil(Max_Radius_Of_Ex_Circle/E);J=S.zeros((A,B,C,E));return A,B,C,E,F,G,H,I,J
def e(matrix,List_dict,Cw,Cx,Cy,Cz):
	C=matrix
	for B in List_dict:
		G=B[M];H=B[N];I=B[O];F=B[P]
		for A in E(3):
			try:
				J=D.floor(G[A]/Cw);K=D.floor(H[A]/Cx);L=D.floor(I[A]/Cy);Q=D.floor(F[A]/Cz)
				if F[A]<10001:C[J][K][L][Q]=1
			except:pass
	return C
def U(T1,T2):
	C=T2;A=T1
	if B(A)>B(C):
		for D in E(B(A)-B(C)):C=C+'0'
	elif B(A)<B(C):
		for D in E(B(C)-B(A)):A=A+'0'
	return A,C
def Match(CT,ST):
	A,F=U(CT,ST);G=ST.count('1');D=0
	for C in E(B(A)):
		if A[C]==F[C]and A[C]=='1':D+=1
	return D/G*100
def f(UserKey,matrix,W,X,Y,Z):
	A=UserKey
	for B in E(W):
		for C in E(X):
			for D in E(Y):
				for F in E(Z):A=A+str(matrix[B][C][D][0]).replace('.','')
	return A
def CreateTemplate(fileName,InputFolder,UserKey,key):
	G=key
	with open(InputFolder+'/'+fileName+'.txt','r')as g:h=g.readlines()
	for i in h:
		H=i.split(' ')
		try:A.append([L(H[0]),L(H[1])]);C.append(L(H[2]))
		except:pass
	A;C;j=c(A);I=[];A6=0
	for D in j:U=D[0];V=D[1];W=D[2];k=A[U];l=A[V];m=A[W];n=C[U];o=C[V];p=C[W];q=K(n,G);r=K(o,G);s=K(p,G);X=Y(k,l,m);t=[q,r,s];u=a(D,X);v=b(D,X);w=Z(D);E={};E[M]=w;E[N]=t;E[O]=u;E[P]=v;I.append(E)
	J=0;Q=0;R=0;S=0
	for F in I:
		for B in F[N]:
			if B>J:J=B
		for B in F[M]:
			if B>Q:Q=B
		for B in F[O]:
			if B>R:R=B
		for B in F[P]:
			if B>S and B<10001:S=B
	x,y,z,A0,A1,A2,A3,A4,T=d(Q,J,R,S);T=e(T,I,A1,A2,A3,A4);A5=f(UserKey,T,x,y,z,A0);return A5