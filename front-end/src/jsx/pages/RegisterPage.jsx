import React from 'react';
import axios from 'axios';
import { Form, Header } from 'semantic-ui-react';
import MessageSuccess from '../components/MessageSuccess';
import MessageFail from '../components/MessageFail';

const registerBoxStyle = {
    padding: 20,
    margin: 'auto',
    width: '70%'
};

const inputBoxStyle = {
    width: '40%',
    margin: 'auto'
}

class RegisterPage extends React.Component {
    constructor() {
        super();
        this.state = {
            name: '',
            username: '',
            password: '',
            confirmedPassword: '',
            email: '',
            openSuccess: false,
            openFail: false
        }
    }

    handleChange = (e, { name, value }) => this.setState({ [name]: value });

    handleSubmit = () => {
        const { name, username, email, password, confirmedPassword } = this.state;
        if (password === confirmedPassword) {
            const user = {name, username, password, email};
            axios.post('http://localhost:5000/register', user).then(response =>{
                if(response.status === 201) {
                    this.setState({openSuccess: true, username:'', password: '', confirmedPassword: '', email: ''})
                } else if (response.status === 400) {
                    this.setState({openFail: true})
                }
            })
        } else {
            this.setState({openFail: true})
        }
    } 

    render() {
        const { name, username, password, confirmedPassword, email, openSuccess, openFail } = this.state;
        return (
            <div style={registerBoxStyle}>
                <Header as='h2' attached='top'>
                    Register
                </Header>
                <Form onSubmit={this.handleSubmit} className="attached segment">
                    <div style={inputBoxStyle}>
                        <Form.Input label='Enter Name:' placeholder="Name" type="text" name='name' value={name} onChange={this.handleChange} required />
                        <Form.Input label='Enter username:' placeholder="Username" type="text" name='username' value={username} onChange={this.handleChange} required />
                        <Form.Input label='Enter password:' type='password' placeholder="Password" name='password' value={password} onChange={this.handleChange} required />
                        <Form.Input label='Confirm password:' type="password" placeholder="Confirm Password" name='confirmedPassword' value={confirmedPassword} required onChange={this.handleChange} />
                        <Form.Input label='Email:' type="email" placeholder="Email" name='email' value={email} onChange={this.handleChange} required />
                        <Form.Button primary>
                            Register
                        </Form.Button>
                    </div>
                </Form>
                <MessageSuccess open={openSuccess} />
                <MessageFail open={openFail} />
            </div>
        );
    }
};

export default RegisterPage;