document.addEventListener("DOMContentLoaded", function () {
    const addToCartButtons = document.querySelectorAll(".add-to-cart");
    const cartItems = document.querySelector(".cart-items");
    const cartTotal = document.getElementById("cart-total");

    let total = 0;

    addToCartButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const productCard = button.closest(".product-card");
            const productName = productCard.querySelector("h2").textContent;
            const productPrice = parseFloat(productCard.querySelector("p:last-child").textContent.replace("$", ""));
            total += productPrice;

            const cartItem = document.createElement("li");
            cartItem.textContent = `${productName} - $${productPrice}`;
            cartItems.appendChild(cartItem);

            cartTotal.textContent = total.toFixed(2);
        });
    });
});
