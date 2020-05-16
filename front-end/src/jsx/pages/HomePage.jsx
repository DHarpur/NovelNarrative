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

const HomePage = () => {
    return (
        <Fragment>
            <Header textAlign={'center'} style={titleStyle} as="h1">
                Home Page
            </Header>
            <div style={segmentStyle}>
                <Header attached="top" style={titleStyle}>Trending Movies</Header>
                <Segment inverted attached="bottom">
                    <ImageGallery movie maxIndex={5}/>
                </Segment>
            </div>
            <div style={segmentStyle}>
                <Header style={titleStyle} attached="top">Trending TV Shows</Header>
                <Segment inverted attached="bottom">
                    <ImageGallery tvshow maxIndex={5}/>
                </Segment>
            </div>
        </Fragment>
    );
}

export default HomePage;