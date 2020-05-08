//иницилизируем пространство имен для доступа к компонентам карты
ymaps.ready(init); 



function init() {
	//конструктор
	var map = new ymaps.Map('map', {
		center: [59.94, 30.32], // центр карты
		zoom: 10
	});
}