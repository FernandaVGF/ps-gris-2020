# PROCESSO SELETIVO - Grupo de Resposta a Incidentes de Segurança

# Nome: Fernanda Veiga Gomes da Fonseca
# TAG - Bash - Entrega: 15/03/2020


#!/bin/bash

## 1- Realiza backup.

# Data atual no formato YYYYMMDD.
data=`date +%Y%m%d`

# Cria um arquivo .tar.gz contendo a data de backup em seu nome.
destino=/home/fernanda/Backup/$data.tar.gz

# Local dos arquivos que serão copiados.
origem=/home/fernanda/Imagens

# Realiza o backup.
tar -cpzf $destino $origem

## 2- Exclui backups antigos.
cd /home/fernanda/Backup

# Arquivos com menos de três dias.
dia1=$(date -d "$data -1 days" +"%Y%m%d")
dia2=$(date -d "$data -2 days" +"%Y%m%d")

# Remove todos os arquivos com mais de três dias.
shopt -s extglob
rm -v !("${dia1}.tar.gz"|"${dia2}.tar.gz")