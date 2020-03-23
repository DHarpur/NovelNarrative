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
            movies: [],
            isLoading: false,
            totalResults: 0
        };
    }

    componentDidMount() {
        const { url, key } = this.state;
        axios.get("https://api.themoviedb.org/3/movie/popular?api_key=0e06afa781352e6f44ec54642c09e121&language=en-US&page=1")
            .then(data => this.setState({movies: data.data.results}))
            .catch(error => console.log('Error:', error));
    }

    render() {
        const movies = this.state.movies;
        console.log(movies);
        return (
            <Container>
                <Card.Group itemsPerRow={4} style={{marginTop: '20px'}}>
                    {movies.map(movie => { 
                        return <ImageCard movieDetails={movie} /> 
                    })}
                </Card.Group>
            </Container>
        );
    }
};

export default ImageGallery;