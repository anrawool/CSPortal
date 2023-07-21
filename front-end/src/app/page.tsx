import styles from './page.module.css'
import ImageComponent from './login/illustration';

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.card}>
        <div className={styles.gridcontainer}>
          <div className={styles.griditem}>

          </div>
          <div className={styles.griditem}>
            <ImageComponent/>
          </div>
        </div>
      </div>      
    </main>
  )
}
