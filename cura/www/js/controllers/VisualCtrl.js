angular.module('starter.controllers')
.controller('VisualCtrl', function ($scope, $stateParams, Visuals) {

  $scope.items = [
            {id:0,urlName:"sleep/graph/2/cycle", name:"Sleep Cycle", yAxisLabel:"Phases"},
            {id:1,urlName:"rr", name:"Resting Heart Rate", yAxisLabel:"beats/min"},
            {id:2,urlName:"sleep/graph/2/", name:"Sleep Score", yAxisLabel:""},
            {id:3,urlName:"bp",name:"Blood Pressure", yAxisLabel:"bp level"},
            {id:4, urlName:"rr",name: "Respiration Rate", yAxisLabel:"rr level"},
            {id:5, urlName:"wgt",name: "Weight over time", yAxisLabel:"Lbs"},
            {id:6, urlName:"multi",name: "Heart Rate", yAxisLabel:"beats/mins"},
            {id:7, urlName:"stress",name: "Stress", yAxisLabel:"Stress Units"},
            {id:8, urlName:"skin",name: "Skin Temperature", yAxisLabel:"Degree"}
            ];
  
  //$scope.entries = Visuals.query({attr:"sleep",sd:"akshay", ed:"pushparaja"});
  
  $scope.update = function(){
    $scope.vOption.period.value = moment().format("M/D/YY");
    $scope.dayfn(0);
    //$scope.updateWithParams(0,0);
    /*$scope.vOption.title.text = $scope.vOption.menuSelect.name+" Chart";
    $scope.vOption.chart.yAxis.axisLabel = $scope.vOption.menuSelect.yAxisLabel;

    var colorOptions = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f","#bcbd22","#17becf"];
    $scope.visuals = [];

    $scope.visuals = Visuals.bp({attr:$scope.vOption.menuSelect.urlName,sd:"2013-01-29T00:00:00.000000Z", ed:"2013-01-30T00:00:00.000000Z"}, function(){  
      for (var i = 0; i < $scope.visuals.length; i++) {
        $scope.visuals[i]["color"] = colorOptions[i];
      };
    });*/ 
  }
  
  $scope.updateWithParams = function(sd,ed){
    
    $scope.sleepDisplay = false;
    
    if ($scope.vOption.menuSelect.id == 0) {
      $scope.sleepDisplay = true;
    }
    $scope.vOption.title.text = $scope.vOption.menuSelect.name+" Chart";
    $scope.vOption.chart.yAxis.axisLabel = $scope.vOption.menuSelect.yAxisLabel;

    var colorOptions = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f","#bcbd22","#17becf"];
    $scope.visuals = [];
    console.log("Hi");
    $scope.visuals = Visuals.query({attr:$scope.vOption.menuSelect.urlName,sd:sd, ed:ed}, function(){  
      console.log("Inside");
      for (var i = 0; i < $scope.visuals.length; i++) {
        $scope.visuals[i]["color"] = colorOptions[i];
      };
    }); 
  }


  $scope.dayfn = function(date_v){
    //$scope.current = new moment();
    $scope.dayClass = "button button-calm";
    $scope.weekClass = "button button-light";
    $scope.monthClass = "button button-light";
    console.log(date_v);
    $scope.vOption.periodType = 0;
    var temp = {start:0, end:0};
    if (date_v == 0) {
      temp = getDateRange(new moment(), "day");
      $scope.day.tracker = 0;
    }else{
      temp = getDateRange(date_v, "day");
    }
    
    $scope.day.start = temp.start;
    $scope.day.end = temp.end;
    console.log($scope.day.start.format("YYYY/M/D"));
    $scope.updateWithParams($scope.day.start.format("YYYY-MM-DD"), "");
    $scope.vOption.period.value = temp.start.format("M/D/YY");
  }
  
  $scope.weekfn = function(date_v){
    $scope.dayClass = "button button-light";
    $scope.weekClass = "button button-calm";
    $scope.monthClass = "button button-light";
    $scope.vOption.periodType = 1;
    var temp = {start:0, end:0};
    if (date_v == 0) {
      temp = getDateRange(new moment(), "week");
      $scope.day.tracker = 0;
    }else{
      temp = getDateRange(date_v, "week");
    }
    
    $scope.day.start = temp.start;
    $scope.day.end = temp.end;
    console.log($scope.day.start.format("YYYY/M/D")+" AP "+$scope.day.end.format("YYYY/M/D"));
    $scope.updateWithParams($scope.day.start.format("YYYY-MM-DD"), $scope.day.end.format("YYYY-MM-DD"));
    $scope.vOption.period.value = temp.start.format("M/D/YY")+" to "+temp.end.format("M/D/YY"); 
    //var now = moment().day(7);
    //var newStart = getFormatted(-7,0, );
    //console.log($scope.today.month()); 
    //console.log($scope.today.year()); 
    //console.log(getMonthDateRange($scope.today.year(), $scope.today.month()));
  }

  $scope.monthfn = function(){
    console.log("month");
    $scope.dayClass = "button button-light";
    $scope.weekClass = "button button-light";
    $scope.monthClass = "button button-calm";
    $scope.vOption.periodType = 2;
  }

  $scope.nextfn = function(){
    console.log("next");
    if ($scope.vOption.periodType == 0) {
      $scope.day.tracker++;
      console.log("Day tracker: "+$scope.day.tracker);
      var temp = moment().add($scope.day.tracker,'d');
      console.log(temp);
      $scope.dayfn(temp);
    }else if ($scope.vOption.periodType == 1) {
      $scope.week.tracker += 7;
      console.log("Week tracker: "+$scope.week.tracker);
      var temp = moment().add($scope.week.tracker,'d');
      console.log(temp);
      $scope.weekfn(temp);

    }else{

    }
    
  }

  $scope.prevfn = function(){
    console.log("prev");
    if ($scope.vOption.periodType == 0) {
      $scope.day.tracker--;
      console.log("day tracker: "+$scope.day.tracker);
      var temp = moment().add($scope.day.tracker,'d');
      console.log(temp);
      $scope.dayfn(temp);
    }else if ($scope.vOption.periodType == 1) {
      $scope.week.tracker -= 7;
      console.log("Week tracker: "+$scope.week.tracker);
      var temp = moment().add($scope.week.tracker,'d');
      console.log(temp);
      $scope.weekfn(temp);
    }else{
      
    }
        
  }

  function getMonthDateRange(year, month) {

    // month in moment is 0 based, so 9 is actually october, subtract 1 to compensate
    // array is 'year', 'month', 'day', etc
    var startDate = moment([year, month]);

    // Clone the value before .endOf()
    var endDate = moment(startDate).endOf('month');

    // just for demonstration:
    //console.log(startDate.toDate());
    //console.log(endDate.toDate());

    // make sure to call toDate() for plain JavaScript date type
    return { start: startDate, end: endDate };
  }

  function getDateRange(date_v, attr){
    var startDate = moment(date_v).startOf(attr);
    var endDate = moment(startDate).endOf(attr)
    return { start: startDate, end: endDate };
  }
  
  //$scope.curr = moment();
  /*$scope.day = getDateRange($scope.current, "day");
  $scope.day.tracker = 0;
  $scope.week = getDateRange($scope.curr);
  $scope.week.tracker = 0;
  $scope.month = getMonthDateRange($scope.current.year(), $scope.current.month());
  $scope.month.tracker = 0;*/
  $scope.day = {
            start: 0,
            end: 0,
            tracker:0
            };
  $scope.week = {
            start: 0,
            end: 0,
            tracker:0
            };
  $scope.month = {
            start: 0,
            end: 0,
            tracker:0
            };
  $scope.visuals = [{values:$scope.entries, key:'Test Wave', color: '#ff7f0e'}];
  $scope.vOption = {
            chart: {
                type: 'lineChart',
                height: 450,
                margin : {
                    top: 20,
                    right: 20,
                    bottom: 40,
                    left: 55
                },
                x: function(d){ return d.x; },
                y: function(d){ return d.y; },
                useInteractiveGuideline: true,
                dispatch: {
                    /*stateChange: function(e){ console.log("stateChange"); },
                    changeState: function(e){ console.log("changeState"); },
                    tooltipShow: function(e){ console.log("tooltipShow"); },
                    tooltipHide: function(e){ console.log("tooltipHide"); }*/
                },
                xAxis: {
                    axisLabel: 'Time (ms)',
                    tickFormat: function(d){
                        return d3.time.format("%I:%M %p %a %Y")(new Date(d*1000))
                    }
                },
                yAxis: {
                    axisLabel: 'Voltage (v)',
                    tickFormat: function(d){
                        return d3.format('.02f')(d);
                    },
                    axisLabelDistance: 30
                },
                callback: function(chart){
                    console.log("!!! lineChart callback !!!");              
                }
            },
            period:{ value: new Date()},
            periodType: 0, //0 is day, 1 is week and 2 is month
            title: {
                enable: false,
                text: 'Line Chart Sample 1'
            }/*,
            subtitle: {
                enable: true,
                text: 'Subtitle for simple line chart. Lorem ipsum dolor sit amet, at eam blandit sadipscing, vim adhuc sanctus disputando ex, cu usu affert alienum urbanitas.',
                css: {
                    'text-align': 'center',
                    'margin': '10px 13px 0px 7px'
                }
            },
            caption: {
                enable: true,
                html: '<b>Figure 1.</b> Lorem ipsum dolor sit amet, at eam blandit sadipscing, <span style="text-decoration: underline;">vim adhuc sanctus disputando ex</span>, cu usu affert alienum urbanitas. <i>Cum in purto erat, mea ne nominavi persecuti reformidans.</i> Docendi blandit abhorreant ea has, minim tantas alterum pro eu. <span style="color: darkred;">Exerci graeci ad vix, elit tacimates ea duo</span>. Id mel eruditi fuisset. Stet vidit patrioque in pro, eum ex veri verterem abhorreant, id unum oportere intellegam nec<sup>',
                css: {
                    'text-align': 'justify',
                    'margin': '10px 13px 0px 7px'
                }
            }*/
        };
        
        $scope.vOption.menuSelect = $scope.items[0];
        $scope.update();
        $scope.dayClass = "button button-calm";
        $scope.weekClass = "button button-light";
        $scope.monthClass = "button button-light";
        //$scope.dayfn(0);

})


