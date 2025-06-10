#!/bin/bash

# Script helper para manejar el bot de Rasa

set -e

COMPOSE_FILE="docker-compose.yml"

show_help() {
    echo "Bot Helper Script - Gestión de Rasa Hospital Bot"
    echo ""
    echo "Uso: ./bot.sh [COMANDO]"
    echo ""
    echo "Comandos disponibles:"
    echo "  train       - Entrenar el modelo"
    echo "  dev         - Iniciar en modo desarrollo"
    echo "  prod        - Iniciar en modo producción"
    echo "  stop        - Detener todos los servicios"
    echo "  logs        - Ver logs de todos los servicios"
    echo "  logs-train  - Ver logs del entrenamiento"
    echo "  logs-server - Ver logs del servidor"
    echo "  logs-actions- Ver logs del action server"
    echo "  clean       - Limpiar contenedores y volúmenes"
    echo "  rebuild     - Reconstruir imágenes"
    echo "  test        - Probar el bot"
    echo "  shell       - Abrir shell interactivo"
    echo "  help        - Mostrar esta ayuda"
    echo ""
}

train_model() {
    echo "🚀 Entrenando modelo..."
    docker-compose --profile train up rasa-train
    echo "✅ Entrenamiento completado"
}

start_dev() {
    echo "🔧 Iniciando en modo desarrollo..."
    docker-compose --profile dev up -d
    echo "✅ Bot iniciado en modo desarrollo"
    echo "   - Action Server: http://localhost:5055"
    echo "   - HTTP API: http://localhost:5005"
}

start_prod() {
    echo "🚀 Iniciando en modo producción..."
    docker-compose --profile production up -d
    echo "✅ Bot iniciado en modo producción"
}

stop_services() {
    echo "🛑 Deteniendo servicios..."
    docker-compose --profile dev --profile production --profile train down
    echo "✅ Servicios detenidos"
}

show_logs() {
    docker-compose --profile dev --profile production logs -f
}

show_train_logs() {
    docker-compose --profile train logs rasa-train
}

show_server_logs() {
    docker-compose --profile dev --profile production logs -f rasa-server
}

show_actions_logs() {
    docker-compose --profile dev --profile production logs -f rasa-actions
}

clean_all() {
    echo "🧹 Limpiando contenedores y volúmenes..."
    docker-compose --profile dev --profile production --profile train down -v
    docker system prune -f
    echo "✅ Limpieza completada"
}

rebuild_images() {
    echo "🔨 Reconstruyendo imágenes..."
    docker-compose build --no-cache
    echo "✅ Imágenes reconstruidas"
}

test_bot() {
    echo "🧪 Probando el bot..."
    curl -X POST http://localhost:5005/webhooks/rest/webhook \
      -H "Content-Type: application/json" \
      -d '{"sender": "test", "message": "hola"}' \
      2>/dev/null | jq '.' || echo "❌ Error: Asegúrate de que el bot esté corriendo"
}

open_shell() {
    echo "🐚 Abriendo shell interactivo..."
    docker-compose exec  -it rasa-shell rasa shell
}

# Función principal
case "${1:-help}" in
    train)
        train_model
        ;;
    dev)
        start_dev
        ;;
    prod)
        start_prod
        ;;
    stop)
        stop_services
        ;;
    logs)
        show_logs
        ;;
    logs-train)
        show_train_logs
        ;;
    logs-server)
        show_server_logs
        ;;
    logs-actions)
        show_actions_logs
        ;;
    clean)
        clean_all
        ;;
    rebuild)
        rebuild_images
        ;;
    test)
        test_bot
        ;;
    shell)
        open_shell
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo "❌ Comando desconocido: $1"
        echo ""
        show_help
        exit 1
        ;;
esac