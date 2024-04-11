from factories.create_media import MediaFactory

factory = MediaFactory()
midia1 = factory.criarMidia('livro', 'John Green', 'Tartarugas Até Lá em Baixo')
midia2 = factory.criarMidia('fime', 'J. K. Rowling', 'Harry Potter e a Câmara Secreta')
print(midia1.showInfo())