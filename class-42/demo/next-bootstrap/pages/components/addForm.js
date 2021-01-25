import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'



import 'bootstrap/dist/css/bootstrap.min.css';


function handleSubmit(e){
    e.preventDefault();
    console.log(e);
}


export default function AddForm(){
    return(
        <Form onSubmit={handleSubmit}>
            <Form.Group>
                <Form.Label>Item Name</Form.Label>
                <Form.Control type="text" placeholder="Enter item name" />
                <Form.Text className="text-muted">
                What would you like to add today, make it fun ...
                </Form.Text>
            </Form.Group>

            <Form.Group>
                <Form.Label>Owner</Form.Label>
                <Form.Control type="text" placeholder="Who is the Owner" />
            </Form.Group>

            <Form.Group>
                <Form.Label>Decription of Item</Form.Label>
                <Form.Control as="textarea" rows={3} />
            </Form.Group>

            <Button variant="primary" type="submit">
                Add
            </Button>
        </Form>
    );
}
