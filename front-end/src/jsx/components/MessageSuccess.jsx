import React from 'react';
import { Message } from 'semantic-ui-react';

const MessageSuccess = ({open}) => {
    return (
        <Message success attached='bottom' header="User registration was successful" content="You may now login with your username" hidden={!open}/>
    );
}

export default MessageSuccess;
