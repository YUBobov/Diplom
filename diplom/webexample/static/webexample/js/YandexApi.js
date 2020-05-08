//иницилизируем пространство имен для доступа к компонентам карты
ymaps.ready(init); 



function init() {
	//конструктор
	var map = new ymaps.Map('map', {
		center: [56.84, 60.61], // центр карты
		zoom: 15
	});
	//
	map.controls.add('zoomControl');
	//
	//map.controls.add('searchControl');
	//Для измерения расстояния
	map.controls.add('mapTools');
	map.controls.add('searchControl');
}