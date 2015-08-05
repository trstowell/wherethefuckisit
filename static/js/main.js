var app = angular.module("wherethefuckisit", ['ui.bootstrap','ngRoute', 'ngDialog']);

app.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
}]);

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

app.config(['ngDialogProvider', function (ngDialogProvider) {
    ngDialogProvider.setDefaults({
        className: 'ngdialog-theme-default',
        showClose: true,
        closeByDocument: false,
        closeByEscape: true,
    });
}]);

app.config( function($routeProvider, $locationProvider) {
     $routeProvider.
         when('/', {
             templateUrl: '/static/partials/send.html',
             controller: 'SendController'
         }).
         otherwise({
             redirectTo: '/'
         });

         $locationProvider.html5Mode(true);

});

app.controller("MainController", function ($scope, ngDialog) {

});

app.controller("SendController", function($scope, $http, ngDialog){

    $scope.callData = {};

    $scope.call = function(){
        $scope.callData.toFormatted = "+1 (".concat($scope.callData.to.slice(0,3)).concat(")")
            .concat(" - ").concat($scope.callData.to.slice(3,6))
            .concat(" - ").concat($scope.callData.to.slice(6,11));

        console.log($scope.callData.toFormatted);
        console.log("Calling: ".concat($scope.callData.to));

        $http.get("http://127.0.0.1:6969/call/".concat($scope.callData.to));

        $scope.openDialog();

    };

    $scope.text = function(){
    };

    $scope.openDialog = function () {
        ngDialog.open({
            template: '/static/partials/callDialog.html',
            controller: 'CallController',
            scope: $scope
        });
    }
});

app.controller("CallController", function ($scope, ngDialog) {
    console.log("Inside: ".concat($scope.callData.toFormatted));

    $scope.closeAllDialogsPls = function ( ){
        ngDialog.closeAll();
    }

});
