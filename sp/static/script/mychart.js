const ctx = document.getElementById('myChart');
const earnings = document.getElementById('earnings');

new Chart(ctx, {
  type: 'polarArea',
  data: {
    labels: ['Red', 'Blue', 'Yellow'],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3],
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
  }
});

new Chart(earnings, {
    type: 'line',
    data: {
      labels: ['January', 'February', 'March', 'April' ,'May', 'June'],
      datasets: [{
        label: 'Earnings',
        data: [65, 59, 80, 81, 56, 55, 40],
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }]
    },
    options: {
      responsive: true,
    }
  });

