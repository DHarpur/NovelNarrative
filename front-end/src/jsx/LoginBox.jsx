import React from 'react';
import { Form, Button } from 'react-bootstrap';

const loginBoxStyle = {
    border: '1px black solid',
    padding: 20,
    width: '40%',
    display: 'inline-block',
    marginLeft: 10,
    boxShadow: '0px 4px 8px 0px rgba(0, 0, 0, 0.2)'
};

const LoginBox = () => {
    return (
        <div style={loginBoxStyle}>
            <p>
                Login
            </p>
            <Form>
                <Form.Group>
                    <Form.Label>Username</Form.Label>
                    <Form.Control type="text" placeholder="Username" />
                </Form.Group>
                <Form.Group controlId="formGroupPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
        </div>
    );
};

export default LoginBox;