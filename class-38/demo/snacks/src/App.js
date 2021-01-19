import React from 'react';
import './App.css';

function Header(props){
    return(
        <header className="header">
            <h1>Snacks App</h1>
            <h3>Deafult Snack is: {props.defaultSnack}</h3>
        </header>
    );
}


function Footer(props){
    return(
        <footer className={props.cls}>
            <small>{props.text}</small>
        </footer>
    )
}


function Snack(props){
    return (
        <li>
            <h4>Name: {props.snack.name}</h4>
            <h4>Type: {props.snack.type}</h4>
        </li>
    )
}


function SnackList(props){
    // let arrayOfThings = [<li>hi</li>, <li>hi</li>, <li>hi</li>];
    return(
        <main className="main">
            <h2>Snacks List</h2>
            <h3>Number of snacks: {props.snacksList.length}</h3>
            <ul>
                { props.snacksList.map( snack => <Snack snack={snack} />) }
            </ul>
            {/* <ul>
                {arrayOfThings}
            </ul> */}
        </main>
    )
}


class SnackForm extends React.Component{
    constructor(props){
        super(props);
        this.props = props;
        this.state = {
            name:""
        };

        this.handleChange = this.handleChange.bind(this); // Configuration
        this.handleSubmit = this.handleSubmit.bind(this); // Configuration
    }

    render(){
        return(
            <form onSubmit={this.handleSubmit}>
                <label> {this.props.title}
                    <input type="text" onChange={this.handleChange}></input>
                </label>

                <input type="submit" value="Add" />
            </form>
        )
    }

    handleChange(event){
        console.log("Change Happened!!!");
        console.log(event.target.value);
        this.setState({name: event.target.value});
    }

    handleSubmit(event){
        event.preventDefault();
        console.log(this.state.name);
        this.props.onSnackCreate(this.state);
    }
}




class App extends React.Component{

    constructor(){
        super();
        this.state = {
            snacks: [
                {
                    id: 1,
                    name: "Apples",
                    type: "fruits"
                },
                {
                    id: 2,
                    name: "Cookies",
                    type: "sweets"
                },
                {
                    id: 3,
                    name: "Cucumber",
                    type: "veggies"
                }
            ],
            dSnack: "Apples",
            counter: 0
        };
        this.handleCreateSnack = this.handleCreateSnack.bind(this);
    }


    handleCreateSnack(snack){
        alert(snack.name);
        let allSnacks = this.state.snacks;
        allSnacks.push({id: 4, name: snack.name, type: "Any"});
        this.setState({snacks: allSnacks});
    }

    render(){
        return(
            <div className="App">
                <h2>{this.state.counter}</h2>
                <button onClick={() => this.setState({counter: this.state.counter+1}) }>Increment</button>

                <Header defaultSnack={this.state.dSnack}/>
                <SnackList snacksList={this.state.snacks}/>
                <h1>Would you like to add a new Snack? </h1>
                <SnackForm title="Add Snack Form"  onSnackCreate= { (snack) => this.handleCreateSnack(snack) } />
                <Footer cls="footer" text="@copyright ASAC"/>
            </div>
        );
    }
}

export default App;
