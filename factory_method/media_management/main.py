from media_factory import MediaFactory

factory = MediaFactory()
media_book = factory.create_media('livro', 'John Green', 'Tartarugas Até Lá em Baixo')
media_movie = factory.create_media('filme', 'J. K. Rowling', 'Harry Potter e a Câmara Secreta')
print(media_book.show_info())
print(media_movie.show_info())