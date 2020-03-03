import React from 'react';
import LoginBox from '../LoginBox';
import RegisterBox from '../RegisterBox';

const boxStyle = {
    margin: 'auto'
};

const LoginPage = () => {
    return(
        <div>
            <h2>
                Login or Register Page
            </h2>
            <div style={boxStyle}>
                <LoginBox />
                <RegisterBox />
            </div>
        </div>
    );
};

export default LoginPage;