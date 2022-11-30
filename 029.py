v=float(input('sua velocidade: '))
m=7 * (v-80)
if v>80:
    print('sua velocidade foi\33[1:31:40m {}Km/h \33[m \n vc foi multado e pagara multa de \33[1:33:40mR${:.2f}\33[m'.format(v, m))
print('obrigado, tenha um bom dia!!!')
