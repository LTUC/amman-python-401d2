import styles from '../styles.module.css'
import Header from '../componenets/Header'
import Footer from '../componenets/Footer'
import MyLayout from '../componenets/MyLayout'
export default function Home(props) {
  return (
        <MyLayout>
            <p>Hello World</p>
            <p>{props.users[0].first_name}</p>
            <img src={props.users[0].avatar}/>
            <Footer users={props.users}/>
        </MyLayout>
  )
}

export async function getServerSideProps(){
    const response = await fetch('https://reqres.in/api/users');
    const jsonData  = await response.json();
    console.log(jsonData)
    return {props: {users: jsonData.data}}
}
