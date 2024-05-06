cd ecommerce
mkdir vendas
mkdir vendas/backup

cp dados_de_vendas.csv vendas/
cd vendas


data=$(date +"%Y%m%d")
cp dados_de_vendas.csv backup/dados-"$data".csv
mv backup/dados-"$data".csv backup/backup-dados-"$data".csv
touch backup/relatorio-"$data".txt

data_sistema=$(date +"%Y/%m/%d %H:%M")
primeira_data=$(awk -F ',' 'NR==2 {print $5}' backup/backup-dados-"$data".csv)
ultima_data=$(awk -F ',' 'END {print $5}' backup/backup-dados-"$data".csv)
quantidade_itens=$(cut -d',' -f2 backup/backup-dados-"$data".csv | sort | uniq | wc -l)

echo "Data: $data_sistema" >> backup/relatorio-"$data".txt
echo "Data do primeiro registro: $primeira_data" >> backup/relatorio-"$data".txt
echo "Data do último registro: $ultima_data" >> backup/relatorio-"$data".txt
echo "Quantidade total de itens diferentes vendidos: $quantidade_itens" >> backup/relatorio-"$data".txt
echo "Primeiras linhas do arquivo backup-dados-$data.csv:" >> backup/relatorio-"$data".txt
head -n 10 backup/backup-dados-"$data".csv >> backup/relatorio-"$data".txt

zip backup/backup-dados-"$data".zip backup/backup-dados-"$data".csv
rm backup/backup-dados-"$data".csv

cd ..
rm vendas/dados_de_vendas.csv

