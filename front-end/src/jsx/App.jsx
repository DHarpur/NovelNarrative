import React, { Component, Fragment } from 'react';
import { Navbar, Nav, Button, Form } from 'react-bootstrap';
import { BrowserRouter, Switch, Route, Link } from 'react-router-dom';
import { LinkContainer } from 'react-router-bootstrap';
import ImageGallery from './ImageGallery';

class AppComponent extends Component {
    render() {
        return (
            <BrowserRouter>
                <div>
                    <Navbar bg="primary" variant="dark" >
                        <Navbar.Brand as={Link} to=''>
                            NovelNarrative
                        </Navbar.Brand>
                        <Nav className="mr-auto" >
                            <LinkContainer to="#movies">
                                <Nav.Link >Movies</Nav.Link>
                            </LinkContainer>
                            <LinkContainer to="#tvshows">
                                <Nav.Link>TV Shows</Nav.Link>
                            </LinkContainer>
                            <LinkContainer to="#books">
                                <Nav.Link>Books</Nav.Link>
                            </LinkContainer>
                        </Nav>
                        <Form inline>
                            <Button variant="dark" style={{marginRight: '5px'}}>Login</Button>
                            <Button variant="dark">Register</Button>
                        </Form>
                    </Navbar>
                    <div>
                            <Route path='/' component={AppComponent} />
                    </div>
                </div>
                <ImageGallery />
            </BrowserRouter>
        );
    }
}

export default AppComponent;