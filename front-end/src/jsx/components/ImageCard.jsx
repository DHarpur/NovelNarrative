import React, { useState } from 'react';
import { Card, Icon, Image } from 'semantic-ui-react';

const cardStyle = {
    boxShadow: '0px 4px 8px 0px rgba(0, 0, 0, 0.4)'
};

const imgStyle = {
    opacity: 0.8
}

const descriptionExpanded = {
    textOverflow: 'ellipsis',
    overflow: 'hidden',
    whiteSpace: 'pre-wrap'
}

const descriptionSmall = {
    textOverflow: 'ellipsis',
    overflow: 'hidden',
    whiteSpace: 'pre'
}

const ImageCard = ({itemDetails, i, movie, book}) => {
    const [hover, setHover] = useState(false);
    const [expanded, setExpanded] = useState(false)
    return (
        (movie) ?
        <Card style={(hover ? cardStyle : null)} onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)} onClick={() => setExpanded(!expanded)}>
            <Image src={"https://image.tmdb.org/t/p/original" + itemDetails.poster_path} style={(hover ? imgStyle : null)} wrapped />
            <Card.Content>
                <Card.Header>{itemDetails.title}</Card.Header>
                <Card.Meta><span className="date">{itemDetails.release_date}</span></Card.Meta>
                <Card.Description style={expanded ? descriptionExpanded : descriptionSmall}>
                    {itemDetails.overview}
                </Card.Description>
            </Card.Content>
            <Card.Content extra>
                <Card.Description>
                    User Rating: {itemDetails.vote_average}
                </Card.Description>
            </Card.Content>
        </Card>
        :
        <Card style={(hover ? cardStyle : null)} onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)} onClick={() => setExpanded(!expanded)}>
            <Image src={itemDetails.image} style={(hover ? imgStyle : null)} wrapped />
            <Card.Content>
                <Card.Header>{itemDetails.title}</Card.Header>
                <Card.Meta><span className="date">{itemDetails.author}</span></Card.Meta>
            </Card.Content>
        </Card>
    );
};

export default ImageCard;