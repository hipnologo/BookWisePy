
# BookWisePy FastAPI

BookWisePy is a FastAPI application designed to provide information about books. Utilizing the Open Library API, it allows users to fetch book details by ISBN, title, or author.

## Features

- **Get Book by ISBN**: Retrieve detailed information about a book using its ISBN.
- **Search Book by Title**: Search for books by title and get detailed information about the first match.
- **Find Books by Author**: List books written by a specified author.

## Getting Started

To run BookWisePy locally, follow these instructions.

### Prerequisites

- Python 3.7+
- Poetry for dependency management

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/BookWisePy.git
   ```
2. Navigate to the project directory:
   ```sh
   cd BookWisePy
   ```
3. Install the dependencies using Poetry:
   ```sh
   poetry install
   ```

### Running the Application

Start the FastAPI application with:
```sh
poetry run uvicorn bookwisepy.app:app --reload
```
or 
```sh
poetry run uvicorn bookwisepy.app:app --reload --port 8001
```
The `--reload` flag enables hot reloading during development.

## Usage

Once the application is running, you can access the following endpoints:

- Get book by ISBN: `GET /isbn/{isbn}`
- Search book by title: `GET /title/{title}`
- Find books by author: `GET /author/{author}`

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the Apache License 2.0 - see the [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/) for details.

<a href="https://www.buymeacoffee.com/hipnologod" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
