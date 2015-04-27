angular.module('starter.controllers')
.controller('VisualCtrl', function($scope, $stateParams, Visuals) {
  
  $scope.items = [
            {id:0,urlName:"sleep/cycle", name:"Sleep Cycle", yAxisLabel:"Phases", xAxisLabel:"Time", username:"mshrimal"},
            {id:1,urlName:"sleep/heart", name:"Resting Heart Rate", yAxisLabel:"beats/min", xAxisLabel:"Time", username:"mshrimal"},
            {id:2,urlName:"sleep/score", name:"Sleep Score", yAxisLabel:"Score [0-100]", xAxisLabel:"Time", username:"mshrimal"},
            {id:3,urlName:"bloodpressure",name:"Blood Pressure", yAxisLabel:"millimeters of mercury", xAxisLabel:"Time", username:"mshrimal"},
            {id:4, urlName:"iexpress/breathingrate",name: "Respiration Rate", yAxisLabel:"breaths/min", xAxisLabel:"Time", username:"archieag"},
            {id:5, urlName:"weight",name: "Weight over time", yAxisLabel:"Kgs", xAxisLabel:"Time", username:"mshrimal"},
            {id:6, urlName:"iexpress/heartrate",name: "Heart Rate", yAxisLabel:"beats/mins", xAxisLabel:"Time", username:"archieag"},
            {id:7, urlName:"stress",name: "Stress", yAxisLabel:"Stress Score", xAxisLabel:"Events", username:"mshrimal"},
            {id:8, urlName:"bloodoxygen",name: "Blood Oxygen", yAxisLabel:"Blood Oxygen %", xAxisLabel:"Time", username:"mshrimal"},
            {id:9, urlName:"wv",name: "Washroom visits", yAxisLabel:"# Night time washroom visits", xAxisLabel:"Time", username:"mshrimal"},
            {id:10, urlName:"iexpress/skintemperature",name: "Skin Temperature", yAxisLabel:"Degree", xAxisLabel:"Time", username:"archieag"}
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
    $scope.sleep.static.exit = 0;
    $scope.sleep.static.total = 0;
    $scope.sleep.static.latency = 0;
    $scope.sleep.static.res = 0;
    $scope.sleep.static.score = 0;
    
    if ($scope.vOption.menuSelect.id == 0) {
      $scope.sleepDisplay = true;
    }
    $scope.vOption.title.text = $scope.vOption.menuSelect.name+" Chart";
    $scope.vOption.chart.yAxis.axisLabel = $scope.vOption.menuSelect.yAxisLabel;
    $scope.vOption.chart.xAxis.axisLabel = $scope.vOption.menuSelect.xAxisLabel;

    var colorOptions = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f","#bcbd22","#17becf"];
    $scope.visuals = [];
    console.log("Before making the query call");
    $scope.visuals = Visuals.query({attr:$scope.vOption.menuSelect.urlName,sd:sd, ed:ed, username:$scope.vOption.menuSelect.username}, function(){  
      console.log("Inside the query call");
      console.log($scope.visuals);
      for (var i = 0; i < $scope.visuals.length; i++) {
        $scope.visuals[i]["color"] = colorOptions[i];
      };
    });
    $scope.sleep.exit = Visuals.static({attr:'sleep/exit',sd:sd, ed:ed, username:'mshrimal'}, function(){  
        for (var i = 0; i < $scope.sleep.exit[0].values.length; i++) {
          console.log($scope.sleep.exit[0].values[i]["y"]);
          $scope.sleep.static.exit += Math.abs($scope.sleep.exit[0].values[i]["y"]);
        };
    });
    $scope.sleep.total = Visuals.static({attr:'sleep/totalsleep',sd:sd, ed:ed, username:'mshrimal'}, function(){  
        for (var i = 0; i < $scope.sleep.total[0].values.length; i++) {
          console.log($scope.sleep.total[0].values[i]["y"]);
          $scope.sleep.static.total += $scope.sleep.total[0].values[i]["y"];
        };
    });
    $scope.sleep.latency = Visuals.static({attr:'sleep/latency',sd:sd, ed:ed, username:'mshrimal'}, function(){  
        console.log($scope.sleep.latency[0].values.length);
        for (var i = 0; i < $scope.sleep.latency[0].values.length; i++) {
          console.log($scope.sleep.latency[0].values[i]["y"]);
          $scope.sleep.static.latency += $scope.sleep.latency[0].values[i]["y"];
        };
        if ($scope.sleep.latency[0].values.length > 0) {
          $scope.sleep.static.latency = $scope.sleep.static.latency / $scope.sleep.latency[0].values.length;
        };
    });
    $scope.sleep.resp = Visuals.static({attr:'sleep/resp',sd:sd, ed:ed, username:'mshrimal'}, function(){  
        console.log($scope.sleep.resp[0].values.length);
        for (var i = 0; i < $scope.sleep.resp[0].values.length; i++) {
          console.log($scope.sleep.resp[0].values[i]["y"]);
          $scope.sleep.static.resp += $scope.sleep.resp[0].values[i]["y"];
        };
        if ($scope.sleep.resp[0].values.length > 0) {
          $scope.sleep.static.resp = $scope.sleep.static.resp / $scope.sleep.resp[0].values.length;
        }
        
    });
    $scope.sleep.score = Visuals.static({attr:'sleep/score',sd:sd, ed:ed, username:'mshrimal'}, function(){  
        console.log($scope.sleep.score[0].values.length);
        for (var i = 0; i < $scope.sleep.score[0].values.length; i++) {
          console.log($scope.sleep.score[0].values[i]["y"]);
          $scope.sleep.static.score += $scope.sleep.score[0].values[i]["y"];
        };
        if ($scope.sleep.score[0].values.length > 0) {
          $scope.sleep.static.score = $scope.sleep.static.score / $scope.sleep.score[0].values.length;
        }
        
    });
  }


  $scope.dayfn = function(date_v){
    //$scope.current = new moment();
    $scope.dayClass = "button button-calm";
    $scope.weekClass = "button button-light";
    $scope.monthClass = "button button-light";
    console.log("day fn called");
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
    //  console.log($scope.day.start.format("YYYY/M/D"));
    $scope.updateWithParams($scope.day.start.format("YYYY-MM-DD"), $scope.day.start.format("YYYY-MM-DD"));
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
  $scope.sleep = {
          exit : [],
          total: [],
          latency: [],
          resp: [],
          score: [],
          static: {
            exit: 0,
            total: 0,
            latency: 0,
            resp: 0,
            score: 0
          }
            };
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
                        //return d3.time.format("%I:%M %p %a %Y")(new Date(d*1000));
                        if ($scope.vOption.periodType == 0) {
                          return d3.time.format("%I:%M %p")(new Date(d*1000))  
                        }else{
                          return d3.time.format("%Y-%m-%d")(new Date(d*1000))  
                        }
                        
                        //return d3.format('.02f')(d);
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
            }
        };
        
        $scope.vOption.menuSelect = $scope.items[0];
        $scope.update();
        $scope.dayClass = "button button-calm";
        $scope.weekClass = "button button-light";
        $scope.monthClass = "button button-light";
        //$scope.dayfn(0);
})