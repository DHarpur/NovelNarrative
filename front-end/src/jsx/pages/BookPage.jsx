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

const BookPage = () => {
    return(
        <Fragment>
            <Header textAlign={'center'} style={titleStyle} as="h1">
                Recommended Books
            </Header>
            <div style={segmentStyle}>
                <Header attached="top" style={titleStyle}>Trending Movies</Header>
                <Segment inverted attached="bottom">
                    <ImageGallery book maxIndex={15}/>
                </Segment>
            </div>
        </Fragment>
    );  
};

export default BookPage;