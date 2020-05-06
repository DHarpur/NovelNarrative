import React, { useState } from 'react';
import { Button, Modal } from 'semantic-ui-react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';


const LogoutButton = (props) => {
    const [open, openModal]  = useState(false);
    const token = props.token;
    const history = useHistory();
    const handleLogout = () => {
        axios.post('http://localhost:5000/logout', { headers: {Authorization: token}}).then(
            response => {
                console.log(response);
                localStorage.removeItem('authToken');
                history.push('/');
                openModal(false);
                window.location.reload();
            }
        )
    };
    return (
        <React.Fragment>
            <Button onClick={() => openModal(true)}>Logout</Button>
            <Modal size='mini' open={open} onClose={() => openModal(false)}>
                <Modal.Header>
                    Logout
                </Modal.Header>
                <Modal.Content>
                    <p>Are you sure you want to Logout?</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button negative>No</Button>
                    <Button
                        positive
                        icon='checkmark'
                        labelPosition='right'
                        content='Yes'
                        onClick={handleLogout}
                    />
                </Modal.Actions>
            </Modal>
        </React.Fragment>
    );
}

export default LogoutButton;