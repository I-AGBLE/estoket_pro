// Show Password
document.addEventListener("DOMContentLoaded", function () {
    const showPassword = document.getElementById("showPassword");
    const passwordFields = document.querySelectorAll('input[type="password"]');

    showPassword.addEventListener("change", function () {
        const type = this.checked ? "text" : "password";

        passwordFields.forEach(field => {
            field.type = type;
        });
    });
});



// all services infinity loader
let page = 2;
let loading = false;
let hasNext = true;
let timeout = null;

const container = document.getElementById('services-container');
const loader = document.getElementById('loader');

// Debounced scroll
window.addEventListener('scroll', () => {
    clearTimeout(timeout);

    timeout = setTimeout(() => {
        if (loading || !hasNext) return;

        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
            loadMore();
        }
    }, 200);
});

function loadMore() {
    loading = true;
    loader.style.display = 'block';

    fetch(`?page=${page}`, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(res => res.json())
    .then(data => {
        loader.style.display = 'none';

        data.data.forEach(service => {
            const div = document.createElement('div');
            div.classList.add('service-card');

            div.innerHTML = `
                <h3>${service.title}</h3>
                ${service.image ? `<img src="${service.image}" loading="lazy">` : ''}
                <p><strong>Category:</strong> ${service.category}</p>
                <p>${service.description}</p>
                <p><strong>By:</strong> ${service.user_name}</p>
            `;

            container.appendChild(div);
        });

        hasNext = data.has_next;
        page++;
        loading = false;
    })
    .catch(err => {
        console.error(err);
        loader.style.display = 'none';
        loading = false;
    });
}