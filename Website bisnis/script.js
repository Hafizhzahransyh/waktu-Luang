document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Mencegah pengiriman form

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Tampilkan pesan sukses (di sini Anda bisa menambahkan logika pengiriman email)
    alert(`Terima kasih, ${name}! Pesan Anda telah dikirim.`);
    
    // Reset form setelah pengiriman
    this.reset();
});