import React, { Fragment, Component } from 'react';
import { Navbar, Nav, Button, Form } from 'react-bootstrap';
import { Switch, Route, Link } from 'react-router-dom';
import MoviePage from './pages/MoviePage';
import HomePage from './pages/HomePage';
import TVShowPage from './pages/TVShowPage';
import BookPage from './pages/BookPage';
import LoginPage from './pages/LoginPage';

class Navigation extends Component {
    render() {
        return (
            <div>
                <Navbar bg="primary" variant="dark" >
                    <Navbar.Brand as={Link} to='/'>
                        NovelNarrative
                    </Navbar.Brand>
                    <Nav className="mr-auto" >
                        <Nav.Link as={Link} to="movies">Movies</Nav.Link>
                        <Nav.Link as={Link} to="tvshows">TV Shows</Nav.Link>
                        <Nav.Link as={Link} to="books">Books</Nav.Link>
                    </Nav>
                    <Form inline>
                        <Button variant="dark" style={{marginRight: '5px'}} href='/login'>Login</Button>
                        <Button variant="dark" href='/login'>Register</Button>
                    </Form>
                </Navbar>
                <div>
                    <Switch>
                        <Route exact path='/' component={HomePage} />
                        <Route path='/movies' component={MoviePage} />
                        <Route path='/tvshows' component={TVShowPage} />
                        <Route path='/books' component={BookPage} />
                        <Route path='/login' component={LoginPage} />
                        <Route render={function () {
                            return <p>Not found</p>
                        }} />
                    </Switch>
                </div>
            </div>
        );
    };
};

export default Navigation;