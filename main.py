from src.utils import Welcome
from src.download import Videos, Playlists, Songs

Welcome()


def main():
    while True:
        print(
            'Escolha um formato para download:\n[1] - Áudio\n[2] - Vídeo\n[3] - Playlist'
        )
        option = str(input('-->> '))

        if (option in '123') and (len(option) == 1):
            Welcome()

            option = int(option)
            url = str(
                input(
                    f"URL {'da' if option == 3 else 'do'} {'playlist' if option == 3 else 'video'}:\n-->> "
                ))

            if option == 1:
                Songs(url)
                break
            elif option == 2:
                Videos(url)
                break
            elif option == 3:
                Playlists(url)
                break

        elif option == 'exit':
            print('** GoodBye ^~^ **')
            exit()

        else:
            Welcome()
            continue


if __name__ == '__main__':
    main()