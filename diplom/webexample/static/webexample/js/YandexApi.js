//иницилизируем пространство имен для доступа к компонентам карты
ymaps.ready(init); 

var dista =0;

function init() {
	//конструктор
	let map = new ymaps.Map('map', {
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

	//Функция подсчета расстояния карта
	
	//Функция подсчета расстояния карта
	map.behaviors.get('ruler').geometry.events.add('change', function(e){
		line = map.behaviors.get('ruler').geometry.getCoordinates();
		dista = 0;
	    for (let i = 0; i < line.length-1; i++) {
	    		dista += ymaps.coordSystem.geo.getDistance(line[i],line[i+1]);}
	    //console.log(dista);
	    sessionStorage.setItem('local',dista);
	});

	if (sessionStorage.getItem('local')!= null){
		document.querySelectorAll('#pricee').forEach(function(element){
			//console.log(element.innerHTML);
			let money=element.innerHTML;
			dis=sessionStorage.getItem('local');
			let result = Math.round(money*Math.ceil(dis)/1000);
			element.innerHTML=result;
		});
	}

	/*document.querySelectorAll('.form-control').forEach(function(element){
		element.onchange= function (){
			index = element.value;
			console.log(index);

			alert((document.getElementById(index).innerHTML));
		}
		});*/

	

	/*money = Number.parseInt(document.getElementById("pricee").innerHTML);
	console.log(money);
	dis=localStorage.getItem('local')
	result = Math.round(money*Math.ceil(dis)/1000);
	console.log(result);
	document.getElementById("pricee").innerHTML = result;
	console.log(document.getElementsByClassName("price").length)*/

	

}

	







/*route.model.events.add('requestsuccess', function () {

            var activeRoute = route.getActiveRoute();
            if (activeRoute) {
                // Получим протяженность маршрута.
                var length = route.getActiveRoute().properties.get("distance")
                print(length.value)
            }
        });*/
//print(Map.baloon.getData.value())  




