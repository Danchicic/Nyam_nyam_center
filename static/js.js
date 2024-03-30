// Получаем все карточки товаров на странице
const cards = document.querySelectorAll('.dish');

// Добавляем слушатель события на текстовое поле для поиска
const searchInput = document.getElementById('search');
searchInput.addEventListener('input', function () {
    const searchText = this.value.toLowerCase();

    cards.forEach(card => {
        const cardName = card.querySelector('img').getAttribute('alt').toLowerCase();

        // Проверяем соответствие введенного текста названию карточки
        if (cardName.includes(searchText)) {
            card.style.display = 'block'; // Показываем карточку, если текст найден
        } else {
            card.style.display = 'none'; // Скрываем карточку, если текст не найден
        }
    });
});

const categoryInput = document.getElementById("categories-select");
console.log(categoryInput);
categoryInput.addEventListener('change', function () {
    const category = this.value.toLowerCase();
    console.log(category);
    cards.forEach(card => {
        const cardCategory = card.querySelector('p').getAttribute("category").toLowerCase().trim();

        if (cardCategory == category) {
            card.style.display = 'block';

        } else {
            card.style.display = 'none';
        }
    });
});