import React from 'react'
import {Grid, Col, Row} from 'react-bootstrap'

const Album = React.createClass({

  render() {

    return (
        <Grid>
        <Row>
          <Col md={10} sm={10}>
            HI!
          </Col>
          <Col md={2} sm={2}>
            YO!
          </Col>
        </Row>
      </Grid>
        )                   

}});


export default Album;