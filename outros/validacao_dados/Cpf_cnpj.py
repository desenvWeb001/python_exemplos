
from validate_docbr import CPF, CNPJ

#factory

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválidos!!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido")
    
    def __str__(self):
        return self.fortamata_cpf()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def fortamata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!!!")
    def __str__(self):
        return self.formata_cnpj()
    
    def valida(self, documento):
        mascara = CNPJ()
        return mascara.validate(documento)
    
    def formata_cnpj(self):
        valida_cnpj = CNPJ()
        return valida_cnpj.mask(self.cnpj)



###################################################

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if self.tipo_documento == "cpf":
            if self.valida_cpf(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido")
            
        elif self.tipo_documento == "cnpj":
            if self.valida_cnpj(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido")
        else:
            raise ValueError("Documento inválido")
            
    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.formata_cpf()
        elif self.tipo_documento == "cnpj":
            return self.formata_cnpj()
    
    def valida_cpf(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválidos")
        
    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def valida_cnpj(self, documnento):
        if len(documnento) == 14:
            valida_cnpj = CNPJ()
            return valida_cnpj.validate(documnento)
        else:
            raise ValueError("Quantidade de digitos inválidos")   
            
            

