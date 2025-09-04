#!/usr/bin/env python3
"""
Exemplo de uso da API do Gerenciador de Tarefas
Este script demonstra como interagir com a API REST do aplicativo Flask
"""

import requests
import json

# URL base da API
BASE_URL = "http://localhost:5000"

def test_api():
    """Testa as funcionalidades da API"""
    
    print("🚀 Testando API do Gerenciador de Tarefas")
    print("=" * 50)
    
    # 1. Listar todas as tarefas (inicialmente vazio)
    print("\n1. Listando tarefas existentes...")
    try:
        response = requests.get(f"{BASE_URL}/api/tasks")
        if response.status_code == 200:
            tasks = response.json()
            print(f"✅ Encontradas {len(tasks)} tarefas")
            for task in tasks:
                print(f"   - {task['title']} ({'✅' if task['completed'] else '⏳'})")
        else:
            print(f"❌ Erro: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Erro: Não foi possível conectar ao servidor")
        print("   Certifique-se de que o servidor Flask está rodando (python app.py)")
        return
    
    # 2. Adicionar uma nova tarefa
    print("\n2. Adicionando nova tarefa...")
    new_task = {
        "title": "Estudar Flask",
        "description": "Aprender os conceitos básicos do Flask"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/tasks",
            json=new_task,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 201:
            task = response.json()
            print(f"✅ Tarefa criada com sucesso!")
            print(f"   ID: {task['id']}")
            print(f"   Título: {task['title']}")
            print(f"   Descrição: {task['description']}")
        else:
            print(f"❌ Erro ao criar tarefa: {response.status_code}")
            print(f"   Resposta: {response.text}")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    # 3. Adicionar mais algumas tarefas
    print("\n3. Adicionando mais tarefas...")
    more_tasks = [
        {"title": "Fazer exercícios", "description": "30 minutos de caminhada"},
        {"title": "Ler um livro", "description": "Capítulo 5 do livro de Python"},
        {"title": "Organizar o quarto", "description": "Limpar e organizar"}
    ]
    
    for task_data in more_tasks:
        try:
            response = requests.post(
                f"{BASE_URL}/api/tasks",
                json=task_data,
                headers={'Content-Type': 'application/json'}
            )
            if response.status_code == 201:
                print(f"✅ Adicionada: {task_data['title']}")
            else:
                print(f"❌ Erro ao adicionar {task_data['title']}")
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    # 4. Listar todas as tarefas novamente
    print("\n4. Listando todas as tarefas...")
    try:
        response = requests.get(f"{BASE_URL}/api/tasks")
        if response.status_code == 200:
            tasks = response.json()
            print(f"✅ Total de tarefas: {len(tasks)}")
            for task in tasks:
                status = "✅ Concluída" if task['completed'] else "⏳ Pendente"
                print(f"   [{task['id']}] {task['title']} - {status}")
                if task['description']:
                    print(f"       📝 {task['description']}")
                print(f"       🕒 Criada em: {task['created_at']}")
                print()
        else:
            print(f"❌ Erro: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Teste da API concluído!")
    print("💡 Acesse http://localhost:5000 para ver a interface web")

if __name__ == "__main__":
    test_api()

