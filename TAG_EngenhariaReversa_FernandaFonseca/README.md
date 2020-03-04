O código necessário para reverter a encriptação do diretório do usuário é semelhante ao usado na mesma.
Entretanto, aqui apenas consta uma função do código para operação efetiva da decriptação, baseada na função "main" do arquivo encriptador.

O arquivo decriptador também poderia ser baixado de uma URL, usando uma interface criada pela biblioteca libcurl.
Ele seria utilizado por um código principal, responsável por alterar os nomes das pastas atarvés de chamadas do sistema, assim como o arquivo executado para a encriptação.
Nele, todas as pastas do diretório seriam decriptadas e alteradas, não havendo a necessidade de salvar uma cópia como no executável original.

O código de decriptação propriamente dito é o conjunto de arquivos (funções) utilizados no encriptador, apenas com o arquivo "main" modificado.
Conforme foi constatado na análise prévia para entender o propósito do executável, o inteiro correspondente a cada caracter dos nomes das pastas do diretório é utilizado em uma operação de soma, a qual utiliza um caracter do segundo parâmetro da função.
Dessa forma, para reverter a encriptação, o inteiro de cada caracter encriptado deve ser utilizado em uma diferença com o mesmo caracter do parâmetro da função, resultado das funções de inicialização.
Assim, os caracteres correspondentes aos resultados das operações podem ser reunidos para que as pastas do diretório sejam renomeadas pelo código principal.
