import React, { useState } from 'react';
import { Card, Icon, Image } from 'semantic-ui-react';

const cardStyle = {
    boxShadow: '0px 4px 8px 0px rgba(0, 0, 0, 0.4)'
};

const imgStyle = {
    opacity: 0.8
}

const ImageCard = ({movieDetails, i}) => {
    const [hover, setHover] = useState(false);
    return (
        <Card style={(hover ? cardStyle : null)} onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}>
            <Image src={"https://image.tmdb.org/t/p/original" + movieDetails.poster_path} style={(hover ? imgStyle : null)} wrapped />
            <Card.Content>
                <Card.Header>{movieDetails.title}</Card.Header>
                <Card.Meta><span className="date">{movieDetails.release_date}</span></Card.Meta>
                <Card.Description>
                    {movieDetails.overview}
                </Card.Description>
            </Card.Content>
            <Card.Content extra>
                <Card.Description>
                    User Rating: {movieDetails.vote_average}
                </Card.Description>
            </Card.Content>
        </Card>
    );
};

export default ImageCard;