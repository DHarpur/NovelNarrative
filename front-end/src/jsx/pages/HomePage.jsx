import React, { Fragment } from 'react';
import { Header } from 'semantic-ui-react';
import ImageGallery from '../ImageGallery';
import Navigation from '../Navigation';

const MoviePage = () => {
    return(
        <Fragment>
            <Header as="h1">
                Home Page
            </Header>
            <ImageGallery />
        </Fragment>
    );
}

export default MoviePage;