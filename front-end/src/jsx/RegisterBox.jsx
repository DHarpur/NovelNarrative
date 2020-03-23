import React from 'react';
import { Form, Button } from 'semantic-ui-react';

const registerBoxStyle = {
    border: '1px black solid',
    padding: 20,
    width: '40%',
    display: 'inline-block',
    boxShadow: '0px 4px 8px 0px rgba(0, 0, 0, 0.2)'
};

const RegisterBox = () => {
    return (
        <div style={registerBoxStyle}>
            <p>
                Register
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
                <Form.Field controlId="formGroupPassword">
                    <label>Confirm Password</label>
                    <input type="password" placeholder="Confirm Password" />
                </Form.Field>
                <Button type="submit">
                    Register
                </Button>
            </Form>
        </div>
    );
};

export default RegisterBox;