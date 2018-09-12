
// Form Graph
const createGraph = (data) => {
  // set the dimensions and margins of the graph
  let margin = { top: 20, right: 20, bottom: 30, left: 50 },
    width = 750 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

  // parse the date / time
  let parseTime = d3.timeParse("%m/%d/%Y");

  // set the ranges
  let x = d3.scaleTime().range([0, width]);
  let y = d3.scaleLinear().range([height, 0]);

  // gridlines in x axis function
  function make_x_gridlines() {
    return d3.axisBottom(x)
      .ticks(12)
  }

  // gridlines in y axis function
  function make_y_gridlines() {
    return d3.axisLeft(y)
      .ticks(33)
  }

  // define the line
  let valueline = d3.line()
    .x(d => x(d.date))
    .y(d => y(d.rank))

  // append the svg obgect to the body of the page
  // appends a 'group' element to 'svg'
  // moves the 'group' element to the top left margin
  let svg = d3.select("#graphed").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
      "translate(" + margin.left + "," + margin.top + ")");


  // Scale the range of the data
  x.domain(d3.extent(data, function (d) { return d.date; }));
  y.domain([0, d3.max(data, function (d) { return d.rank; })]);


  // add the X gridlines
  svg.append("g")
    .attr("class", "grid")
    .attr("transform", "translate(0," + height + ")")
    .call(make_x_gridlines()
      .tickSize(-height)
      .tickFormat("")
    )

  // add the Y gridlines
  svg.append("g")
    .attr("class", "grid")
    .call(make_y_gridlines()
      .tickSize(-width)
      .tickFormat("")
    )

  // Add the valueline path.
  svg.append("path")
    .data([data])
    .attr("class", "line")
    .attr("d", valueline);

  // Add the X Axis
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  svg.append("text")
    .attr("transform", "translate(300, 390)")
    .text("Race Date");


  // Add the Y Axis
  svg.append("g")
    .call(d3.axisLeft(y));
  svg.append("text")
    .attr("transform", "translate(-25, -10)")
    .text("Finishing Position");
}


// Select Driver from list in aside

const makeSelection = driverId => {
  let data = [];
  let selectedDriver = driverId.id;
  // Check if there is already a driver selected
  let driverSelected = document.getElementsByClassName('selected-driver')[0] 
    ? document.getElementsByClassName('selected-driver')[0]
    : null; 

  // Clear old graph on new selection
  $('#graphed').empty();

  // Clear old selected driver and set new one
  if (driverSelected) {
    driverSelected.setAttribute('class', '');
  }
  driverId.setAttribute('class', 'selected-driver');
}
// Get Driver Id from selector and display graph
const getId = (driverId) => {
  let data = [];
  let selectedDriver = driverId[driverId.selectedIndex].id;
  $('#graphed').empty();

  for (let i = 0; i < driverInfo.length; i++) {
    if (selectedDriver == driverInfo[i].driver) {
      raceData.forEach((raceInfo) => {
        let position = driverInfo[i].position
        if (raceInfo.id === driverInfo[i].race) {
          let year = parseInt(raceInfo.start_time.substring(0, 4));
          let month = parseInt(raceInfo.start_time.substring(5, 7));
          let day = parseInt(raceInfo.start_time.substring(8, 10));
          let startDate = month + '/' + day + '/' + year;
          let parseTime = d3.timeParse("%m/%d/%Y");
          startDate = parseTime(startDate);
          data.push({ 'date': startDate, 'rank': position });
        }
      })
      data.forEach(d => d.rank =+ d.rank);
    };
  }
  createGraph(data);
}
