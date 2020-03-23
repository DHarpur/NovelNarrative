import React, { Fragment } from 'react';
import { Header } from 'semantic-ui-react';
import ImageGallery from '../ImageGallery';

const BookPage = () => {
    return (
        <Fragment>
            <Header as="h1">
                Book Page
            </Header>
            <ImageGallery />
        </Fragment>
    );
};

export default BookPage;