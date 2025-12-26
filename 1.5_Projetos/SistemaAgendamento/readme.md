# Projeto 1 – Sistema de Agendamento

Este projeto cria um **sistema de agendamento de eventos**, permitindo ao usuário organizar compromissos, evitar conflitos de horários e gerar relatórios de eventos.

## Funcionalidades principais

O programa deve permitir ao usuário realizar três operações principais:

### 1. Adicionar evento
- O usuário informa título, data e hora do evento.  
- Se já existir um evento no mesmo horário, o sistema alerta: `"Conflito de horário!"`  
- Caso contrário, o evento é adicionado normalmente.

Exemplo de uso:  
Operação: adicionar  
Evento: Reunião Equipe  
Data: 2025-12-27  
Hora: 14:00  

Operação: adicionar  
Evento: Chamada Cliente  
Data: 2025-12-27  
Hora: 14:00  

Conflito de horário: Reunião Equipe

### 2. Remover evento
- Permite remover um evento informando título, data e hora.  
- Se o evento não existir, o sistema alerta: `"Evento não encontrado"`

Exemplo de uso:  
Operação: remover  
Evento: Reunião Equipe  
Data: 2025-12-27  
Hora: 14:00  

Evento removido: Reunião Equipe

### 3. Listar eventos
- Mostra todos os eventos cadastrados ordenados por data e hora.  
- Inclui contagem total de eventos.

Exemplo de saída:  
Relatório de eventos:  
2025-12-27 09:00 – Café da manhã  
2025-12-27 12:00 – Almoço com cliente  
2025-12-27 15:00 – Treinamento interno  

Total de eventos: 3

### **Bônus de lógica**
- Detectar automaticamente **conflitos de horário** ao adicionar eventos.  
- Permitir filtrar eventos por dia ou semana.  
- Preparar o sistema para futuros recursos de **POO**, como classes `Evento` e `Calendario`.

### **Objetivos de aprendizado**
- Trabalhar **listas e dicionários** para armazenar eventos  
- Manipular **loops e condicionais**  
- Criar **funções** para cada operação (`adicionar_evento`, `remover_evento`, `listar_eventos`)  
- Implementar **lógica de conflito de horário**  
