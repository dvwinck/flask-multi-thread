#!/bin/zsh

# URL do serviço Flask
URL="http://127.0.0.1:5000/random_number"

# Número de chamadas
NUM_CALLS=100

echo "Iniciando $NUM_CALLS chamadas paralelas para $URL..."

# Loop para iniciar chamadas em paralelo
for i in {1..$NUM_CALLS}
do
  for j in {1..$NUM_CALLS}
  do
      (echo "Chamada $i,$j: $(curl -s $URL)" &)
  done
  sleep 1
done

# Esperar por todas as chamadas paralelas serem concluídas
wait

echo "Todas as chamadas foram realizadas."