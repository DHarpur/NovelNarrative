import React from 'react';
import { Header } from 'semantic-ui-react';
import LoginBox from '../LoginBox';
import RegisterBox from '../RegisterBox';
import { Fragment } from 'react';

const boxStyle = {
    margin: 'auto'
};

const LoginPage = () => {
    return(
        <Fragment>
            <Header as="h1">
                Login or Register Page
            </Header>
            <div style={boxStyle}>
                <LoginBox />
                <RegisterBox />
            </div>
        </Fragment>
    );
};

export default LoginPage;