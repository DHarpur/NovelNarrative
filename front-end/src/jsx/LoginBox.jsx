import React from 'react';
import { Form, Button } from 'semantic-ui-react';

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
                <Form.Field>
                    <label>Username</label>
                    <input type="text" placeholder="Username" />
                </Form.Field>
                <Form.Field controlId="formGroupPassword">
                    <label>Password</label>
                    <input type="password" placeholder="Password" />
                </Form.Field>
                <Button type="submit">
                    Submit
                </Button>
            </Form>
        </div>
    );
};

export default LoginBox;
