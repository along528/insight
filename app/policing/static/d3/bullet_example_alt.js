
var margin = {top: 5, right: 10, bottom: 20, left: 300},
    //width = 960 - margin.left - margin.right,
    width = 1100 - margin.left - margin.right,
    height = 60 - margin.top - margin.bottom;

var chart = d3.bullet()
    .width(width)
    .height(height);

var json_file = document.getElementById("helper").getAttribute("data-name");
//d3.json("../static/d3/bullets.json", function(error, data) {
d3.json("../static/d3/json_alt/"+json_file, function(error, data) {
  if (error) throw error;

  var svg = d3.select("#features").selectAll("svg")
      .data(data)
    .enter().append("svg")
      .attr("class", "bullet")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
      .call(chart);

  var title = svg.append("g")
      .style("text-anchor", "end")
      .attr("transform", "translate(-6," + height / 2 + ")");

  title.append("text")
      .attr("class", "title")
      .text(function(d) { return d.title; });

  title.append("text")
      .attr("class", "subtitle")
      .attr("dy", "1em")
      .text(function(d) { return d.subtitle; });

 //svg.datum(all_dist).call(chart.duration(1)); // TODO automatic transition
 //svg.datum(dummy).call(chart.duration(1)); // TODO automatic transition

  d3.select("#button1").on("click", function() {
    //svg.datum(all_dist).call(chart.duration(1500)); // TODO automatic transition
    svg.datum(all_dist).call(chart.duration(2000)); // TODO automatic transition
  });
  d3.select("#button2").on("click", function() {
    //svg.datum(cat_dist).call(chart.duration(1500)); // TODO automatic transition
    svg.datum(cat_dist).call(chart.duration(2000)); // TODO automatic transition
  });
});

function dummy(d) {
  d.ranges_tmp = d.dummy 
  d.markers_tmp = d.dummy
  d.markers_dist_tmp = d.dummy
  d.measures_tmp = d.dummy
  return d;
}
function all_dist(d) {
  d.ranges_tmp = d.ranges 
  //d.ranges_tmp = d.dummy 
  d.markers_tmp = d.markers
  d.markers_dist_tmp = d.markers_all
  d.measures_tmp = d.dummy
  return d;
}

function cat_dist(d) {
  d.ranges_tmp = d.measures 
  //d.ranges_tmp = d.dummy 
  d.markers_tmp = d.markers
  d.markers_dist_tmp = d.markers_cat
  d.measures_tmp = d.dummy
  return d;
}

function randomizer(d) {
  var k = d3.max(d.ranges) * .2;
  return function(d) {
    return Math.max(0, d + k * (Math.random() - .5));
  };
}


