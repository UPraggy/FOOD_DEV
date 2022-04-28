# Raciocínio Automático em Situações de Incerteza e Imprecisão

# SUMÁRIO

- **[INTRODUÇÃO](#introdução)**
- **[MODULO 1](#modulo-1)**
- **[MODULO 2](#modulo-2)**


# INTRODUÇÃO
Neste Módulo, tem como objetivo resumir os conceitos de Representação de Conhecimento, Raciocínio Automático e Aprendizado.<br>
**Ele será resumido em topicos simples com base em alguns conceitos e atividades que constam no Conteúdo digital.**

# MODULO 1
- **[ATIVIDADES MOD 1](#atividades-mod-1)**
- **[CONCEITOS MOD 1](#conceitos-mod-1)**

## ATIVIDADES MOD 1
![image](https://user-images.githubusercontent.com/100146657/165299375-48ee3ed7-a87f-4b99-b5e2-eace54184d23.png)
![image](https://user-images.githubusercontent.com/100146657/165299929-50790840-1197-4bd6-a902-fda773f33eab.png)
![image](https://user-images.githubusercontent.com/100146657/165300158-55afc623-1926-4f26-81f3-eac1a7237a59.png)
![image](https://user-images.githubusercontent.com/100146657/165300182-3ee75c42-fd81-44a2-8188-71d23f8477b8.png)

Nessa etapa ele chegou a formula em que **Grama molhada (G)** depende de **Chuva (C)**

![image](https://user-images.githubusercontent.com/100146657/165300346-d2d9db69-828c-492e-83ba-78b9fc1757a3.png)

Como o problema não cita o Regador (R), ele é "descartado" das operações<br>
Esse "descarte" ver em forma de soma como afirmação do **r** de um lado da soma e negação do **r** no outro lado.
Assim ele começa a fazer a devida analise e operações na tabela.

![image](https://user-images.githubusercontent.com/100146657/165300653-3b64d9ff-232c-4f6b-bd97-cebbac258e1a.png)
![image](https://user-images.githubusercontent.com/100146657/165300676-ad5a3dfe-a95c-4365-bc67-7180c8511ee7.png)

Assim como acima no numerador no denominador, não é diferente, a operação de "descarte" também é feita, porém com o **r** e o **c**,
pois oque queremos agora é apenas o **g**

![image](https://user-images.githubusercontent.com/100146657/165301577-ef4e61b1-bacb-49e2-9efd-ae28b3eecd64.png)
![image](https://user-images.githubusercontent.com/100146657/165301645-25db8fef-2d2e-4410-b181-c59d9badad7d.png)
![image](https://user-images.githubusercontent.com/100146657/165301675-9db6f90f-fb25-466c-9ae9-d11d4534f617.png)
![image](https://user-images.githubusercontent.com/100146657/165301716-c60878b6-64de-453a-8f0d-47cf5a87f171.png)

Ao final é verificado:

![image](https://user-images.githubusercontent.com/100146657/165301805-51ae714d-86b5-40c1-86bc-e21dbdfd0bd1.png)

## CONCEITOS MOD 1
### Variaveis
- **Variaveis aleatorias bolenanas** - podem assumir o valor verdadeiro e falso.<br>
- **Variaveis aleatorias discretas** - composto por um conjunto de valores enumeráveis, uma possível variável aleatória discreta seria Tempo, em que os valores possíveis poderiam ser ensolarado, chuvoso, nublado e nevoeiro.<br>
- **Variaveis aleatorias continuas** - é formado por números reais compreendidos em um intervalo, de forma que entre quaisquer dois valores desse intervalo, há sempre uma quantidade infinita de valores.<br><br>
### Probabilidade
- **Probabilidade incondicional** - em resumo é o grau de crença (probabilidade) que se atribui a um fato, sem haver qualquer informação adicional sobre ele.<br>
- **Probabilidade condicional** - em resumo é o grau de crença (probabilidade) que se atribui a um fato e havendo alguma informação adicional (evidência) sobre ele.<br>
#### Probabilidade condicional - FORMULA
![image](https://user-images.githubusercontent.com/100146657/165290194-2b8762a3-57cc-43c5-adc7-06f50d96a131.png)

![image](https://user-images.githubusercontent.com/100146657/165290261-cfb81a23-520b-4730-8e14-44b71613b8f7.png)

**A PARTIR DESSAS EQUAÇÕES É POSSIVEL DERIVAR A EQUAÇÃO ABAIXO CONHECIDA COMO REGRA DE BAYERS**<br>
#### REGRA DE BAYERS (Regra Bayesiana) - FORMULA
![image](https://user-images.githubusercontent.com/100146657/165291391-6ad25b0a-25e5-40f6-ae0f-25af24333e7c.png)

**OBS.:** Essa formula é aplicada quando é invertida a ordem pois **b** depende de **a (a|b)**, mas no caso de inversão **b|a** é aplicada essa formula
#### INDEPENDENCIA
Para situações como essa, a probabilidade condicional é dada pela equação:

![image](https://user-images.githubusercontent.com/100146657/165291627-8f542bd3-518f-4402-8731-91a7c2b881f4.png)

**OBS.:** O sinal | significa dependencia EX: a|b - **b** depende de **a** para que ele ocorra ou assuma um valor logico (V ou F).x
Com isso, a **regra do produto** passa a ser definida conforme a equação:

![image](https://user-images.githubusercontent.com/100146657/165291644-aef5216d-ecd2-4801-ba36-e9faed4e7cd9.png)

### Inferência com distribuições conjuntas totais - EXEMPLO BASICO
Dada a tabela:

![image](https://user-images.githubusercontent.com/100146657/165291945-6eb72878-9fb5-4491-bfcf-bd18ddddf53e.png)

É possível calcular tanto probabilidades incondicionais quanto condicionais.

#### Probabilidades Incondicionais
![image](https://user-images.githubusercontent.com/100146657/165292124-a7163e1d-1f35-4631-9628-e5805e871676.png)

![image](https://user-images.githubusercontent.com/100146657/165292149-470c0270-bcca-4e01-82e7-f975a6b1fef5.png)

![image](https://user-images.githubusercontent.com/100146657/165292169-9f05a03d-04aa-4d18-8b85-960368adeb85.png)

#### Probabilidades Condicionais
![image](https://user-images.githubusercontent.com/100146657/165292266-b14715f3-c214-4722-b9e5-3b5eb37c8574.png)

### Inferência com a regra de Bayes - EXEMPLO
![image](https://user-images.githubusercontent.com/100146657/165292512-4fff10f1-6779-4dd6-b30a-df5ba15df0eb.png)

![image](https://user-images.githubusercontent.com/100146657/165292524-af0fa8d0-1abf-4d65-9c2c-3c0a33891d43.png)

![image](https://user-images.githubusercontent.com/100146657/165292536-04d6d67b-76d6-4f26-aaaa-2508a3d4c260.png)

#### Redes bayesianas (REDE DE BAYERS)
**Rede bayesiana** - é um grafo direcionado e acíclico, em que os nós representam as variáveis aleatórias tanto de evidência quanto de hipótese (diagnóstico), e as arestas representam as dependências que existem entre as variáveis.<br>
**OBS.:**
![image](https://user-images.githubusercontent.com/100146657/165299751-dac5215f-42f6-4c6d-bf00-c4f810bede5f.png)

![image](https://user-images.githubusercontent.com/100146657/165299476-1d1d7bed-4d7c-4c40-9c78-9392846c151e.png)

A cada P é necessario verificar a condicão ex: **c|a** que valor **c** assume quando a for **V**

# MODULO 2
- **[ATIVIDADES MOD 2](#atividades-mod-2)**
- **[CONCEITOS MOD 2](#conceitos-mod-2)**

## ATIVIDADES MOD 2


## CONCEITOS MOD 2
**Eventos de incerteza** - São eventos que podem ou não acontecer com alguma chance, dada por uma medida de probabilidade que varia entre 0 e 1.<br>
**Eventos imprecisos** - Quando se trata de eventos imprecisos, não estamos falando de algo que pode ou não acontecer, mas que acontece de fato, com determinada intensidade que varia entre 0 e 1.

![image](https://user-images.githubusercontent.com/100146657/165302667-08c6d28e-be64-4098-827a-2f65aac051aa.png)

**0** - Quando o elemento não pertence ao conjunto.

**1** - Quando o elemento pertence ao conjunto.

### Propriedades das operações com conjuntos tradicionais
![image](https://user-images.githubusercontent.com/100146657/165302624-1219571a-57b4-4825-9f7e-1b8c9071e6ae.png)


### Conjuntos nebulosos
De acordo com os conjuntos tradicionais é possivel determinar um conjunto e/ou os elementos que o compõe, normalmente é algo preciso, se você retira um elemento
aquele conjunto deixa de ser o mesmo. Entretando, para aqueles conjuntos imprecisos em que não é facil determinar alguma caracteristica, seja seu conteudo ou propriedades ele é chamado de conjunto nebuloso.<br>

#### Situação precisa: conjunto de laranjas
Uma laranja lima faz parte do conjunto de laranjas? Obviamente que sim. E quanto a uma maçã? Você certamente não hesitou em responder que não. Podemos dizer com precisão que uma maçã não faz parte do conjunto de laranjas. Estamos diante de uma situação precisa.

#### Situação imprecisa: conjunto de pessoas altas
Quando uma pessoa começa a ser alta? Podemos dizer que uma pessoa de 1,80 é alta? E se ela estiver ao lado de uma pessoa de 1,95? E uma pessoa de 1,60 pode ser considerada alta? E se essa pessoa de 1,60 tiver 10 anos de idade? A ideia de pessoa alta já não parece tão precisa quanto o conjunto de laranjas, certo?

### Operações com conjuntos nebulosos
![image](https://user-images.githubusercontent.com/100146657/165304187-12a8d230-6b9e-43e8-8a5a-31aadcfe116a.png)
![image](https://user-images.githubusercontent.com/100146657/165304127-a91d90bc-e591-42eb-968d-694d5fd40c3f.png)

![image](https://user-images.githubusercontent.com/100146657/165304260-39cf07cf-e2dc-4abd-baef-53ca3ff08678.png)
![image](https://user-images.githubusercontent.com/100146657/165304286-08af5d49-fb95-45f9-9785-2273635740a7.png)

![image](https://user-images.githubusercontent.com/100146657/165304326-edbc24bc-ecd8-4c18-b411-20e850e16427.png)
![image](https://user-images.githubusercontent.com/100146657/165304353-d05a45ce-04d8-445f-bcf0-a0e8fe179447.png)

![image](https://user-images.githubusercontent.com/100146657/165304379-142eb793-01bb-4980-8c28-cef91d0b94af.png)
![image](https://user-images.githubusercontent.com/100146657/165304408-7414e0a5-df98-4623-ba37-faef219306f3.png)

#### Propriedades das operações com conjuntos nebulosos
**EX:**

![image](https://user-images.githubusercontent.com/100146657/165304477-d5d6c45a-8135-48f1-8c11-a73399347804.png)
![image](https://user-images.githubusercontent.com/100146657/165304517-a6777e34-9cb9-42e5-957e-36c8903f5a00.png)








