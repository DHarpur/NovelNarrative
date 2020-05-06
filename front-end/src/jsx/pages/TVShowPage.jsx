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

const TVShowPage = () => {
    return(
        <Fragment>
            <Header textAlign={'center'} style={titleStyle} as="h1">
                TV Show Page
            </Header>
            <div style={segmentStyle}>
                <Header style={titleStyle} attached="top">Trending TV Shows</Header>
                <Segment inverted attached="bottom">
                    <ImageGallery tvshow maxIndex={15}/>
                </Segment>
            </div>
        </Fragment>
    );
};

export default TVShowPage;