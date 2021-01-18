import React from 'react';

import './App.css';

function Header(){
    return (
        <header className="App">This is a header</header>
    );
}


function FoodChoice1(props){
    console.log(props);
    const food = "Shawerma";

    return(
        <div className="food">
            <h2>Food Choice 1 for today is</h2>
            <h3>{props.favFood}</h3>
        </div>
    )
}


class FoodChoice2 extends React.Component{
    constructor(){

        super();
        this.state = {
            food: "Potato"
        };
    }


    changeFood(favFood){
        console.log(favFood);
        this.setState( { food:favFood });
    }

    render(){
        return(
            <>
                <button onClick={ () => this.changeFood("Shawerma")}>Shawerma</button>
                <button onClick={ () => this.changeFood("Pasta")}>Pasta</button>
                <button onClick={ () => this.changeFood("Sajeyeh")}>Sajeyeh</button>

                <div className="food">
                    <h2>Food Choice 2 for today is</h2>
                    <h3>{this.state.food}</h3>
                </div>
            </>
        )
    }

}




function Main(){
    return (
        <main>
            <div className="App">

                {/* <h1>Hello {courseName}</h1> */}
                <h1>Hello {getCourseName()}</h1>
                <p>Welcome to our awesome React world!!! </p>

            </div>
        </main>
    )

}


function Footer(){
    return(
        <footer className="App">
            <p>Copy Right @</p>
            <span>ASAC</span>
        </footer>
    )
}

function App() {
    return (
        <>
            <Header />
            <Main />
            {/* <FoodChoice1 favFood="Pasta"/> */}
            <FoodChoice2 />
            <Footer />
        </>
    );
}


function getCourseName(){
    return "401 Python";
}


export default App;
