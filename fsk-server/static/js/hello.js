function Hello($scope, $http) {
    $http.get('http://localhost:5000/greeting').
        success(function(data) {
            $scope.greeting = data;
        });
}
