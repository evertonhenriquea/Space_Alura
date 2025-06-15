from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        required=True,
        max_length=100,
        label="Nome de Login",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    senha = forms.CharField(
        required=True,
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        required=True,
        max_length=100,
        label="Nome De Cadastro",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@xpto.com"
            }
        )
    )
    senha_1 = forms.CharField(
        required=True,
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        required=True,
        label="Confirme sua senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Digite sua senha novamente"
            }
        )
    )
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("O Nome não pode conter espaços em branco.")
            else:
                return nome
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("As senhas não coincidem.")
            else:
                return senha_2
        else:
            raise forms.ValidationError("Por favor, preencha ambos os campos de senha.")