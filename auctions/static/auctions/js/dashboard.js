document.addEventListener("DOMContentLoaded", function () {
  var ctx = document.getElementById("barChart").getContext("2d");
  var barChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["January", "February", "March", "April", "May", "June"],
      datasets: [
        {
          label: "Sample Data",
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });

  var ctx2 = document.getElementById("lineGraph").getContext("2d");
  var lineGraph = new Chart(ctx2, {
    type: "line",
    data: {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
      datasets: [
        {
          label: "Sample Line Data",
          data: [12, 19, 3, 5, 2, 3],
          borderColor: "rgba(255, 99, 132, 1)",
          borderWidth: 2,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });

  // Pir Chart Initialization
  var ctxPie = document.getElementById("pieChart").getContext("2d");
  var pieChart = new Chart(ctxPie, {
      type: "pie",
      data: {
          labels: ["Data1", "Data2", "Data3"],
          datasets: [{
              data: [300, 50, 100],
              backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
              hoverBackgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"]
          }]
      },
      options: {
          responsive: true
      }
  });


  // Radar Chart Initialization
  var ctxRadar = document.getElementById('radarChart').getContext('2d');
  var radarChart = new Chart(ctxRadar, {
      type: 'radar',
      data: {
          labels: ['Eating', 'Drinking', 'Sleeping', 'Designing', 'Coding', 'Cycling', 'Running'],
          datasets: [{
              label: 'My First Dataset',
              data: [65, 59, 90, 81, 56, 55, 40],
              fill: true,
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgb(255, 99, 132)',
              pointBackgroundColor: 'rgb(255, 99, 132)',
              pointBorderColor: '#fff',
              pointHoverBackgroundColor: '#fff',
              pointHoverBorderColor: 'rgb(255, 99, 132)'
          }]
      },
      options: {
          elements: {
              line: {
                  borderWidth: 3
              }
          }
      }
  });


  // Polar Chart Initialization
  var ctxPolar = document.getElementById('polarChart').getContext('2d');
  var polarChart = new Chart(ctxPolar, {
      type: 'polarArea',
      data: {
          labels: ['Red', 'Green', 'Yellow', 'Grey', 'Blue'],
          datasets: [{
              label: 'My First Dataset',
              data: [11, 16, 7, 3, 14],
              backgroundColor: ['rgb(255, 99, 132)', 'rgb(75, 192, 192)', 'rgb(255, 205, 86)', 'rgb(201, 203, 207)', 'rgb(54, 162, 235)']
          }]
      },
      options: {
          responsive: true
      }
  });

  // Bubble Chart Initialization
  var ctxBubble = document.getElementById('bubbleChart').getContext('2d');
  var bubbleChart = new Chart(ctxBubble, {
      type: 'bubble',
      data: {
          datasets: [{
              label: 'John',
              data: [{
                  x: 3,
                  y: 7,
                  r: 10
              }],
              backgroundColor: 'rgb(255, 99, 132)'
          }, {
              label: 'Peter',
              data: [{
                  x: 5,
                  y: 7,
                  r: 10
              }],
              backgroundColor: 'rgb(54, 162, 235)'
          }, {
              label: 'Donald',
              data: [{
                  x: 7,
                  y: 7,
                  r: 10
              }],
              backgroundColor: 'rgb(255, 205, 86)'
          }, {
              label: 'Linus',
              data: [{
                  x: 1,
                  y: 7,
                  r: 10
              }],
              backgroundColor: 'rgb(75, 192, 192)'
          }]
      },
      options: {
          responsive: true,
          plugins: {
              legend: {
                  position: 'top',
              },
              title: {
                  display: true,
                  text: 'Chart.js Bubble Chart'
              }
          }
      }
  });


  // Scatter Chart Initialization
  var ctxScatter = document.getElementById('scatterChart').getContext('2d');
  var scatterChart = new Chart(ctxScatter, {
      type: 'scatter',
      data: {
          datasets: [{
              label: 'Scatter Dataset',
              data: [{
                  x: -10,
                  y: 0
              }, {
                  x: 0,
                  y: 10
              }, {
                  x: 10,
                  y: 5
              }]
          }]
      },
      options: {
          scales: {
              x: {
                  type: 'linear',
                  position: 'bottom'
              }
          }
      }
  });

  // Area Chart Initialization
  var ctxArea = document.getElementById('areaChart').getContext('2d');
  var areaChart = new Chart(ctxArea, {
      type: 'line',
      data: {
          labels: ['January', 'February', 'March', 'April', 'May', 'June'],
          datasets: [{
              label: 'Dataset 1',
              data: [0, 10, 5, 2, 20, 30],
              borderColor: 'rgb(255, 99, 132)',
              backgroundColor: 'rgba(255, 99, 132, 0.5)',
          }, {
              label: 'Dataset 2',
              data: [0, 5, 10, 20, 30, 45],
              borderColor: 'rgb(54, 162, 235)',
              backgroundColor: 'rgba(54, 162, 235, 0.5)',
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });


  // Doughnut Chart Initialization
  var ctxDoughnut = document.getElementById('doughnutChart').getContext('2d');
  var doughnutChart = new Chart(ctxDoughnut, {
      type: 'doughnut',
      data: {
          labels: ['Red', 'Blue', 'Yellow'],
          datasets: [{
              label: 'My First Dataset',
              data: [300, 50, 100],
              backgroundColor: ['rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 205, 86)'],
              hoverOffset: 4
          }]
      },
      options: {
          responsive: true
      }
  });

});
