def calcul_fourier_coeff(n,T,f): #f is a function
    if n>0:
        an = (1/T)*integrate.quad(lambda x: f(x,T)*np.cos(n*np.pi*x/T),-T,T)[0]
        bn = (1/T)*integrate.quad(lambda x: f(x,T)*np.sin(n*np.pi*x/T),-T,T)[0]
        return (an,bn)
    else:
        print("Erreur Fatale")

def fourier_coeff(n,T,choice):
    if choice==1:#Fonction dent de scie
        pass
