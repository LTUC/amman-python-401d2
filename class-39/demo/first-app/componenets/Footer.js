import styles from '../styles.module.css'
import Link from 'next/link'

function Footer(props){
    return(
        <footer className={styles.footer}>
            <h3>We have {props.users.length} users</h3>
            <ul>
                {   props.users.map( (user) => {
                        console.log(user.first_name);
                        return(<li key={user.id}>
                            <Link href="/user/[id].js" as={`/user/${user.id}`}>
                                <a>{user.first_name}{user.last_name}</a>
                            </Link>
                        </li>)

                    })
                }
            </ul>
            <small>@copyright ASAC</small>
        </footer>
    )
}

export default Footer;
