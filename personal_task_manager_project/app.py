from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Lista simples para armazenar tarefas (em produção, use um banco de dados)
tasks = []

@app.route('/')
def index():
    """Página principal - lista todas as tarefas"""
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    """Adiciona uma nova tarefa"""
    title = request.form.get('title')
    description = request.form.get('description', '')
    
    if title:
        task = {
            'id': len(tasks) + 1,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        tasks.append(task)
        flash('Tarefa adicionada com sucesso!', 'success')
    else:
        flash('Título da tarefa é obrigatório!', 'error')
    
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    """Marca uma tarefa como concluída"""
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            flash('Tarefa marcada como concluída!', 'success')
            break
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    """Remove uma tarefa"""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    flash('Tarefa removida!', 'success')
    return redirect(url_for('index'))

@app.route('/api/tasks')
def api_tasks():
    """API endpoint para retornar todas as tarefas em JSON"""
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def api_add_task():
    """API endpoint para adicionar uma nova tarefa via JSON"""
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({'error': 'Título é obrigatório'}), 400
    
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': False,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    tasks.append(task)
    
    return jsonify(task), 201

@app.errorhandler(404)
def not_found(error):
    """Página de erro 404"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Página de erro 500"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Configurações para desenvolvimento
    app.run(debug=True, host='0.0.0.0', port=5000)
