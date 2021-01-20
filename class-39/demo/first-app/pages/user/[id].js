import MyLayout from '../../componenets/MyLayout'

export default function UserDetails(props){
    return(
        <MyLayout>
            <h2>{props.user.first_name} {props.user.last_name}</h2>
            <img src={props.user.avatar}/>
        </MyLayout>
    )
}

export async function getServerSideProps(context){
    const id = context.query.id;
    const response = await fetch(`https://reqres.in/api/users/${id}`);
    const jsonData  = await response.json();
    return {props: {user: jsonData.data}}
}
