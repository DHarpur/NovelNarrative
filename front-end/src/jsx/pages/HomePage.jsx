import React, { Fragment } from 'react';
import ImageGallery from '../ImageGallery';
import Navigation from '../Navigation';

const MoviePage = () => {
    return(
        <Fragment>
            <div>
                <h2>Home Page</h2>
            </div>
            <ImageGallery />
        </Fragment>
    );
}

export default MoviePage;