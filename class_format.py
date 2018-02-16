class main_cls:

    def __init__(self, name_input, name_output='contatti_formatted' ):
        self.name_input = name_input
        self.name_output = name_output

    def lettura(self, func):
        '''quando chiami la funzione scrivere che tipo di funzione
        applicare in modo tale da mantenere il codice riutilizzabile'''
        # legge il file di cell puliti
        import re

        with open('{}'.format(self.name_input), 'r') as f:
            for line in f:
                if re.match('[0-9]{10}', line.strip()):
                    func(line)

    def write(self, stringa):
        num = stringa.strip()
        output = self.name_output + '.txt'
        # crea un file txt formattato per essere un vcf
        with open(output, 'a') as f:
            f.writelines('BEGIN:VCARD\nVERSION:3.0\n')
            f.writelines('FN:' + num + '\n')
            f.writelines('N:;' + num + ';;;' + '\n')
            f.writelines('TEL;TYPE=HOME,VOICE: ' + num + '\n')
            f.writelines('END:VCARD\n')


def main():

    import os

    path = os.getcwd()

    def pulizia(x):
        if istanza.name_output + '.vcf' in os.listdir():
            delete = 'echo ' + '| cd ' + path + '| del ' + istanza.name_output + '.vcf'
            os.system(delete)

    def changename(x):
        # rinomina il file formattato in vcf
        command = 'echo ' + '| cd ' + path + '| rename ' + istanza.name_output +'.txt' + ' *.vcf'
        os.system(command)
        return input('\nil programma ha creato il file ---> ' + istanza.name_output + '.vcf' + '\n\n')

    while True:
        dizionario_file = dict(enumerate(os.listdir()))
        for x in sorted(dizionario_file):
            print('\n\n\t' + str(x) + ' ----->' + dizionario_file[x] + '\n')
        inp = int(input('Da quale file vuoi creare il gruppo?\n\n'))
        # attenzione se l'input non int errore! usare try except
        if inp in dizionario_file:
            istanza = main_cls(dizionario_file[inp])
            istanza.lettura(istanza.write)
            # se c'è il file contatti_formatted.vcf lo cancello
            pulizia(istanza.name_output)
            changename(istanza.name_output)
            break


if __name__ == '__main__':
    main()
