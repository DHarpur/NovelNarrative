import React from 'react';
import { Form, Button, Header } from 'semantic-ui-react';
import axios from 'axios';
import { withRouter } from 'react-router-dom';

const loginBoxStyle = {
    padding: 20,
    margin: 'auto',
    width: '70%'
};

const inputBoxStyle = {
    width: '40%',
    margin: 'auto'
}

class LoginPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: '',
            token: '', 
            user: {}
        };
        console.log(props);
    }

    handleChange = (e, { name, value }) => this.setState({ [name]: value });

    handleLogin = () => {
        const { username, password } = this.state;
        const { history } = this.props;
        if (username !== '' && password !== '') {
            const user = {username, password};
            axios.post('http://localhost:5000/login', user).then(response => {
                if(response.status === 200) {
                    const authToken = response.data.authToken.token;
                    const userResponse = response.data.user;
                    console.log(authToken);
                    console.log(response);
                    localStorage.setItem('authToken', authToken);
                    this.setState({token: authToken, user: userResponse});
                    this.props.updateToken(userResponse);
                    history.push("/");
                }
            })
        }
    };

    render() {
        const { username, password } = this.state;
        return (
            <div style={loginBoxStyle}>
                <Header as='h2' attached='top'>
                    Login
                </Header>
                <Form className="attached segment" onSubmit={this.handleLogin}>
                    <div style={inputBoxStyle}>
                        <Form.Input label='Enter username:' placeholder="Username" type="text" name='username' value={username} onChange={this.handleChange} required />
                        <Form.Input label='Enter password:' type='password' placeholder="Password" name='password' value={password} onChange={this.handleChange} required />
                        <Button type="submit" primary>
                            Submit
                        </Button>
                    </div>
                </Form>
            </div>
        );
    }
};
export default withRouter(LoginPage);