import React, { Fragment } from 'react';
import { Navbar, Nav } from 'react-bootstrap';

const Navigation = () => {
    return (
        <Fragment>
            <Navbar bg="primary" variant="dark" >
                    <Navbar.Brand href='#home'>
                        NovelNarrative
                    </Navbar.Brand>
                    <Nav className="mr-auto" >
                        <Nav.Link href="#movies">Movies</Nav.Link>
                        <Nav.Link href="#tvshows">TV Shows</Nav.Link>
                        <Nav.Link href="#books">Books</Nav.Link>
                    </Nav>
            </Navbar>
        </Fragment>
    );
};

export default Navigation;