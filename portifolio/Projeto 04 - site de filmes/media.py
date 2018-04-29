# Arquivo de defição da classe Movie e seus métodos associados

import webbrowser
# biblioteca python necessária para interação com o webbrowser 

class Movie():
    """Esta classe define filmes e seus métodos relacionados"""
    def __init__(self, movie_storyline, movie_title, poster_image, trailer_youtube):
        """Método que cria instâncias da classe Movie para cada filme que será inserido no site
        Argumentos:
            self.storyline = resenha do filme
            self.title = título do filme
            self.poster_image_url = url com um poster do filme
            self.trailer.trailer_youtube_url = url com o trailer do filme
        Retorna:
            Uma instância da classe Movie com os argumentos definidos."""
        self.storyline = movie_storyline
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Método que abre o navegador padrão na página definida pelo usuário
        com o trailer do filme"""
        webbrowser.open(self.trailer_youtube_url)
