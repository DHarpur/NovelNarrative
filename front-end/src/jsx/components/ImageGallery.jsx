import React from "react";
import axios from "axios";
import ImageCard from "./ImageCard";
import { Card, Container } from 'semantic-ui-react';
import { Component } from "react";

class ImageGallery extends Component {

    constructor(props) {
        super(props);
        this.state = {
            baseURL: "http://api.themoviedb.org/3/movie/popular?api_key=",
            apiKey: "0e06afa781352e6f44ec54642c09e121",
            items: [],
            isLoading: false,
            totalResults: 0
        };
        
    }

    componentDidMount() {
        const token = localStorage.getItem('authToken');
        const movie = this.props.movie;
        const tvshow = this.props.tvshow;
        const book = this.props.book;
        if(token) {
            if(movie) {
                axios.get("https://api.themoviedb.org/3/movie/popular?api_key=0e06afa781352e6f44ec54642c09e121&language=en-US&page=1")
                    .then(data => this.setState({items: data.data.results}))
                    .catch(error => console.log('Error:', error));
            } else if (tvshow) {
                axios.get("https://api.themoviedb.org/3/tv/popular?api_key=0e06afa781352e6f44ec54642c09e121&language=en-US&page=1")
                    .then(data => this.setState({items: data.data.results}))
                    .catch(error => console.log('Error:', error));
            } else if (book) {
                axios.get("http://localhost:5000/books/recommend/5")
                    .then(data => {
                        console.log(data);
                        this.setState({items: data.data});
                    }).catch(error => console.log('Error:', error));
            }
        }
        else {
            if(movie) {
                axios.get("https://api.themoviedb.org/3/movie/popular?api_key=0e06afa781352e6f44ec54642c09e121&language=en-US&page=1")
                    .then(data => this.setState({items: data.data.results}))
                    .catch(error => console.log('Error:', error));
            } else if (tvshow) {
                axios.get("https://api.themoviedb.org/3/tv/popular?api_key=0e06afa781352e6f44ec54642c09e121&language=en-US&page=1")
                    .then(data => this.setState({items: data.data.results}))
                    .catch(error => console.log('Error:', error));
            } else if (book) {
                axios.get("https://api.themoviedb.org/3/movie/popular?api_key=0e06afa781352e6f44ec54642c09e121&language=en-US&page=1")
                    .then(data => this.setState({items: data.data.results}))
                    .catch(error => console.log('Error:', error));
            }
        }
    }

    render() {
        const items = this.state.items;
        const maxIndex = this.props.maxIndex;
        const { movie, tvshow, book } = this.props;
        return (
            <Container>
                <Card.Group itemsPerRow={5} style={{marginTop: '20px'}}>
                    {items.slice(0, maxIndex).map(item => { 
                        return <ImageCard itemDetails={item} movie book /> 
                    })}
                </Card.Group>
            </Container>
        );
    }
};

export default ImageGallery;