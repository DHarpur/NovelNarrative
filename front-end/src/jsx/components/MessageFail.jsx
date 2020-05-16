import React from 'react';
import { Message } from 'semantic-ui-react';

const MessageFail = ({open}) => {
    return (
        <Message attached='bottom' error header="There were some errors with your submission." content="Please check that everything was entered correctly." hidden={!open}/>
    );
}

export default MessageFail;
