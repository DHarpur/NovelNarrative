import React from 'react';
import { Menu, Button } from 'semantic-ui-react';
import { Route, Switch, Link } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomePage';
import MoviePage from './pages/MoviePage';
import TVShowPage from './pages/TVShowPage';
import BookPage from './pages/BookPage';
import RegisterPage from './pages/RegisterPage';
import LogoutPopup from './components/LogoutPopup';

class Navigation extends React.Component {
    constructor() {
        super();
        this.state = { 
            token: '',
            user: {}
        }
    }

    updateToken = (user) => {
        const authToken = localStorage.getItem('authToken');
        this.setState({token: authToken, user: user});
    }

    render() {
        const { token } = this.state;
        return (
            token ? 
            <React.Fragment>
                <Menu stackable>
                    <Menu.Item header as={Link} to='/'>
                        NovelNarrative
                    </Menu.Item>
                    <Menu.Item as={Link} to='/movies'>
                        Movies
                    </Menu.Item>
                    <Menu.Item as={Link} to='/tvshows'>
                        TV Shows
                    </Menu.Item>
                    <Menu.Item as={Link} to='/books'>
                        Books
                    </Menu.Item>
                    <Menu.Menu position={"right"}>
                        <Menu.Item>
                            <LogoutPopup token={token} />
                        </Menu.Item>
                    </Menu.Menu>
                </Menu>
                <React.Fragment>
                    <Switch>
                        <Route exact path='/' component={HomePage} />
                        <Route path='/movies' component={MoviePage} />
                        <Route path='/tvshows' component={TVShowPage} />
                        <Route path='/books' component={BookPage} />
                    </Switch>
                </React.Fragment>
            </React.Fragment>
            :
            <React.Fragment>
                <Menu stackable>
                    <Menu.Item header as={Link} to='/'>
                        NovelNarrative
                    </Menu.Item>
                    <Menu.Item as={Link} to='/movies'>
                        Movies
                    </Menu.Item>
                    <Menu.Item as={Link} to='/tvshows'>
                        TV Shows
                    </Menu.Item>
                    <Menu.Item as={Link} to='/books'>
                        Books
                    </Menu.Item>
                    <Menu.Menu position={"right"}>
                        <Menu.Item href='/login'>
                            <Button primary>Login</Button>
                        </Menu.Item>
                        <Menu.Item  href='/register'>
                            <Button>Register</Button>
                        </Menu.Item>
                    </Menu.Menu>
                </Menu>
                <React.Fragment>
                    <Switch>
                        <Route exact path='/' component={HomePage} />
                        <Route path='/movies' component={MoviePage} />
                        <Route path='/tvshows' component={TVShowPage} />
                        <Route path='/books' component={BookPage} />
                        <Route path='/login' render={(props) => <LoginPage updateToken={this.updateToken} />} />
                        <Route path='/register' component={RegisterPage} />
                    </Switch>
                </React.Fragment>
            </React.Fragment>
        );
    }
}

export default Navigation;