// var React = require('react')
// var ReactDOM = require('react-dom')

// var Hello = React.createClass ({
//     render: function() {
//         return (
//             <h1>
//             Hello, React!
//             </h1>
//         )
//     }
// })

// ReactDOM.render(<Hello />, document.getElementById('myapp'));



// 'use strict';

// import React from 'react'
// import {ProgressBar, Grid} from 'react-bootstrap'
// import Reflux from 'reflux'
// import importExpressions from './importExpressions'
// //import Album from './components/album'
// //import Actions from './actions'


// const MainController = React.createClass({
//   mixins: [Reflux.connect(importExpressions, 'expressions')],

//   render() {
//     if (! this.state.expressions.isHydrated) {
//       // Store hasn't been hydrated yet so we display a progress bar
//       return <Grid><ProgressBar active now={100} /></Grid>
//     }
//     else {
//       // The store has data so we can display the album
//       return (
//         <showData
//          index_data={this.state.expressions.index_data}/>
//       )
//     }
//   }

// });


// function initPreRendered(div) {
//   console.log('IN INIT PRE RENDER');
//   importExpressions.fetchData().then(()=>{
//     React.render(<MainController />, div);
//   });
// }


// var div = document.getElementById('myapp');
//     initPreRendered(div);
// }














