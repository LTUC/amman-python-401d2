import Row from 'react-bootstrap/Row'
import Toast from 'react-bootstrap/Toast'


import 'bootstrap/dist/css/bootstrap.min.css';


export default function TodoList(props){
    return(
        <Row>
            {props.todos.map( item => (
                <Toast>
                    <Toast.Header>
                        <strong className="mr-auto">{item.name}</strong>
                        <small>{item.owner}</small>
                    </Toast.Header>
                    <Toast.Body>{item.desc}</Toast.Body>
                </Toast>)
            )}
        </Row>
    );
}
