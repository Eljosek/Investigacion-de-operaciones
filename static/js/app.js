// JavaScript para la aplicación de Programación Lineal
// Funcionalidades interactivas y validaciones

document.addEventListener('DOMContentLoaded', function() {
    
    // Verificar si hay ejemplos guardados en localStorage
    checkForStoredExample();
    
    // Configurar validación del formulario
    setupFormValidation();
    
    // Configurar tooltips de Bootstrap
    enableTooltips();
    
    // Configurar efectos visuales
    setupVisualEffects();
    
    // Inicializar modo oscuro
    initializeDarkMode();
});

/**
 * Verifica si hay un ejemplo guardado en localStorage y lo carga
 */
function checkForStoredExample() {
    const objective = localStorage.getItem('example_objective');
    const constraints = localStorage.getItem('example_constraints');
    
    if (objective && constraints) {
        const objectiveField = document.getElementById('objective');
        const constraintsField = document.getElementById('constraints');
        
        if (objectiveField && constraintsField) {
            objectiveField.value = objective;
            constraintsField.value = constraints;
            
            // Limpiar localStorage
            localStorage.removeItem('example_objective');
            localStorage.removeItem('example_constraints');
            
            // Mostrar notificación
            showNotification('Ejemplo cargado exitosamente', 'success');
        }
    }
}

/**
 * Configura la validación del formulario principal
 */
function setupFormValidation() {
    const form = document.getElementById('lpForm');
    if (!form) return;
    
    form.addEventListener('submit', function(event) {
        if (!validateForm()) {
            event.preventDefault();
            event.stopPropagation();
        } else {
            // Mostrar indicador de carga
            showLoadingState();
        }
        
        form.classList.add('was-validated');
    });
    
    // Validación en tiempo real
    const objective = document.getElementById('objective');
    const constraints = document.getElementById('constraints');
    
    if (objective) {
        objective.addEventListener('input', validateObjective);
    }
    
    if (constraints) {
        constraints.addEventListener('input', validateConstraints);
    }
}

/**
 * Valida el formulario completo
 */
function validateForm() {
    const objective = document.getElementById('objective').value.trim();
    const constraints = document.getElementById('constraints').value.trim();
    
    let isValid = true;
    
    // Validar función objetivo
    if (!validateObjectiveString(objective)) {
        showFieldError('objective', 'Formato de función objetivo inválido');
        isValid = false;
    }
    
    // Validar restricciones
    if (!validateConstraintsString(constraints)) {
        showFieldError('constraints', 'Una o más restricciones tienen formato inválido');
        isValid = false;
    }
    
    return isValid;
}

/**
 * Valida el formato de la función objetivo
 */
function validateObjectiveString(objective) {
    const regex = /(max|min|maximizar|minimizar)\s*z\s*=\s*[+-]?\s*\d*\.?\d*\s*x\s*[+-]\s*\d*\.?\d*\s*y/i;
    return regex.test(objective.replace(/\s+/g, ' '));
}

/**
 * Valida el formato de las restricciones
 */
function validateConstraintsString(constraints) {
    const lines = constraints.split('\n').filter(line => line.trim());
    
    for (const line of lines) {
        const cleanLine = line.replace(/\s+/g, ' ').trim();
        
        // Patrones válidos para restricciones
        const patterns = [
            // Restricción completa: ax + by <= c (permite coeficientes opcionales)
            /^[+-]?\s*\d*\.?\d*\s*x\s*[+-]\s*\d*\.?\d*\s*y\s*(<=|>=|=|≤|≥)\s*[+-]?\d+\.?\d*$/,
            // Restricción solo con x: x <= c, x >= c
            /^[+-]?\s*\d*\.?\d*\s*x\s*(<=|>=|=|≤|≥)\s*[+-]?\d+\.?\d*$/,
            // Restricción solo con y: y <= c, y >= c  
            /^[+-]?\s*\d*\.?\d*\s*y\s*(<=|>=|=|≤|≥)\s*[+-]?\d+\.?\d*$/,
            // Restricciones entre variables: x <= y, y >= x, etc.
            /^[+-]?\s*\d*\.?\d*\s*x\s*(<=|>=|=|≤|≥)\s*[+-]?\s*\d*\.?\d*\s*y$/,
            /^[+-]?\s*\d*\.?\d*\s*y\s*(<=|>=|=|≤|≥)\s*[+-]?\s*\d*\.?\d*\s*x$/
        ];
        
        // Verificar si la línea coincide con algún patrón
        const isValid = patterns.some(pattern => pattern.test(cleanLine));
        
        if (!isValid) {
            return false;
        }
    }
    
    return lines.length > 0;
}

/**
 * Validación en tiempo real para función objetivo
 */
function validateObjective() {
    const field = document.getElementById('objective');
    const value = field.value.trim();
    
    if (value === '') {
        clearFieldError('objective');
        return;
    }
    
    if (validateObjectiveString(value)) {
        showFieldSuccess('objective');
    } else {
        showFieldError('objective', 'Formato: "maximizar z = 3x + 2y"');
    }
}

/**
 * Validación en tiempo real para restricciones
 */
function validateConstraints() {
    const field = document.getElementById('constraints');
    const value = field.value.trim();
    
    if (value === '') {
        clearFieldError('constraints');
        return;
    }
    
    if (validateConstraintsString(value)) {
        showFieldSuccess('constraints');
    } else {
        showFieldError('constraints', 'Formato: "x + 2y <= 8"');
    }
}

/**
 * Muestra error en un campo específico
 */
function showFieldError(fieldId, message) {
    const field = document.getElementById(fieldId);
    field.classList.remove('is-valid');
    field.classList.add('is-invalid');
    
    // Buscar o crear elemento de feedback
    let feedback = field.nextElementSibling;
    if (!feedback || !feedback.classList.contains('invalid-feedback')) {
        feedback = document.createElement('div');
        feedback.className = 'invalid-feedback';
        field.parentNode.insertBefore(feedback, field.nextSibling);
    }
    
    feedback.textContent = message;
}

/**
 * Muestra éxito en un campo específico
 */
function showFieldSuccess(fieldId) {
    const field = document.getElementById(fieldId);
    field.classList.remove('is-invalid');
    field.classList.add('is-valid');
    
    // Remover mensaje de error si existe
    const feedback = field.nextElementSibling;
    if (feedback && feedback.classList.contains('invalid-feedback')) {
        feedback.remove();
    }
}

/**
 * Limpia los estilos de error/éxito de un campo
 */
function clearFieldError(fieldId) {
    const field = document.getElementById(fieldId);
    field.classList.remove('is-invalid', 'is-valid');
    
    const feedback = field.nextElementSibling;
    if (feedback && feedback.classList.contains('invalid-feedback')) {
        feedback.remove();
    }
}

/**
 * Muestra estado de carga en el formulario
 */
function showLoadingState() {
    const submitBtn = document.querySelector('button[type="submit"]');
    if (submitBtn) {
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Resolviendo...';
        submitBtn.disabled = true;
        
        // Agregar clase de carga al formulario
        document.getElementById('lpForm').classList.add('loading');
    }
}

/**
 * Función para limpiar completamente el formulario
 */
function clearForm() {
    const form = document.getElementById('lpForm');
    if (form) {
        form.reset();
        form.classList.remove('was-validated');
        
        // Limpiar estilos de validación
        const fields = form.querySelectorAll('.form-control');
        fields.forEach(field => {
            field.classList.remove('is-valid', 'is-invalid');
        });
        
        // Remover mensajes de feedback
        const feedbacks = form.querySelectorAll('.invalid-feedback');
        feedbacks.forEach(feedback => feedback.remove());
        
        showNotification('Formulario limpiado', 'info');
    }
}

/**
 * Función para cargar un ejemplo predefinido
 */
function loadExample() {
    const examples = [
        {
            objective: 'maximizar z = 3x + 2y',
            constraints: 'x + 2y <= 8\n2x + y <= 10\nx >= 0\ny >= 0'
        },
        {
            objective: 'minimizar z = 2x + 3y',
            constraints: 'x + y >= 4\n2x + y >= 6\nx >= 0\ny >= 0'
        },
        {
            objective: 'maximizar z = x + 4y',
            constraints: 'x + 2y <= 12\n2x + y <= 16\nx + y >= 5\nx >= 0\ny >= 0'
        }
    ];
    
    // Seleccionar ejemplo aleatorio
    const randomExample = examples[Math.floor(Math.random() * examples.length)];
    
    document.getElementById('objective').value = randomExample.objective;
    document.getElementById('constraints').value = randomExample.constraints;
    
    showNotification('Ejemplo cargado', 'success');
}

/**
 * Configura tooltips de Bootstrap
 */
function enableTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * Configura efectos visuales adicionales
 */
function setupVisualEffects() {
    // Efecto de aparición gradual para las cards
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
    
    // Efecto hover para botones
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

/**
 * Muestra una notificación temporal
 */
function showNotification(message, type = 'info') {
    const alertClass = type === 'error' ? 'danger' : type;
    const iconClass = type === 'error' ? 'exclamation-triangle' : 
                     type === 'success' ? 'check-circle' : 'info-circle';
    
    const notification = document.createElement('div');
    notification.className = `alert alert-${alertClass} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        <i class="fas fa-${iconClass}"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remover después de 3 segundos
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 3000);
}

/**
 * Función para copiar texto al portapapeles
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        showNotification('Copiado al portapapeles', 'success');
    }, function(err) {
        console.error('Error al copiar: ', err);
        showNotification('Error al copiar', 'error');
    });
}

/**
 * Función para exportar resultados
 */
function exportResults() {
    const resultsContainer = document.querySelector('.container');
    if (resultsContainer) {
        // Aquí podrías implementar exportación a PDF o imagen
        showNotification('Función de exportación en desarrollo', 'info');
    }
}

/**
 * Inicializa el modo oscuro desde localStorage
 */
function initializeDarkMode() {
    const darkMode = localStorage.getItem('darkMode') === 'true';
    if (darkMode) {
        document.documentElement.setAttribute('data-theme', 'dark');
        updateDarkModeIcon(true);
    }
}

/**
 * Alterna entre modo claro y oscuro
 */
function toggleDarkMode() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const isDark = currentTheme === 'dark';
    
    if (isDark) {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('darkMode', 'false');
        updateDarkModeIcon(false);
        showNotification('Modo claro activado', 'info');
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('darkMode', 'true');
        updateDarkModeIcon(true);
        showNotification('Modo oscuro activado', 'info');
    }
}

/**
 * Actualiza el icono del botón de modo oscuro
 */
function updateDarkModeIcon(isDark) {
    const icon = document.getElementById('darkModeIcon');
    if (icon) {
        if (isDark) {
            icon.className = 'fas fa-sun';
        } else {
            icon.className = 'fas fa-moon';
        }
    }
}

// Funciones globales para uso en templates
window.clearForm = clearForm;
window.loadExample = loadExample;
window.copyToClipboard = copyToClipboard;
window.exportResults = exportResults;
window.toggleDarkMode = toggleDarkMode;