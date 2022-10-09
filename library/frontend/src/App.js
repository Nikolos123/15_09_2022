import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorList from "./components/Author";
import axios from "axios";
import BookList from "./components/Book";
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom";
import NotFound404 from "./components/NotFound404";
import BooksAuthors from "./components/BooksAuthors";
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
            'token':'',
        }
    }

    get_token(username, password) {
       const data = {username:username,password:password}
        axios.post('http://127.0.0.1:8007/api-token-auth/',data).then(response =>{
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный пароль или логин'))
    }

    set_token(token){
        const cookies = new Cookies()
        cookies.set('token',token)
        this.setState({'token':token},()=> this.load_data())
    }
    is_auth(){
        return !!this.state.token
    }
    logout(){
        this.set_token('')
        this.setState({'authors':[]},()=> this.load_data())
        this.setState({'books':[]},()=> this.load_data())
    }
    get_headers(){
        let headers = {
            'Content-Type': 'applications/json'
        }
        if (this.is_auth()){
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }
    get_token_from_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
         this.setState({'token':token},()=> this.load_data())
    }
    load_data(){
        const headers = this.get_headers()
         axios.get('http://127.0.0.1:8007/api/authors/',{headers}).then(response => {
            const authors = response.data
            this.setState({
                'authors': authors
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8007/api/books/',{headers}).then(response => {
            const books = response.data
            this.setState({
                'books': books
            })
        }).catch(error => console.log(error))

    }
    componentDidMount() {

      this.get_token_from_storage()

    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li>
                            <Link to='/'>Authors</Link>
                        </li>
                        <li>
                            <Link to='/books'>Books</Link>
                        </li>
                        <li>
                            {this.is_auth() ? <button onClick={ ()=>this.logout()}>Logout </button> : <Link to='/login'>Login</Link>}
                        </li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element={<Navigate to='/authors'/>}/>
                        <Route path='/authors'>
                            <Route index element={<AuthorList authors={this.state.authors}/>}/>
                            <Route path=':authorId' element={<BooksAuthors books={this.state.books}/>}/>
                        </Route>

                        <Route exact path='/books' element={<BookList books={this.state.books}/>}/>
                        <Route exact path='/login' element={<LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route path='*' element={<NotFound404/>}/>

                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}


export default App;
