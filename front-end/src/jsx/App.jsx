import React, { Component, Fragment } from 'react';
import Navigation from './Navigation';
import ImageGallery from './ImageGallery';

class AppComponent extends Component {
    render() {
        return (
            <Fragment>
                <Navigation />
                <ImageGallery />
            </Fragment>
        );
    }
}

export default AppComponent;