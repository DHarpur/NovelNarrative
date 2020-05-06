import React, { Fragment } from 'react';
import { Header, Segment } from 'semantic-ui-react';

import ImageGallery from '../components/ImageGallery';

const titleStyle = {
    paddingTop: 20,
}

const segmentStyle = {
    width: '75%',
    margin: 'auto', 
    paddingBottom: 50
}

const MoviePage = () => {
    return(
        <Fragment>
            <Header textAlign={'center'} style={titleStyle} as="h1">
                Movie Page
            </Header>
            <div style={segmentStyle}>
                <Header attached="top" style={titleStyle}>Trending Movies</Header>
                <Segment inverted attached="bottom">
                    <ImageGallery movie maxIndex={15}/>
                </Segment>
            </div>
        </Fragment>
    );  
};

export default MoviePage;