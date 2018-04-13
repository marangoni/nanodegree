import media
import fresh_tomatoes

forrest_gump = media.Movie("Forrest Gump",
                        """A história atravessa várias décadas na vida do personagem central, Forrest Gump, um homem simples do Alabama que viaja ao redor do mundo, encontra figuras históricas, influencia a cultura popular e é testemunha de alguns dos eventos históricos mais notórios da segunda metade do século XX.""",
                        "https://upload.wikimedia.org/wikipedia/pt/thumb/c/c0/ForrestGumpPoster.jpg/260px-ForrestGumpPoster.jpg",
                        "https://www.youtube.com/watch?v=uPIEn0M8su0")


A_vida_e_bela = media.Movie("A vida é bela",
                            """Na Itália, durante a Segunda Guerra Mundial, o judeu Guido é capturado e mandado para um campo de concentração em Berlim, juntamente com seu filho, o pequeno Giosué. Usando sua inteligência, espirituosidade e bom humor, ele faz com que o filho acredite que ambos estão participando num jogo do qual devem sair campeões, sem que o menino perceba os horrores do regime nazista.""",
                            "https://upload.wikimedia.org/wikipedia/pt/thumb/a/af/La_vita_%C3%A8_bella.jpg/250px-La_vita_%C3%A8_bella.jpg",
                            "https://www.youtube.com/watch?v=8beVLRzEqD0"
                            )
Superman = media.Movie("Superman",
                       """Aos 18 anos, logo após a morte de Jonathan devido a um ataque cardíaco, Clark ouve um "chamado" psíquico e descobre um cristal brilhante nos restos de sua espaçonave. Ele o obriga a viajar para o Ártico, onde o cristal constrói a Fortaleza da Solidão. No interior, uma visão holográfica de Jor-El aparece e explica as origens de Clark, educando-o sobre seus poderes e responsabilidades. Depois de 12 anos de treinamento, com seus poderes totalmente desenvolvidos, ele deixa a Fortaleza vestindo um terno azul e vermelho com o brasão da família Casa de El em seu peito e se torna um repórter no Planeta Diário em Metropolis. """,
                       "https://upload.wikimedia.org/wikipedia/pt/thumb/6/6d/Superman_ver1.jpg/250px-Superman_ver1.jpg",
                       "https://www.youtube.com/watch?v=XWHyvubVdPA")

Big_hero = media.Movie("Operação Big Hero",
                       """Hiro Hamada é um prodígio da robótica, que vive com seu irmão mais velho Tadashi e a tia dona de um restaurante, Cass. Preocupado com as encrencas em que Hiro se mete, Tadashi leva o irmão para conhecer o lugar onde ele estuda e trabalha, o Centro de Robótica do Instituto de Tecnologia de San Fransokyo. Após conhecer os colegas de Tadashi - a esquentada GoGo Tomago, o neurótico Wasabi, a eufórica Honey Lemon, e o fanático por quadrinhos Fred - e a invenção mais nova do irmão, o robô-médico Baymax, Hiro cria interesse em entrar na faculdade. """,
                       "https://upload.wikimedia.org/wikipedia/pt/b/b0/Big-Hero-6-movie-poster.jpg",
                       "https://www.youtube.com/watch?v=f1alHTCUTPc")

Cinema_paradiso = media.Movie("Cinema Paradiso",
                       """Salvatore Di Vita é um cineasta bem-sucedido que vive em Roma. Um dia ele recebe um telefonema de sua mãe avisando que Alfredo está morto. A menção deste nome traz lembranças de sua infância e, principalmente, do Cinema Paradiso, para onde Salvatore, então chamado de Totó, fugia sempre que podia, depois que terminava a missa (ele era coroinha). No começo, ele costumava espreitar as projeções através das cortinas do cinema, que o padre via primeiro para censurar as imagens que possuíam beijos, e fazia companhia a Alfredo, o projecionista. Foi ali que Totó aprendeu a amar o cinema.. """,
                       "https://upload.wikimedia.org/wikipedia/pt/b/bd/Cinema_Paradiso.jpg",
                       "https://www.youtube.com/watch?v=aEy16pvTnMY")

Wiplash = media.Movie("Wiplash",
                       """Andrew Neiman é um estudante baterista de jazz do melhor conservatório dos Estados Unidos. Pretende ser um dos grandes músicos, tendo como ídolo Buddy Rich. Terence Fletcher é professor do conservatório. É extremamente exigente com seus alunos e está a procura de músicos para a banda da escola. Recruta Andrew, que ainda é baterista reserva em sua turma. Caravan e Whiplash são as principais composições ensaiadas pela banda. Porém os métodos duros de Fletcher podem ser demais para Andrew. """,
                       "https://upload.wikimedia.org/wikipedia/pt/thumb/c/cd/Whiplash_em_busca_da_perfeicao.png/240px-Whiplash_em_busca_da_perfeicao.png",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

filmes = [forrest_gump, A_vida_e_bela, Superman, Big_hero, Cinema_paradiso, Wiplash]
fresh_tomatoes.open_movies_page(filmes)
