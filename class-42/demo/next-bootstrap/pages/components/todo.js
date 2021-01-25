import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Form from 'react-bootstrap/Form'
import FormControl from 'react-bootstrap/FormControl'
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'


import 'bootstrap/dist/css/bootstrap.min.css';


import AddForm from '../components/addForm'
import TodoList from '../components/todoList'

const itemsList = [
    {id:1, name:'eat', owner:'Ahmad', desc:'Eat the same sandwitch everyday.. Like seriously????'},
    {id:2, name:'study', owner:'all class', desc:'Study data structures to go through the interview, dont forget react!!!'},
    {id:3, name:'have fun', owner:'not developers', desc:'Just go out like normal people'},
    {id:4, name:'dance', owner:'Everyone', desc:'Dnace like you are celebrating getting a job at Google'}
];


export default function Todo(props){
    return(
        <>
            <header>
                <Navbar bg="dark" variant="dark">
                    <Nav className="mr-auto">
                        <Nav.Link style={{color: 'red'}} href="/">Home</Nav.Link>
                    </Nav>
                    <Form inline>
                        <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                        <Button variant="outline-info">Search</Button>
                    </Form>
                </Navbar>
            </header>
            <Container>
                <Row>
                    <Col>
                        <Navbar bg="primary" variant="dark">
                            <Nav className="mr-auto">
                                <Nav.Link href="/">Home</Nav.Link>
                            </Nav>
                        </Navbar>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <AddForm />
                    </Col>
                    <Col>
                        <TodoList todos={itemsList} />
                    </Col>
                </Row>
            </Container>
        </>
    )
}
