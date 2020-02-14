import React, { useState } from 'react';
import { Card } from 'react-bootstrap';
import image from '../images/BladeRunner2049.jpg';

const cardStyle = {
    boxShadow: '0px 4px 8px 0px rgba(0, 0, 0, 0.2)'
};

const imgStyle = {
    opacity: 0.8
}

const ImageCard = () => {
    const [hover, setHover] = useState(false);
    return (
        <Card style={(hover ? cardStyle : null)} onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}>
            <Card.Img variant='top' src={image} style={(hover ? imgStyle : null)} />
            <Card.Body>
                <Card.Title>BladeRunner 2049</Card.Title>
                <Card.Text>
                    K, an officer with the Los Angeles Police Department, unearths a secret that could cause chaos. 
                    He goes in search of a former blade runner who has been missing for three decades.
                </Card.Text>
            </Card.Body>
        </Card>
    );
};

export default ImageCard;