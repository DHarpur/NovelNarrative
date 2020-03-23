import React, { Fragment } from 'react';
import { Header } from 'semantic-ui-react';

import ImageGallery from '../ImageGallery';

const headerStyle = {
    paddingLeft: 50,
}

const MoviePage = () => {
    return(
        <Fragment>
            <Header as='h1' style={headerStyle}>
                Movie Page
            </Header>
            <ImageGallery />
        </Fragment>
    );  
};

export default MoviePage;