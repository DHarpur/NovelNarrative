import React, { Fragment, Component } from 'react';
import AppComponent from './App';
import { Navbar, Nav, Button, Form } from 'react-bootstrap';
import { Switch, Route, Link } from 'react-router-dom';
import { LinkContainer } from 'react-router-bootstrap';

class Navigation extends Component {
    render() {
        return (
            <div>
                <Navbar bg="primary" variant="dark" >
                        <Navbar.Brand as={Link} to='/'>
                            NovelNarrative
                        </Navbar.Brand>
                        <Nav className="mr-auto" >
                            <LinkContainer to="#movies">
                                <Nav.Link >Movies</Nav.Link>
                            </LinkContainer>
                            <Nav.Link as={Link} to="#tvshows">TV Shows</Nav.Link>
                            <Nav.Link as={Link} to="#books">Books</Nav.Link>
                        </Nav>
                        <Form inline>
                            <Button variant="dark" style={{marginRight: '5px'}}>Login</Button>
                            <Button variant="dark">Register</Button>
                        </Form>
                </Navbar>
                <div>
                    <Switch>
                        <Route exact path='/' component={AppComponent} />
                        <Route render={function () {
                            return <p>Not found</p>
                        }} />
                    </Switch>
                </div>
            </div>
        );
    };
}

export default Navigation;