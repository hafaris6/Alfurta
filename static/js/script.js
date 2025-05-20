// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Auto close alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            // Create a Bootstrap alert instance and close it
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Preview image URL in add product form
    const imageInput = document.getElementById('image');
    if (imageInput) {
        imageInput.addEventListener('blur', function() {
            const imageUrl = this.value;
            if (imageUrl) {
                // Check if preview exists, otherwise create it
                let previewContainer = document.getElementById('image-preview-container');
                if (!previewContainer) {
                    previewContainer = document.createElement('div');
                    previewContainer.id = 'image-preview-container';
                    previewContainer.className = 'mt-2';
                    this.parentNode.appendChild(previewContainer);
                }
                
                // Update preview
                previewContainer.innerHTML = `
                    <p>معاينة الصورة:</p>
                    <img src="${imageUrl}" class="img-thumbnail" style="max-height: 200px;" alt="معاينة الصورة">
                `;
            }
        });
    }

    // Phone number validation for Arabic numbers
    const phoneInput = document.getElementById('phone');
    if (phoneInput) {
        phoneInput.addEventListener('input', function() {
            // Remove any non-numeric characters
            this.value = this.value.replace(/[^0-9]/g, '');
        });
    }
});
