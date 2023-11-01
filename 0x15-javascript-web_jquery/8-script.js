$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (movieData) {
      const movies = movieData.results;
      for (const movie of movies) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      }
    }
  });
});
