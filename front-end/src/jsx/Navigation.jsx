import React, { Fragment, Component } from 'react';
import { Button, Form, Menu } from 'semantic-ui-react';
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
                <Menu>
                    <Menu.Item header as={Link} to='/'>
                        NovelNarrative
                    </Menu.Item>
                    <Menu.Item as={Link} to="movies">Movies</Menu.Item>
                    <Menu.Item as={Link} to="tvshows">TV Shows</Menu.Item>
                    <Menu.Item as={Link} to="books">Books</Menu.Item>
                    <Menu.Menu position={"right"}>
                        <Menu.Item href='/login'>
                            <Button primary>Login</Button>
                        </Menu.Item>
                        <Menu.Item  href='/login'>
                            <Button>Register</Button>
                        </Menu.Item>
                    </Menu.Menu>
                </Menu>
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