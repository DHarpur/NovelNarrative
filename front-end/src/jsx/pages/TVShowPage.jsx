import React, { Fragment } from 'react';
import { Header } from 'semantic-ui-react';
import ImageGallery from '../ImageGallery';

const TVShowPage = () => {
    return(
        <Fragment>
            <Header as='h1' >
                TV Show Page
            </Header>
            <ImageGallery />
        </Fragment>
    );
};

export default TVShowPage;