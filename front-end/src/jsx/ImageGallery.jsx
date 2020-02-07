import React from "react";
import ImageCard from "./ImageCard";
import { Container, Row, Col } from 'react-bootstrap';
import { Component } from "react";

class ImageGallery extends Component {
    render() {
        return (
            <Container fluid style={{marginTop: '20px'}}>
                <Row className="justify-content-md-center" >
                    <Col md={2}>
                        <ImageCard />
                    </Col>
                    <Col md={2}>
                        <ImageCard />
                    </Col>
                    <Col md={2}>
                        <ImageCard />
                    </Col>
                    <Col md={2}>
                        <ImageCard />
                    </Col>
                    <Col md={2}>
                        <ImageCard />
                    </Col>
                    <Col md={2}>
                        <ImageCard />
                    </Col>
                </Row>
            </Container>
        );
    }
};

export default ImageGallery;