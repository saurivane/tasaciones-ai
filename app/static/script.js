document.getElementById('priceForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const submitButton = this.querySelector('button');
    const originalText = submitButton.innerText;
    submitButton.innerText = 'Calculando...';
    submitButton.disabled = true;

    const resultDiv = document.getElementById('result');
    resultDiv.style.display = 'none';
    resultDiv.className = '';

    const formData = {
        habitaciones: parseInt(document.getElementById('habitaciones').value),
        metros: parseInt(document.getElementById('metros').value),
        numero_planta: parseFloat(document.getElementById('numero_planta').value),
        garage: parseInt(document.getElementById('garage').value),
        ascensor: parseInt(document.getElementById('ascensor').value),
        ubicacion: parseInt(document.getElementById('ubicacion').value)
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const data = await response.json();
        const predictedPrice = data.predicted_price;

        // Calculate range (5%)
        const minPrice = predictedPrice * 0.95;
        const maxPrice = predictedPrice * 1.05;

        // Format currency
        const formatter = new Intl.NumberFormat('es-ES', {
            style: 'currency',
            currency: 'EUR',
            maximumFractionDigits: 0
        });

        resultDiv.innerHTML = `
            <div class="predicted-price">Precio Estimado</div>
            <div class="price-main">${formatter.format(predictedPrice)}</div>
            <div class="price-range">
                <span class="range-label">Rango estimado</span>
                <div class="range-values">
                    <span class="range-item"><small>min:</small> ${formatter.format(minPrice)}</span>
                    <span class="range-sep">|</span>
                    <span class="range-item"><small>max:</small> ${formatter.format(maxPrice)}</span>
                </div>
            </div>
            <div class="disclaimer">
                * El precio está basado en las buenas condiciones del inmueble por lo que el precio real puede variar.
            </div>
        `;
        resultDiv.className = 'success';
        resultDiv.style.display = 'block';

        // Show lead form after short delay
        setTimeout(() => {
            document.getElementById('lead-form-container').style.display = 'block';
            document.getElementById('lead-form-container').scrollIntoView({ behavior: 'smooth' });
        }, 800);

        // Store current prediction and property data for the lead form
        // We use keys that match exactly what the Google Apps Script expects
        window.currentPropertyData = {
            precio_estimado: predictedPrice,
            habitaciones: formData.habitaciones,
            metros: formData.metros,
            planta: formData.numero_planta,
            garaje: formData.garage,
            ascensor: formData.ascensor,
            ubicacion: formData.ubicacion
        };

    } catch (error) {
        resultDiv.innerHTML = `Ocurrió un error al calcular el precio.<br><small>${error.message}</small>`;
        resultDiv.className = 'error';
        resultDiv.style.display = 'block';
    } finally {
        submitButton.innerText = originalText;
        submitButton.disabled = false;
    }
});

// Google Sheets Integration URL (Apps Script Web App)
const GOOGLE_SHEETS_URL = 'https://script.google.com/macros/s/AKfycbxaMfFfy1GvXQUMdg_LPc4BQUOuJ6eCIhb-uGJn-DxU-m-ObysbIqX3pDOT8a2aOJOM9g/exec';

document.getElementById('leadForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const submitBtn = this.querySelector('button');
    const originalText = submitBtn.innerText;
    submitBtn.innerText = 'Enviando...';
    submitBtn.disabled = true;

    const leadData = {
        nombre: document.getElementById('lead_nombre').value,
        email: document.getElementById('lead_email').value,
        telefono: document.getElementById('lead_telefono').value,
        autorizacion: document.getElementById('lead_autorizacion').checked,
        ...window.currentPropertyData
    };

    try {
        // We use fetch with mode: 'no-cors' if using Apps Script directly as a web app
        // Or handle it properly with JSONP/CORS in Apps Script (preferred in my provided script)
        const response = await fetch(GOOGLE_SHEETS_URL, {
            method: 'POST',
            mode: 'no-cors', // Important for Apps Script if not handling OPTIONS
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(leadData)
        });

        // Since no-cors doesn't return response body/status, we assume success if it doesn't throw
        this.innerHTML = `
            <div class="success" style="padding: 30px; border-radius: 15px; margin-top: 20px;">
                <h4 style="margin: 0 0 10px 0;">¡Solicitud enviada con éxito!</h4>
                <p style="margin: 0; font-size: 0.9rem;">Un asesor de San Isidro Gestión se pondrá en contacto contigo pronto.</p>
            </div>
        `;

    } catch (error) {
        console.error('Error submitting lead:', error);
        alert('Hubo un error al enviar tus datos. Por favor, inténtalo de nuevo.');
        submitBtn.innerText = originalText;
        submitBtn.disabled = false;
    }
});
